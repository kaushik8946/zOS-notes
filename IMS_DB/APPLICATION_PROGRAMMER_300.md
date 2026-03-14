# IMS DB Application Programmer - 300 Questions

**Total Questions:** 300

**Distribution by Module:**
- Module 1 (Hierarchical Structures): 40 questions
- Module 2 (Control Blocks - DBD/PSB/PCB): 40 questions
- Module 3 (COBOL DL/I Programming): 35 questions
- Module 4 (SSAs): 45 questions
- Module 5 (Data Retrieval - GU/GN/GNP/GHU/GHN/GHNP): 45 questions
- Module 6 (Modification - ISRT/REPL/DLET): 40 questions
- Module 7 (Secondary Indexing): 20 questions
- Module 8 (Logical Databases): 10 questions
- Module 9 (Recovery/Restart): 10 questions
- Module 10 (Database Organizations): 10 questions
- Module 11 (Advanced Features): 5 questions

---

### Q1. What is the top segment in an IMS hierarchy called?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Easy
**Type:** Single Choice

1. Root segment
2. Parent segment
3. Master segment
4. Top segment

**Correct Answer:** Option 1

---

### Q2. How many root segments can a database have?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Easy
**Type:** Single Choice

1. Only one
2. Two
3. Unlimited
4. Depends on DBD

**Correct Answer:** Option 1

---

### Q3. What is a twin segment?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Easy
**Type:** Single Choice

1. Segments with same parent and segment type
2. Identical segments
3. Duplicate segments
4. Backup segments

**Correct Answer:** Option 1

---

### Q4. What defines parent-child relationship?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Medium
**Type:** Single Choice

1. Physical child pointer
2. Logical pointer
3. DBD specification
4. PSB mapping

**Correct Answer:** Option 1

---

### Q5. What is a dependent segment?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Easy
**Type:** Single Choice

1. A segment below root in hierarchy
2. A deleted segment
3. A backup segment
4. An indexed segment

**Correct Answer:** Option 1

---

### Q6. Maximum hierarchy levels in IMS?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Medium
**Type:** Single Choice

1. 15
2. 20
3. 10
4. 255

**Correct Answer:** Option 1

---

### Q7. What is a physical child?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Easy
**Type:** Single Choice

1. Segment directly connected in DBD
2. Any descendant
3. Root segment
4. Indexed segment

**Correct Answer:** Option 1

---

### Q8. Hierarchical path means?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Easy
**Type:** Single Choice

1. Route from root to target segment
2. All segments
3. Database structure
4. Index path

**Correct Answer:** Option 1

---

### Q9. What is segment occurrence?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Easy
**Type:** Single Choice

1. Instance of segment type
2. Segment definition
3. Segment pointer
4. Segment buffer

**Correct Answer:** Option 1

---

### Q10. How are twins ordered?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Medium
**Type:** Single Choice

1. By sequence field or insertion
2. Randomly
3. By size
4. Alphabetically

**Correct Answer:** Option 1

---

### Q11. What is a child segment?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Easy
**Type:** Single Choice

1. Segment one level below parent
2. Any dependent
3. Root segment
4. Last segment

**Correct Answer:** Option 1

---

### Q12. Hierarchical sequence means?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Medium
**Type:** Single Choice

1. Top to bottom, left to right order
2. Random order
3. Size order
4. Time order

**Correct Answer:** Option 1

---

### Q13. What determines segment position?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Medium
**Type:** Single Choice

1. Sequence field or FIRST/LAST/HERE
2. Random
3. Size
4. Creation time

**Correct Answer:** Option 1

---

### Q14. Leaf segment is?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Easy
**Type:** Single Choice

1. Segment with no children
2. Root segment
3. First segment
4. Deleted segment

**Correct Answer:** Option 1

---

### Q15. Sibling segments are?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Easy
**Type:** Single Choice

1. Segments sharing same parent
2. Any related segments
3. Root segments
4. Deleted segments

**Correct Answer:** Option 1

---

### Q16. What is database record?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Medium
**Type:** Single Choice

1. Root and all dependents
2. Single segment
3. Database definition
4. PCB entry

**Correct Answer:** Option 1

---

### Q17. Descendant segment is?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Easy
**Type:** Single Choice

1. Any segment below in hierarchy
2. Direct child only
3. Root segment
4. Peer segment

**Correct Answer:** Option 1

---

### Q18. What maintains hierarchy?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Medium
**Type:** Single Choice

1. Pointer systems in database
2. DBD only
3. PSB only
4. Application code

**Correct Answer:** Option 1

---

### Q19. Parent-child link uses?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Medium
**Type:** Single Choice

1. Physical or logical pointers
2. Keys only
3. Names only
4. Indexes

**Correct Answer:** Option 1

---

### Q20. Multiple parents possible?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Hard
**Type:** Single Choice

1. Yes, with logical relationships
2. No, never
3. Only for root
4. Only in HDAM

**Correct Answer:** Option 1

---

### Q21. Hierarchical precedence is?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Medium
**Type:** Single Choice

1. Processing order in hierarchy
2. Segment priority
3. Access method
4. Database type

**Correct Answer:** Option 1

---

### Q22. What is segment level?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Easy
**Type:** Single Choice

1. Distance from root
2. Segment size
3. Number of children
4. Processing order

**Correct Answer:** Option 1

---

### Q23. Root segment count per record?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Easy
**Type:** Single Choice

1. Always one
2. Multiple allowed
3. Zero allowed
4. Depends on organization

**Correct Answer:** Option 1

---

### Q24. How to identify twins?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Medium
**Type:** Single Choice

1. Sequence field value
2. Memory address
3. Creation time
4. Segment name

**Correct Answer:** Option 1

---

### Q25. Hierarchical structure stored in?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Easy
**Type:** Single Choice

1. DBD
2. PSB
3. PCB
4. ACB

**Correct Answer:** Option 1

---

### Q26. Physical parent is?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Medium
**Type:** Single Choice

1. Segment defined as parent in DBD
2. Any ancestor
3. Root segment
4. Previous segment

**Correct Answer:** Option 1

---

### Q27. What is segment type?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Easy
**Type:** Single Choice

1. Segment name definition in DBD
2. Segment instance
3. Segment value
4. Segment pointer

**Correct Answer:** Option 1

---

### Q28. Sequence field purpose?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Easy
**Type:** Single Choice

1. Order twins uniquely
2. Index database
3. Point to parent
4. Store data

**Correct Answer:** Option 1

---

### Q29. Concatenated key is?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Hard
**Type:** Single Choice

1. All sequence fields from root to segment
2. Multiple keys
3. Compound key
4. Foreign key

**Correct Answer:** Option 1

---

### Q30. How many children types allowed?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Medium
**Type:** Single Choice

1. Multiple segment types
2. Only one
3. Two maximum
4. Depends on DBDGEN

**Correct Answer:** Option 1

---

### Q31. Hierarchical integrity means?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Medium
**Type:** Single Choice

1. Parent-child relationships maintained
2. No duplicates
3. Indexed properly
4. Backed up

**Correct Answer:** Option 1

---

### Q32. Delete root deletes?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Medium
**Type:** Single Choice

1. All dependents automatically
2. Root only
3. Nothing
4. Requires manual deletion

**Correct Answer:** Option 1

---

### Q33. Position in hierarchy affects?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Hard
**Type:** Single Choice

1. Access path and DL/I calls needed
2. Segment size
3. Segment name
4. Nothing

**Correct Answer:** Option 1

---

### Q34. Fully concatenated key includes?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Hard
**Type:** Single Choice

1. All keys from root to segment
2. Segment key only
3. Parent key only
4. All segment keys

