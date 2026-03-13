#!/usr/bin/env python3
"""
Generate additional IMS Application Programming questions to reach 300 total.
Based on IMS DB concepts from the redbook and existing question patterns.
"""

import json
import random

# IMS Application Programming concepts to generate questions about
IMS_APP_CONCEPTS = {
    "DL/I Calls": [
        {"call": "GU (Get Unique)", "desc": "retrieve first segment occurrence that satisfies the SSA"},
        {"call": "GN (Get Next)", "desc": "retrieve the next segment in hierarchical sequence"},
        {"call": "GNP (Get Next within Parent)", "desc": "retrieve next segment occurrence under same parent"},
        {"call": "ISRT (Insert)", "desc": "add new segment occurrence to the database"},
        {"call": "REPL (Replace)", "desc": "update an existing segment"},
        {"call": "DLET (Delete)", "desc": "remove a segment and its dependents"},
    ],
    "SSA Types": [
        {"type": "Unqualified SSA", "desc": "specifies segment type without conditions"},
        {"type": "Qualified SSA", "desc": "specifies segment type with field conditions"},
        {"type": "Command Code SSA", "desc": "specifies special processing options"},
    ],
    "Database Concepts": [
        {"concept": "Segment", "desc": "basic unit of data in IMS hierarchy"},
        {"concept": "Field", "desc": "data element within a segment"},
        {"concept": "Key Field", "desc": "field used to sequence segment occurrences"},
        {"concept": "Sequence Field", "desc": "field that determines segment order"},
        {"concept": "Parent-Child", "desc": "hierarchical relationship between segments"},
        {"concept": "Twin Segments", "desc": "multiple occurrences of same segment type under one parent"},
        {"concept": "Root Segment", "desc": "top-level segment in hierarchy"},
        {"concept": "Database Record", "desc": "one occurrence of root and all its dependents"},
    ],
    "PCB Concepts": [
        {"concept": "PCB (Program Communication Block)", "desc": "defines database view for program"},
        {"concept": "Status Code", "desc": "return code from DL/I call"},
        {"concept": "SENSEG (Sensitive Segment)", "desc": "segment accessible to program"},
        {"concept": "Processing Options", "desc": "Get, Insert, Replace, Delete capabilities"},
    ],
    "DBD/PSB": [
        {"concept": "DBD (Database Description)", "desc": "defines physical database structure"},
        {"concept": "PSB (Program Specification Block)", "desc": "defines program's database view"},
        {"concept": "Sensitive Field", "desc": "field accessible to program"},
    ],
    "Navigation": [
        {"concept": "Hierarchical Sequence", "desc": "top to bottom, left to right traversal"},
        {"concept": "Sequential Processing", "desc": "processing segments in hierarchical order"},
        {"concept": "Direct Processing", "desc": "accessing specific segment directly"},
        {"concept": "Path Call", "desc": "retrieving multiple segments in one call"},
    ],
    "Program Types": [
        {"type": "Batch Program", "desc": "offline IMS database processing"},
        {"type": "BMP (Batch Message Program)", "desc": "batch program with message capabilities"},
    ],
}

