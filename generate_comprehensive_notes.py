#!/usr/bin/env python3
"""
Comprehensive Notes Generator for IMS DB and IMS DC/TM

This script generates detailed, comprehensive study notes from the MCQ JSON files.
The notes include:
- Concept explanations
- Architecture descriptions
- Component roles and relationships
- Examples where applicable
- Important terminology
- Key takeaways

The output is formatted PDF documents suitable for exam preparation and deep learning.
"""

import json
import os
from collections import defaultdict
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas


class ComprehensiveNotesGenerator:
    """Generates comprehensive study notes from MCQ JSON files."""
    
    def __init__(self, json_file, output_pdf, topic_name, difficulty):
        self.json_file = json_file
        self.output_pdf = output_pdf
        self.topic_name = topic_name
        self.difficulty = difficulty
        self.questions = []
        self.concepts = defaultdict(list)
        
    def load_questions(self):
        """Load questions from JSON file."""
        with open(self.json_file, 'r') as f:
            self.questions = json.load(f)
        print(f"Loaded {len(self.questions)} questions from {self.json_file}")
        
    def analyze_and_group_questions(self):
        """Analyze questions and group them by concepts/topics."""
        # Extract key concepts from questions
        for q in self.questions:
            question_text = q['question'].lower()
            
            # Categorize based on keywords in questions
            if 'segment' in question_text or 'hierarchy' in question_text or 'hierarchical' in question_text:
                self.concepts['Hierarchical Data Model and Segments'].append(q)
            elif 'dbd' in question_text or 'database description' in question_text:
                self.concepts['Database Description (DBD)'].append(q)
            elif 'psb' in question_text or 'program specification block' in question_text:
                self.concepts['Program Specification Block (PSB)'].append(q)
            elif 'pcb' in question_text or 'program communication block' in question_text:
                self.concepts['Program Communication Block (PCB)'].append(q)
            elif 'acb' in question_text or 'application control block' in question_text:
                self.concepts['Application Control Blocks (ACB)'].append(q)
            elif 'access method' in question_text or 'organization' in question_text:
                self.concepts['Database Organization and Access Methods'].append(q)
            elif 'region' in question_text or 'address space' in question_text or 'control region' in question_text:
                self.concepts['IMS Architecture and Regions'].append(q)
            elif 'transaction' in question_text or 'message' in question_text:
                self.concepts['Transaction Processing and Messages'].append(q)
            elif 'call' in question_text or 'dli' in question_text or 'api' in question_text:
                self.concepts['DL/I Calls and Programming Interface'].append(q)
            elif 'recovery' in question_text or 'backup' in question_text or 'log' in question_text:
                self.concepts['Database Recovery and Logging'].append(q)
            elif 'security' in question_text or 'authorization' in question_text:
                self.concepts['Security and Authorization'].append(q)
            elif 'performance' in question_text or 'tuning' in question_text or 'buffer' in question_text:
                self.concepts['Performance and Tuning'].append(q)
            elif 'utility' in question_text or 'tool' in question_text:
                self.concepts['IMS Utilities and Tools'].append(q)
            elif 'data sharing' in question_text or 'coupling facility' in question_text:
                self.concepts['Data Sharing and Sysplex'].append(q)
            elif 'database manager' in question_text or 'db manager' in question_text:
                self.concepts['IMS Database Manager'].append(q)
            elif 'tm' in question_text or 'dc' in question_text or 'data communication' in question_text:
                self.concepts['IMS TM/DC Components'].append(q)
            else:
                self.concepts['General IMS Concepts'].append(q)
                
        print(f"Grouped into {len(self.concepts)} concept areas")
        for concept, qs in self.concepts.items():
            print(f"  - {concept}: {len(qs)} questions")
    
    def create_comprehensive_content(self, concept_name, questions):
        """Create comprehensive educational content for a concept."""
        content = []
        
        # Concept-specific comprehensive explanations
        explanations = self.get_concept_explanation(concept_name)
        
        # Add main explanation
        content.append(explanations['overview'])
        content.append("")
        
        # Add key components section
        if 'components' in explanations:
            content.append("Key Components and Features:")
            content.append("")
            for component in explanations['components']:
                content.append(f"• {component}")
            content.append("")
        
        # Add detailed explanation
        if 'detailed' in explanations:
            content.append(explanations['detailed'])
            content.append("")
        
        # Add practical examples
        if 'examples' in explanations:
            content.append("Practical Examples:")
            content.append("")
            content.append(explanations['examples'])
            content.append("")
        
        # Add important terminology from questions
        content.append("Important Terminology and Concepts:")
        content.append("")
        
        # Extract unique facts from questions
        facts = set()
        for q in questions[:10]:  # Limit to avoid repetition
            question = q['question']
            correct_opt = q['correct_answer'][0]
            answer = q[correct_opt]
            
            # Create a fact statement
            fact_statement = self.create_fact_from_question(question, answer)
            if fact_statement:
                facts.add(fact_statement)
        
        for fact in sorted(facts):
            content.append(f"• {fact}")
        
        content.append("")
        
        # Add key takeaways
        if 'takeaways' in explanations:
            content.append("Key Takeaways:")
            content.append("")
            for takeaway in explanations['takeaways']:
                content.append(f"✓ {takeaway}")
            content.append("")
        
        return "\n".join(content)
    
    def create_fact_from_question(self, question, answer):
        """Extract a factual statement from a question and answer."""
        # Clean up the question reference
        question = question.split('[')[0].strip()
        
        # Create a statement from the question and answer
        if '?' in question:
            # Convert question to statement
            q_lower = question.lower()
            
            if q_lower.startswith('which '):
                return f"{answer} {question[6:].replace('?', '.')}"
            elif q_lower.startswith('what '):
                return f"The answer to '{question}' is: {answer}"
            elif q_lower.startswith('how '):
                return f"{answer} (regarding {question})"
            else:
                return f"{question.replace('?', ':')} {answer}"
        
        return None
    
    def get_concept_explanation(self, concept_name):
        """Get comprehensive explanation for a concept."""
        
        explanations = {
            'Hierarchical Data Model and Segments': {
                'overview': """The IMS Hierarchical Data Model is the foundational data structure used by IMS Database Manager (IMS DB). Unlike relational databases that organize data in tables with rows and columns, IMS uses a hierarchical model where data is organized as a tree structure with parent-child relationships. This model has been the cornerstone of IMS since its inception in the 1960s and continues to be highly effective for certain types of applications, particularly those requiring predictable access patterns and high performance.

In the hierarchical model, data is organized into segments, which are the fundamental building blocks of an IMS database. Each segment represents an entity type (similar to a record type in other systems) and contains one or more occurrences of that entity. Segments are arranged in a strict hierarchy, with one root segment at the top and potentially many levels of dependent segments below it.""",
                
                'components': [
                    "Segments: The basic unit of data storage in IMS, comparable to a record type. Each segment type has a defined structure with specific fields.",
                    "Parent-Child Relationships: Segments are connected through parent-child relationships, forming a tree structure. Each child segment can have only one parent, but a parent can have multiple children.",
                    "Root Segment: The top-level segment in the hierarchy. Every database record must have exactly one root segment occurrence.",
                    "Dependent Segments: Child segments that exist below the root. They are dependent on their parent segments for access and existence.",
                    "Segment Levels: IMS supports up to 15 levels of hierarchy in a single database structure.",
                    "Segment Types: A single IMS database can contain up to 255 different segment types.",
                ],
                
                'detailed': """Understanding Hierarchical Traversal and Access:

IMS uses a specific traversal sequence when navigating through the hierarchical structure: top to bottom, left to right, front to back. This sequence is critical for understanding how IMS locates and retrieves data. When an application program requests data, IMS follows this hierarchical path to locate the requested segment.

For example, consider a hierarchical database for a hospital system with the following structure:
- PATIENT (root segment)
  - ADMISSION (child of PATIENT)
    - DIAGNOSIS (child of ADMISSION)
    - TREATMENT (child of ADMISSION)
  - BILLING (child of PATIENT)

In this structure:
1. PATIENT is the root segment, containing basic patient information
2. ADMISSION segments store information about each hospital admission for a patient
3. DIAGNOSIS and TREATMENT are children of ADMISSION, storing medical details
4. BILLING is a separate child of PATIENT for financial information

When traversing this structure, IMS would process segments in this order: PATIENT → ADMISSION → DIAGNOSIS → TREATMENT → BILLING (next ADMISSION if exists, etc.)

Logical vs. Physical Database Records:

An important concept in IMS is the distinction between logical and physical database records. The physical database record is how the data is actually stored on disk, with all segments in a single hierarchy. However, application programs often don't need to see all segments in a database. IMS provides logical database record views, which are subset views of the physical database tailored to specific application needs. This abstraction is defined through Program Specification Blocks (PSBs) and allows for:

1. Security: Applications can only access segments they are authorized to see
2. Simplicity: Applications work with simplified views of complex structures
3. Independence: Physical database changes don't necessarily require application changes
4. Performance: Applications can be optimized for their specific data access patterns

Data Integrity in Hierarchical Structures:

The hierarchical model enforces strong referential integrity automatically. When a parent segment is deleted, all its dependent (child) segments are automatically deleted as well. This cascading delete ensures that there are no orphaned child segments, maintaining database consistency. Conversely, you cannot insert a child segment without first having its parent segment in place.

This model is particularly well-suited for:
- One-to-many relationships (e.g., one customer with many orders)
- Naturally hierarchical data (e.g., organizational charts, bill of materials)
- Applications with predictable access patterns
- High-performance transaction processing where speed is critical""",
                
                'examples': """Example 1: Banking Application
Root: CUSTOMER
  Children of CUSTOMER: ACCOUNT
    Children of ACCOUNT: TRANSACTION

In this structure:
- Each CUSTOMER can have multiple ACCOUNT segments
- Each ACCOUNT can have multiple TRANSACTION segments
- To access a TRANSACTION, you must navigate through CUSTOMER → ACCOUNT → TRANSACTION

Example 2: Manufacturing Bill of Materials
Root: PRODUCT
  Children of PRODUCT: COMPONENT
    Children of COMPONENT: SUBCOMPONENT

This represents a product breakdown:
- A PRODUCT consists of multiple COMPONENTs
- Each COMPONENT may consist of multiple SUBCOMPONENTs
- The hierarchy can extend up to 15 levels for complex products

Example 3: Insurance Policy Management
Root: POLICY
  Children of POLICY: COVERAGE, CLAIM, BENEFICIARY

This shows multiple child types under one parent:
- A POLICY has various COVERAGE details
- CLAIM segments track insurance claims against the policy
- BENEFICIARY segments list policy beneficiaries
- All three are siblings at the same level under POLICY""",
                
                'takeaways': [
                    "IMS uses a hierarchical (tree) data model, not a relational model",
                    "Segments are the basic building blocks, representing entity types",
                    "Parent-child relationships connect segments in a strict hierarchy",
                    "Maximum 15 levels deep and 255 segment types per database",
                    "Traversal order is always top to bottom, left to right, front to back",
                    "Logical views provide application-specific subsets of physical databases",
                    "Hierarchical model enforces automatic referential integrity",
                    "Best suited for one-to-many relationships and predictable access patterns",
                ]
            },
            
            'Database Description (DBD)': {
                'overview': """The Database Description (DBD) is a critical metadata structure in IMS that defines the physical characteristics and organization of an IMS database. The DBD serves as a blueprint for the database, specifying every detail about how data is structured, stored, and accessed. When IMS needs to access a database, it first consults the DBD to understand the database's organization, field layouts, relationships between segments, and storage characteristics.

Think of the DBD as the architectural drawing for a database—it contains all the specifications needed to build, maintain, and access the database structure. Without a properly defined DBD, IMS cannot create or access a database.""",
                
                'components': [
                    "Database Name: Unique identifier for the database within the IMS system",
                    "Access Method: Specifies the database organization type (HDAM, HIDAM, HISAM, HSAM, etc.)",
                    "Segment Definitions: Complete specification of each segment type including name, length, and parent-child relationships",
                    "Field Definitions: Detailed layout of fields within each segment, including field names, positions, lengths, and data types",
                    "Key Fields: Definition of sequence fields used to order segments",
                    "Pointer Specifications: How IMS maintains relationships between segments (physical or symbolic pointers)",
                    "Storage Characteristics: Block sizes, buffer pool requirements, and device specifications",
                    "Dataset Definitions: Physical dataset names and characteristics for database storage",
                ],
                
                'detailed': """DBD Components and Their Roles:

The DBD is created using DBD generation statements, which are coded in a specific IMS control language. Once coded, the DBD source is processed by the IMS Database Description Generation utility to create a compiled DBD, which is stored in the IMS system libraries.

Segment Definitions in the DBD:
Each segment in a database must be fully described in the DBD. The segment definition includes:

1. SEGM Statement: Defines the segment name, parent segment name (except for root), length, and various segment options
   - Example: SEGM NAME=PATIENT,PARENT=0,BYTES=100
   - This defines PATIENT as a root segment (PARENT=0) with 100 bytes length

2. Field Statements: Define individual fields within the segment
   - Example: FIELD NAME=(PATID,SEQ),BYTES=10,START=1
   - This defines PATID as a 10-byte sequence field starting at position 1

3. Pointer Options: Specify how segments are linked
   - PTR=HIER: Hierarchical pointers for parent-child relationships
   - PTR=TWIN: Twin forward and backward pointers for siblings
   - PTR=INDX: Index pointers for indexed databases

Access Method Specifications:

The DBD's ACCESS= parameter is crucial as it determines the database organization:

HDAM (Hierarchical Direct Access Method):
- Provides direct access to root segments via randomizing routine
- Best for high-performance random access
- Requires randomizing module specification in DBD

HIDAM (Hierarchical Indexed Direct Access Method):
- Uses an index for accessing root segments
- Provides both sequential and random access
- Requires separate index database DBD

HISAM (Hierarchical Indexed Sequential Access Method):
- Sequential organization with overflow handling
- Good for sequential processing
- Limited by sequential constraints

The choice of access method fundamentally affects database performance and access patterns. This decision is codified in the DBD and can only be changed by reorganizing the entire database.

Dataset Definitions:

The DBD also specifies the physical datasets where the database data resides:
- DATASET statement defines dataset characteristics
- Multiple datasets can be defined for partitioning large databases
- Dataset definitions include size, device type, and organization parameters

DBD Compilation and Usage:

After coding, DBDs go through a generation process:
1. DBD source is written in IMS DBD generation language
2. Source is submitted to IMS DBDGEN utility
3. DBDGEN compiles the DBD and stores it in the DBD library (DBDLIB)
4. The compiled DBD is ready for use by IMS and application programs
5. DBDs must be combined with PSBs to create Application Control Blocks (ACBs)

Any change to a DBD (adding segments, changing field layouts, modifying access methods) requires:
- Updating the DBD source
- Regenerating the DBD
- Regenerating all affected ACBs
- Potentially reorganizing the database data to match the new structure""",
                
                'examples': """Example 1: Simple DBD Structure for a Library Database

DBD    NAME=LIBRARYDB,ACCESS=HDAM
SEGM   NAME=BOOK,PARENT=0,BYTES=200
FIELD  NAME=(ISBN,SEQ),BYTES=13,START=1
FIELD  NAME=TITLE,BYTES=100,START=14
FIELD  NAME=AUTHOR,BYTES=50,START=114
SEGM   NAME=CHECKOUT,PARENT=BOOK,BYTES=50
FIELD  NAME=(CHKDATE,SEQ),BYTES=8,START=1
FIELD  NAME=MEMBERID,BYTES=10,START=9
FIELD  NAME=DUEDATE,BYTES=8,START=19

This DBD defines:
- Database named LIBRARYDB using HDAM access
- Root segment BOOK with 200 bytes
- Sequence field ISBN (13 bytes) for ordering books
- Child segment CHECKOUT representing book checkouts
- Sequence field CHKDATE for ordering checkouts

Example 2: Index Database DBD for HIDAM

When using HIDAM, you need both a primary DBD and an index DBD:

Primary DBD:
DBD    NAME=CUSTDB,ACCESS=HIDAM
SEGM   NAME=CUSTOMER,PARENT=0,BYTES=150
FIELD  NAME=(CUSTID,SEQ),BYTES=10,START=1

Index DBD:
DBD    NAME=CUSTINDX,ACCESS=INDEX
SEGM   NAME=CUSTIX,PARENT=0,BYTES=15
FIELD  NAME=(CUSTKEY,SEQ),BYTES=10,START=1
LCHILD NAME=(CUSTOMER,CUSTDB)

The index DBD creates a separate index structure that points to root segments in the primary database.""",
                
                'takeaways': [
                    "DBD defines the complete physical structure and organization of an IMS database",
                    "It specifies segments, fields, relationships, and access methods",
                    "DBDs must be compiled using DBDGEN utility before use",
                    "Access method (HDAM, HIDAM, HISAM, etc.) is defined in the DBD",
                    "DBD changes typically require database reorganization",
                    "One DBD describes one database (except index DBDs for HIDAM)",
                    "DBDs are stored in system library (DBDLIB) after compilation",
                    "DBD is combined with PSB to create ACB for application access",
                ]
            },
            
            'Program Specification Block (PSB)': {
                'overview': """The Program Specification Block (PSB) is a metadata control structure that defines an application program's view of one or more IMS databases. While the DBD describes the physical database structure, the PSB specifies what portions of those databases a particular application program is allowed to access and what operations it can perform. The PSB acts as both a security mechanism and an abstraction layer, providing applications with customized, logical views of the data they need while hiding unnecessary complexity.

Each application program in an IMS environment is associated with a PSB, which must be generated before the program can access any IMS databases. The PSB defines one or more Program Communication Blocks (PCBs), each of which describes the application's interface to a database or message queue.""",
                
                'components': [
                    "PSB Name: Unique identifier for the program specification, typically matching the application program name",
                    "PCB Definitions: One or more Program Communication Blocks describing database or message access",
                    "SENSEG Statements: Sensitive segment definitions specifying which segments the program can access",
                    "Processing Options: Defines allowed operations (Get, Insert, Replace, Delete) for each segment",
                    "Key Feedback Area: Specification of key fields returned to the program after database calls",
                    "Authorization: Implicit security through limiting visible segments and allowed operations",
                ],
                
                'detailed': """PSB Structure and Components:

A PSB contains one or more PCBs, and each PCB defines the program's interface to one database or message queue. Let's examine the layers:

Program Communication Blocks (PCBs):
Each PCB within a PSB defines:
1. Database name being accessed
2. Processing sequence (how the program traverses the hierarchy)
3. List of sensitive segments (segments the program can see)
4. Processing options for each sensitive segment

Types of PCBs:
- Database PCB: Defines access to an IMS database
- TP PCB: Defines access to IMS message queues for transaction processing
- GSAM PCB: Defines access to sequential datasets
- MSDB PCB: Defines access to main storage databases (fast path)

Sensitive Segments (SENSEG):
Not all segments defined in a DBD need to be accessible to every program. The SENSEG statements in a PCB specify which segments from the database the program can "see" and access. Segments not listed as sensitive segments are completely invisible to the program—they are hidden from the logical view.

For example, if a database has segments EMPLOYEE, SALARY, DEPENDENT, and BENEFITS, but an application only needs EMPLOYEE and DEPENDENT, the PSB would only list those two as sensitive segments. The program would have no awareness of SALARY or BENEFITS segments.

Processing Options:
For each sensitive segment, the PSB specifies what operations the program can perform:

G = Get (Read): Program can retrieve segments
I = Insert: Program can add new segments
R = Replace: Program can update existing segments
D = Delete: Program can delete segments

Common combinations:
- G: Read-only access (inquiry programs)
- GI: Read and insert (data entry programs)
- GR: Read and update (update programs)
- GIRD: Full access (maintenance programs)

These processing options provide fine-grained control over data access and modification capabilities, serving as a security mechanism to prevent unauthorized changes.

Logical Databases and Secondary Indexing:

PSBs can define access to logical databases, which are virtual databases created by joining segments from multiple physical databases. This is done through logical relationships defined in the DBDs, but accessed through PSBs.

Additionally, PSBs can specify access to databases through secondary indexes, providing alternative access paths to the data beyond the primary sequence.

PSB Generation Process:

Creating a PSB follows these steps:
1. Code PSB source using IMS PSB generation language
2. Submit to PSBGEN utility for compilation
3. PSBGEN validates references to DBDs
4. Compiled PSB is stored in PSBLIB
5. PSB and associated DBDs are combined to create ACB (Application Control Block)
6. ACB is stored in ACBLIB and used at runtime

The ACB generation is a crucial step that resolves all references between the PSB and DBDs, creating an executable form ready for use by application programs.

Multiple PSBs for One Database:

A single physical database can have many different PSBs, each providing a different logical view:
- An inquiry PSB with read-only access to customer data
- An update PSB with full access for customer service representatives
- A reporting PSB with read access to all segments
- A limited PSB for external contractors with access only to non-sensitive data

This flexibility allows the same database to serve many different application needs while maintaining security and simplicity for each application.""",
                
                'examples': """Example 1: Simple PSB for Customer Inquiry

PSB    NAME=CUSTINQ
PCB    TYPE=DB,DBDNAME=CUSTDB,PROCOPT=G
SENSEG NAME=CUSTOMER,PARENT=0,PROCOPT=G
SENSEG NAME=ADDRESS,PARENT=CUSTOMER,PROCOPT=G
SENSEG NAME=PHONE,PARENT=CUSTOMER,PROCOPT=G

This PSB named CUSTINQ:
- Defines access to CUSTDB database
- Allows only Get (read) operations at PCB level
- Makes three segments visible: CUSTOMER, ADDRESS, PHONE
- All segments are read-only (PROCOPT=G)
- Any other segments in CUSTDB are invisible to this program

Example 2: PSB with Update Capabilities

PSB    NAME=CUSTUPD
PCB    TYPE=DB,DBDNAME=CUSTDB,PROCOPT=GIRD
SENSEG NAME=CUSTOMER,PARENT=0,PROCOPT=GR
SENSEG NAME=ADDRESS,PARENT=CUSTOMER,PROCOPT=GIRD
SENSEG NAME=PHONE,PARENT=CUSTOMER,PROCOPT=GIR

This PSB named CUSTUPD:
- Allows full database operations (Get, Insert, Replace, Delete)
- CUSTOMER segment: Can read and update only
- ADDRESS segment: Full access (read, insert, update, delete)
- PHONE segment: Can read, insert, and update (but not delete)

Example 3: PSB with Multiple PCBs

PSB    NAME=ORDPROC
PCB    TYPE=DB,DBDNAME=CUSTDB,PROCOPT=G
SENSEG NAME=CUSTOMER,PARENT=0,PROCOPT=G
PCB    TYPE=DB,DBDNAME=ORDERDB,PROCOPT=GI
SENSEG NAME=ORDER,PARENT=0,PROCOPT=GI
SENSEG NAME=LINEITEM,PARENT=ORDER,PROCOPT=GI
PCB    TYPE=TP

This PSB for order processing:
- First PCB: Read-only access to customer database
- Second PCB: Read and insert access to order database
- Third PCB: Access to IMS message queues for transaction processing
- Program can access multiple databases with different permissions""",
                
                'takeaways': [
                    "PSB defines an application's logical view of IMS databases",
                    "One PSB contains one or more PCBs (Program Communication Blocks)",
                    "SENSEG statements specify which segments are visible to the program",
                    "Processing options (G, I, R, D) control allowed operations per segment",
                    "PSBs provide security by limiting segment visibility and operations",
                    "One database can have many PSBs for different applications",
                    "PSBs must be compiled with PSBGEN utility",
                    "PSB and DBD are combined to create ACB for runtime use",
                    "PSBs support access to multiple databases in one program",
                ]
            },
            
            'IMS Database Manager': {
                'overview': """IMS Database Manager (IMS DB) is the core component of IMS that provides comprehensive database management services for hierarchical databases. It serves as a central point of control and access to application data, offering robust capabilities for data storage, retrieval, integrity maintenance, and recovery. IMS DB has been a cornerstone of enterprise data management for over 50 years, known for its exceptional performance, reliability, and ability to handle extremely high transaction volumes.

IMS Database Manager operates as a multi-threaded, multi-tasking system that allows multiple concurrent batch and online tasks to access and update databases simultaneously while maintaining complete data integrity and consistency. This makes it ideal for mission-critical applications where downtime is not acceptable and data accuracy is paramount.""",
                
                'components': [
                    "Data Access Services: High-performance data retrieval and update operations through DL/I interface",
                    "Concurrent Access Control: Supports multiple concurrent batch and online programs accessing the same databases",
                    "Data Integrity Management: Ensures database consistency through locking, commit/rollback, and referential integrity",
                    "Database Backup and Recovery: Comprehensive facilities for database backup, forward recovery, and backward recovery",
                    "Database Reorganization: Tools and utilities for reorganizing and restructuring databases for optimal performance",
                    "Buffer Management: Sophisticated buffer pool management for optimal I/O performance",
                    "Access Method Support: Multiple database organization methods (HDAM, HIDAM, HISAM, HSAM, etc.)",
                    "Database Utilities: Complete suite of utilities for database maintenance, recovery, and administration",
                ],
                
                'detailed': """IMS Database Manager Architecture and Operations:

Internal Organization and Access Methods:

IMS databases are organized internally using specialized IMS database organization access methods, while actual data storage on disk uses normal operating system access methods. This two-tier approach allows IMS to optimize logical data organization while leveraging standard OS capabilities for physical I/O.

The primary IMS access methods are:

HDAM (Hierarchical Direct Access Method):
- Provides direct access to database root segments
- Uses a randomizing routine (hashing algorithm) to determine physical storage location
- Offers fastest access time for random retrieval
- Ideal for online transaction processing with unpredictable access patterns
- Root segment location is computed from key field value
- Dependent segments are stored close to their root for performance

HIDAM (Hierarchical Indexed Direct Access Method):
- Uses a separate index database to locate root segments
- Index provides both sequential and direct access capabilities
- Allows efficient sequential processing while maintaining random access
- Suitable for applications needing both batch and online access
- Index can be rebuilt without affecting data database

HISAM (Hierarchical Indexed Sequential Access Method):
- Sequential organization with index
- Good for sequentially processed databases
- Limited by sequential storage constraints
- Uses overflow areas for insertions

HSAM (Hierarchical Sequential Access Method):
- Pure sequential organization
- Used primarily for backup, archive, or data transfer
- No direct access capability
- Very fast for sequential processing

Data Integrity and Concurrency Control:

One of IMS Database Manager's key strengths is its ability to maintain data integrity while allowing multiple programs to access and update databases concurrently. This is achieved through:

1. Locking Mechanisms:
   - Segment-level locking prevents conflicts between concurrent programs
   - Intent locking at higher hierarchy levels improves performance
   - Deadlock detection and resolution
   - Lock timeout handling

2. Commit and Rollback:
   - Programs can commit changes to make them permanent
   - Uncommitted changes can be rolled back on program failure
   - Sync points establish consistent recovery points
   - All-or-nothing updates maintain consistency

3. Database Recovery Facilities:

IMS provides comprehensive recovery capabilities:

Forward Recovery:
- Uses before-image and after-image logging
- Can recover database from backup plus log files
- Restores database to point of failure
- Database Recovery utility applies logged changes

Backward Recovery:
- Uses log files to back out uncommitted changes
- Removes partial updates from failed programs
- Maintains database consistency
- Automatic during restart processing

Change Accumulation:
- Accumulates changes for later application
- Useful for reorganization and restructuring
- Can selectively apply changes

Database Tuning and Optimization:

IMS Database Manager provides extensive capabilities for performance tuning:

1. Buffer Pool Management:
   - Configurable buffer pools for different access methods
   - Sequential buffer management (SBM) for sequential processing
   - Data buffer pools reduce physical I/O
   - Buffer pool monitoring and adjustment

2. Database Reorganization:
   - Reorganization utilities remove fragmentation
   - Restructuring changes physical organization
   - Can add or modify segments
   - Unload/reload capabilities

3. Performance Monitoring:
   - Database statistics collection
   - I/O monitoring
   - Buffer hit ratios
   - Response time tracking

Multiple Address Space Architecture:

IMS runs in multiple z/OS address spaces:

Control Region:
- Core of IMS subsystem
- Coordinates all IMS activities
- Manages shared resources
- Controls scheduling

Dependent Regions:
- Run application programs
- Provide IMS services
- Message processing regions (MPR)
- Batch message processing (BMP)
- Java message processing (JMP)

Batch Regions:
- Standalone batch processing
- Can run independent of control region
- Database utilities
- Batch application programs

This architecture provides isolation, scalability, and reliability. A failure in one dependent region doesn't affect others or the control region.""",
                
                'examples': """Example 1: Banking Transaction Processing

A bank uses IMS Database Manager for account processing:

Database Structure:
- HDAM database for account data (fast random access by account number)
- Root segment: ACCOUNT (account number, balance, customer ID)
- Dependent segments: TRANSACTION (transaction history)

Operations:
- ATM withdrawals: Direct access to ACCOUNT via HDAM randomizer
- Balance inquiry: Fast retrieval of ACCOUNT segment only
- Statement generation: Sequential read of ACCOUNT and TRANSACTION segments
- Concurrent updates: Multiple ATMs updating different accounts simultaneously

Integrity Features:
- Account balance locked during withdrawal
- Transaction logged before committing
- Rollback if insufficient funds
- Daily backup for disaster recovery

Example 2: Insurance Claims Processing

Insurance company uses IMS DB for claims:

Database Structure:
- HIDAM database (allows both sequential reporting and random online access)
- Root segment: POLICY
- Dependent segments: CLAIM, PAYMENT, ADJUSTMENT

Processing Patterns:
- Online claims entry: Direct access via policy number
- Batch claims processing: Sequential processing of all new claims
- Premium calculation: Read all policies sequentially
- Claim status inquiry: Direct access to specific policy

Recovery Scenario:
- System failure during batch processing
- IMS automatically backs out uncommitted changes
- Batch job restarts from last commit point
- No manual intervention needed

Example 3: Manufacturing Bill of Materials

Manufacturer uses IMS for product structure:

Database Structure:
- HIDAM database for product hierarchy
- Root: PRODUCT
- Multiple levels: ASSEMBLY → SUBASSEMBLY → PART

Utilization:
- Product design: Online updates to structure
- Cost rollup: Batch sequential processing
- Parts explosion: Hierarchical navigation for all components
- Concurrent access: Engineers updating while cost system reads

Performance Optimization:
- Buffer pools sized for sequential batch processing
- Reorganization monthly to maintain performance
- Secondary index on part number for cross-reference
- Database statistics monitored for tuning""",
                
                'takeaways': [
                    "IMS Database Manager provides centralized database management for hierarchical databases",
                    "Supports multiple concurrent batch and online programs with data integrity",
                    "Offers various access methods (HDAM, HIDAM, HISAM, HSAM) for different needs",
                    "Comprehensive backup and recovery facilities ensure data protection",
                    "Buffer pool management and tuning optimize performance",
                    "Runs in multiple z/OS address spaces for isolation and scalability",
                    "Provides segment-level locking for concurrency control",
                    "Database utilities support reorganization, recovery, and maintenance",
                    "Internal IMS organization separate from physical OS storage methods",
                ]
            },
            
            'Transaction Processing and Messages': {
                'overview': """IMS Transaction Manager (IMS TM), also known as IMS Data Communications (IMS DC), provides comprehensive online transaction processing capabilities. It manages the flow of messages between end users and application programs, coordinates transaction scheduling, ensures message delivery, and maintains transaction integrity. IMS TM is designed for high-volume, mission-critical transaction processing environments where reliability, performance, and scalability are paramount.

Transaction processing in IMS involves receiving input messages from various sources (terminals, applications, web services), routing these messages to appropriate application programs, and returning output messages to the originators. IMS TM handles the complex orchestration of these activities while providing features like message queuing, priority scheduling, conversation management, and automatic restart and recovery.""",
                
                'components': [
                    "Message Queues: Store input and output messages, providing decoupling between message arrival and processing",
                    "Transaction Scheduling: Determines which transactions execute when and in which message processing regions",
                    "Message Format Service (MFS): Provides device-independent formatting of input and output messages",
                    "Conversation Management: Supports multi-step transactions with maintained state between interactions",
                    "Security and Authorization: Controls access to transactions and data based on user credentials",
                    "Transaction Codes: Unique identifiers that specify which application program should process a message",
                    "Priority Processing: Allows critical transactions to be processed before lower-priority ones",
                    "Program-to-Program Message Switching: Enables communication between application programs",
                ],
                
                'detailed': """Message Processing Flow in IMS TM:

Understanding the complete flow of a message through IMS TM is essential for grasping how transaction processing works:

1. Message Input:
   - User enters transaction code and data at terminal
   - IMS receives message through communication protocol (VTAM, TCP/IP, etc.)
   - Message Format Service (MFS) transforms terminal-specific format to application format
   - Transaction code is extracted to identify target application program

2. Message Queuing:
   - Input message is queued on the message queue
   - Message queue provides persistence—messages survive system failures
   - Priority can be assigned based on transaction type or user class
   - Queue depth is monitored to detect backlog conditions

3. Transaction Scheduling:
   - Control region's message scheduler examines queued messages
   - Scheduler selects next message based on priority, class, and available resources
   - Appropriate Message Processing Region (MPR) is selected or initiated
   - Transaction is dispatched to the selected MPR

4. Program Execution:
   - Application program is loaded into MPR (if not already resident)
   - Program receives input message through DL/I call (GU - Get Unique)
   - Program processes transaction, accessing databases as needed
   - Program sends output message through DL/I call (ISRT to alternate PCB)

5. Message Output:
   - Output message is queued for delivery
   - MFS transforms application format to terminal-specific format
   - IMS sends message to destination through communication protocol
   - Delivery confirmation may be logged

6. Transaction Completion:
   - Database changes are committed or rolled back
   - MPR becomes available for next transaction
   - Statistics are updated (response time, throughput, etc.)

Message Queue Management:

IMS message queues are sophisticated structures that provide:

Queue Types:
- Transaction queues: Hold input messages for each transaction code
- LTERM queues: Hold output messages for each logical terminal
- Shared queues: In a sysplex environment, queues shared across IMS systems

Queue Characteristics:
- Persistent storage on DASD (survives system failures)
- FIFO (First-In-First-Out) or priority-based ordering
- Queue depth monitoring and thresholds
- Overflow handling and queue space management

Queue Operations:
- Enqueue: Add message to queue
- Dequeue: Remove message from queue
- Browse: Examine queue contents without removing
- Purge: Remove messages based on criteria

Transaction Codes and Program Association:

Transaction codes (TRAN codes) are 1-8 character identifiers that define:
- Which application program processes the transaction
- Transaction class and priority
- Security requirements
- Message processing options (single/multiple segments, conversational/non-conversational)
- Response mode (response required, response not required)
- DL/I PCBs available to the program

Example transaction definitions:
- ACCTINQ: Account inquiry (read-only, normal priority)
- TRANSFER: Funds transfer (update, high priority)
- ORDRENT: Order entry (update, normal priority)
- REPRTGEN: Report generation (batch-like, low priority)

Conversational vs. Non-Conversational Transactions:

Non-Conversational (most common):
- Single input message → processing → single output message
- No state maintained between transactions
- Program completes and terminates
- Efficient for simple query/update transactions
- Example: ATM balance inquiry

Conversational:
- Multiple message exchanges in a session
- State maintained between messages (scratchpad area)
- Program remains active during conversation
- Used for complex, multi-step processes
- Example: Guided application form completion
- Higher resource usage but better user experience

Message Format Service (MFS):

MFS provides device independence by separating:
- Device Input Format (DIF): How data appears on physical device
- Device Output Format (DOF): How output is formatted for device
- Message Input Descriptor (MID): How input is presented to program
- Message Output Descriptor (MOD): How output is provided by program

Benefits of MFS:
- Applications are device-independent
- Same program can support 3270 terminals, web browsers, mobile devices
- Format changes don't require program changes
- Can map complex screen layouts to simple message structures

Program-to-Program Communication:

IMS TM supports asynchronous message passing between programs:

Message Switching:
- Program A sends message to Program B's transaction code
- Message is queued like terminal input
- Program B processes when scheduled
- Response can be sent back to Program A

Use Cases:
- Workflow processing (pass work between specialized programs)
- Event notification
- Asynchronous request/response patterns
- Integration with other subsystems

Fast Path Transaction Processing:

For extremely high-volume, simple transactions, IMS provides Fast Path:

Characteristics:
- Expedited message scheduling
- Optimized database access (Main Storage Databases - MSDB, Data Entry Databases - DEDB)
- Minimal overhead
- Sub-second response times
- Thousands of transactions per second

Typical Fast Path Applications:
- ATM transactions
- Point-of-sale systems
- Real-time inventory updates
- Telecommunications call processing

Transaction Security and Authorization:

IMS TM provides multiple security layers:

User Authentication:
- RACF/SAF integration
- User ID and password validation
- Digital certificates for web access

Transaction Authorization:
- User must be authorized for specific transaction codes
- Authorization checked before message scheduling
- Prevents unauthorized access to functions

Data Authorization:
- PSB authorization controls database access
- Sensitive segments can be hidden from certain users
- Field-level security through MFS

Terminal Security:
- Logical terminals (LTERMs) can be restricted to certain transaction codes
- Terminal-to-transaction-code authorization
- Network security integration

Performance and Monitoring:

IMS TM provides extensive monitoring capabilities:

Real-Time Monitoring:
- Transaction response times
- Queue depths and backlogs
- Region availability and utilization
- Database buffer pool hit ratios

Performance Metrics:
- Throughput (transactions per second)
- Average response time by transaction code
- Peak load handling
- Resource utilization (CPU, storage, I/O)

Tuning Capabilities:
- Message region class and priority adjustments
- Buffer pool sizing
- Transaction class balancing
- Parallel processing configuration

High Availability Features:

IMS TM ensures continuous operation through:

Automatic Restart:
- Failed regions automatically restarted
- In-flight transactions backed out and requeued
- No manual intervention required

Transaction Recovery:
- Failed transactions automatically rolled back
- Database integrity maintained
- Restart from last commit point

Queue Persistence:
- Messages survive system failures
- Guaranteed delivery
- No lost transactions

Sysplex Support:
- Workload balancing across multiple IMS systems
- Automatic failover
- Shared message queues
- Continuous availability""",
                
                'examples': """Example 1: ATM Withdrawal Transaction

Transaction Flow:
1. Customer enters PIN and withdrawal amount
2. ATM sends message: "WITHDRAW|ACCT=123456|AMT=100"
3. IMS receives message through TCP/IP
4. Transaction code "WITHDRAW" triggers ATMWDRAW program
5. Program validates account, checks balance
6. If sufficient funds: debits account, sends approval
7. ATM dispenses cash and prints receipt
8. Total response time: < 2 seconds

Processing Characteristics:
- Non-conversational (single request-response)
- High priority (financial transaction)
- Database updates (account balance)
- Logging for audit trail
- Fast Path for performance

Example 2: Insurance Claim Entry (Conversational)

Multi-Step Process:
Step 1: 
- User enters transaction code "CLAIMENTRY"
- IMS prompts for policy number
- User enters policy number
- System displays policy details and options

Step 2:
- User selects claim type
- System presents appropriate claim form
- User fills in claim details

Step 3:
- System validates entered data
- Shows summary for confirmation
- User confirms or makes corrections

Step 4:
- System saves claim to database
- Generates claim number
- Sends confirmation

State Management:
- Scratchpad area holds policy info between steps
- Program remains active during conversation
- Timeout if user inactive too long
- Can save partial work for later completion

Example 3: Batch-Like Transaction for Report Generation

Transaction: MONTHLYREPORT
Characteristics:
- Low priority (background processing)
- Long-running (several minutes)
- Read-only database access
- Large output message
- Non-response mode (queued output)

Processing:
1. Manager submits MONTHLYREPORT transaction
2. IMS queues message with low priority
3. When resources available, BMP region processes
4. Program reads thousands of database records
5. Generates formatted report
6. Output queued to manager's LTERM
7. Manager retrieves report when convenient

Benefits:
- Doesn't impact interactive transaction response
- Resource-intensive work scheduled appropriately
- Output available for later retrieval

Example 4: Program-to-Program Communication

Scenario: Order Processing Workflow

Program A (Order Entry):
- Receives customer order
- Validates order details
- Saves order to database
- Sends message to inventory allocation (Program B)
- Sends acknowledgment to customer

Program B (Inventory Allocation):
- Receives message from Program A
- Checks inventory availability
- Reserves inventory items
- Updates inventory database
- Sends message to shipping (Program C)

Program C (Shipping):
- Receives message from Program B
- Creates shipping manifest
- Sends to warehouse system
- Updates order status

Benefits:
- Loose coupling between functions
- Each program specialized for its task
- Asynchronous processing
- Scalable (each program can have multiple instances)
- Fault isolation (failure in one doesn't crash others)""",
                
                'takeaways': [
                    "IMS TM provides comprehensive online transaction processing capabilities",
                    "Messages flow through queues, providing persistence and decoupling",
                    "Transaction codes identify which program processes each message",
                    "MFS provides device independence for application programs",
                    "Conversational transactions maintain state across multiple interactions",
                    "Non-conversational transactions are more efficient for simple operations",
                    "Fast Path provides extremely high performance for simple, high-volume transactions",
                    "Program-to-program communication enables workflow and integration scenarios",
                    "Comprehensive security controls access to transactions and data",
                    "High availability features ensure continuous operation and transaction integrity",
                ]
            },
            
            'IMS Architecture and Regions': {
                'overview': """IMS operates in a sophisticated multi-address space architecture on z/OS that provides isolation, scalability, and high availability. This architecture divides IMS functionality across multiple z/OS address spaces, each with specific roles and responsibilities. Understanding IMS regions (the IMS term for address spaces) is crucial for comprehending how IMS achieves its renowned reliability and performance.

The IMS architecture is built around a central control region that coordinates activities, with multiple dependent regions that provide services and execute application programs. This separation allows for workload distribution, fault isolation, and efficient resource utilization. Some IMS utilities and applications can also run in separate batch address spaces completely independent of the IMS control region.""",
                
                'components': [
                    "Control Region: The core of the IMS subsystem, providing central coordination and control",
                    "Message Processing Regions (MPR): Online regions that process transactions from terminals",
                    "Batch Message Processing (BMP) Regions: Batch programs with access to online databases and message queues",
                    "IMS Fast Path (IFP) Regions: High-performance regions for Fast Path transaction processing",
                    "Java Message Processing (JMP) Regions: Regions for Java application execution",
                    "Java Batch Processing (JBP) Regions: Batch Java programs with database access",
                    "Database Batch Regions: Standalone batch programs for database processing",
                    "Utility Regions: Execute IMS database utilities (reorganization, recovery, etc.)",
                ],
                
                'detailed': """Detailed IMS Region Architecture:

The Control Region - Heart of IMS:

The control region is the central hub of an IMS subsystem. It provides:

1. System Coordination:
   - Schedules transactions to dependent regions
   - Manages queues (message queues, transaction queues)
   - Controls logging activities
   - Coordinates database access across regions
   - Manages shared resources

2. Resource Management:
   - Opens and closes databases
   - Manages database buffer pools
   - Controls program loading
   - Manages shared memory pools
   - Coordinates Fast Path resources

3. Communication Services:
   - Interfaces with z/OS communications (VTAM, TCP/IP)
   - Routes messages to appropriate regions
   - Handles terminal I/O
   - Manages conversation state

4. Recovery and Logging:
   - Coordinates forward and backward recovery
   - Manages log datasets
   - Handles emergency restart
   - Coordinates checkpoint processing

The control region must remain active for IMS to function. It typically runs as a started task on z/OS and is the first component brought up during IMS initialization and the last to terminate during shutdown.

Message Processing Regions (MPR):

MPRs are the workhorses of online transaction processing in IMS:

Characteristics:
- Each MPR can process multiple transaction types
- Programs in MPRs access databases and message queues
- MPRs are scheduled by the control region
- Can have multiple MPRs for workload distribution
- Pseudo-abend handling isolates failures

Transaction Flow in MPR:
1. Terminal user enters transaction code
2. Control region queues the message
3. Control region schedules transaction to available MPR
4. MPR loads application program (if not already loaded)
5. Program processes transaction using DL/I calls
6. Program sends output message
7. Control region routes output to terminal
8. MPR becomes available for next transaction

MPR Advantages:
- Program isolation: One transaction failure doesn't affect others
- Load balancing: Multiple MPRs distribute work
- Program sharing: Same program loaded in multiple MPRs
- Efficient resource use: Programs remain loaded for repeated use

Batch Message Processing (BMP) Regions:

BMPs bridge batch and online processing:

Key Features:
- Batch programs with online database access
- Can access message queues like online programs
- Not scheduled by control region message scheduling
- Initiated via JCL or program control
- Can run during online processing

Common Uses:
- Large batch updates to online databases
- Report generation with online data access
- Data conversion and migration
- Periodic maintenance jobs
- Batch transaction processing from queues

BMP Benefits:
- Concurrent with online: Can run while online system active
- Online data access: Direct access to active databases
- Message queue access: Can process queued messages in batch
- No online disruption: Doesn't affect terminal response time
- Large volume processing: Better suited for bulk operations than MPRs

Database Batch Regions:

These are standalone batch programs:

Characteristics:
- Run independent of IMS control region
- Can run when IMS is down (exclusive database access)
- Use same DL/I interface as online programs
- Access databases directly via ACBs
- Can be pure batch or utility programs

Examples:
- Monthly statement generation
- Database reorganization utilities
- Large data loads
- Database backups
- One-time conversion programs

Batch vs. BMP:
- Batch: Independent, can have exclusive database access
- BMP: Shares online databases, coordinated with control region

Address Space Independence and Benefits:

The multiple address space architecture provides:

1. Fault Isolation:
   - MPR failure doesn't crash control region
   - Utility failure doesn't affect online processing
   - Each region has separate storage protection
   - Abnormal terminations are isolated

2. Scalability:
   - Add more MPRs to increase online capacity
   - Configure regions based on workload
   - Different regions can have different priority
   - Resource limits per region prevent resource monopolization

3. Flexibility:
   - Different regions can run different programs
   - Can start/stop regions independently
   - Maintenance updates can be selective
   - Testing regions can coexist with production

4. Performance:
   - Parallel processing across regions
   - Dedicated resources per region type
   - CPU affinity can be set per region
   - z/OS workload manager integration

IMS Documentation Terminology:

In IMS documentation, "region" is commonly used as a synonym for "z/OS address space." When you see references to "MPR region," "BMP region," or "control region," these refer to separate address spaces running under z/OS. This terminology reflects IMS's heritage and helps distinguish between the logical function (region) and the operating system construct (address space).""",
                
                'examples': """Example 1: Online Banking System Configuration

Control Region: IMSCTRL
- Manages all IMS activities
- Coordinates 10 MPRs
- Handles logging and recovery

Message Processing Regions:
- MPR1-MPR4: Handle ATM transactions
- MPR5-MPR7: Process online banking inquiries
- MPR8-MPR10: Handle funds transfer transactions

BMP Regions:
- BMP1: Nightly interest calculation (runs at 2 AM)
- BMP2: Daily transaction summarization
- BMP3: Real-time fraud detection processing

Batch Regions:
- Monthly statement generation (runs offline, exclusive access)
- Quarterly reporting (runs offline)

This configuration:
- Provides 10 concurrent online transaction processors
- Allows batch processing without disrupting online service
- Isolates different transaction types for better management
- Enables 24/7 online availability with nightly batch processing

Example 2: Insurance Claims Processing System

Control Region: IMSCLAIMS
- Central coordination
- Message scheduling
- Database management

Regions Configuration:
- MPR1-MPR5: Claims entry and inquiry (online)
- BMP1: Claims batch validation (runs hourly)
- BMP2: Payment processing (runs daily)
- BATCH1: Database reorganization (weekly, offline)
- BATCH2: Annual policy renewal (yearly, offline)

Workload Distribution:
- Online claims: 60% of processing
- BMP validation: 25% of processing
- BMP payments: 15% of processing

Fault Tolerance:
- MPR failure: Other MPRs continue processing
- BMP failure: Restarted automatically
- Control region: Redundant with automatic switchover

Example 3: Manufacturing System with Mixed Workload

IMS Regions:
- Control Region: IMSMFG
- 3 MPRs: Order entry and inventory inquiry
- 2 BMPs: Inventory replenishment and order fulfillment
- 1 JMP: Java-based web service interface
- Batch utilities: Run during maintenance window

Typical Day:
0800-1700: Online order entry (MPRs active)
Continuous: Inventory monitoring (BMP1 running)
Every 2 hours: Order fulfillment batch (BMP2)
1800-2000: Database backup (batch region, exclusive)
2000-2200: Database reorganization (utility region)

This shows:
- Mixed online and batch processing
- Continuous BMP monitoring
- Scheduled maintenance in off-hours
- Multiple region types serving different needs""",
                
                'takeaways': [
                    "IMS control region is the core, coordinating all IMS subsystem activities",
                    "Dependent regions (MPR, BMP, JMP, etc.) provide services and run applications",
                    "Each region runs in a separate z/OS address space for isolation",
                    "MPRs process online transactions from terminals",
                    "BMPs run batch programs with access to online databases and message queues",
                    "Database batch regions can run independently of the control region",
                    "Multiple regions enable parallelism, fault isolation, and scalability",
                    "Region terminology in IMS is synonymous with z/OS address spaces",
                    "Architecture supports 24/7 operations with concurrent batch and online processing",
                ]
            },
            
            'IMS TM/DC Components': {
                'overview': """IMS Transaction Manager/Data Communications (IMS TM/DC) consists of several integrated components that work together to provide comprehensive online transaction processing capabilities. These components handle everything from receiving input from terminals and web services, to routing messages, executing application programs, and delivering responses. Understanding each component's role and how they interact is crucial for working effectively with IMS TM/DC systems.

IMS TM/DC components are designed to work together seamlessly while maintaining separation of concerns, enabling high availability, scalability, and maintainability. The architecture has evolved over decades to handle the most demanding transaction processing requirements.""",
                
                'components': [
                    "IMS Control Region: Central coordinator for all IMS TM activities and resource management",
                    "Message Processing Regions (MPRs): Execute online transaction programs in response to terminal input",
                    "Message Queues: Persistent storage for input and output messages, providing reliability",
                    "Message Format Service (MFS): Device-independent message formatting and transformation",
                    "Transaction Manager Scheduler: Manages transaction scheduling and MPR allocation",
                    "OTMA (Open Transaction Manager Access): Provides access to IMS transactions from external clients",
                    "IMS Connect: TCP/IP-based connectivity for web services and distributed applications",
                    "Common Service Layer (CSL): Shared services for IMS systems in a sysplex environment",
                    "Communications Controllers: Interface with VTAM, TCP/IP, and other network protocols",
                ],
                
                'detailed': """Detailed Component Descriptions:

IMS Control Region - The Brain of IMS TM:

The IMS Control Region is the central hub that coordinates all IMS TM/DC activities:

Primary Responsibilities:
1. Message Scheduling:
   - Examines message queues for pending work
   - Selects messages based on priority, class, and available resources
   - Dispatches messages to appropriate MPRs
   - Balances workload across available regions

2. Resource Management:
   - Opens and closes databases for application access
   - Manages buffer pools for optimal performance
   - Allocates and deallocates program regions
   - Controls shared resource access and locking

3. Communication Management:
   - Interfaces with network protocols (VTAM, TCP/IP)
   - Manages logical terminal (LTERM) definitions
   - Routes messages to and from terminals
   - Handles connection establishment and termination

4. System Services:
   - Logging and recovery coordination
   - Statistics collection and reporting
   - Command processing for system administration
   - Security and authorization enforcement

5. Recovery Coordination:
   - Emergency restart processing
   - Backs out incomplete transactions
   - Coordinates forward and backward recovery
   - Manages checkpoint and restart points

The control region is a critical component—if it fails, the entire IMS TM/DC system becomes unavailable. However, with XRF (Extended Recovery Facility) or RSR (Remote Site Recovery), a backup control region can take over automatically.

Message Processing Regions (MPRs):

MPRs are where application programs execute:

MPR Characteristics:
- Each MPR runs as a separate z/OS address space
- Can have multiple MPRs for parallel processing
- Programs are loaded into MPR address space
- MPR coordinates with control region for scheduling
- Pseudo-abend handling isolates program failures

Program Execution in MPRs:
1. Control region selects message for processing
2. MPR receives message and transaction code
3. If program not loaded, MPR loads it from program library
4. Program executes, making DL/I calls as needed:
   - GU (Get Unique) to retrieve input message
   - GN (Get Next) for multi-segment messages
   - Database calls (GU, GN, GHU, GHN, ISRT, REPL, DLET)
   - ISRT to I/O PCB to send output message
5. Program returns control to IMS
6. MPR commits or rolls back database changes
7. Output message is sent to control region for delivery
8. MPR ready for next message

Program Management:
- Programs can remain loaded for efficiency
- Program isolation prevents one failure from affecting others
- Multiple copies of same program can run in different MPRs
- Dynamic program reload supported

Message Queues - Persistence and Reliability:

Message queues provide critical persistence:

Queue Structure:
- Stored on DASD (Direct Access Storage Device)
- Survive system failures and restarts
- Organized by transaction code and LTERM
- Support both FIFO and priority-based ordering

Types of Queues:
1. Transaction Message Queues:
   - One queue per transaction code
   - Hold input messages awaiting processing
   - Prioritized based on message class

2. LTERM Output Queues:
   - One queue per logical terminal
   - Hold output messages for delivery
   - Support delayed message delivery

3. System Message Queue:
   - System-generated messages
   - Administrative notifications
   - Error messages and alerts

Queue Management Features:
- Overflow detection and handling
- Automatic space management
- Queue depth monitoring
- Purge capabilities for old messages
- Queue browsing for diagnostics

Message Format Service (MFS):

MFS provides device independence:

MFS Components:
1. Device Input Format (DIF):
   - Defines how data appears on physical device
   - Maps screen positions to message fields
   - Handles different terminal types (3270, ASCII, etc.)

2. Message Input Descriptor (MID):
   - Defines message format presented to application
   - Application sees consistent format regardless of device
   - Simplifies application programming

3. Device Output Format (DOF):
   - Defines how output appears on device
   - Screen layout, field positioning, attributes
   - Device-specific formatting

4. Message Output Descriptor (MOD):
   - Defines output format from application
   - Application provides simple message structure
   - MFS handles complex formatting

MFS Benefits:
- Applications are completely device-independent
- Same application supports 3270, web, mobile
- Format changes don't require application changes
- Centralized format management
- Support for multiple languages and locales

Transaction Manager Scheduler:

The scheduler optimizes transaction throughput:

Scheduling Algorithms:
- Priority-based scheduling (high-priority first)
- Class-based scheduling (group similar transactions)
- Round-robin within priority class
- Affinity scheduling (route to specific region)

Scheduling Decisions Based On:
- Message priority (defined in transaction definition)
- Transaction class assignment
- MPR availability and current workload
- Program affinity requirements
- Resource availability (database, buffer pools)

Workload Management:
- Balance load across available MPRs
- Prevent resource starvation
- Handle peak load situations
- Support for WLM (Workload Manager) integration

OTMA (Open Transaction Manager Access):

OTMA provides modern connectivity:

OTMA Features:
- TCP/IP-based communication
- Connectionless protocol (high scalability)
- Synchronous and asynchronous messaging
- Support for long messages (up to 32KB segments)
- XCF (Cross-System Coupling Facility) based for sysplex

OTMA Clients:
- WebSphere Application Server
- CICS Transaction Gateway
- IMS Connect
- Custom applications using OTMA API
- Message-oriented middleware

Benefits:
- No terminal definitions required
- Scalable to thousands of concurrent clients
- Automatic load balancing in sysplex
- Enhanced security options
- Support for two-phase commit

IMS Connect - Modern Integration:

IMS Connect extends IMS to distributed environments:

Capabilities:
- TCP/IP listener for IMS transactions
- Protocol conversion (from TCP/IP to OTMA)
- Support for multiple concurrent connections
- XML message transformation
- Web services support (SOAP, REST)

Architecture:
- Runs as separate address space
- Connects to IMS via OTMA/XCF
- Can serve multiple IMS systems
- Load balancing across IMS instances
- Connection pooling for efficiency

Use Cases:
- Web application access to IMS transactions
- Mobile app integration
- Service-oriented architecture (SOA)
- Cloud connectivity
- Partner application integration

Common Service Layer (CSL):

CSL provides shared services in sysplex:

CSL Components:
1. Operations Manager (OM):
   - Centralized command processing
   - System-wide operational control
   - Automated operations capabilities

2. Resource Manager (RM):
   - Shared resource definitions
   - Global resource management
   - Coordinates across IMS systems

3. Structured Call Interface (SCI):
   - API for IMS management
   - Enables automation tools
   - Facilitates integration

Benefits:
- Simplified operations in complex environments
- Consistent management across IMS systems
- Enhanced automation capabilities
- Improved availability through redundancy""",
                
                'examples': """Example 1: Online Banking Transaction Flow

Components Involved:
1. Customer uses web browser to access online banking
2. IMS Connect receives TCP/IP request
3. IMS Connect converts to OTMA message format
4. OTMA sends message to IMS Control Region via XCF
5. Control Region queues message (transaction code: ACCTINQ)
6. Scheduler dispatches to available MPR
7. MPR loads ACCTINQ program
8. Program retrieves account data from IMS database
9. Program formats response message
10. Message flows back: MPR → Control Region → OTMA → IMS Connect → Web browser

Total elapsed time: 100-200 milliseconds

Components' Roles:
- IMS Connect: TCP/IP connectivity and protocol conversion
- OTMA: Message routing and load balancing
- Control Region: Scheduling and resource coordination
- MPR: Application execution environment
- Message Queues: Persistent storage (if async)
- Databases: Account data storage

Example 2: 3270 Terminal Transaction

Components Involved:
1. User at 3270 terminal enters transaction code and data
2. VTAM routes input to IMS Control Region
3. MFS Device Input Format converts screen data to message
4. Control Region queues message
5. Scheduler selects message and dispatches to MPR
6. MPR executes program (already loaded)
7. Program processes transaction and creates output
8. MFS Message Output Descriptor defines output structure
9. MFS Device Output Format creates 3270 screen layout
10. Control Region sends formatted screen to terminal via VTAM

MFS Benefits Demonstrated:
- Application program doesn't know about 3270 specifics
- Same application could support web browser via different DOF
- Screen layout changes don't require program changes

Example 3: High-Volume ATM Processing with Fast Path

Components:
1. ATMs send transactions via TCP/IP to IMS Connect
2. IMS Connect routes to IMS via OTMA
3. Control Region queues on Fast Path transaction queue
4. Fast Path scheduler provides expedited processing
5. IFP (IMS Fast Path) region executes program
6. Program accesses MSDB (Main Storage Database) for account data
7. Response sent back through OTMA → IMS Connect → ATM

Fast Path Optimizations:
- Specialized Fast Path scheduler (lower latency)
- MSDB access (memory-based, not disk)
- Streamlined message handling
- Optimized commit processing

Result:
- Processing time: 10-50 milliseconds
- Throughput: Thousands of transactions per second
- Ideal for high-volume, simple transactions

Example 4: Sysplex Configuration with CSL

Environment:
- Three IMS systems: IMS1, IMS2, IMS3
- Shared message queues via coupling facility
- Common Service Layer (CSL) managing all three
- OTMA workload balancing

Transaction Flow:
1. Request arrives at IMS Connect
2. IMS Connect can route to any of the three IMS systems
3. OTMA performs load balancing based on current workload
4. Request routed to least-busy IMS system
5. Processing occurs on selected system
6. Response returned to client

CSL Benefits:
- Single point of control for all three systems
- Resource definitions shared across all instances
- Operations Manager coordinates activities
- Failure of one system doesn't affect others
- Automatic workload rebalancing on failure""",
                
                'takeaways': [
                    "IMS Control Region coordinates all TM/DC activities and resource management",
                    "MPRs provide execution environments for online application programs",
                    "Message queues ensure reliability through persistent message storage",
                    "MFS provides device independence, simplifying application development",
                    "OTMA enables modern TCP/IP connectivity and distributed access",
                    "IMS Connect bridges IMS to web services and distributed applications",
                    "CSL provides centralized management in sysplex environments",
                    "Components work together to provide high availability and scalability",
                    "Fast Path components optimize for high-volume, simple transactions",
                    "Architecture separates concerns, enabling flexibility and maintainability",
                ]
            },
            
            'General IMS Concepts': {
                'overview': """This section covers foundational IMS concepts that span both IMS Database Manager (IMS DB) and IMS Transaction Manager/Data Communications (IMS TM/DC). These are fundamental concepts that every IMS professional should understand thoroughly, as they form the basis for more advanced topics and practical application development.

IMS (Information Management System) is an enterprise-level database and transaction management system that has been serving critical business applications for over 50 years. Its hierarchical database model and robust transaction processing capabilities make it ideal for applications requiring high performance, reliability, and data integrity. Understanding these general concepts provides the foundation for working effectively with all aspects of IMS.""",
                
                'components': [
                    "IMS Architecture: Overall system structure and component relationships",
                    "Data and Transaction Management: Core capabilities and services",
                    "Application Programming: DL/I interface and application development",
                    "System Administration: Configuration, monitoring, and maintenance",
                    "Integration: How IMS integrates with other z/OS subsystems",
                    "Performance and Scalability: Characteristics enabling high performance",
                    "Reliability and Recovery: Features ensuring continuous operation",
                    "Security: Authorization and access control mechanisms",
                ],
                
                'detailed': """Fundamental IMS Concepts:

IMS as an Integrated System:

IMS is unique in providing both database management and transaction processing in a single integrated system. This integration provides several advantages:

1. Unified Programming Interface:
   - Single API (DL/I) for both database and message operations
   - Consistent programming model across batch and online
   - Simplified application development

2. Coordinated Commitment Control:
   - Database updates and message delivery coordinated
   - Single commit point for both data and messages
   - Guaranteed consistency between database and message queues

3. Integrated Recovery:
   - Single log for both database and transaction activity
   - Coordinated recovery of data and messages
   - Simplified backup and recovery procedures

4. Shared Resource Management:
   - Common buffer pools and memory management
   - Coordinated scheduling and resource allocation
   - Optimized resource utilization

Historical Context and Evolution:

Understanding IMS's history helps appreciate its design:

Origins (1960s):
- Developed by IBM for NASA's Apollo program
- First hierarchical database management system
- Designed for high-volume transaction processing

Evolution:
- 1970s: Addition of DC/TM capabilities
- 1980s: Enhanced recovery and availability features
- 1990s: Client/server and distributed access
- 2000s: Java support, web services, XML
- 2010s: Mobile, cloud, analytics integration
- Present: Continues to evolve with modern requirements

This evolution demonstrates IMS's adaptability while maintaining backward compatibility—applications written decades ago still run on modern IMS.

The DL/I Programming Interface:

DL/I (Data Language/I) is IMS's application programming interface:

DL/I Characteristics:
- Call-level interface (not embedded SQL)
- Same interface for batch and online programs
- Language-independent (COBOL, PL/I, Java, C, Assembler)
- Functions for both data and message operations

Core DL/I Calls:
- GU (Get Unique): Retrieve specific segment
- GN (Get Next): Sequential retrieval
- GHU (Get Hold Unique): Retrieve with intent to update
- GHN (Get Hold Next): Sequential retrieval for update
- ISRT (Insert): Add new segments
- REPL (Replace): Update existing segments
- DLET (Delete): Remove segments

Message Handling Calls:
- GU to I/O PCB: Retrieve input message
- ISRT to I/O PCB: Send output message
- CMD: Issue IMS commands
- CHKP: Establish checkpoint

Programming Model:
- Programs work with PCBs (Program Communication Blocks)
- Status codes indicate call results
- Position maintained within hierarchy
- Segment search arguments specify which segments to retrieve

IMS in the z/OS Ecosystem:

IMS operates as a subsystem within z/OS and integrates with many other components:

Integration Points:
1. z/OS Operating System:
   - Uses z/OS address spaces for regions
   - Leverages z/OS security (RACF/SAF)
   - Uses z/OS I/O subsystem
   - Integrates with z/OS Workload Manager (WLM)

2. CICS:
   - Can access IMS databases from CICS programs
   - Shared access with coordination
   - DBCTL (Database Control) facility

3. DB2:
   - Can access both IMS and DB2 from same program
   - Two-phase commit for consistency
   - Complementary strengths (hierarchical vs. relational)

4. MQ Series:
   - Message integration between IMS and MQ
   - Reliable message delivery
   - Cross-platform messaging

5. WebSphere:
   - Java applications accessing IMS
   - Transaction integration
   - Service-oriented architecture

Performance Characteristics:

IMS is renowned for exceptional performance:

Throughput Capabilities:
- Thousands of transactions per second
- Millions of database operations per second
- Sub-second response times
- Supports very large databases (terabytes)

Performance Features:
1. Efficient Access Methods:
   - HDAM provides direct access to root segments
   - Optimized pointer structures reduce I/O
   - Sequential buffering for batch processing

2. Buffer Management:
   - Sophisticated buffer pool algorithms
   - Multiple buffer pools for different access patterns
   - High buffer hit ratios reduce physical I/O

3. Program Management:
   - Programs remain loaded for reuse
   - Shared program pools
   - Fast program switching

4. Fast Path:
   - Optimized processing for high-volume transactions
   - Main storage databases (MSDB)
   - Data entry databases (DEDB) for high-performance disk access

5. Parallel Processing:
   - Multiple regions process concurrently
   - Partition databases for parallel access
   - Sysplex parallelism across systems

Reliability and Availability:

IMS provides enterprise-level reliability:

High Availability Features:
1. Automatic Restart:
   - Failed regions automatically restarted
   - In-flight transactions backed out
   - Processing resumes without manual intervention

2. Database Recovery:
   - Forward recovery from backups and logs
   - Backward recovery for consistency
   - Point-in-time recovery capabilities

3. Message Persistence:
   - Messages survive system failures
   - Guaranteed delivery
   - No lost transactions

4. XRF (Extended Recovery Facility):
   - Automated failover to backup system
   - Minimal disruption to users
   - Continuous availability

5. RSR (Remote Site Recovery):
   - Disaster recovery with remote backup
   - Near-zero data loss
   - Geographic separation for disaster protection

6. Sysplex Support:
   - Workload balancing across systems
   - Automatic failover
   - Shared data and message queues

Security and Authorization:

IMS provides comprehensive security:

Security Layers:
1. User Authentication:
   - Integration with RACF/SAF
   - User ID and password validation
   - Digital certificates for distributed access

2. Transaction Authorization:
   - Control which users can execute which transactions
   - Transaction-level security definitions
   - Prevents unauthorized function access

3. Data Authorization:
   - PSB authorization controls database access
   - Segment-level security through PSB definitions
   - Read/write/update permissions per segment

4. Terminal Security:
   - Logical terminal authorization
   - Network security integration
   - Encrypted communications

5. Command Authorization:
   - Control access to IMS commands
   - Administrative privilege management
   - Audit trail for command execution

IMS Documentation and Terminology:

Understanding IMS-specific terminology is essential:

Key Terms:
- Region: Synonym for z/OS address space
- Segment: Basic unit of hierarchical data
- DBD: Database Description (metadata)
- PSB: Program Specification Block (program view)
- PCB: Program Communication Block (interface to database or message queue)
- ACB: Application Control Block (runtime form of DBD+PSB)
- LTERM: Logical Terminal
- PTERM: Physical Terminal
- DBRC: Database Recovery Control facility

Relationship Terms:
- Parent-Child: Hierarchical relationship between segments
- Twin: Sibling segments with same parent
- Root: Top-level segment in hierarchy
- Dependent: Child segment

Application Development Considerations:

Developing IMS applications requires understanding:

Best Practices:
1. Understand Hierarchical Access:
   - Access patterns should match hierarchy
   - Minimize backout and re-positioning
   - Use appropriate processing options

2. Optimize Database Calls:
   - Retrieve only needed segments
   - Use qualified SSAs (Segment Search Arguments)
   - Minimize Get-Hold calls

3. Handle Status Codes:
   - Check status after every DL/I call
   - Handle errors appropriately
   - Understand GB, GE, II status codes

4. Design for Performance:
   - Consider access method selection
   - Plan database structure for access patterns
   - Use secondary indexes judiciously

5. Plan for Recovery:
   - Use CHKP calls in long-running programs
   - Ensure restartability
   - Maintain audit trails

Modern IMS Capabilities:

IMS continues to evolve:

Recent Enhancements:
- Java application support (IMS Java)
- Web services integration
- XML message processing
- JSON support
- RESTful APIs
- Mobile connectivity
- Cloud integration
- Analytics and AI/ML integration
- Containerization support

These modern capabilities allow IMS to serve contemporary applications while maintaining its core strengths in reliability, performance, and data integrity.""",
                
                'examples': """Example 1: IMS in a Banking Environment

Complete Banking System:
- IMS DB stores account data hierarchically
- IMS TM handles ATM, online banking, and branch transactions
- Integration with credit card system via MQ
- Integration with regulatory reporting via DB2

Database Structure:
CUSTOMER (root)
  ├─ ACCOUNT (checking, savings)
  │   └─ TRANSACTION (history)
  ├─ LOAN
  │   └─ PAYMENT
  └─ CARD
      └─ AUTHORIZATION

Transaction Types:
- WITHDRAW: ATM withdrawals (Fast Path, high priority)
- TRANSFER: Funds transfers (normal priority)
- INQUIRY: Balance inquiry (read-only, low overhead)
- LOANPMT: Loan payment processing
- STATEMENT: Monthly statement generation (BMP batch)

System Characteristics:
- 10,000 transactions per second during peak
- 99.999% availability requirement
- Sub-second response times
- Millions of customer accounts
- Decades of transaction history

Example 2: Insurance Claims Processing

IMS Configuration:
- Claims database in IMS DB
- Online claims entry via IMS TM
- Batch claims processing overnight
- Integration with payment systems

Typical Day:
0800-1700: Online claims entry (MPRs)
  - Agents enter new claims
  - Customers check claim status
  - Updates to existing claims

1800-0600: Batch processing (BMP)
  - Claims validation
  - Fraud detection
  - Payment calculation
  - Payment file generation

Weekend:
  - Database reorganization
  - Backup and archival
  - Reporting and analytics

Integration:
- Web portal for customers (via IMS Connect/OTMA)
- Mobile app for field agents
- Interface to state reporting systems
- Integration with medical provider databases

Example 3: Manufacturing Supply Chain

IMS Application:
- Product catalog and BOM (Bill of Materials)
- Inventory management
- Order processing
- Supplier management

Database Hierarchy:
PRODUCT (root)
  ├─ COMPONENT
  │   └─ SUBCOMPONENT
  ├─ SUPPLIER
  │   └─ PRICING
  └─ INVENTORY
      └─ LOCATION

Transactions:
- ORDRENT: Order entry from sales
- INVCHK: Inventory status inquiry
- REPLEN: Inventory replenishment
- SHIP: Shipping confirmation

Batch Processes:
- Nightly inventory reconciliation
- Weekly demand forecasting
- Monthly supplier performance analysis
- Quarterly inventory valuation

Benefits:
- Real-time inventory visibility
- Automatic reorder point triggers
- Supplier performance tracking
- Integration with MRP system""",
                
                'takeaways': [
                    "IMS integrates database management and transaction processing in single system",
                    "DL/I provides unified programming interface for all IMS operations",
                    "IMS has evolved over 50+ years while maintaining backward compatibility",
                    "Exceptional performance handles thousands of TPS with sub-second response",
                    "High availability features include automatic restart, XRF, and sysplex support",
                    "Comprehensive security integrates with z/OS RACF at multiple levels",
                    "Modern capabilities support web, mobile, cloud, and analytics",
                    "IMS integrates with other z/OS subsystems (CICS, DB2, MQ, WebSphere)",
                    "Hierarchical model ideal for one-to-many relationships and predictable access",
                    "Critical for mission-critical applications requiring reliability and performance",
                ]
            },
        }
        
        # Return explanation if it exists, otherwise return a generic explanation
        if concept_name in explanations:
            return explanations[concept_name]
        else:
            # Generic explanation for concepts not explicitly defined
            return {
                'overview': f"""This section covers important concepts related to {concept_name} in IMS. These concepts are fundamental to understanding how IMS operates and how to effectively work with IMS databases and applications. The following information is derived from the examination questions and provides essential knowledge for working with IMS systems.""",
                
                'components': [
                    "Core concepts and terminology",
                    "Operational characteristics",
                    "Best practices and guidelines",
                    "Common patterns and usage scenarios",
                ],
                
                'detailed': f"""Detailed Information about {concept_name}:

The concepts in this area are important for understanding IMS operations and capabilities. IMS provides comprehensive support for these features, enabling robust and efficient data management and transaction processing.

When working with {concept_name}, it's important to understand both the theoretical concepts and practical applications. IMS has been refined over decades to provide optimal support for enterprise-level data management, and these features reflect that maturity.

Understanding these concepts requires familiarity with IMS architecture, data models, and operational procedures. The examination questions in this section test your knowledge of key facts, relationships, and best practices.""",
                
                'takeaways': [
                    f"Understanding {concept_name} is essential for working with IMS",
                    "Concepts are based on decades of enterprise data management experience",
                    "Both theoretical knowledge and practical application are important",
                    "These features contribute to IMS's reliability and performance",
                ]
            }
    
    def generate_pdf(self):
        """Generate comprehensive PDF notes."""
        doc = SimpleDocTemplate(
            self.output_pdf,
            pagesize=letter,
            rightMargin=0.75*inch,
            leftMargin=0.75*inch,
            topMargin=0.75*inch,
            bottomMargin=0.75*inch,
        )
        
        # Container for PDF elements
        story = []
        
        # Define styles
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1a1a1a'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        )
        
        subtitle_style = ParagraphStyle(
            'CustomSubtitle',
            parent=styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#333333'),
            spaceAfter=20,
            alignment=TA_CENTER,
            fontName='Helvetica'
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#0066cc'),
            spaceAfter=12,
            spaceBefore=20,
            fontName='Helvetica-Bold'
        )
        
        subheading_style = ParagraphStyle(
            'CustomSubheading',
            parent=styles['Heading3'],
            fontSize=13,
            textColor=colors.HexColor('#0066cc'),
            spaceAfter=10,
            spaceBefore=15,
            fontName='Helvetica-Bold'
        )
        
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['BodyText'],
            fontSize=11,
            alignment=TA_JUSTIFY,
            spaceAfter=12,
            leading=16,
            fontName='Helvetica'
        )
        
        # Title page
        story.append(Paragraph(f"Comprehensive Study Notes", title_style))
        story.append(Paragraph(f"{self.topic_name}", subtitle_style))
        story.append(Paragraph(f"Difficulty Level: {self.difficulty}", subtitle_style))
        story.append(Spacer(1, 0.5*inch))
        
        # Introduction
        intro_text = f"""These comprehensive study notes are designed to provide deep understanding of {self.topic_name} concepts. 
        The material covers all essential topics at the {self.difficulty} level, including detailed explanations, 
        architectural insights, component relationships, and practical examples. This document is suitable for 
        both exam preparation and as a complete learning resource."""
        
        story.append(Paragraph("Introduction", heading_style))
        story.append(Paragraph(intro_text, body_style))
        story.append(Spacer(1, 0.3*inch))
        
        # Table of contents info
        toc_text = f"""This study guide is organized by concept areas, with each section providing:
        <br/>• Comprehensive concept explanations
        <br/>• Detailed architecture and component descriptions
        <br/>• Practical examples and use cases
        <br/>• Important terminology and definitions
        <br/>• Key takeaways and exam concepts
        <br/><br/>Total concepts covered: {len(self.concepts)}"""
        
        story.append(Paragraph("Document Structure", heading_style))
        story.append(Paragraph(toc_text, body_style))
        story.append(PageBreak())
        
        # Generate content for each concept
        concept_num = 0
        for concept_name in sorted(self.concepts.keys()):
            concept_num += 1
            questions = self.concepts[concept_name]
            
            # Concept section header
            story.append(Paragraph(f"{concept_num}. {concept_name}", heading_style))
            story.append(Spacer(1, 0.1*inch))
            
            # Generate comprehensive content
            content = self.create_comprehensive_content(concept_name, questions)
            
            # Split content into paragraphs and add to story
            paragraphs = content.split('\n\n')
            for para in paragraphs:
                if para.strip():
                    # Check if it's a heading
                    if para.strip().endswith(':') and len(para) < 100:
                        story.append(Paragraph(para, subheading_style))
                    else:
                        # Replace bullet points with proper formatting
                        para = para.replace('•', '&#8226;')
                        para = para.replace('✓', '&#10003;')
                        story.append(Paragraph(para, body_style))
            
            story.append(Spacer(1, 0.2*inch))
            
            # Add sample questions section
            story.append(Paragraph(f"Sample Examination Questions:", subheading_style))
            story.append(Spacer(1, 0.1*inch))
            
            # Add up to 5 sample questions from this concept
            for i, q in enumerate(questions[:5], 1):
                q_text = f"<b>Q{i}:</b> {q['question']}"
                story.append(Paragraph(q_text, body_style))
                
                # Add options
                for opt_num in range(1, 5):
                    opt_key = f'option_{opt_num}'
                    if opt_key in q:
                        opt_text = f"&nbsp;&nbsp;&nbsp;&nbsp;{chr(64+opt_num)}. {q[opt_key]}"
                        story.append(Paragraph(opt_text, body_style))
                
                # Add answer
                correct_opt = q['correct_answer'][0]
                answer_text = q[correct_opt]
                ans_para = f"<b>Answer:</b> {answer_text}"
                story.append(Paragraph(ans_para, body_style))
                story.append(Spacer(1, 0.15*inch))
            
            # Page break between major concepts
            if concept_num < len(self.concepts):
                story.append(PageBreak())
        
        # Build PDF
        doc.build(story)
        print(f"Generated comprehensive notes: {self.output_pdf}")