**Correct Answer:** Option 1

---

### Q35. Hierarchical pointers maintain?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Medium
**Type:** Single Choice

1. Parent-child and twin relationships
2. Data only
3. Index only
4. Nothing

**Correct Answer:** Option 1

---

### Q36. Path call retrieves?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Hard
**Type:** Single Choice

1. Segment and all ancestors
2. Segment only
3. All descendants
4. Root only

**Correct Answer:** Option 1

---

### Q37. Insert segment requires?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Medium
**Type:** Single Choice

1. Parent must exist
2. Root exists only
3. Nothing
4. Index exists

**Correct Answer:** Option 1

---

### Q38. Twin chain is?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Hard
**Type:** Single Choice

1. Linked list of same segment type under parent
2. Any segments
3. Root segments
4. Index entries

**Correct Answer:** Option 1

---

### Q39. Hierarchical access means?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Medium
**Type:** Single Choice

1. Must traverse from root
2. Direct access only
3. Random access
4. Sequential only

**Correct Answer:** Option 1

---

### Q40. Segment sensitivity in PSB affects?

**Topic:** IMS DB - Hierarchical Structures
**Difficulty:** Hard
**Type:** Single Choice

1. Which segments application can access
2. Segment size
3. Segment location
4. Nothing

**Correct Answer:** Option 1

---

### Q41. What does DBD stand for?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Easy
**Type:** Single Choice

1. Database Description
2. Database Definition
3. Data Block Description
4. Direct Block Data

**Correct Answer:** Option 1

---

### Q42. What does PSB stand for?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Easy
**Type:** Single Choice

1. Program Specification Block
2. Program Structure Block
3. Processing Segment Block
4. Program Status Block

**Correct Answer:** Option 1

---

### Q43. What does PCB stand for?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Easy
**Type:** Single Choice

1. Program Communication Block
2. Program Control Block
3. Processing Control Block
4. Program Code Block

**Correct Answer:** Option 1

---

### Q44. DBD is created using?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Easy
**Type:** Single Choice

1. DBDGEN utility
2. PSBGEN utility
3. ACBGEN utility
4. Compiler

**Correct Answer:** Option 1

---

### Q45. PSB is created using?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Easy
**Type:** Single Choice

1. PSBGEN utility
2. DBDGEN utility
3. Compiler
4. Linkage editor

**Correct Answer:** Option 1

---

### Q46. PCB is contained in?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Easy
**Type:** Single Choice

1. PSB
2. DBD
3. ACB
4. Application code

**Correct Answer:** Option 1

---

### Q47. DBD defines?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Easy
**Type:** Single Choice

1. Physical database structure
2. Program view
3. Application logic
4. Processing options

**Correct Answer:** Option 1

---

### Q48. PSB defines?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Easy
**Type:** Single Choice

1. Application's view of database
2. Physical structure
3. Storage method
4. Access method

**Correct Answer:** Option 1

---

### Q49. How many PCBs in a PSB?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. One or more
2. Always one
3. Exactly two
4. Maximum five

**Correct Answer:** Option 1

---

### Q50. PCB defines?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. Database view for specific processing
2. Physical structure
3. All databases
4. Storage allocation

**Correct Answer:** Option 1

---

### Q51. SENSEG in PSB means?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Easy
**Type:** Single Choice

1. Sensitive segment
2. Sensor segment
3. Sequential segment
4. Secondary segment

**Correct Answer:** Option 1

---

### Q52. Processing options in SENSEG?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. G, I, R, D, A
2. Read, Write
3. Input, Output
4. Get, Put

**Correct Answer:** Option 1

---

### Q53. What is PROCOPT=G?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Easy
**Type:** Single Choice

1. Get (read only)
2. Get and Insert
3. General processing
4. Generate

**Correct Answer:** Option 1

---

### Q54. What is PROCOPT=GI?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. Get and Insert
2. Get Index
3. General Insert
4. Get Information

**Correct Answer:** Option 1

---

### Q55. What is PROCOPT=GIRD?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. Get, Insert, Replace, Delete
2. General processing
3. Get Index Read Delete
4. Get Insert Retrieve Data

**Correct Answer:** Option 1

---

### Q56. ACB stands for?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Easy
**Type:** Single Choice

1. Application Control Block
2. Access Control Block
3. Active Control Block
4. Application Code Block

**Correct Answer:** Option 1

---

### Q57. ACB is created from?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. DBD and PSB
2. DBD only
3. PSB only
4. Application source

**Correct Answer:** Option 1

---

### Q58. PSBGEN combines?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Easy
**Type:** Single Choice

1. PCB definitions
2. DBD definitions
3. Segments
4. Applications

**Correct Answer:** Option 1

---

### Q59. Key feedback area in PCB?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. Returns concatenated key
2. Returns status code
3. Returns segment name
4. Returns nothing

**Correct Answer:** Option 1

---

### Q60. Status code returned where?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Easy
**Type:** Single Choice

1. PCB status code field
2. Working storage
3. Linkage section
4. File section

**Correct Answer:** Option 1

---

### Q61. Successful call status?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Easy
**Type:** Single Choice

1. Blank or spaces
2. OK
3. 00
4. SUCCESS

**Correct Answer:** Option 1

---

### Q62. GE status code means?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. Segment not found
2. Get error
3. General error
4. Good entry

**Correct Answer:** Option 1

---

### Q63. GB status code means?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. End of database
2. Get blank
3. Good batch
4. Go back

**Correct Answer:** Option 1

---

### Q64. II status code means?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Hard
**Type:** Single Choice

1. Insert error - segment exists
2. Invalid insert
3. Index issue
4. Insert incomplete

**Correct Answer:** Option 1

---

### Q65. DBD NAME specifies?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Easy
**Type:** Single Choice

1. Database name
2. Dataset name
3. Program name
4. Segment name

**Correct Answer:** Option 1

---

### Q66. SEGM statement in DBD defines?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. Segment type
2. Processing option
3. Program view
4. Storage size

**Correct Answer:** Option 1

---

### Q67. FIELD statement in DBD defines?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. Field within segment
2. Entire segment
3. Database
4. Processing option

**Correct Answer:** Option 1

---

### Q68. DATASET in DBD specifies?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. Physical dataset name
2. Logical dataset
3. Program name
4. Segment name

**Correct Answer:** Option 1

---

### Q69. PCB mask in COBOL is?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. 01 level structure in linkage
2. Working storage field
3. File definition
4. Procedure division item

**Correct Answer:** Option 1

---

### Q70. How many DBDs for one database?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Easy
**Type:** Single Choice

1. One
2. Two
3. Multiple
4. Depends on size

**Correct Answer:** Option 1

---

### Q71. How many PSBs for one DBD?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. Multiple allowed
2. One only
3. Two only
4. None

**Correct Answer:** Option 1

---

### Q72. PROCOPT=A means?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Hard
**Type:** Single Choice

1. All processing options
2. Add only
3. Alter only
4. Access only

**Correct Answer:** Option 1

---

### Q73. Sensitive segment means?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. Application can access it
2. Segment is protected
3. Segment is indexed
4. Segment is deleted

**Correct Answer:** Option 1

---

### Q74. Non-sensitive segment means?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. Application cannot access it
2. Segment is public
3. Segment is unprotected
4. Segment is optional

**Correct Answer:** Option 1

---

### Q75. DBD ACCESS specifies?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Hard
**Type:** Single Choice

1. Database organization type
2. Processing option
3. Application access
4. Security level

**Correct Answer:** Option 1

---

### Q76. LCHILD in DBD defines?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Hard
**Type:** Single Choice

1. Logical child relationship
2. Last child
3. Linked child
4. Lower child