def generate_dli_call_questions(start_num):
    """Generate questions about DL/I calls"""
    questions = []
    num = start_num
    
    # GU questions
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What is the primary purpose of the GU (Get Unique) DL/I call in an IMS application program?",
        "option_1": "To retrieve all segments in hierarchical sequence",
        "option_2": "To retrieve the first segment occurrence that satisfies the SSA criteria",
        "option_3": "To retrieve the next segment under the current parent",
        "option_4": "To retrieve all twin segments at once",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    # GN questions
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "When an IMS application program issues a GN (Get Next) call, what segment does it retrieve?",
        "option_1": "The first segment in the database",
        "option_2": "The next segment occurrence under the same parent",
        "option_3": "The next segment in hierarchical sequence from current position",
        "option_4": "The next root segment only",
        "choice_type": "Single Choice",
        "correct_answer": ["option_3"]
    })
    num += 1
    
    # GNP questions
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "How does GNP (Get Next within Parent) differ from GN in IMS application programming?",
        "option_1": "GNP retrieves only root segments while GN retrieves all segments",
        "option_2": "GNP retrieves next segment under same parent while GN continues hierarchical sequence",
        "option_3": "GNP requires qualified SSA while GN requires unqualified SSA",
        "option_4": "GNP is faster but retrieves fewer segments than GN",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    # ISRT questions
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What does the ISRT DL/I call do in an IMS application program?",
        "option_1": "Deletes a segment from the database",
        "option_2": "Updates an existing segment",
        "option_3": "Inserts a new segment into the database",
        "option_4": "Retrieves a segment for processing",
        "choice_type": "Single Choice",
        "correct_answer": ["option_3"]
    })
    num += 1
    
    # REPL questions
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What is the purpose of the REPL DL/I call?",
        "option_1": "To insert a new segment",
        "option_2": "To replace or update an existing segment",
        "option_3": "To delete a segment",
        "option_4": "To retrieve a segment",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    # DLET questions
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What happens when an IMS application program issues a DLET (Delete) call on a parent segment?",
        "option_1": "Only the parent segment is deleted",
        "option_2": "The parent and all its dependent child segments are deleted",
        "option_3": "The operation fails with an error",
        "option_4": "Only the child segments are deleted",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    # More DL/I call questions
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "Before an IMS application program can issue a REPL call, what must it do first?",
        "option_1": "Issue an ISRT call",
        "option_2": "Issue a DLET call",
        "option_3": "Issue a GU or GN call to establish position",
        "option_4": "Issue a GNP call",
        "choice_type": "Single Choice",
        "correct_answer": ["option_3"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "An IMS application needs to retrieve all ORDER segments for a specific CUSTOMER. Which DL/I calls should be used?",
        "option_1": "GU for the CUSTOMER, then GN calls for each ORDER",
        "option_2": "GU for the CUSTOMER, then GNP calls for each ORDER",
        "option_3": "Multiple GU calls for each ORDER",
        "option_4": "GN calls only without initial GU",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_ssa_questions(start_num):
    """Generate questions about SSAs"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What does SSA stand for in IMS application programming?",
        "option_1": "System Segment Address",
        "option_2": "Segment Search Argument",
        "option_3": "Sequential Storage Access",
        "option_4": "Structured Segment Array",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What is the difference between a qualified and unqualified SSA in IMS?",
        "option_1": "Qualified SSA includes field conditions, unqualified specifies only segment type",
        "option_2": "Qualified SSA is faster, unqualified is slower",
        "option_3": "Qualified SSA can only be used with GU, unqualified with GN",
        "option_4": "There is no difference",
        "choice_type": "Single Choice",
        "correct_answer": ["option_1"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "In an IMS application program, what is the format of a qualified SSA?",
        "option_1": "SEGNAME",
        "option_2": "SEGNAME(FIELDNAME operator value)",
        "option_3": "SEGNAME.FIELDNAME=value",
        "option_4": "SEGNAME/FIELDNAME/value",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "An IMS COBOL program needs to retrieve a CUSTOMER segment where CUSTNO = 12345. Which SSA is correct?",
        "option_1": "CUSTOMER",
        "option_2": "CUSTOMER(CUSTNO=12345)",
        "option_3": "CUSTOMER*CUSTNO*12345",
        "option_4": "CUSTOMER.CUSTNO.EQ.12345",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What operators can be used in a qualified SSA in IMS application programs?",
        "option_1": "Only = (equal)",
        "option_2": "=, >, <, >=, <=, ¬= (not equal)",
        "option_3": "Only = and <>",
        "option_4": "=, >, <, LIKE, IN",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_hierarchy_questions(start_num):
    """Generate questions about IMS hierarchy concepts"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "In an IMS hierarchical database, what is a root segment?",
        "option_1": "The last segment in the hierarchy",
        "option_2": "The top-level segment in the hierarchy",
        "option_3": "Any segment with child segments",
        "option_4": "The segment with the most fields",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What are twin segments in IMS?",
        "option_1": "Two segments with identical data",
        "option_2": "Multiple occurrences of the same segment type under one parent",
        "option_3": "Segments at the same level in the hierarchy",
        "option_4": "Backup copies of segments",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "In IMS hierarchical processing, what sequence is used to traverse segments?",
        "option_1": "Bottom to top, right to left, back to front",
        "option_2": "Top to bottom, left to right, front to back",
        "option_3": "Left to right, top to bottom, back to front",
        "option_4": "Random access based on key fields",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What is a database record in IMS from an application programmer's perspective?",
        "option_1": "A single segment occurrence",
        "option_2": "All segments of the same type",
        "option_3": "One root segment occurrence and all its dependent segments",
        "option_4": "A collection of related tables",
        "choice_type": "Single Choice",
        "correct_answer": ["option_3"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "In IMS, what determines the order of twin segments?",
        "option_1": "The order they were inserted",
        "option_2": "The sequence field value",
        "option_3": "Alphabetical order of segment name",
        "option_4": "Random order",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_pcb_questions(start_num):
    """Generate questions about PCB"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What does PCB stand for in IMS application programming?",
        "option_1": "Program Control Block",
        "option_2": "Program Communication Block",
        "option_3": "Process Control Buffer",
        "option_4": "Primary Control Block",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What information does a PCB provide to an IMS application program?",
        "option_1": "Only the database name",
        "option_2": "Only the segment types",
        "option_3": "The database view including sensitive segments and processing options",
        "option_4": "Only the status codes",
        "choice_type": "Single Choice",
        "correct_answer": ["option_3"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "After a DL/I call, where does an IMS application program find the status code?",
        "option_1": "In the segment I/O area",
        "option_2": "In the PCB status code field",
        "option_3": "In the DBD",
        "option_4": "In a global variable",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "What does a status code of 'GE' indicate in an IMS application program after a DL/I call?",
        "option_1": "Segment found successfully",
        "option_2": "Segment not found (end of database)",
        "option_3": "Duplicate key error",
        "option_4": "Security violation",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What processing options can be specified in a PCB for an IMS application program?",
        "option_1": "Only G (Get)",
        "option_2": "G (Get), I (Insert), R (Replace), D (Delete)",
        "option_3": "Only I (Insert) and D (Delete)",
        "option_4": "Only G (Get) and R (Replace)",
        "choice_type": "Multiple Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_dbd_psb_questions(start_num):
    """Generate questions about DBD and PSB"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What does DBD stand for in IMS?",
        "option_1": "Database Description",
        "option_2": "Database Definition",
        "option_3": "Data Block Description",
        "option_4": "Direct Block Definition",
        "choice_type": "Single Choice",
        "correct_answer": ["option_1"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What does PSB stand for in IMS application programming?",
        "option_1": "Program Storage Block",
        "option_2": "Program Specification Block",
        "option_3": "Process Segment Buffer",
        "option_4": "Primary System Block",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What is the relationship between DBD and PSB in IMS?",
        "option_1": "DBD describes physical structure; PSB describes program's view of database",
        "option_2": "DBD is for batch programs; PSB is for online programs",
        "option_3": "DBD and PSB are identical",
        "option_4": "DBD is created by programmers; PSB is created by DBAs",
        "choice_type": "Single Choice",
        "correct_answer": ["option_1"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What are sensitive segments in an IMS PSB?",
        "option_1": "Segments that contain confidential data",
        "option_2": "Segments that are accessible to the application program",
        "option_3": "Segments that cannot be modified",
        "option_4": "Segments that are encrypted",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "If an IMS application program tries to access a segment that is not defined as sensitive in its PSB, what happens?",
        "option_1": "The segment is returned successfully",
        "option_2": "A status code error is returned",
        "option_3": "The program abends",
        "option_4": "The segment is returned but marked as read-only",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_segment_field_questions(start_num):
    """Generate questions about segments and fields"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What is a segment in IMS hierarchical database?",
        "option_1": "A collection of related tables",
        "option_2": "A basic unit of data containing related fields",
        "option_3": "A database index",
        "option_4": "A pointer to another segment",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What is a key field in an IMS segment?",
        "option_1": "The first field in the segment",
        "option_2": "A field used to uniquely identify and sequence segment occurrences",
        "option_3": "A field that cannot be updated",
        "option_4": "A field that references another segment",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "Can an IMS segment exist without a key field?",
        "option_1": "No, all segments must have a key field",
        "option_2": "Yes, key fields are optional in IMS segments",
        "option_3": "Only root segments require key fields",
        "option_4": "Only child segments require key fields",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What is the purpose of a sequence field in IMS segments?",
        "option_1": "To generate sequence numbers automatically",
        "option_2": "To determine the order in which twin segments are stored and retrieved",
        "option_3": "To count the number of segments",
        "option_4": "To validate segment data",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "In an IMS application program, how are segment fields accessed?",
        "option_1": "Through SQL SELECT statements",
        "option_2": "Through the segment I/O area after a successful DL/I call",
        "option_3": "Through direct memory pointers",
        "option_4": "Through XML parsing",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_navigation_questions(start_num):
    """Generate questions about database navigation"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What happens to database position after a successful GU call in an IMS program?",
        "option_1": "Position is set to the beginning of the database",
        "option_2": "Position is set to the retrieved segment",
        "option_3": "Position is not changed",
        "option_4": "Position is set to the root segment",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "An IMS program issues: GU on root, GN on child1, GN on child2. What is the next segment retrieved by another GN?",
        "option_1": "Another child2 twin",
        "option_2": "The next segment in hierarchical sequence after child2",
        "option_3": "The root segment",
        "option_4": "Another child1 segment",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What is sequential processing in IMS application programming?",
        "option_1": "Processing segments in random order",
        "option_2": "Processing segments in hierarchical sequence",
        "option_3": "Processing only root segments",
        "option_4": "Processing segments in reverse order",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "An IMS program needs to process all ITEM segments under a specific ORDER. After GU to the ORDER, which approach is correct?",
        "option_1": "Use GN calls until status code GE",
        "option_2": "Use GNP calls until status code GE",
        "option_3": "Use GU calls for each ITEM",
        "option_4": "Use ISRT calls",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_status_code_questions(start_num):
    """Generate questions about IMS status codes"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What status code indicates a successful DL/I call in an IMS program?",
        "option_1": "OK",
        "option_2": "00 (spaces)",
        "option_3": "GE",
        "option_4": "GA",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What does the status code 'GB' mean in an IMS application program?",
        "option_1": "Segment found successfully",
        "option_2": "End of database reached",
        "option_3": "End of database record (reached end of current path)",
        "option_4": "Duplicate key error",
        "choice_type": "Single Choice",
        "correct_answer": ["option_3"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "In an IMS program, what status code indicates a duplicate key error during ISRT?",
        "option_1": "GE",
        "option_2": "II",
        "option_3": "DK",
        "option_4": "DA",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_cobol_ims_questions(start_num):
    """Generate questions about COBOL and IMS programming"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "Which programming languages can be used to write IMS application programs?",
        "option_1": "Only COBOL",
        "option_2": "COBOL, Java, PL/I, C, C++, Assembler",
        "option_3": "Only COBOL and Assembler",
        "option_4": "Only Java",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "In a COBOL IMS program, where is the PCB defined?",
        "option_1": "In the WORKING-STORAGE SECTION",
        "option_2": "In the LINKAGE SECTION",
        "option_3": "In the FILE SECTION",
        "option_4": "In the CONFIGURATION SECTION",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "In a COBOL IMS program, where is the segment I/O area typically defined?",
        "option_1": "In the LINKAGE SECTION",
        "option_2": "In the WORKING-STORAGE SECTION",
        "option_3": "In the FILE SECTION",
        "option_4": "In the PROCEDURE DIVISION",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "What is the correct COBOL syntax for a DL/I call in an IMS program?",
        "option_1": "EXEC DLI GU PCB SSA SEGMENT",
        "option_2": "CALL 'CBLTDLI' USING function, PCB, segment-io-area, SSA",
        "option_3": "PERFORM DLI-GU USING PCB SSA",
        "option_4": "INVOKE DLI-CALL WITH GU PCB SEGMENT",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_processing_questions(start_num):
    """Generate questions about segment processing"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "When an IMS application deletes a parent segment, what happens to its children?",
        "option_1": "Children remain unchanged",
        "option_2": "Children are automatically deleted (cascade delete)",
        "option_3": "Children become root segments",
        "option_4": "Operation fails with an error",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "Before inserting a child segment in an IMS program, what must exist?",
        "option_1": "The parent segment must already exist in the database",
        "option_2": "All sibling segments must exist",
        "option_3": "The root segment of a different hierarchy",
        "option_4": "No prerequisites are needed",
        "choice_type": "Single Choice",
        "correct_answer": ["option_1"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "An IMS program inserts segments in this order: ROOT, CHILDA, CHILDB. If CHILDA is under ROOT and CHILDB is under CHILDA, what is the result?",
        "option_1": "All insertions succeed creating a 3-level hierarchy",
        "option_2": "CHILDB insertion fails because position is not set correctly",
        "option_3": "Only ROOT insertion succeeds",
        "option_4": "All insertions succeed but in wrong hierarchy level",
        "choice_type": "Single Choice",
        "correct_answer": ["option_1"]
    })
    num += 1
    
    return questions, num

def generate_path_call_questions(start_num):
    """Generate questions about path calls"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What is a path call in IMS application programming?",
        "option_1": "A call that retrieves only the root segment",
        "option_2": "A call that retrieves multiple segments in a path with a single DL/I call",
        "option_3": "A call that updates multiple segments",
        "option_4": "A call that defines the navigation path",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "When would an IMS application programmer use a path call instead of multiple GN calls?",
        "option_1": "When better performance is needed by reducing DL/I call overhead",
        "option_2": "When only root segments are needed",
        "option_3": "When deleting segments",
        "option_4": "Path calls cannot be used in application programs",
        "choice_type": "Single Choice",
        "correct_answer": ["option_1"]
    })
    num += 1
    
    return questions, num

def generate_batch_program_questions(start_num):
    """Generate questions about IMS batch programs"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What is an IMS batch program?",
        "option_1": "A program that runs online with user interaction",
        "option_2": "A program that accesses IMS databases offline without online requirements",
        "option_3": "A program that only reads data",
        "option_4": "A program that runs in the control region",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What is a BMP (Batch Message Program) in IMS?",
        "option_1": "A batch program with no message processing capability",
        "option_2": "A batch program that can also process messages",
        "option_3": "An online program only",
        "option_4": "A system utility program",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "Can IMS batch programs update the database?",
        "option_1": "No, batch programs are read-only",
        "option_2": "Yes, if the PSB grants Insert, Replace, or Delete processing options",
        "option_3": "Only during offline hours",
        "option_4": "Only with special system permissions",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_additional_concepts_questions(start_num):
    """Generate questions about additional IMS concepts"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What is the significance of hierarchical sequence in IMS application programming?",
        "option_1": "It determines the physical storage location",
        "option_2": "It defines the order in which segments are retrieved during sequential processing",
        "option_3": "It has no significance for application programs",
        "option_4": "It only applies to batch programs",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "When an IMS application program retrieves a segment, where is the data placed?",
        "option_1": "In the PCB",
        "option_2": "In the segment I/O area defined by the program",
        "option_3": "In the DBD",
        "option_4": "In the PSB",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "In IMS, what is the maximum number of segment levels in a hierarchical structure?",
        "option_1": "10",
        "option_2": "15",
        "option_3": "20",
        "option_4": "Unlimited",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What is the maximum number of segment types in an IMS hierarchical structure?",
        "option_1": "127",
        "option_2": "255",
        "option_3": "512",
        "option_4": "1024",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What is the purpose of the DL/I interface in IMS application programs?",
        "option_1": "To compile the program",
        "option_2": "To provide a standard interface for database access operations",
        "option_3": "To create the database",
        "option_4": "To manage system resources",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "If an IMS program issues a REPL call without first retrieving the segment, what happens?",
        "option_1": "The replace succeeds on the last segment position",
        "option_2": "A status code error is returned (no current position)",
        "option_3": "A random segment is replaced",
        "option_4": "The program abends",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "Can an IMS application program access multiple databases in a single execution?",
        "option_1": "No, only one database per program",
        "option_2": "Yes, if multiple PCBs are defined in the PSB",
        "option_3": "Only in batch mode",
        "option_4": "Only with special system authorization",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What is the entry point parameter in an IMS application program?",
        "option_1": "The database name",
        "option_2": "The pointer to the PCB list",
        "option_3": "The program name",
        "option_4": "The segment name",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "An IMS program retrieves a parent segment and then issues ISRT for a child. The child ISRT uses a qualified SSA. What must be ensured?",
        "option_1": "The SSA qualification matches the parent key",
        "option_2": "The parent segment was the last segment retrieved (position is established)",
        "option_3": "The child key field is unique",
        "option_4": "The database must be reorganized first",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What happens if an IMS program tries to insert a root segment with a duplicate key?",
        "option_1": "The insertion succeeds with a twin created",
        "option_2": "Status code 'II' is returned indicating duplicate key",
        "option_3": "The old segment is automatically replaced",
        "option_4": "The program abends",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_field_sensitivity_questions(start_num):
    """Generate questions about field sensitivity"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What are sensitive fields in an IMS PSB?",
        "option_1": "Fields that contain sensitive data like passwords",
        "option_2": "Fields that the application program can access",
        "option_3": "Fields that cannot be modified",
        "option_4": "Fields that trigger security alerts",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "If a segment has 10 fields but only 5 are defined as sensitive in the PSB, what does the IMS program see?",
        "option_1": "All 10 fields",
        "option_2": "Only the 5 sensitive fields",
        "option_3": "No fields",
        "option_4": "An error is returned",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_checkpoint_restart_questions(start_num):
    """Generate questions about checkpoint/restart"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What is the purpose of checkpoint calls in IMS batch programs?",
        "option_1": "To test the database connection",
        "option_2": "To save program position for potential restart after failure",
        "option_3": "To delete all processed segments",
        "option_4": "To create backups of the database",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "After an IMS batch program restart from a checkpoint, where does execution resume?",
        "option_1": "At the beginning of the program",
        "option_2": "At the last checkpoint position",
        "option_3": "At a random position",
        "option_4": "At the end of the database",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_command_code_questions(start_num):
    """Generate questions about command codes"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What are command codes in IMS SSAs?",
        "option_1": "Codes that identify the DL/I call type",
        "option_2": "Special processing options specified in the SSA",
        "option_3": "Error codes returned by DL/I",
        "option_4": "Database security codes",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "What does the 'F' command code do in an IMS SSA?",
        "option_1": "Forces a database reorganization",
        "option_2": "Indicates this is the first segment in the path",
        "option_3": "Skips to the first occurrence of the segment",
        "option_4": "Filters out deleted segments",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "What does the 'D' command code do in an IMS SSA?",
        "option_1": "Deletes the segment",
        "option_2": "Specifies this is a dependent segment",
        "option_3": "Uses a path call to retrieve this segment and all its dependents",
        "option_4": "Disables security checking",
        "choice_type": "Single Choice",
        "correct_answer": ["option_3"]
    })
    num += 1
    
    return questions, num

def generate_secondary_index_questions(start_num):
    """Generate questions about secondary indexing"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What is the purpose of a secondary index in IMS from an application perspective?",
        "option_1": "To create backup copies of data",
        "option_2": "To provide an alternate access path to segments using non-key fields",
        "option_3": "To improve system performance only",
        "option_4": "To encrypt sensitive data",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "When an IMS application uses a secondary index, how does it affect the program's view of the hierarchy?",
        "option_1": "No effect, hierarchy remains the same",
        "option_2": "The indexed segment appears as the root in the program's view",
        "option_3": "All segments become root segments",
        "option_4": "The hierarchy is inverted",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_logical_relationship_questions(start_num):
    """Generate questions about logical relationships"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "What is a logical relationship in IMS databases?",
        "option_1": "A physical link between two segments",
        "option_2": "A logical connection between segments in different physical hierarchies",
        "option_3": "A parent-child relationship",
        "option_4": "A security relationship",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "From an IMS application programmer's perspective, how are logical relationships accessed?",
        "option_1": "Through special system calls",
        "option_2": "Through normal DL/I calls as if they were physical children",
        "option_3": "Through SQL queries",
        "option_4": "They cannot be accessed by application programs",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_database_positioning_questions(start_num):
    """Generate questions about database positioning"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What is database positioning in IMS application programming?",
        "option_1": "The physical location of data on disk",
        "option_2": "The current location in the hierarchy after the last successful DL/I call",
        "option_3": "The beginning of the database",
        "option_4": "The end of the database",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "If an IMS program issues GU for a root, then GN for a child, and the child GN fails with status 'GE', what is the position?",
        "option_1": "At the root segment",
        "option_2": "Position is undefined after an unsuccessful call",
        "option_3": "At the beginning of the database",
        "option_4": "At the end of the database",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_concatenated_key_questions(start_num):
    """Generate questions about concatenated keys"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "What is a concatenated key in IMS?",
        "option_1": "Two fields joined in one segment",
        "option_2": "The combination of key fields from the root down to a specific segment",
        "option_3": "A compound primary key",
        "option_4": "Multiple segments with the same key",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "Why are concatenated keys important for IMS application programmers?",
        "option_1": "They are not important",
        "option_2": "They uniquely identify a segment occurrence in the entire database",
        "option_3": "They improve system performance",
        "option_4": "They reduce storage requirements",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_data_integrity_questions(start_num):
    """Generate questions about data integrity"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "How does an IMS application program commit database changes?",
        "option_1": "Explicitly with a COMMIT call",
        "option_2": "Changes are committed when the program terminates normally",
        "option_3": "With a SAVE call",
        "option_4": "Changes are committed immediately after each DL/I call",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What happens to database changes if an IMS program abnormally terminates?",
        "option_1": "All changes are committed",
        "option_2": "All changes are rolled back (backed out)",
        "option_3": "Changes are partially committed",
        "option_4": "The database becomes corrupted",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_more_ssa_questions(start_num):
    """Generate more detailed SSA questions"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "In an IMS qualified SSA, what character is used to enclose the qualification statement?",
        "option_1": "Square brackets []",
        "option_2": "Parentheses ()",
        "option_3": "Curly braces {}",
        "option_4": "Angle brackets <>",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "An IMS program needs to find CUSTOMER where CITY='NEW YORK' and STATE='NY'. How should the SSA be constructed?",
        "option_1": "CUSTOMER(CITY='NEW YORK'&STATE='NY')",
        "option_2": "CUSTOMER(CITY='NEW YORK',STATE='NY')",
        "option_3": "Two separate SSAs are required",
        "option_4": "This cannot be done in one SSA",
        "choice_type": "Single Choice",
        "correct_answer": ["option_1"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What character is used in IMS SSA to specify AND logic between multiple conditions?",
        "option_1": "& (ampersand)",
        "option_2": "+ (plus)",
        "option_3": "* (asterisk)",
        "option_4": ", (comma)",
        "choice_type": "Single Choice",
        "correct_answer": ["option_1"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What character is used in IMS SSA to specify OR logic between multiple conditions?",
        "option_1": "& (ampersand)",
        "option_2": "+ (plus)",
        "option_3": "| (pipe)",
        "option_4": ", (comma)",
        "choice_type": "Single Choice",
        "correct_answer": ["option_3"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "In an IMS unqualified SSA, what information is specified?",
        "option_1": "Only the segment name",
        "option_2": "Segment name and field values",
        "option_3": "Only field conditions",
        "option_4": "Database name and segment name",
        "choice_type": "Single Choice",
        "correct_answer": ["option_1"]
    })
    num += 1
    
    return questions, num

def generate_more_dli_questions(start_num):
    """Generate more DL/I call questions"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "An IMS program issues GU for ROOT, then GNP for CHILD. If no CHILD exists, what status code is returned?",
        "option_1": "GE (segment not found)",
        "option_2": "GB (end of database record)",
        "option_3": "GK (wrong segment type)",
        "option_4": "II (duplicate insert)",
        "choice_type": "Single Choice",
        "correct_answer": ["option_1"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What is the function parameter for a GU call in CBLTDLI?",
        "option_1": "'GU' (with quotes)",
        "option_2": "GU (without quotes)",
        "option_3": "'GU  ' (4-character field)",
        "option_4": "1 (numeric code)",
        "choice_type": "Single Choice",
        "correct_answer": ["option_3"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "How many SSAs can be specified in a single DL/I call?",
        "option_1": "Only one",
        "option_2": "Up to 15 (matching the maximum hierarchy depth)",
        "option_3": "Exactly two",
        "option_4": "Unlimited",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "In an IMS GU call with multiple SSAs, what does each SSA represent?",
        "option_1": "Different databases",
        "option_2": "Different programs",
        "option_3": "A level in the hierarchical path to the target segment",
        "option_4": "Alternative search criteria",
        "choice_type": "Single Choice",
        "correct_answer": ["option_3"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "Which DL/I call would an IMS program use to retrieve the first CUSTOMER segment?",
        "option_1": "GN",
        "option_2": "GU",
        "option_3": "GNP",
        "option_4": "ISRT",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "After successfully retrieving a segment with GU, which call retrieves the next segment in sequence?",
        "option_1": "Another GU",
        "option_2": "GN",
        "option_3": "GNP",
        "option_4": "REPL",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "An IMS program processes orders: GU for CUSTOMER, then loop GNP for ORDER segments. What happens when no more ORDERs exist for that CUSTOMER?",
        "option_1": "Status code 'GE' is returned",
        "option_2": "Status code 'GB' is returned",
        "option_3": "The program abends",
        "option_4": "The next CUSTOMER's orders are returned",
        "choice_type": "Single Choice",
        "correct_answer": ["option_1"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "Can an IMS application program issue multiple GU calls in succession?",
        "option_1": "No, only one GU per program execution",
        "option_2": "Yes, GU can be issued multiple times",
        "option_3": "Only in batch programs",
        "option_4": "Only for root segments",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_more_hierarchy_questions(start_num):
    """Generate more hierarchy questions"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "In an IMS hierarchy, what is the relationship between a segment and the segment directly above it?",
        "option_1": "Sibling relationship",
        "option_2": "Parent-child relationship",
        "option_3": "Twin relationship",
        "option_4": "Peer relationship",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What are segments at the same level under the same parent called in IMS?",
        "option_1": "Twins",
        "option_2": "Siblings",
        "option_3": "Peers",
        "option_4": "Cousins",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "In an IMS database with a root segment PATIENT, can there be multiple PATIENT occurrences?",
        "option_1": "No, only one root allowed",
        "option_2": "Yes, there can be multiple root segment occurrences (database records)",
        "option_3": "Only if they have different keys",
        "option_4": "Only in batch mode",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "If an IMS hierarchy has segments A(root), B(child of A), C(child of B), what is C's relationship to A?",
        "option_1": "Direct child",
        "option_2": "Grandchild (descendant)",
        "option_3": "Twin",
        "option_4": "No relationship",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "Can an IMS segment have more than one parent?",
        "option_1": "Yes, segments can have multiple parents",
        "option_2": "No, each segment has only one physical parent",
        "option_3": "Only root segments can have multiple parents",
        "option_4": "Only with special configuration",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What determines the hierarchical structure shown to an IMS application program?",
        "option_1": "The physical storage method",
        "option_2": "The PSB definition (which segments are sensitive)",
        "option_3": "The program logic",
        "option_4": "The operating system",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_more_segment_questions(start_num):
    """Generate more segment-related questions"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What is the typical size limit for an IMS segment?",
        "option_1": "No limit",
        "option_2": "Maximum of several thousand bytes",
        "option_3": "Exactly 256 bytes",
        "option_4": "Maximum of 80 bytes",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "Can an IMS segment contain repeating groups of fields?",
        "option_1": "No, fields cannot repeat within a segment",
        "option_2": "Yes, segments can contain repeating field groups",
        "option_3": "Only in root segments",
        "option_4": "Only with special database options",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "In IMS, what is a segment occurrence?",
        "option_1": "A segment type definition",
        "option_2": "One specific instance of a segment type with actual data",
        "option_3": "A segment that occurs only once",
        "option_4": "A deleted segment",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "Can different segment types in an IMS hierarchy have different lengths?",
        "option_1": "No, all segments must be the same length",
        "option_2": "Yes, each segment type can have its own length",
        "option_3": "Only if they are at the same level",
        "option_4": "Only root segments can have different lengths",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_more_pcb_status_questions(start_num):
    """Generate more PCB and status code questions"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "After each DL/I call, what should an IMS application program check first?",
        "option_1": "The segment data",
        "option_2": "The status code in the PCB",
        "option_3": "The database name",
        "option_4": "The PSB name",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "What status code indicates that an IMS program tried to access a segment not defined in its PSB?",
        "option_1": "GE",
        "option_2": "GK",
        "option_3": "GA",
        "option_4": "AM",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What information is available in the PCB after a successful GU call?",
        "option_1": "Only the status code",
        "option_2": "Status code, segment level, and key feedback area",
        "option_3": "Only the segment name",
        "option_4": "Only the database name",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "Where is the key feedback area located in IMS?",
        "option_1": "In the segment I/O area",
        "option_2": "In the PCB",
        "option_3": "In the DBD",
        "option_4": "In the PSB",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What is stored in the key feedback area after a successful retrieve call?",
        "option_1": "The entire segment",
        "option_2": "The concatenated key of the retrieved segment",
        "option_3": "Only the root key",
        "option_4": "The status code",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_more_insert_questions(start_num):
    """Generate more insert-related questions"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "When inserting a new root segment, what must an IMS program provide?",
        "option_1": "Parent segment key",
        "option_2": "The complete segment data in the I/O area",
        "option_3": "Previous root segment reference",
        "option_4": "Database password",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "To insert a new child segment, an IMS program must first establish position at which level?",
        "option_1": "At the root segment",
        "option_2": "At the immediate parent of the segment to be inserted",
        "option_3": "At any segment in the hierarchy",
        "option_4": "Position is not required for insert",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "If multiple twin segments exist, where is a new twin inserted when ISRT is issued?",
        "option_1": "At the beginning of the twin chain",
        "option_2": "In sequence based on the key field value",
        "option_3": "At the end of the twin chain",
        "option_4": "At a random position",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "Can an IMS program insert a segment without a key field?",
        "option_1": "No, all segments must have keys",
        "option_2": "Yes, if the segment type is defined without a key in the DBD",
        "option_3": "Only root segments require keys",
        "option_4": "Only for batch programs",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_more_delete_questions(start_num):
    """Generate more delete-related questions"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "Before issuing a DLET call, what must an IMS program do?",
        "option_1": "Issue a checkpoint",
        "option_2": "Successfully retrieve the segment to be deleted",
        "option_3": "Retrieve all child segments",
        "option_4": "Issue a REPL call first",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "An IMS program has a hierarchy: ROOT-CHILD1-CHILD2. If it deletes CHILD1, what happens to CHILD2?",
        "option_1": "CHILD2 remains and becomes a child of ROOT",
        "option_2": "CHILD2 is also deleted (cascade delete)",
        "option_3": "The delete fails",
        "option_4": "CHILD2 becomes an orphan segment",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "Can an IMS program delete the root segment?",
        "option_1": "No, root segments cannot be deleted",
        "option_2": "Yes, if the program has delete authority in its PSB",
        "option_3": "Only by system programmers",
        "option_4": "Only in batch mode",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_more_replace_questions(start_num):
    """Generate more replace-related questions"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "Can an IMS program use REPL to change a segment's key field?",
        "option_1": "Yes, any field can be changed including the key",
        "option_2": "No, key fields cannot be changed with REPL",
        "option_3": "Only in root segments",
        "option_4": "Only if the key is not unique",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "To change a segment's key field, what should an IMS application program do?",
        "option_1": "Use REPL with a special flag",
        "option_2": "Delete the segment and insert a new one with the new key",
        "option_3": "Use a special UPDKEY call",
        "option_4": "Key fields can never be changed",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "After a REPL call, what is the database position?",
        "option_1": "At the root segment",
        "option_2": "At the replaced segment",
        "option_3": "Position is lost",
        "option_4": "At the next segment",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_more_processing_questions(start_num):
    """Generate more processing-related questions"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What is sequential processing in an IMS application program?",
        "option_1": "Processing segments in physical storage order",
        "option_2": "Processing segments one after another in hierarchical sequence",
        "option_3": "Processing segments in reverse order",
        "option_4": "Processing only root segments",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What is direct access processing in IMS?",
        "option_1": "Accessing segments without using DL/I",
        "option_2": "Accessing a specific segment directly using qualified SSAs",
        "option_3": "Accessing only root segments",
        "option_4": "Accessing segments in random order",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "An IMS program processes all segments sequentially using GN. How does it know when to stop?",
        "option_1": "When the program counter reaches maximum",
        "option_2": "When status code 'GB' or 'GE' is returned",
        "option_3": "When 1000 segments are processed",
        "option_4": "The program must manually count segments",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_more_cobol_questions(start_num):
    """Generate more COBOL/IMS questions"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "In a COBOL IMS program, what is CBLTDLI?",
        "option_1": "The segment name",
        "option_2": "The DL/I interface module name for COBOL programs",
        "option_3": "A status code",
        "option_4": "A database name",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "In a COBOL IMS program, what length should the function parameter be?",
        "option_1": "2 characters",
        "option_2": "4 characters",
        "option_3": "8 characters",
        "option_4": "Variable length",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "In a COBOL IMS program, which data division section contains the PCB mask?",
        "option_1": "WORKING-STORAGE SECTION",
        "option_2": "LINKAGE SECTION",
        "option_3": "FILE SECTION",
        "option_4": "LOCAL-STORAGE SECTION",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "In a COBOL IMS program, how is the entry parm (PCB list address) received?",
        "option_1": "Through ACCEPT statement",
        "option_2": "Through the ENTRY statement parameter or PROCEDURE DIVISION USING",
        "option_3": "Through an environment variable",
        "option_4": "Through a file",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_more_misc_questions(start_num):
    """Generate miscellaneous IMS questions"""
    questions = []
    num = start_num
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What does DL/I stand for in IMS?",
        "option_1": "Data Language Interface",
        "option_2": "Data Language/I (Input)",
        "option_3": "Database Language Interface",
        "option_4": "Data Link Interface",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "Can an IMS application program mix database and message processing?",
        "option_1": "No, they must be separate programs",
        "option_2": "Yes, IMS programs can use both database and message PCBs",
        "option_3": "Only in batch programs",
        "option_4": "Only in online programs",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "If an IMS PSB has multiple database PCBs, how does the program access a specific database?",
        "option_1": "By specifying the database name in each call",
        "option_2": "By using the appropriate PCB pointer/reference in the DL/I call",
        "option_3": "By issuing a SELECT DATABASE call first",
        "option_4": "All databases are accessed simultaneously",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "What is the I/O area in an IMS application program?",
        "option_1": "A file buffer",
        "option_2": "The memory area where segment data is passed between program and DL/I",
        "option_3": "The PCB",
        "option_4": "The SSA",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "Must the I/O area in an IMS program match the segment length exactly?",
        "option_1": "Yes, it must match exactly",
        "option_2": "No, it can be larger (only needed data is moved)",
        "option_3": "It can only be larger, never smaller",
        "option_4": "It must be exactly 256 bytes",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_even_more_questions(start_num):
    """Generate additional questions on various topics"""
    questions = []
    num = start_num
    
    # Parent-child relationships
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "In IMS, can a child segment exist without its parent?",
        "option_1": "Yes, child segments are independent",
        "option_2": "No, a parent must exist before its children can be inserted",
        "option_3": "Only for root children",
        "option_4": "Only in batch mode",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    # Database navigation
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "After retrieving segment A at level 2, an IMS program issues GN. Which segment is retrieved next?",
        "option_1": "The next twin of A",
        "option_2": "The first child of A if it exists, otherwise the next segment in hierarchical sequence",
        "option_3": "The parent of A",
        "option_4": "The root segment",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    # Multiple databases
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "Can an IMS program issue DL/I calls against multiple databases in one execution?",
        "option_1": "No, only one database per execution",
        "option_2": "Yes, if the PSB includes PCBs for multiple databases",
        "option_3": "Only if databases are in the same DBDGEN",
        "option_4": "Only in online mode",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    # Processing options
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "If a PCB has processing option 'G' only, which DL/I calls can the program use?",
        "option_1": "All DL/I calls",
        "option_2": "Only GU, GN, and GNP (retrieval calls)",
        "option_3": "Only ISRT and DLET",
        "option_4": "Only REPL",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    # Error handling
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What should an IMS application program do when it receives an unexpected status code?",
        "option_1": "Ignore it and continue",
        "option_2": "Check the status code and handle the error appropriately",
        "option_3": "Always abend the program",
        "option_4": "Retry the call indefinitely",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    # Segment search
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "An IMS program needs to find an ORDER with ORDERNO=5000. If ORDERs are sequenced by ORDERNO, which is more efficient?",
        "option_1": "GN calls until ORDERNO=5000 is found",
        "option_2": "GU with qualified SSA: ORDER(ORDERNO=5000)",
        "option_3": "Both are equally efficient",
        "option_4": "Sequential scan is always faster",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    # Commit scope
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "In an IMS batch program, when are database updates physically written?",
        "option_1": "Immediately after each DL/I call",
        "option_2": "At commit points (checkpoint or program termination)",
        "option_3": "Every 100 calls",
        "option_4": "Only when the database is closed",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    # Segment length
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "Who defines the length of an IMS segment?",
        "option_1": "The application programmer in the program",
        "option_2": "The DBA in the DBD (Database Description)",
        "option_3": "It is always 256 bytes",
        "option_4": "The operating system",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    # Field types
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "Can IMS segment fields contain different data types (numeric, character, etc.)?",
        "option_1": "No, all fields must be character",
        "option_2": "Yes, fields can be various types (character, packed, binary, etc.)",
        "option_3": "Only numeric types",
        "option_4": "Only character types",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    # PSB scheduling
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "How does an IMS application program specify which PSB to use?",
        "option_1": "In the program code",
        "option_2": "Through JCL or scheduling parameters when the program is executed",
        "option_3": "It is hardcoded in the DBD",
        "option_4": "Through a configuration file",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    return questions, num

def generate_final_additional_questions(start_num):
    """Generate final set of questions to reach 300"""
    questions = []
    num = start_num
    
    # More DL/I calls
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What is the difference between GN and GNP when processing twin segments?",
        "option_1": "No difference",
        "option_2": "GNP stays within the current parent, GN may move to next parent",
        "option_3": "GN is faster",
        "option_4": "GNP requires qualified SSA",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "An IMS program retrieves CUSTOMER, then loops through ORDERs with GNP. After the last ORDER (status GE), what is the position?",
        "option_1": "At the CUSTOMER segment",
        "option_2": "Position is undefined after GE status",
        "option_3": "At the first ORDER",
        "option_4": "At the next CUSTOMER",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    # More segments
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "In IMS, what is a segment type?",
        "option_1": "The data type of the segment",
        "option_2": "The definition or template for segments with the same structure",
        "option_3": "A category of databases",
        "option_4": "A processing option",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "Can two different segment types in IMS have the same name?",
        "option_1": "Yes, if in different hierarchies",
        "option_2": "No, segment names must be unique within a DBD",
        "option_3": "Only if they are at different levels",
        "option_4": "Yes, always allowed",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    # More about keys
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "If an IMS segment has a unique key, can there be duplicate key values among twin segments?",
        "option_1": "Yes, twins can have duplicate keys",
        "option_2": "No, each twin must have a unique key value",
        "option_3": "Only for non-root segments",
        "option_4": "Only in batch mode",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "What happens if an IMS program inserts a segment with a duplicate key when unique key is specified?",
        "option_1": "The insert succeeds and creates a twin",
        "option_2": "Status code 'II' (duplicate insert) is returned",
        "option_3": "The old segment is replaced",
        "option_4": "The program abends",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    # More field questions
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Easy",
        "question": "In IMS, can a segment have multiple fields?",
        "option_1": "No, only one field per segment",
        "option_2": "Yes, a segment can contain multiple fields",
        "option_3": "Only root segments can have multiple fields",
        "option_4": "Maximum of two fields per segment",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "In an IMS segment, where is the key field typically located?",
        "option_1": "At the end of the segment",
        "option_2": "At the beginning of the segment",
        "option_3": "In the middle of the segment",
        "option_4": "Location doesn't matter",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    # Command codes
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Medium",
        "question": "Where are command codes specified in an IMS SSA?",
        "option_1": "Before the segment name",
        "option_2": "After the segment name, before the qualification",
        "option_3": "In the PCB",
        "option_4": "In a separate parameter",
        "choice_type": "Single Choice",
        "correct_answer": ["option_2"]
    })
    num += 1
    
    questions.append({
        "questionnumber": num,
        "topic": "IMS DB",
        "difficulty": "Hard",
        "question": "What does the 'P' command code do in an IMS path call?",
        "option_1": "Processes only parent segments",
        "option_2": "Sets the position to the specified segment",
        "option_3": "Specifies that this segment is to be returned in the path",
        "option_4": "Performs parallel processing",
        "choice_type": "Single Choice",
        "correct_answer": ["option_3"]
    })
    num += 1
    
    return questions, num

def generate_all_additional_questions():
    """Generate all additional questions"""
    all_questions = []
    current_num = 1  # Will be adjusted later
    
    # Generate from all categories
    qs, current_num = generate_dli_call_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_ssa_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_hierarchy_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_pcb_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_dbd_psb_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_segment_field_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_navigation_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_status_code_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_cobol_ims_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_processing_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_path_call_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_batch_program_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_additional_concepts_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_field_sensitivity_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_checkpoint_restart_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_command_code_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_secondary_index_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_logical_relationship_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_database_positioning_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_concatenated_key_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_data_integrity_questions(current_num)
    all_questions.extend(qs)
    
    # Additional rounds
    qs, current_num = generate_more_ssa_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_more_dli_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_more_hierarchy_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_more_segment_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_more_pcb_status_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_more_insert_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_more_delete_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_more_replace_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_more_processing_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_more_cobol_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_more_misc_questions(current_num)
    all_questions.extend(qs)
    
    qs, current_num = generate_even_more_questions(current_num)
    all_questions.extend(qs)
    
    return all_questions

if __name__ == '__main__':
    questions = generate_all_additional_questions()
    print(f"Generated {len(questions)} additional questions")
    
    if questions:  # Safety check for empty list
        print(f"Question numbers: {questions[0]['questionnumber']} to {questions[-1]['questionnumber']}")
    else:
        print("Warning: No questions generated")
    
    # Save to file
    with open('additional_questions.json', 'w') as f:
        json.dump(questions, f, indent=2)
    
    print("✓ Saved to additional_questions.json")