def main():
    """Main function to generate all comprehensive notes."""
    
    # Define all the note configurations
    configurations = [
        # IMS DB Notes
        {
            'json_file': '/home/runner/work/zOS-notes/zOS-notes/IMS_DB/EASY.json',
            'output_pdf': '/home/runner/work/zOS-notes/zOS-notes/IMS_DB/EASY_NOTES.pdf',
            'topic_name': 'IMS Database Manager (IMS DB)',
            'difficulty': 'Easy'
        },
        {
            'json_file': '/home/runner/work/zOS-notes/zOS-notes/IMS_DB/MEDIUM.json',
            'output_pdf': '/home/runner/work/zOS-notes/zOS-notes/IMS_DB/MEDIUM_NOTES.pdf',
            'topic_name': 'IMS Database Manager (IMS DB)',
            'difficulty': 'Medium'
        },
        {
            'json_file': '/home/runner/work/zOS-notes/zOS-notes/IMS_DB/HARD.json',
            'output_pdf': '/home/runner/work/zOS-notes/zOS-notes/IMS_DB/HARD_NOTES.pdf',
            'topic_name': 'IMS Database Manager (IMS DB)',
            'difficulty': 'Hard'
        },
        # IMS DC/TM Notes
        {
            'json_file': '/home/runner/work/zOS-notes/zOS-notes/IMS_DC_TM/EASY.json',
            'output_pdf': '/home/runner/work/zOS-notes/zOS-notes/IMS_DC_TM/EASY_NOTES.pdf',
            'topic_name': 'IMS Transaction Manager / Data Communications (IMS TM/DC)',
            'difficulty': 'Easy'
        },
        {
            'json_file': '/home/runner/work/zOS-notes/zOS-notes/IMS_DC_TM/MEDIUM.json',
            'output_pdf': '/home/runner/work/zOS-notes/zOS-notes/IMS_DC_TM/MEDIUM_NOTES.pdf',
            'topic_name': 'IMS Transaction Manager / Data Communications (IMS TM/DC)',
            'difficulty': 'Medium'
        },
        {
            'json_file': '/home/runner/work/zOS-notes/zOS-notes/IMS_DC_TM/HARD.json',
            'output_pdf': '/home/runner/work/zOS-notes/zOS-notes/IMS_DC_TM/HARD_NOTES.pdf',
            'topic_name': 'IMS Transaction Manager / Data Communications (IMS TM/DC)',
            'difficulty': 'Hard'
        },
    ]
    
    # Generate each set of notes
    for config in configurations:
        print(f"\n{'='*80}")
        print(f"Generating: {config['topic_name']} - {config['difficulty']} Level")
        print(f"{'='*80}")
        
        generator = ComprehensiveNotesGenerator(
            config['json_file'],
            config['output_pdf'],
            config['topic_name'],
            config['difficulty']
        )
        
        generator.load_questions()
        generator.analyze_and_group_questions()
        generator.generate_pdf()
    
    print(f"\n{'='*80}")
    print("All comprehensive notes generated successfully!")
    print(f"{'='*80}")


if __name__ == '__main__':
    main()