**Correct Answer:** Option 1

---

### Q77. XDFLD in DBD defines?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Hard
**Type:** Single Choice

1. Secondary index field
2. Extra field
3. Extended field
4. External field

**Correct Answer:** Option 1

---

### Q78. PSB language parameter?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. COBOL, PL/I, ASSEM, etc.
2. English only
3. Any language
4. Compiled language

**Correct Answer:** Option 1

---

### Q79. Multiple database PCBs?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Medium
**Type:** Single Choice

1. Allowed in one PSB
2. Not allowed
3. Maximum two
4. Requires special DBDGEN

**Correct Answer:** Option 1

---

### Q80. I/O area purpose?

**Topic:** IMS DB - Control Blocks (DBD/PSB/PCB)
**Difficulty:** Easy
**Type:** Single Choice

1. Hold segment data for DL/I call
2. Store PCB
3. Store DBD
4. Store status

**Correct Answer:** Option 1

---

### Q81. DL/I call format in COBOL?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Easy
**Type:** Single Choice

1. CALL 'CBLTDLI' USING...
2. CALL 'DLITCBL' USING...
3. EXEC DLI
4. CALL DLI

**Correct Answer:** Option 1

---

### Q82. First parameter in DL/I call?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Easy
**Type:** Single Choice

1. Function code
2. PCB
3. I/O area
4. SSA

**Correct Answer:** Option 1

---

### Q83. Second parameter in DL/I call?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Easy
**Type:** Single Choice

1. PCB mask
2. Function code
3. I/O area
4. SSA

**Correct Answer:** Option 1

---

### Q84. Third parameter in DL/I call?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Easy
**Type:** Single Choice

1. I/O area
2. Function code
3. PCB
4. SSA

**Correct Answer:** Option 1

---

### Q85. PCB mask defined in?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Easy
**Type:** Single Choice

1. LINKAGE SECTION
2. WORKING-STORAGE
3. PROCEDURE DIVISION
4. FILE SECTION

**Correct Answer:** Option 1

---

### Q86. I/O area defined in?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Easy
**Type:** Single Choice

1. WORKING-STORAGE SECTION
2. LINKAGE SECTION
3. PROCEDURE DIVISION
4. FILE SECTION

**Correct Answer:** Option 1

---

### Q87. Entry parameter list contains?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Medium
**Type:** Single Choice

1. PCB addresses
2. PCB values
3. Segment data
4. Status codes

**Correct Answer:** Option 1

---

### Q88. ENTRY statement in DL/I program?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Medium
**Type:** Single Choice

1. Receives PCB pointers from IMS
2. Defines entry point
3. Calls DL/I
4. Exits program

**Correct Answer:** Option 1

---

### Q89. GOBACK statement in DL/I?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Easy
**Type:** Single Choice

1. Returns control to IMS
2. Goes to previous call
3. Restarts program
4. Calls subroutine

**Correct Answer:** Option 1

---

### Q90. Status code checked after?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Easy
**Type:** Single Choice

1. Every DL/I call
2. Program start only
3. End of program
4. Not required

**Correct Answer:** Option 1

---

### Q91. Successful status code?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Easy
**Type:** Single Choice

1. Spaces or blank
2. Zero
3. OK
4. 00

**Correct Answer:** Option 1

---

### Q92. How to check status in COBOL?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Medium
**Type:** Single Choice

1. IF DB-STATUS = SPACES
2. IF STATUS = 0
3. IF RC = 0
4. IF DLI-OK

**Correct Answer:** Option 1

---

### Q93. I/O area must be?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Medium
**Type:** Single Choice

1. 01 level in WORKING-STORAGE
2. 77 level field
3. In LINKAGE
4. In FILE SECTION

**Correct Answer:** Option 1

---

### Q94. PCB mask structure?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Medium
**Type:** Single Choice

1. 01 level with defined fields
2. 77 level field
3. Array
4. Table

**Correct Answer:** Option 1

---

### Q95. DBD name in PCB mask?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Hard
**Type:** Single Choice

1. PIC X(8) field
2. PIC X(4) field
3. PIC 9(8) field
4. PIC X(16)

**Correct Answer:** Option 1

---

### Q96. Segment level in PCB?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Hard
**Type:** Single Choice

1. PIC XX field
2. PIC 9(4) field
3. PIC X(4) field
4. PIC S9(4)

**Correct Answer:** Option 1

---

### Q97. Status code field in PCB?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Medium
**Type:** Single Choice

1. PIC XX field
2. PIC X(4) field
3. PIC 9(2) field
4. PIC S9(4)

**Correct Answer:** Option 1

---

### Q98. Processing options in PCB mask?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Hard
**Type:** Single Choice

1. PIC X(4) field
2. PIC XX field
3. PIC 9(4) field
4. PIC X(8)

**Correct Answer:** Option 1

---

### Q99. Key feedback area length?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Hard
**Type:** Single Choice

1. PIC S9(4) COMP
2. PIC X(4)
3. PIC 9(4)
4. PIC XX

**Correct Answer:** Option 1

---

### Q100. SSA defined as?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Medium
**Type:** Single Choice

1. PIC X field in WORKING-STORAGE
2. In LINKAGE
3. In PCB
4. In I/O area

**Correct Answer:** Option 1

---

### Q101. Unqualified SSA length?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Medium
**Type:** Single Choice

1. 9 bytes
2. 8 bytes
3. 10 bytes
4. Variable

**Correct Answer:** Option 1

---

### Q102. Qualified SSA structure?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Hard
**Type:** Single Choice

1. Segment-name + open-paren + qualification + close-paren
2. Segment-name only
3. Qualification only
4. Command code only

**Correct Answer:** Option 1

---

### Q103. Function code length?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Medium
**Type:** Single Choice

1. 4 bytes
2. 2 bytes
3. 8 bytes
4. Variable

**Correct Answer:** Option 1

---

### Q104. GU function code?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Easy
**Type:** Single Choice

1. 'GU  '
2. 'GET '
3. 'GETU'
4. 'GNUN'

**Correct Answer:** Option 1

---

### Q105. GN function code?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Easy
**Type:** Single Choice

1. 'GN  '
2. 'GNET'
3. 'GNXT'
4. 'NEXT'

**Correct Answer:** Option 1

---

### Q106. ISRT function code?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Easy
**Type:** Single Choice

1. 'ISRT'
2. 'INS '
3. 'ADD '
4. 'PUT '

**Correct Answer:** Option 1

---

### Q107. How to pass SSA count?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Hard
**Type:** Single Choice

1. Implicitly by number of SSAs
2. Explicit count parameter
3. In PCB
4. In function code

**Correct Answer:** Option 1

---

### Q108. Compiler option for DL/I?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Medium
**Type:** Single Choice

1. None specific required
2. DYNAM
3. DLI
4. IMS

**Correct Answer:** Option 1

---

### Q109. Link-edit with what stub?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Hard
**Type:** Single Choice

1. DFSLI000 or appropriate stub
2. ILBDLI00
3. CBLDLI
4. IMSDLI

**Correct Answer:** Option 1

---

### Q110. Where to code ENTRY?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Medium
**Type:** Single Choice

1. PROCEDURE DIVISION USING
2. WORKING-STORAGE
3. LINKAGE SECTION
4. IDENTIFICATION DIVISION

**Correct Answer:** Option 1

---

### Q111. Multiple PCBs referenced by?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Hard
**Type:** Single Choice

1. Position in ENTRY USING list
2. PCB name
3. PCB number
4. DBD name

**Correct Answer:** Option 1

---

### Q112. AIB alternative to?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Hard
**Type:** Single Choice

1. PCB list in ENTRY
2. I/O area
3. SSA
4. Function code

**Correct Answer:** Option 1

---

### Q113. COBOL COMP for length fields?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Medium
**Type:** Single Choice

1. Binary numeric
2. Packed decimal
3. Display numeric
4. ASCII

**Correct Answer:** Option 1

---

### Q114. Standard sequence for call?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Hard
**Type:** Single Choice

1. Function, PCB, I/O area, SSAs
2. PCB, Function, I/O, SSAs
3. I/O, PCB, Function, SSAs
4. SSAs, Function, PCB, I/O

**Correct Answer:** Option 1

---

### Q115. Return code location?

**Topic:** IMS DB - COBOL DL/I Programming
**Difficulty:** Medium
**Type:** Single Choice

1. DB-PCB-STATUS in PCB mask
2. RETURN-CODE special register
3. I/O area
4. SSA

**Correct Answer:** Option 1

---

### Q116. SSA stands for?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Easy
**Type:** Single Choice

1. Segment Search Argument
2. Segment Selection Area
3. System Search Argument
4. Sequential Search Area

**Correct Answer:** Option 1

---

### Q117. Unqualified SSA contains?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Easy
**Type:** Single Choice

1. Segment name only
2. Segment name and qualification
3. Qualification only
4. Command codes only

**Correct Answer:** Option 1

---

### Q118. Qualified SSA contains?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Easy
**Type:** Single Choice

1. Segment name and field qualification
2. Segment name only
3. Command codes only
4. Nothing

**Correct Answer:** Option 1

---

### Q119. SSA segment name length?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. 8 bytes
2. 4 bytes
3. 10 bytes
4. Variable

**Correct Answer:** Option 1

---

### Q120. Unqualified SSA format?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. SEGNAME + space
2. SEGNAME*
3. SEGNAME()
4. SEGNAME

**Correct Answer:** Option 1

---

### Q121. Qualified SSA starts with?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. Segment name + left paren
2. Segment name + asterisk
3. Segment name + space
4. Just field name

**Correct Answer:** Option 1

---

### Q122. Qualified SSA ends with?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. Right paren + space
2. Right paren only
3. Space only
4. Asterisk

**Correct Answer:** Option 1

---

### Q123. SSA qualification format?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. FIELDNAME OPERATOR VALUE
2. OPERATOR FIELDNAME VALUE
3. VALUE OPERATOR FIELDNAME
4. FIELDNAME VALUE

**Correct Answer:** Option 1

---

### Q124. Equal operator in SSA?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Easy
**Type:** Single Choice

1. = (EQ)
2. EQ only
3. == (EQ)
4. .EQ.

**Correct Answer:** Option 1

---

### Q125. Greater than operator?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Easy
**Type:** Single Choice

1. > (GT)
2. GT only
3. .GT.
4. =>

**Correct Answer:** Option 1

---

### Q126. Less than operator?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Easy
**Type:** Single Choice

1. < (LT)
2. LT only
3. .LT.
4. =<

**Correct Answer:** Option 1

---

### Q127. Greater or equal operator?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Easy
**Type:** Single Choice

1. >= (GE)
2. GE only
3. .GE.
4. =>

**Correct Answer:** Option 1

---

### Q128. Less or equal operator?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Easy
**Type:** Single Choice

1. <= (LE)
2. LE only
3. .LE.
4. =<

**Correct Answer:** Option 1

---

### Q129. Not equal operator?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. ¬= (NE)
2. NE only
3. .NE.
4. <>

**Correct Answer:** Option 1

---

### Q130. Command code position?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. After segment name, before paren
2. Before segment name
3. After paren
4. At end

**Correct Answer:** Option 1

---

### Q131. Command code indicator?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Easy
**Type:** Single Choice

1. Asterisk (*)
2. Ampersand (&)
3. Percent (%)
4. Hash (#)

**Correct Answer:** Option 1

---

### Q132. Multiple command codes separated by?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. No separator, consecutive
2. Comma
3. Space
4. Semicolon

**Correct Answer:** Option 1

---

### Q133. F command code means?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Easy
**Type:** Single Choice

1. First occurrence
2. Find
3. Forward
4. Fast

**Correct Answer:** Option 1

---

### Q134. L command code means?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Easy
**Type:** Single Choice

1. Last occurrence
2. Locate
3. Link
4. Loop

**Correct Answer:** Option 1

---

### Q135. D command code means?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. Path call
2. Delete
3. Direct
4. Data

**Correct Answer:** Option 1

---

### Q136. P command code means?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Hard
**Type:** Single Choice

1. Set parentage
2. Path
3. Parent
4. Position

**Correct Answer:** Option 1

---

### Q137. U command code means?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Hard
**Type:** Single Choice

1. Maintain position
2. Update
3. Unload
4. Unique

**Correct Answer:** Option 1

---

### Q138. V command code means?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Hard
**Type:** Single Choice

1. Use current position
2. Verify
3. Value
4. View

**Correct Answer:** Option 1

---

### Q139. C command code means?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Hard
**Type:** Single Choice

1. Concatenated key
2. Continue
3. Check
4. Count

**Correct Answer:** Option 1

---

### Q140. N command code means?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Hard
**Type:** Single Choice

1. Path call, this level only
2. Next
3. Null
4. Navigate

**Correct Answer:** Option 1

---

### Q141. Q command code means?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Hard
**Type:** Single Choice

1. Enqueue segment
2. Query
3. Queue
4. Qualified

**Correct Answer:** Option 1

---

### Q142. Multiple qualifications use?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Hard
**Type:** Single Choice

1. Boolean operators
2. Comma separator
3. AND implied
4. OR operator

**Correct Answer:** Option 1

---

### Q143. Boolean AND operator?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Hard
**Type:** Single Choice

1. * (ampersand &)
2. AND
3. +
4. .AND.

**Correct Answer:** Option 1

---

### Q144. Boolean OR operator?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Hard
**Type:** Single Choice

1. + (plus)
2. OR
3. |
4. .OR.

**Correct Answer:** Option 1

---

### Q145. SSA field name length?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. 8 bytes
2. 4 bytes
3. 10 bytes
4. Variable

**Correct Answer:** Option 1

---

### Q146. Qualification value length?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. Variable, field dependent
2. Fixed 8 bytes
3. Fixed 4 bytes
4. Fixed 10 bytes

**Correct Answer:** Option 1

---

### Q147. Generic search uses?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Hard
**Type:** Single Choice

1. *= operator
2. %= operator
3. ~= operator
4. &= operator

**Correct Answer:** Option 1

---

### Q148. SSA for root segment?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Easy
**Type:** Single Choice

1. Root segment name
2. Empty SSA
3. NULL
4. Not required

**Correct Answer:** Option 1

---

### Q149. Second SSA is for?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. Child under previously specified segment
2. Any segment
3. Root only
4. Last segment

**Correct Answer:** Option 1

---

### Q150. SSA hierarchy matches?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. Database hierarchy
2. PSB hierarchy
3. PCB hierarchy
4. Application hierarchy

**Correct Answer:** Option 1

---

### Q151. Invalid SSA causes?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. Status code error
2. Compilation error
3. Runtime crash
4. Warning only

**Correct Answer:** Option 1

---

### Q152. SSA qualification field must be?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. Defined in DBD
2. In PCB
3. In PSB
4. In I/O area

**Correct Answer:** Option 1

---

### Q153. Multiple SSAs in one call?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. Specifies hierarchical path
2. Not allowed
3. Optional only
4. For parallel processing

**Correct Answer:** Option 1

---

### Q154. No SSA provided means?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Hard
**Type:** Single Choice

1. Use current position
2. Get root
3. Error
4. Get all

**Correct Answer:** Option 1

---

### Q155. SSA with GU call?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Easy
**Type:** Single Choice

1. Positions in database
2. Updates segment
3. Deletes segment
4. Inserts segment

**Correct Answer:** Option 1

---

### Q156. SSA with GN call?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. Continues sequential retrieval
2. Gets unique
3. Gets next root
4. Gets parent

**Correct Answer:** Option 1

---

### Q157. Unqualified SSA with GN?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. Gets next occurrence of segment type
2. Gets specific segment
3. Gets root
4. Gets all

**Correct Answer:** Option 1

---

### Q158. Command code position in qualified SSA?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Hard
**Type:** Single Choice

1. After segment name, before paren
2. Before segment name
3. After value
4. In qualification

**Correct Answer:** Option 1

---

### Q159. SSA blank padding?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Hard
**Type:** Single Choice

1. Required to fill segment name field
2. Not required
3. Optional
4. Forbidden

**Correct Answer:** Option 1

---

### Q160. Case sensitivity in SSA?

**Topic:** IMS DB - Segment Search Arguments (SSAs)
**Difficulty:** Medium
**Type:** Single Choice

1. Segment names must match DBD
2. Case insensitive
3. Upper case only
4. Lower case only

**Correct Answer:** Option 1

---

### Q161. GU stands for?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Easy
**Type:** Single Choice

1. Get Unique
2. Get Unit
3. General Update
4. Get Universal

**Correct Answer:** Option 1

---

### Q162. GN stands for?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Easy
**Type:** Single Choice

1. Get Next
2. Get New
3. General Navigation
4. Get Now

**Correct Answer:** Option 1

---

### Q163. GNP stands for?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Easy
**Type:** Single Choice

1. Get Next within Parent
2. Get Next Path
3. Get Next Position
4. Get New Parent

**Correct Answer:** Option 1

---

### Q164. GHU stands for?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Get Hold Unique
2. Get Hold Unit
3. General Hold Update
4. Get High Unique

**Correct Answer:** Option 1

---

### Q165. GHN stands for?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Get Hold Next
2. Get Hold New
3. Get High Next
4. General Hold Navigation

**Correct Answer:** Option 1

---

### Q166. GHNP stands for?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Get Hold Next within Parent
2. Get Hold Next Path
3. Get Hold New Position
4. Get High Next Parent

**Correct Answer:** Option 1

---

### Q167. GU call establishes?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Easy
**Type:** Single Choice

1. Initial position in database
2. Update mode
3. Insert position
4. Delete position

**Correct Answer:** Option 1

---

### Q168. GN call continues?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Easy
**Type:** Single Choice

1. Sequential retrieval from current position
2. From start
3. From end
4. Random retrieval

**Correct Answer:** Option 1

---

### Q169. GNP retrieves within?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Current parent's children
2. All database
3. Current level
4. Root segments

**Correct Answer:** Option 1

---

### Q170. GU without SSA?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Gets next root segment
2. Causes error
3. Gets any segment
4. Gets first root

**Correct Answer:** Option 1

---

### Q171. GN without SSA?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Gets next segment in hierarchical sequence
2. Causes error
3. Gets root
4. Gets random segment

**Correct Answer:** Option 1

---

### Q172. Hold call purpose?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Easy
**Type:** Single Choice

1. Enables subsequent update/delete
2. Holds position only
3. Locks database
4. Holds memory

**Correct Answer:** Option 1

---

### Q173. GHU allows?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. REPL or DLET of retrieved segment
2. Retrieval only
3. Insert only
4. Nothing special

**Correct Answer:** Option 1

---

### Q174. After successful GU?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Position set at retrieved segment
2. Position at root
3. Position unchanged
4. Position undefined

**Correct Answer:** Option 1

---

### Q175. After successful GN?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Position advances in hierarchical order
2. Position at root
3. Position unchanged
4. Position at end

**Correct Answer:** Option 1

---

### Q176. GN after GU?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Easy
**Type:** Single Choice

1. Gets next segment in sequence
2. Gets same segment
3. Causes error
4. Restarts from root

**Correct Answer:** Option 1

---

### Q177. GNP boundary is?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Current parent's children only
2. Entire database
3. Current level
4. All descendants

**Correct Answer:** Option 1

---

### Q178. GNP crossing parent?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Hard
**Type:** Single Choice

1. Returns GB status code
2. Continues to next parent
3. Causes error
4. Wraps to start

**Correct Answer:** Option 1

---

### Q179. GB status code means?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Easy
**Type:** Single Choice

1. End of database/parent boundary
2. Good batch
3. Get blank
4. Go back

**Correct Answer:** Option 1

---

### Q180. GE status code means?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Easy
**Type:** Single Choice

1. Segment not found
2. General error
3. Get error
4. Good entry

**Correct Answer:** Option 1

---

### Q181. Sequential processing uses?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Easy
**Type:** Single Choice

1. GU followed by GN calls
2. Multiple GU calls
3. GNP only
4. Random GU calls

**Correct Answer:** Option 1

---

### Q182. Path call retrieves?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Hard
**Type:** Single Choice

1. Segment and all parents
2. Segment only
3. All children
4. Nothing special

**Correct Answer:** Option 1

---

### Q183. D command code in retrieval?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Hard
**Type:** Single Choice

1. Returns segment and parents in I/O area
2. Deletes segment
3. Direct access
4. Data only

**Correct Answer:** Option 1

---

### Q184. Qualified SSA with GU?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Retrieves specific segment matching criteria
2. Retrieves any segment
3. Causes error
4. Retrieves root

**Correct Answer:** Option 1

---

### Q185. Multiple SSAs with GU?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Establishes hierarchical path to target
2. Not allowed
3. Optional
4. For multiple segments

**Correct Answer:** Option 1

---

### Q186. GN with qualified SSA?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Gets next matching segment
2. Gets any next
3. Causes error
4. Resets position

**Correct Answer:** Option 1

---

### Q187. Current position maintained?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. After successful retrieval
2. Always reset
3. Never maintained
4. Only with U command

**Correct Answer:** Option 1

---

### Q188. Hierarchical sequence is?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Easy
**Type:** Single Choice

1. Root to leaf, left to right
2. Random
3. Reverse
4. By size

**Correct Answer:** Option 1

---

### Q189. Retrieving twins?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Sequential GN calls
2. Multiple GU calls
3. Special command
4. Not possible

**Correct Answer:** Option 1

---

### Q190. F command code with GU?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Gets first occurrence of twin
2. Fast retrieval
3. Full retrieval
4. Forward only

**Correct Answer:** Option 1

---

### Q191. L command code with GU?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Gets last occurrence of twin
2. Locked retrieval
3. Leaf only
4. Last in database

**Correct Answer:** Option 1

---

### Q192. After unsuccessful GU?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Hard
**Type:** Single Choice

1. Position undefined
2. Position unchanged
3. Position at root
4. Position at end

**Correct Answer:** Option 1

---

### Q193. GN at end of database?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Easy
**Type:** Single Choice

1. Returns GB status
2. Wraps to start
3. Causes error
4. Returns blank

**Correct Answer:** Option 1

---

### Q194. Retrieve by key?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. GU with qualified SSA on key field
2. GN with key
3. Special call
4. Not supported

**Correct Answer:** Option 1

---

### Q195. Concatenated key in SSA?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Hard
**Type:** Single Choice

1. C command code required
2. Automatically handled
3. Not supported
4. Optional

**Correct Answer:** Option 1

---

### Q196. Position after GNP boundary?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Hard
**Type:** Single Choice

1. Unchanged from before GNP
2. At next parent
3. At root
4. Undefined

**Correct Answer:** Option 1

---

### Q197. Retrieve all children of parent?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Hard
**Type:** Single Choice

1. GU parent, then GNP loop
2. Multiple GU
3. GN loop
4. Special call

**Correct Answer:** Option 1

---

### Q198. Get segment count?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Hard
**Type:** Single Choice

1. Count with loop, check GB
2. COUNT function
3. Special call
4. Not possible

**Correct Answer:** Option 1

---

### Q199. Retrieve backwards?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Not directly supported by calls
2. GN with reverse
3. Special call
4. GNPREV call

**Correct Answer:** Option 1

---

### Q200. Retrieve same segment again?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Issue same call again
2. Not possible
3. Special call
4. Use cache

**Correct Answer:** Option 1

---

### Q201. Hold followed by Get?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Hard
**Type:** Single Choice

1. Releases hold
2. Maintains hold
3. Causes error
4. Undefined

**Correct Answer:** Option 1

---

### Q202. Key feedback area contains?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Concatenated key of retrieved segment
2. Segment data
3. Status code
4. Position

**Correct Answer:** Option 1

---

### Q203. Get with PROCOPT=G?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Easy
**Type:** Single Choice

1. Allowed
2. Not allowed
3. Causes warning
4. Conditional

**Correct Answer:** Option 1

---

### Q204. Hold with PROCOPT=G?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Medium
**Type:** Single Choice

1. Not allowed, requires R
2. Allowed
3. Causes warning
4. Conditional

**Correct Answer:** Option 1

---

### Q205. Get deleted segment?

**Topic:** IMS DB - Data Retrieval (GU/GN/GNP/GHU/GHN/GHNP)
**Difficulty:** Hard
**Type:** Single Choice

1. Returns GE status
2. Returns segment
3. Causes error
4. Returns GB

**Correct Answer:** Option 1

---

### Q206. ISRT stands for?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Easy
**Type:** Single Choice

1. Insert
2. Initial Set Record Transaction
3. Insert Sorted Record Transaction
4. Initialize Record

**Correct Answer:** Option 1

---

### Q207. REPL stands for?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Easy
**Type:** Single Choice

1. Replace
2. Replicate
3. Reply
4. Report

**Correct Answer:** Option 1

---

### Q208. DLET stands for?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Easy
**Type:** Single Choice

1. Delete
2. Detail
3. Delay
4. Deliver

**Correct Answer:** Option 1

---

### Q209. ISRT requires PROCOPT?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Easy
**Type:** Single Choice

1. I (Insert)
2. G (Get)
3. R (Replace)
4. D (Delete)

**Correct Answer:** Option 1

---

### Q210. REPL requires PROCOPT?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Easy
**Type:** Single Choice

1. R (Replace)
2. I (Insert)
3. G (Get)
4. D (Delete)

**Correct Answer:** Option 1

---

### Q211. DLET requires PROCOPT?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Easy
**Type:** Single Choice

1. D (Delete)
2. I (Insert)
3. R (Replace)
4. G (Get)

**Correct Answer:** Option 1

---

### Q212. Before REPL must issue?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Easy
**Type:** Single Choice

1. Get Hold call
2. Get call
3. Insert call
4. Nothing

**Correct Answer:** Option 1

---

### Q213. Before DLET must issue?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Easy
**Type:** Single Choice

1. Get Hold call
2. Get call
3. Insert call
4. Nothing

**Correct Answer:** Option 1

---

### Q214. ISRT segment requires?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Medium
**Type:** Single Choice

1. Parent must exist
2. Nothing
3. Root exists
4. Index exists

**Correct Answer:** Option 1

---

### Q215. ISRT root segment?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Medium
**Type:** Single Choice

1. Creates new database record
2. Requires existing root
3. Not allowed
4. Special processing

**Correct Answer:** Option 1

---

### Q216. ISRT dependent segment needs?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Hard
**Type:** Single Choice

1. Qualified SSA path to parent
2. Root SSA only
3. No SSA
4. Delete old parent

**Correct Answer:** Option 1

---

### Q217. Multiple SSAs with ISRT?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Hard
**Type:** Single Choice

1. Specifies where to insert in hierarchy
2. Not allowed
3. Optional
4. For multiple inserts

**Correct Answer:** Option 1

---

### Q218. ISRT with duplicate key?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Medium
**Type:** Single Choice

1. Returns II status code
2. Overwrites
3. Causes error
4. Returns GB

**Correct Answer:** Option 1

---

### Q219. II status code means?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Easy
**Type:** Single Choice

1. Insert failed, duplicate
2. Insert incomplete
3. Invalid insert
4. Insert index

**Correct Answer:** Option 1

---

### Q220. REPL can change?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Hard
**Type:** Single Choice

1. Data fields only, not key
2. Everything including key
3. Nothing
4. Key only

**Correct Answer:** Option 1

---

### Q221. REPL changing key field?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Hard
**Type:** Single Choice

1. Causes LK status code error
2. Allowed if unique
3. Allowed always
4. Deletes segment

**Correct Answer:** Option 1

---

### Q222. LK status code means?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Hard
**Type:** Single Choice

1. Key field change attempted in REPL
2. Lock error
3. Link error
4. Last key

**Correct Answer:** Option 1

---

### Q223. DLET deletes?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Medium
**Type:** Single Choice

1. Segment and all dependents
2. Segment only
3. Nothing
4. Parent also

**Correct Answer:** Option 1

---

### Q224. DLET root segment?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Medium
**Type:** Single Choice

1. Deletes entire database record
2. Deletes root only
3. Not allowed
4. Requires parameter

**Correct Answer:** Option 1

---

### Q225. Hold call before REPL?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Easy
**Type:** Single Choice

1. Required
2. Optional
3. Not allowed
4. Recommended

**Correct Answer:** Option 1

---

### Q226. Hold call before DLET?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Easy
**Type:** Single Choice

1. Required
2. Optional
3. Not allowed
4. Recommended

**Correct Answer:** Option 1

---

### Q227. DA status code means?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Medium
**Type:** Single Choice

1. No segment found for DLET/REPL
2. Data available
3. Direct access
4. Delete all

**Correct Answer:** Option 1

---

### Q228. ISRT position rules?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Hard
**Type:** Single Choice

1. FIRST, LAST, HERE options
2. Random only
3. Automatic
4. Not controllable

**Correct Answer:** Option 1

---

### Q229. RULES=FIRST means?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Medium
**Type:** Single Choice

1. Insert at start of twin chain
2. Insert rule one
3. Insert first segment
4. Insert in root

**Correct Answer:** Option 1

---

### Q230. RULES=LAST means?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Medium
**Type:** Single Choice

1. Insert at end of twin chain
2. Insert last segment
3. Insert rule last
4. Insert in leaf

**Correct Answer:** Option 1

---

### Q231. RULES=HERE means?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Medium
**Type:** Single Choice

1. Insert at current position
2. Insert here now
3. Insert rule here
4. Insert in middle

**Correct Answer:** Option 1

---

### Q232. Sequence field in ISRT?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Hard
**Type:** Single Choice

1. Must be unique for keyed insertion
2. Not required
3. Optional
4. Ignored

**Correct Answer:** Option 1

---

### Q233. REPL without hold?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Medium
**Type:** Single Choice

1. Returns DA status code
2. Allowed
3. Causes error
4. Updates next segment

**Correct Answer:** Option 1

---

### Q234. DLET without hold?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Medium
**Type:** Single Choice

1. Returns DA status code
2. Allowed
3. Causes error
4. Deletes next segment

**Correct Answer:** Option 1

---

### Q235. I/O area for ISRT contains?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Easy
**Type:** Single Choice

1. Data for segment to insert
2. Nothing
3. Key only
4. Parent data

**Correct Answer:** Option 1

---

### Q236. I/O area for REPL contains?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Easy
**Type:** Single Choice

1. New segment data
2. Nothing
3. Key only
4. Status

**Correct Answer:** Option 1

---

### Q237. I/O area for DLET contains?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Medium
**Type:** Single Choice

1. Not used
2. Segment to delete
3. Key
4. Status

**Correct Answer:** Option 1

---

### Q238. SSAs for REPL?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Medium
**Type:** Single Choice

1. Not required (uses held segment)
2. Required
3. Optional
4. For multiple replaces

**Correct Answer:** Option 1

---

### Q239. SSAs for DLET?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Medium
**Type:** Single Choice

1. Not required (uses held segment)
2. Required
3. Optional
4. For multiple deletes

**Correct Answer:** Option 1

---

### Q240. Insert twins with key?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Medium
**Type:** Single Choice

1. Must provide unique values
2. Random values
3. Not possible
4. Automatic

**Correct Answer:** Option 1

---

### Q241. Update committed when?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Hard
**Type:** Single Choice

1. At checkpoint or termination
2. Immediately
3. At COMMIT call
4. Never auto

**Correct Answer:** Option 1

---

### Q242. Rollback updates?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Hard
**Type:** Single Choice

1. Checkpoint/restart facilities
2. ROLLBACK call
3. Not possible
4. Automatic

**Correct Answer:** Option 1

---

### Q243. PROCOPT=A includes?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Medium
**Type:** Single Choice

1. All operations I, R, D, G
2. Get only
3. Insert only
4. Delete only

**Correct Answer:** Option 1

---

### Q244. Modify in batch program?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Easy
**Type:** Single Choice

1. Same calls as online
2. Different calls
3. Not allowed
4. Special mode

**Correct Answer:** Option 1

---

### Q245. Segment change reflected?

**Topic:** IMS DB - Database Modification (ISRT/REPL/DLET)
**Difficulty:** Hard
**Type:** Single Choice

1. After commit point
2. Immediately visible
3. After program end
4. After restart

**Correct Answer:** Option 1

---

### Q246. Secondary index purpose?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Easy
**Type:** Single Choice

1. Alternate access path to data
2. Backup index
3. Second copy of data
4. Security feature

**Correct Answer:** Option 1

---

### Q247. Secondary index defined in?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Medium
**Type:** Single Choice

1. DBD using XDFLD
2. PSB
3. PCB
4. Application

**Correct Answer:** Option 1

---

### Q248. XDFLD statement defines?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Medium
**Type:** Single Choice

1. Index source field
2. External field
3. Extra field
4. Index dataset

**Correct Answer:** Option 1

---

### Q249. Index pointer segment?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Hard
**Type:** Single Choice

1. Points to target data segment
2. Stores index data
3. Root segment
4. Control segment

**Correct Answer:** Option 1

---

### Q250. Index source field can be in?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Medium
**Type:** Single Choice

1. Any segment in hierarchy
2. Root only
3. Leaf only
4. Parent only

**Correct Answer:** Option 1

---

### Q251. Secondary index allows?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Medium
**Type:** Single Choice

1. Direct access by non-key field
2. Faster sequential access
3. Data duplication
4. Security

**Correct Answer:** Option 1

---

### Q252. Index database is?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Hard
**Type:** Single Choice

1. Separate physical database
2. Part of data database
3. Logical database
4. Virtual database

**Correct Answer:** Option 1

---

### Q253. Index maintenance is?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Medium
**Type:** Single Choice

1. Automatic by IMS
2. Manual by program
3. Batch only
4. Optional

**Correct Answer:** Option 1

---

### Q254. Access via index uses?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Easy
**Type:** Single Choice

1. Standard DL/I calls
2. Special index calls
3. SQL queries
4. Utility

**Correct Answer:** Option 1

---

### Q255. PSB for indexed database?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Hard
**Type:** Single Choice

1. Can specify index or data DBD
2. Must specify both
3. Index DBD only
4. Data DBD only

**Correct Answer:** Option 1

---

### Q256. Index segment contains?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Hard
**Type:** Single Choice

1. Key value and pointer
2. Complete data
3. Key only
4. Pointer only

**Correct Answer:** Option 1

---

### Q257. Multiple secondary indexes?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Medium
**Type:** Single Choice

1. Allowed on same database
2. Only one allowed
3. Maximum two
4. Not supported

**Correct Answer:** Option 1

---

### Q258. Index update occurs?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Medium
**Type:** Single Choice

1. When source field changes
2. Manual only
3. Batch only
4. Never auto

**Correct Answer:** Option 1

---

### Q259. Duplicate index keys?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Medium
**Type:** Single Choice

1. Allowed
2. Not allowed
3. Causes error
4. Merged

**Correct Answer:** Option 1

---

### Q260. Index improves?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Easy
**Type:** Single Choice

1. Direct retrieval performance
2. Sequential performance
3. Update performance
4. Delete performance

**Correct Answer:** Option 1

---

### Q261. XDFLD NAME is?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Hard
**Type:** Single Choice

1. Index database name
2. Field name
3. Segment name
4. Dataset name

**Correct Answer:** Option 1

---

### Q262. Sparse index contains?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Hard
**Type:** Single Choice

1. Subset of segments
2. All segments
3. Root only
4. No segments

**Correct Answer:** Option 1

---

### Q263. Index drawback?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Medium
**Type:** Single Choice

1. Overhead on updates
2. Slower retrieval
3. More storage
4. Both 1 and 3

**Correct Answer:** Option 4

---

### Q264. Application view of index?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Hard
**Type:** Single Choice

1. Transparent or explicit based on PCB
2. Always transparent
3. Always explicit
4. Not visible

**Correct Answer:** Option 1

---

### Q265. Index on concatenated field?

**Topic:** IMS DB - Secondary Indexing
**Difficulty:** Hard
**Type:** Single Choice

1. Supported with XDFLD
2. Not supported
3. Manual only
4. Requires utility

**Correct Answer:** Option 1

---

### Q266. Logical database purpose?

**Topic:** IMS DB - Logical Databases
**Difficulty:** Easy
**Type:** Single Choice

1. Combine multiple physical databases
2. Backup database
3. Logical view only
4. Index database

**Correct Answer:** Option 1

---

### Q267. Logical relationship connects?

**Topic:** IMS DB - Logical Databases
**Difficulty:** Medium
**Type:** Single Choice

1. Segments across physical databases
2. Segments in same database
3. Databases to files
4. Applications to data

**Correct Answer:** Option 1

---

### Q268. Logical child is?

**Topic:** IMS DB - Logical Databases
**Difficulty:** Medium
**Type:** Single Choice

1. Segment with logical parent
2. Virtual segment
3. Index segment
4. Backup segment

**Correct Answer:** Option 1

---

### Q269. Logical parent in?

**Topic:** IMS DB - Logical Databases
**Difficulty:** Medium
**Type:** Single Choice

1. Different physical database
2. Same database
3. Index database
4. No parent

**Correct Answer:** Option 1

---

### Q270. DBD for logical database?

**Topic:** IMS DB - Logical Databases
**Difficulty:** Hard
**Type:** Single Choice

1. Combines multiple physical DBDs
2. Standard DBD
3. Special LDBDGEN
4. Not needed

**Correct Answer:** Option 1

---

### Q271. Application accesses logical DB?

**Topic:** IMS DB - Logical Databases
**Difficulty:** Medium
**Type:** Single Choice

1. Using standard DL/I calls
2. Special logical calls
3. SQL only
4. Read-only

**Correct Answer:** Option 1

---

### Q272. Logical relationship defined?

**Topic:** IMS DB - Logical Databases
**Difficulty:** Hard
**Type:** Single Choice

1. In both physical DBDs
2. In PSB
3. In PCB
4. In application

**Correct Answer:** Option 1

---

### Q273. Bidirectional relationship?

**Topic:** IMS DB - Logical Databases
**Difficulty:** Hard
**Type:** Single Choice

1. Supported with paired segments
2. Not supported
3. One way only
4. Automatic

**Correct Answer:** Option 1

---

### Q274. Logical twin chain?

**Topic:** IMS DB - Logical Databases
**Difficulty:** Hard
**Type:** Single Choice

1. Twins via logical relationship
2. Physical twins
3. Index twins
4. Virtual twins

**Correct Answer:** Option 1

---

### Q275. Logical database advantage?

**Topic:** IMS DB - Logical Databases
**Difficulty:** Medium
**Type:** Single Choice

1. Data independence and integration
2. Faster access
3. Less storage
4. Simplified DBD

**Correct Answer:** Option 1

---

### Q276. Checkpoint call?

**Topic:** IMS DB - Recovery and Restart
**Difficulty:** Medium
**Type:** Single Choice

1. CHKP or SYMCHKP
2. CKPT
3. CHECKPOINT
4. SYNC

**Correct Answer:** Option 1

---

### Q277. XRST call purpose?

**Topic:** IMS DB - Recovery and Restart
**Difficulty:** Hard
**Type:** Single Choice

1. Extended restart
2. Extra restart
3. Execute restart
4. Exit restart

**Correct Answer:** Option 1

---

### Q278. Checkpoint establishes?

**Topic:** IMS DB - Recovery and Restart
**Difficulty:** Easy
**Type:** Single Choice

1. Point for restart
2. Backup
3. Lock
4. Commit

**Correct Answer:** Option 1

---

### Q279. Application checkpoint frequency?

**Topic:** IMS DB - Recovery and Restart
**Difficulty:** Medium
**Type:** Single Choice

1. Programmer determined
2. Automatic only
3. Not needed
4. Fixed interval

**Correct Answer:** Option 1

---

### Q280. Restart after abend?

**Topic:** IMS DB - Recovery and Restart
**Difficulty:** Easy
**Type:** Single Choice

1. From last checkpoint
2. From beginning
3. Not possible
4. Manual only

**Correct Answer:** Option 1

---

### Q281. Checkpoint data stored?

**Topic:** IMS DB - Recovery and Restart
**Difficulty:** Medium
**Type:** Single Choice

1. In checkpoint dataset
2. In database
3. In log
4. In PSB

**Correct Answer:** Option 1

---

### Q282. XRST retrieves?

**Topic:** IMS DB - Recovery and Restart
**Difficulty:** Hard
**Type:** Single Choice

1. Checkpoint data
2. Restart point
3. Status codes
4. Database position

**Correct Answer:** Option 1

---

### Q283. ROLL or ROLB call?

**Topic:** IMS DB - Recovery and Restart
**Difficulty:** Hard
**Type:** Single Choice

1. Dynamic backout
2. Roll forward
3. Rollback all
4. Rotate log

**Correct Answer:** Option 1

---

### Q284. Log records used for?

**Topic:** IMS DB - Recovery and Restart
**Difficulty:** Easy
**Type:** Single Choice

1. Recovery and restart
2. Performance
3. Security
4. Reporting

**Correct Answer:** Option 1

---

### Q285. Application responsibility?

**Topic:** IMS DB - Recovery and Restart
**Difficulty:** Medium
**Type:** Single Choice

1. Issue CHKP and handle restart logic
2. Nothing, automatic
3. Manual recovery
4. Log management

**Correct Answer:** Option 1

---

### Q286. HDAM uses?

**Topic:** IMS DB - Database Organizations
**Difficulty:** Medium
**Type:** Single Choice

1. Randomizing routine
2. Sequential
3. Index
4. Linked list

**Correct Answer:** Option 1

---

### Q287. HIDAM uses?

**Topic:** IMS DB - Database Organizations
**Difficulty:** Medium
**Type:** Single Choice

1. Index on root key
2. Randomizing
3. Sequential only
4. Hash

**Correct Answer:** Option 1

---

### Q288. HISAM uses?

**Topic:** IMS DB - Database Organizations
**Difficulty:** Hard
**Type:** Single Choice

1. ISAM access method
2. VSAM
3. Hash
4. Direct

**Correct Answer:** Option 1

---

### Q289. HSAM uses?

**Topic:** IMS DB - Database Organizations
**Difficulty:** Easy
**Type:** Single Choice

1. Sequential access
2. Hash
3. Index
4. Random

**Correct Answer:** Option 1

---

### Q290. Direct access organization?

**Topic:** IMS DB - Database Organizations
**Difficulty:** Medium
**Type:** Single Choice

1. HDAM and HIDAM
2. HISAM only
3. HSAM only
4. All types

**Correct Answer:** Option 1

---

### Q291. Sequential organization?

**Topic:** IMS DB - Database Organizations
**Difficulty:** Easy
**Type:** Single Choice

1. HSAM
2. HDAM
3. HIDAM
4. All types

**Correct Answer:** Option 1

---

### Q292. Root addressable?

**Topic:** IMS DB - Database Organizations
**Difficulty:** Hard
**Type:** Single Choice

1. HDAM and HIDAM
2. HISAM and HSAM
3. All types
4. None

**Correct Answer:** Option 1

---

### Q293. Application sees organization?

**Topic:** IMS DB - Database Organizations
**Difficulty:** Medium
**Type:** Single Choice

1. No, DL/I abstracts it
2. Yes, affects calls
3. Only for tuning
4. Yes, must code differently

**Correct Answer:** Option 1

---

### Q294. Fastest direct access?

**Topic:** IMS DB - Database Organizations
**Difficulty:** Hard
**Type:** Single Choice

1. HDAM with good randomizer
2. HIDAM
3. HISAM
4. HSAM

**Correct Answer:** Option 1

---

### Q295. Index required?

**Topic:** IMS DB - Database Organizations
**Difficulty:** Medium
**Type:** Single Choice

1. HIDAM
2. HDAM
3. HSAM
4. All types

**Correct Answer:** Option 1

---

### Q296. Field level sensitivity?

**Topic:** IMS DB - Advanced Features
**Difficulty:** Hard
**Type:** Single Choice

1. Control access to specific fields
2. Segment sensitivity
3. Database sensitivity
4. PCB sensitivity

**Correct Answer:** Option 1

---

### Q297. Multiple positioning?

**Topic:** IMS DB - Advanced Features
**Difficulty:** Hard
**Type:** Single Choice

1. Multiple concurrent positions in DB
2. One position only
3. Position stacking
4. No positioning

**Correct Answer:** Option 1

---

### Q298. Message processing?

**Topic:** IMS DB - Advanced Features
**Difficulty:** Hard
**Type:** Single Choice

1. Get next message (GN)
2. Standard DL/I calls
3. Special calls
4. Not in DL/I

**Correct Answer:** Option 1

---

### Q299. Data capture exit?

**Topic:** IMS DB - Advanced Features
**Difficulty:** Hard
**Type:** Single Choice

1. User exit for database changes
2. Entry point
3. Exit program
4. Checkpoint

**Correct Answer:** Option 1

---

### Q300. GSAM database?

**Topic:** IMS DB - Advanced Features
**Difficulty:** Hard
**Type:** Single Choice

1. Sequential dataset access via DL/I
2. IMS database type
3. Security module
4. Utility

**Correct Answer:** Option 1

---

