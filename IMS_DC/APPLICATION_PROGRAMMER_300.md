# IMS DC Application Programmer - 300 Questions

This file contains 300 questions covering IMS DC (Data Communications) topics for application programmers.

## Topics Covered
- IMS DC Fundamentals and Concepts
- Message Processing Programs (MPP)
- Transaction Processing
- Message Queuing
- I/O PCB (Program Communication Block)
- Message Format Services (MFS)
- Screen Handling and Formatting
- Message Field Editing
- Multi-segment Message Handling
- Error Recovery Procedures
- Program-to-Program Switching
- Transaction Restart/Recovery
- Data Validation Techniques
- COBOL Program Structure
- PCB Mask Field Details
- Status Code Handling
- Real-world Application Scenarios
- Best Practices and Common Pitfalls

---

## Question 1

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What does IMS DC stand for?

**Options:**
1. Data Communications
2. Database Control
3. Direct Connection
4. Data Center

**Correct Answer:** 1

---

## Question 2

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is the primary purpose of IMS DC?

**Options:**
1. Online transaction processing
2. Batch processing only
3. File management
4. Network routing

**Correct Answer:** 1

---

## Question 3

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Which component manages message flow in IMS DC?

**Options:**
1. IMS Control Region
2. Message Processing Region
3. Batch Message Processing
4. Transaction Manager

**Correct Answer:** 4

---

## Question 4

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is a terminal in IMS DC context?

**Options:**
1. Any input/output device
2. Only physical terminals
3. Logical unit of work
4. Database connection

**Correct Answer:** 1

---

## Question 5

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** IMS DC supports which processing modes?

**Options:**
1. Online only
2. Batch only
3. Both online and batch
4. Real-time only

**Correct Answer:** 3

---

## Question 6

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is the IMS DC environment primarily designed for?

**Options:**
1. High-volume transaction processing
2. Report generation
3. Data warehousing
4. File transfers

**Correct Answer:** 1

---

## Question 7

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Which layer handles communication with terminals?

**Options:**
1. Application layer
2. Communication layer
3. Database layer
4. Control layer

**Correct Answer:** 2

---

## Question 8

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What does LTERM represent?

**Options:**
1. Logical terminal
2. Last terminal
3. Local terminal
4. Link terminal

**Correct Answer:** 1

---

## Question 9

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is the purpose of transaction codes?

**Options:**
1. Identify and route transactions to appropriate programs
2. Encrypt messages
3. Validate user credentials
4. Store transaction history

**Correct Answer:** 1

---

## Question 10

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** IMS DC can process how many transactions?

**Options:**
1. Thousands per second
2. Hundreds per minute
3. Tens per hour
4. One at a time

**Correct Answer:** 1

---

## Question 11

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What does MPP stand for in IMS DC?

**Options:**
1. Message Processing Program
2. Multiple Program Processing
3. Master Program Processor
4. Message Protocol Program

**Correct Answer:** 1

---

## Question 12

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is the primary function of an MPP?

**Options:**
1. Process online transactions
2. Generate reports
3. Backup databases
4. Manage security

**Correct Answer:** 1

---

## Question 13

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How does an MPP receive input?

**Options:**
1. Through message queues
2. Direct terminal access
3. File input
4. Command line

**Correct Answer:** 1

---

## Question 14

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** Can an MPP update databases?

**Options:**
1. Yes, using DL/I calls
2. No, read-only access
3. Only with special authorization
4. Only in batch mode

**Correct Answer:** 1

---

## Question 15

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What happens when an MPP completes processing?

**Options:**
1. Sends response to output queue
2. Terminates immediately
3. Waits for next transaction
4. Restarts the system

**Correct Answer:** 1

---

## Question 16

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Which PCB does an MPP use for message I/O?

**Options:**
1. I/O PCB
2. DB PCB
3. Alternate PCB
4. Express PCB

**Correct Answer:** 1

---

## Question 17

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can multiple MPPs process the same transaction code?

**Options:**
1. Yes, for load balancing
2. No, only one MPP per transaction
3. Only in test environments
4. Only with system approval

**Correct Answer:** 1

---

## Question 18

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is the main difference between MPP and BMP?

**Options:**
1. MPP processes online messages, BMP runs in batch
2. MPP is faster
3. BMP has priority
4. No difference

**Correct Answer:** 1

---

## Question 19

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How does IMS DC schedule MPPs?

**Options:**
1. Based on message queue depth and priority
2. First-come, first-served
3. Random selection
4. Alphabetically by name

**Correct Answer:** 1

---

## Question 20

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What DL/I call retrieves input messages in MPP?

**Options:**
1. GU (Get Unique)
2. GN (Get Next)
3. ISRT (Insert)
4. REPL (Replace)

**Correct Answer:** 1

---

## Question 21

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is the maximum length of a transaction code?

**Options:**
1. 8 characters
2. 4 characters
3. 16 characters
4. 32 characters

**Correct Answer:** 1

---

## Question 22

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** Where is the transaction code placed in a message?

**Options:**
1. At the beginning
2. At the end
3. In the middle
4. Anywhere

**Correct Answer:** 1

---

## Question 23

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What determines which program processes a transaction?

**Options:**
1. Transaction code definition
2. Message content
3. Terminal ID
4. User preference

**Correct Answer:** 1

---

## Question 24

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can a transaction code be associated with multiple programs?

**Options:**
1. No, one-to-one relationship
2. Yes, many-to-many
3. Yes, but not recommended
4. Only in test mode

**Correct Answer:** 1

---

## Question 25

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is transaction priority?

**Options:**
1. Determines processing order
2. Security level
3. Message size limit
4. Response time requirement

**Correct Answer:** 1

---

## Question 26

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What happens if an invalid transaction code is entered?

**Options:**
1. Error message returned to terminal
2. System crash
3. Transaction ignored
4. Default program executed

**Correct Answer:** 1

---

## Question 27

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can transaction codes be defined dynamically?

**Options:**
1. No, must be pre-defined in system definition
2. Yes, at runtime
3. Yes, by any user
4. Only by system administrator

**Correct Answer:** 1

---

## Question 28

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is a conversational transaction?

**Options:**
1. Maintains state between messages
2. Processes multiple messages
3. Uses conversation API
4. Requires user confirmation

**Correct Answer:** 1

---

## Question 29

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is transaction class?

**Options:**
1. Groups transactions for scheduling
2. Security classification
3. Message format type
4. Program language

**Correct Answer:** 1

---

## Question 30

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is a fast path transaction?

**Options:**
1. High-performance transaction with optimizations
2. Quick response transaction
3. Express delivery transaction
4. Shortened transaction code

**Correct Answer:** 1

---

## Question 31

**Topic:** IMS DC - Message Queues  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** Where are input messages stored before processing?

**Options:**
1. Input message queue
2. Database
3. Memory buffer
4. Log file

**Correct Answer:** 1

---

## Question 32

**Topic:** IMS DC - Message Queues  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What determines message processing order?

**Options:**
1. Priority and arrival time
2. Message size
3. Alphabetical order
4. Random selection

**Correct Answer:** 1

---

## Question 33

**Topic:** IMS DC - Message Queues  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What happens to output messages?

**Options:**
1. Placed in output queue for delivery
2. Sent immediately
3. Stored in database
4. Discarded after viewing

**Correct Answer:** 1

---

## Question 34

**Topic:** IMS DC - Message Queues  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can messages have different priorities?

**Options:**
1. Yes, 0-9 or 0-15 depending on system
2. No, all equal priority
3. Yes, low/medium/high only
4. Only in batch mode

**Correct Answer:** 1

---

## Question 35

**Topic:** IMS DC - Message Queues  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is message queuing?

**Options:**
1. Temporarily storing messages for processing
2. Sorting messages
3. Encrypting messages
4. Archiving messages

**Correct Answer:** 1

---

## Question 36

**Topic:** IMS DC - Message Queues  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Where are queues physically stored?

**Options:**
1. In IMS queue datasets
2. In memory only
3. On tape
4. In user files

**Correct Answer:** 1

---

## Question 37

**Topic:** IMS DC - Message Queues  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is a scratch pad area (SPA)?

**Options:**
1. Storage for conversational transaction data
2. Temporary work area
3. Message buffer
4. Error log

**Correct Answer:** 1

---

## Question 38

**Topic:** IMS DC - Message Queues  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can messages be retrieved from queues non-destructively?

**Options:**
1. Yes, using browse functions
2. No, always destructive
3. Only in test mode
4. Only by operators

**Correct Answer:** 1

---

## Question 39

**Topic:** IMS DC - Message Queues  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is message flooding?

**Options:**
1. Queue overflow condition
2. Multiple duplicate messages
3. Rapid message arrival
4. Message corruption

**Correct Answer:** 1

---

## Question 40

**Topic:** IMS DC - Message Queues  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How long can messages remain in queues?

**Options:**
1. Until processed or expired
2. Maximum 24 hours
3. Maximum 1 hour
4. Until system restart

**Correct Answer:** 1

---

## Question 41

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What does I/O PCB stand for?

**Options:**
1. Input/Output Program Communication Block
2. Interface Output Process Control Block
3. Internal Operation PCB
4. Intelligent Output PCB

**Correct Answer:** 1

---

## Question 42

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is the primary use of I/O PCB?

**Options:**
1. Message input and output
2. Database access
3. File operations
4. Program control

**Correct Answer:** 1

---

## Question 43

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Which field in I/O PCB contains the logical terminal name?

**Options:**
1. LTERM field
2. NAME field
3. TERM field
4. ID field

**Correct Answer:** 1

---

## Question 44

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What status code indicates successful message retrieval?

**Options:**
1. Spaces or blank
2. 00
3. OK
4. SUCCESS

**Correct Answer:** 1

---

## Question 45

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Which field indicates message length in I/O PCB?

**Options:**
1. Segment length field
2. Message length field
3. Data length field
4. Size field

**Correct Answer:** 1

---

## Question 46

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** Can I/O PCB be used for database operations?

**Options:**
1. No, only for message I/O
2. Yes, for any operation
3. Only for read operations
4. Only with special setup

**Correct Answer:** 1

---

## Question 47

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is the status code field length in I/O PCB?

**Options:**
1. 2 bytes
2. 4 bytes
3. 8 bytes
4. 1 byte

**Correct Answer:** 1

---

## Question 48

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Which field identifies the originating terminal?

**Options:**
1. LTERM name
2. Terminal ID
3. User ID
4. Source field

**Correct Answer:** 1

---

## Question 49

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What does QC status code indicate?

**Options:**
1. No more messages in queue
2. Queue corrupted
3. Quick complete
4. Query complete

**Correct Answer:** 1

---

## Question 50

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How many I/O PCBs can a program have?

**Options:**
1. Typically one, but can have alternate PCBs
2. Unlimited
3. Maximum of 5
4. Exactly one

**Correct Answer:** 1

---

## Question 51

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** Which DL/I call retrieves the input message?

**Options:**
1. GU (Get Unique)
2. GN (Get Next)
3. ISRT (Insert)
4. REPL (Replace)

**Correct Answer:** 1

---

## Question 52

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** Which DL/I call sends output to terminal?

**Options:**
1. ISRT to I/O PCB
2. REPL to I/O PCB
3. GU from I/O PCB
4. PUT to I/O PCB

**Correct Answer:** 1

---

## Question 53

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is the purpose of GU call against I/O PCB?

**Options:**
1. Retrieve input message from queue
2. Get user information
3. General update
4. Get unique record

**Correct Answer:** 1

---

## Question 54

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can GN be used with I/O PCB?

**Options:**
1. Yes, to retrieve multiple message segments
2. No, only GU is allowed
3. Yes, but deprecated
4. Only in batch mode

**Correct Answer:** 1

---

## Question 55

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** How do you send a message to a specific terminal?

**Options:**
1. ISRT with modified LTERM in I/O PCB
2. GU to terminal
3. SEND command
4. WRITE to terminal

**Correct Answer:** 1

---

## Question 56

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What happens if ISRT fails on I/O PCB?

**Options:**
1. Status code set in I/O PCB
2. Program abends
3. Message lost
4. System restart

**Correct Answer:** 1

---

## Question 57

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can you use REPL with I/O PCB?

**Options:**
1. No, not applicable for messages
2. Yes, to replace messages
3. Yes, for updates
4. Only in conversational mode

**Correct Answer:** 1

---

## Question 58

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is required before issuing GU to I/O PCB?

**Options:**
1. Nothing, just issue the call
2. Open the PCB
3. Initialize message area
4. Set terminal ID

**Correct Answer:** 1

---

## Question 59

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How many ISRT calls can send one logical message?

**Options:**
1. Multiple ISRTs for multi-segment messages
2. Only one ISRT per message
3. Maximum of 10
4. Depends on terminal type

**Correct Answer:** 1

---

## Question 60

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What indicates end of input message segments?

**Options:**
1. QC status code on GN
2. EOF indicator
3. Null segment
4. Zero length

**Correct Answer:** 1

---

## Question 61

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is a non-conversational transaction?

**Options:**
1. Completes in single input/output cycle
2. Requires multiple interactions
3. Has no output
4. Runs in background

**Correct Answer:** 1

---

## Question 62

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What characterizes a conversational transaction?

**Options:**
1. Maintains data between interactions
2. Processes faster
3. Uses less memory
4. Requires no database

**Correct Answer:** 1

---

## Question 63

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Where is conversation state stored?

**Options:**
1. Scratch Pad Area (SPA)
2. Database
3. Program memory
4. Terminal buffer

**Correct Answer:** 1

---

## Question 64

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Which mode is more resource efficient?

**Options:**
1. Non-conversational
2. Conversational
3. Both equal
4. Depends on transaction

**Correct Answer:** 1

---

## Question 65

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** How does SPA get passed between conversations?

**Options:**
1. IMS automatically includes it in messages
2. Program must explicitly pass it
3. Stored in database
4. Via global memory

**Correct Answer:** 1

---

## Question 66

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is a typical use for conversational transactions?

**Options:**
1. Multi-screen data entry
2. Simple inquiries
3. High-volume processing
4. Batch updates

**Correct Answer:** 1

---

## Question 67

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can a program switch between conversational modes?

**Options:**
1. No, determined by transaction definition
2. Yes, dynamically
3. Yes, with special flag
4. Only once per session

**Correct Answer:** 1

---

## Question 68

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What happens if user abandons a conversation?

**Options:**
1. SPA eventually purged by IMS
2. Resources held indefinitely
3. Automatic rollback
4. System error

**Correct Answer:** 1

---

## Question 69

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How is SPA defined?

**Options:**
1. In the transaction definition
2. In the program
3. At runtime
4. In terminal definition

**Correct Answer:** 1

---

## Question 70

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is the disadvantage of conversational transactions?

**Options:**
1. Higher resource consumption
2. Slower response time
3. Less functionality
4. More complex programming

**Correct Answer:** 1

---

## Question 71

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is a message segment?

**Options:**
1. A logical unit of message data
2. Transaction code
3. Terminal identifier
4. Timestamp

**Correct Answer:** 1

---

## Question 72

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is the maximum message segment size?

**Options:**
1. System dependent, typically up to 32KB
2. 64KB
3. 1MB
4. No limit

**Correct Answer:** 1

---

## Question 73

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How are multi-segment messages identified?

**Options:**
1. By IMS internally, transparent to application
2. Sequence numbers
3. Segment IDs
4. Message headers

**Correct Answer:** 1

---

## Question 74

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is message edit/routing?

**Options:**
1. Validating and directing messages
2. Formatting output
3. Encrypting data
4. Compressing messages

**Correct Answer:** 1

---

## Question 75

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can message format be defined?

**Options:**
1. Yes, using MFS (Message Format Service)
2. No, always free format
3. Yes, but not recommended
4. Only for output

**Correct Answer:** 1

---

## Question 76

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is the purpose of LL ZZ fields?

**Options:**
1. Length and reserved fields in message segments
2. Logical link zones
3. Load level zones
4. Location labels

**Correct Answer:** 1

---

## Question 77

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Where is transaction code in message structure?

**Options:**
1. First field after LL ZZ
2. At the end
3. In message header
4. Variable position

**Correct Answer:** 1

---

## Question 78

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is message switching?

**Options:**
1. Routing messages to different destinations
2. Changing message format
3. Swapping message segments
4. Message encryption

**Correct Answer:** 1

---

## Question 79

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can a message contain binary data?

**Options:**
1. Yes, but requires proper handling
2. No, text only
3. Yes, but not recommended
4. Only in file transfers

**Correct Answer:** 1

---

## Question 80

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is message class?

**Options:**
1. Categorization for processing
2. Priority level
3. Format type
4. Security classification

**Correct Answer:** 1

---

## Question 81

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How is I/O PCB defined in COBOL?

**Options:**
1. In LINKAGE SECTION
2. In WORKING-STORAGE
3. In FILE SECTION
4. In PROCEDURE DIVISION

**Correct Answer:** 1

---

## Question 82

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is the ENTRY statement for IMS program?

**Options:**
1. DLITCBL for DL/I programs
2. MAIN
3. START
4. BEGIN

**Correct Answer:** 1

---

## Question 83

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How to issue DL/I call in COBOL?

**Options:**
1. CALL 'CBLTDLI' USING parameters
2. EXEC DLI command
3. DLI statement
4. PERFORM DLI-CALL

**Correct Answer:** 1

---

## Question 84

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What parameters are passed to CBLTDLI?

**Options:**
1. Function code, PCB, I/O area, SSAs
2. PCB only
3. Function and I/O area
4. All PCBs

**Correct Answer:** 1

---

## Question 85

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** How is message I/O area defined?

**Options:**
1. In WORKING-STORAGE or LINKAGE
2. FILE SECTION
3. SPECIAL-NAMES
4. CONFIGURATION SECTION

**Correct Answer:** 1

---

## Question 86

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What COBOL level for PCB mask?

**Options:**
1. 01 level
2. 05 level
3. 77 level
4. 88 level

**Correct Answer:** 1

---

## Question 87

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** How to check status code in COBOL?

**Options:**
1. Test status field in PCB
2. CHECK STATUS statement
3. IF DLI-STATUS
4. INSPECT STATUS

**Correct Answer:** 1

---

## Question 88

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is the PCB mask pointer?

**Options:**
1. Address pointer to PCB in LINKAGE
2. PCB identifier
3. PCB counter
4. PCB flag

**Correct Answer:** 1

---

## Question 89

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How to handle multiple output segments?

**Options:**
1. Multiple ISRT calls
2. Single ISRT with array
3. WRITE-MULTIPLE
4. SEND-ALL

**Correct Answer:** 1

---

## Question 90

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is GOBACK used for?

**Options:**
1. Return control to IMS
2. Go back in processing
3. Return to caller
4. Exit program

**Correct Answer:** 1

---

## Question 91

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What does blank status code mean?

**Options:**
1. Successful operation
2. No status available
3. Unknown error
4. Not processed

**Correct Answer:** 1

---

## Question 92

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What does QD status code mean?

**Options:**
1. Message not found in queue
2. Queue destroyed
3. Quick delete
4. Query denied

**Correct Answer:** 1

---

## Question 93

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is AI status code?

**Options:**
1. Indicates potential data integrity issue
2. All inserted
3. Application interface error
4. Automatic insert

**Correct Answer:** 1

---

## Question 94

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** How should programs handle error status codes?

**Options:**
1. Check after each call and take appropriate action
2. Ignore non-critical errors
3. Let IMS handle all errors
4. Log and continue

**Correct Answer:** 1

---

## Question 95

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What does AM status code indicate?

**Options:**
1. Message format error
2. Access method error
3. All messages processed
4. Automatic mode

**Correct Answer:** 1

---

## Question 96

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** When should program issue rollback?

**Options:**
1. When unrecoverable error occurs
2. After every transaction
3. Only at end of day
4. Never, IMS handles it

**Correct Answer:** 1

---

## Question 97

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is the purpose of checkpoint?

**Options:**
1. Save transaction state for recovery
2. Check program status
3. Verify data
4. Control program flow

**Correct Answer:** 1

---

## Question 98

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How to issue rollback call?

**Options:**
1. CALL 'CBLTDLI' with ROLL function
2. EXEC CICS ROLLBACK
3. ROLLBACK statement
4. UNDO command

**Correct Answer:** 1

---

## Question 99

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What happens on abnormal termination?

**Options:**
1. IMS automatically backs out changes
2. Changes committed
3. Database locked
4. System restart required

**Correct Answer:** 1

---

## Question 100

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is the best way to test DC programs?

**Options:**
1. Use IMS test environment with test terminals
2. Test in production
3. Unit test only
4. No testing needed

**Correct Answer:** 1

---

## Question 101

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How can you simulate terminal input?

**Options:**
1. Use test harness or automation tools
2. Manual typing only
3. Not possible
4. Batch simulation

**Correct Answer:** 1

---

## Question 102

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What debugging techniques are available?

**Options:**
1. Source debuggers, dumps, and traces
2. Printf only
3. No debugging available
4. Manual inspection

**Correct Answer:** 1

---

## Question 103

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How to trace DL/I calls?

**Options:**
1. Enable IMS tracing facilities
2. Add DISPLAY statements
3. Use system logs
4. Not possible

**Correct Answer:** 1

---

## Question 104

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is a common cause of program failures?

**Options:**
1. Incorrect status code handling
2. Too many ISRT calls
3. Message too small
4. Terminal disconnected

**Correct Answer:** 1

---

## Question 105

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** How to test error conditions?

**Options:**
1. Simulate error scenarios
2. Wait for real errors
3. Not necessary
4. Only in production

**Correct Answer:** 1

---

## Question 106

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is program isolation test?

**Options:**
1. Testing program without affecting production
2. Testing in isolation ward
3. Solo testing
4. Disconnected test

**Correct Answer:** 1

---

## Question 107

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How to verify message format?

**Options:**
1. Inspect message segments with debugging tools
2. Visual inspection
3. Automated check
4. Not necessary

**Correct Answer:** 1

---

## Question 108

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What should be tested for conversational transactions?

**Options:**
1. State preservation across interactions
2. Speed only
3. Output format
4. User interface

**Correct Answer:** 1

---

## Question 109

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How to test transaction load?

**Options:**
1. Use load testing tools
2. One transaction at a time
3. Not necessary
4. Production monitoring

**Correct Answer:** 1

---

## Question 110

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is an inquiry program?

**Options:**
1. Read-only program that displays data
2. Program that asks questions
3. Update program
4. Delete program

**Correct Answer:** 1

---

## Question 111

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What characterizes a data entry program?

**Options:**
1. Accepts and validates input data
2. Displays reports
3. Processes batch files
4. Manages terminals

**Correct Answer:** 1

---

## Question 112

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is a maintenance program?

**Options:**
1. Updates, inserts, or deletes data
2. Repairs databases
3. Maintains terminals
4. Backs up data

**Correct Answer:** 1

---

## Question 113

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is a menu-driven program?

**Options:**
1. Presents options for user selection
2. Processes menu data
3. Food ordering system
4. List display program

**Correct Answer:** 1

---

## Question 114

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is typical of high-volume programs?

**Options:**
1. Optimized for performance
2. Complex logic
3. Large messages
4. Long running

**Correct Answer:** 1

---

## Question 115

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is a composite transaction?

**Options:**
1. Combines multiple operations
2. Complex format
3. Multiple terminals
4. Long duration

**Correct Answer:** 1

---

## Question 116

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What security is needed for update programs?

**Options:**
1. Proper authorization and validation
2. Password only
3. None needed
4. Terminal lock

**Correct Answer:** 1

---

## Question 117

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What validation should data entry program perform?

**Options:**
1. Field format, range, and business rules
2. Syntax only
3. No validation needed
4. User identity only

**Correct Answer:** 1

---

## Question 118

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is a report program in DC?

**Options:**
1. Generates formatted output for display
2. Batch reporting
3. Prints reports
4. Logs activities

**Correct Answer:** 1

---

## Question 119

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is the difference between inquiry and maintenance?

**Options:**
1. Inquiry reads only, maintenance updates
2. No difference
3. Inquiry is faster
4. Maintenance is simpler

**Correct Answer:** 1

---

## Question 120

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is alternate PCB?

**Options:**
1. Additional I/O PCB for message routing
2. Backup PCB
3. Alternative database PCB
4. Secondary PCB

**Correct Answer:** 1

---

## Question 121

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is express PCB?

**Options:**
1. PCB for urgent high-priority messages
2. Fast processing PCB
3. Quick response PCB
4. Expedited PCB

**Correct Answer:** 1

---

## Question 122

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is program-to-program message switching?

**Options:**
1. One program sending message to another program
2. Inter-program communication
3. Message forwarding
4. Program linking

**Correct Answer:** 1

---

## Question 123

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is asynchronous output?

**Options:**
1. Output sent after program completion
2. Non-blocking output
3. Delayed output
4. Background output

**Correct Answer:** 1

---

## Question 124

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is command code usage in DC?

**Options:**
1. Special processing options for calls
2. Transaction codes
3. System commands
4. Terminal commands

**Correct Answer:** 1

---

## Question 125

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is dynamic transaction routing?

**Options:**
1. Runtime determination of transaction destination
2. Fast routing
3. Automatic routing
4. Backup routing

**Correct Answer:** 1

---

## Question 126

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is transaction affinity?

**Options:**
1. Related transactions processed by same region
2. Transaction preference
3. User preference
4. Terminal binding

**Correct Answer:** 1

---

## Question 127

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is a security exit in IMS DC?

**Options:**
1. Custom security validation routine
2. Emergency exit
3. Logout function
4. Backup path

**Correct Answer:** 1

---

## Question 128

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is message edit exit?

**Options:**
1. Custom routine for message validation
2. Message formatting
3. Message correction
4. Message deletion

**Correct Answer:** 1

---

## Question 129

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How does IMS schedule transactions?

**Options:**
1. Based on priority, class, and availability
2. First-in-first-out
3. Random
4. Alphabetical

**Correct Answer:** 1

---

## Question 130

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is transaction class scheduling?

**Options:**
1. Groups transactions for resource management
2. Priority classification
3. Type classification
4. User classification

**Correct Answer:** 1

---

## Question 131

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What affects transaction throughput?

**Options:**
1. Number of regions, priorities, resources
2. Network speed only
3. Terminal count
4. Program size

**Correct Answer:** 1

---

## Question 132

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is transaction queuing?

**Options:**
1. Waiting for processing resources
2. Message queuing
3. Terminal queuing
4. Data queuing

**Correct Answer:** 1

---

## Question 133

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How can transaction performance be monitored?

**Options:**
1. IMS monitoring tools and statistics
2. Manual observation
3. User feedback
4. Not possible

**Correct Answer:** 1

---

## Question 134

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is transaction load balancing?

**Options:**
1. Distributing work across regions
2. Message distribution
3. User distribution
4. Terminal balancing

**Correct Answer:** 1

---

## Question 135

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is a transaction timeout?

**Options:**
1. Maximum execution time limit
2. User wait time
3. Queue wait time
4. Response time

**Correct Answer:** 1

---

## Question 136

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What happens when transaction times out?

**Options:**
1. IMS may abend the transaction
2. Automatic retry
3. Extended time granted
4. Nothing

**Correct Answer:** 1

---

## Question 137

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is parallel transaction processing?

**Options:**
1. Multiple transactions executing simultaneously
2. Sequential processing
3. Batch processing
4. Single threading

**Correct Answer:** 1

---

## Question 138

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is a PCB mask?

**Options:**
1. COBOL structure mapping PCB fields
2. PCB security
3. PCB filter
4. PCB template

**Correct Answer:** 1

---

## Question 139

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What fields are in I/O PCB mask?

**Options:**
1. LTERM, status code, date/time, message length
2. Only status code
3. All database fields
4. User information

**Correct Answer:** 1

---

## Question 140

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** Why define PCB mask in LINKAGE SECTION?

**Options:**
1. IMS provides PCB address at runtime
2. Saves memory
3. Required by COBOL
4. Better performance

**Correct Answer:** 1

---

## Question 141

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is the typical size of I/O PCB?

**Options:**
1. 148 bytes
2. 100 bytes
3. 200 bytes
4. Variable

**Correct Answer:** 1

---

## Question 142

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can PCB mask be modified by program?

**Options:**
1. Should not modify, except for routing
2. Yes, freely
3. No, read-only
4. Only status code

**Correct Answer:** 1

---

## Question 143

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is the status code field type?

**Options:**
1. Character field (PIC XX)
2. Numeric field
3. Binary field
4. Alphanumeric

**Correct Answer:** 1

---

## Question 144

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** How to reference PCB fields in COBOL?

**Options:**
1. Through mask variable name
2. Direct PCB reference
3. Using POINTER
4. Not possible

**Correct Answer:** 1

---

## Question 145

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is PCB list?

**Options:**
1. Collection of PCBs passed to program
2. Array of PCBs
3. PCB directory
4. PCB index

**Correct Answer:** 1

---

## Question 146

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How many PCBs can a program access?

**Options:**
1. One I/O PCB plus multiple DB PCBs
2. Only one
3. Unlimited
4. Maximum 10

**Correct Answer:** 1

---

## Question 147

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is modifiable alternate PCB field?

**Options:**
1. LTERM for message routing
2. Status code
3. Date/time
4. User ID

**Correct Answer:** 1

---

## Question 148

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is a response mode transaction?

**Options:**
1. Transaction that sends response to originating terminal
2. Fast response transaction
3. Acknowledged transaction
4. Interactive transaction

**Correct Answer:** 1

---

## Question 149

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is a single mode transaction?

**Options:**
1. Processes one message at a time
2. Has one function
3. Uses one PCB
4. Runs once

**Correct Answer:** 1

---

## Question 150

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is multiple mode transaction?

**Options:**
1. Can process multiple messages per schedule
2. Has multiple functions
3. Uses multiple PCBs
4. Runs multiple times

**Correct Answer:** 1

---

## Question 151

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is transaction commit point?

**Options:**
1. Point where changes are made permanent
2. End of transaction
3. Beginning of transaction
4. Checkpoint

**Correct Answer:** 1

---

## Question 152

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is transaction recovery?

**Options:**
1. Restoring transaction state after failure
2. Getting transaction back
3. Fixing transaction errors
4. Restarting transaction

**Correct Answer:** 1

---

## Question 153

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is a WFI transaction?

**Options:**
1. Wait-for-input transaction
2. Write file input
3. Work flow item
4. Wait for initialization

**Correct Answer:** 1

---

## Question 154

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is transaction code security?

**Options:**
1. Authorization control for transactions
2. Transaction encryption
3. Code protection
4. Terminal security

**Correct Answer:** 1

---

## Question 155

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is transaction serialization?

**Options:**
1. Ensuring sequential access to resources
2. Converting to serial format
3. Transaction logging
4. Numbering transactions

**Correct Answer:** 1

---

## Question 156

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is transaction coupling?

**Options:**
1. Relationship between transactions
2. Transaction joining
3. Transaction linking
4. Transaction dependency

**Correct Answer:** 1

---

## Question 157

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is transaction integrity?

**Options:**
1. ACID properties compliance
2. Data validation
3. Security check
4. Error checking

**Correct Answer:** 1

---

## Question 158

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is the role of IMS Control Region?

**Options:**
1. Manages overall IMS DC operations
2. Controls terminals only
3. Manages databases
4. Handles security

**Correct Answer:** 1

---

## Question 159

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is a dependent region in IMS DC?

**Options:**
1. Region that processes applications
2. Backup region
3. Secondary region
4. Test region

**Correct Answer:** 1

---

## Question 160

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is BMP in IMS?

**Options:**
1. Batch Message Processing program
2. Basic MPP
3. Backup Message Program
4. Best Message Processor

**Correct Answer:** 1

---

## Question 161

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can an MPP access multiple databases?

**Options:**
1. Yes, through multiple DB PCBs
2. No, only one database
3. Yes, but not recommended
4. Only in batch mode

**Correct Answer:** 1

---

## Question 162

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is a transaction synonym?

**Options:**
1. Alternate name for same transaction
2. Similar transaction
3. Backup transaction
4. Related transaction

**Correct Answer:** 1

---

## Question 163

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** Can transaction codes contain special characters?

**Options:**
1. Limited special characters allowed
2. No, alphanumeric only
3. Yes, any character
4. Only underscore

**Correct Answer:** 1

---

## Question 164

**Topic:** IMS DC - Message Queues  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is the system queue in IMS DC?

**Options:**
1. IMS internal queue for messages
2. User queue
3. Database queue
4. Terminal queue

**Correct Answer:** 1

---

## Question 165

**Topic:** IMS DC - Message Queues  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** Can messages be prioritized within a queue?

**Options:**
1. Yes, using priority values
2. No, FIFO only
3. Only manually
4. Only by operators

**Correct Answer:** 1

---

## Question 166

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is MOD name in PCB?

**Options:**
1. Message Output Descriptor
2. Module name
3. Mode name
4. Modify name

**Correct Answer:** 1

---

## Question 167

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How is destination determined for output?

**Options:**
1. From LTERM field in I/O PCB
2. User specification
3. System default
4. Random assignment

**Correct Answer:** 1

---

## Question 168

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is PURG call used for?

**Options:**
1. Flush output messages immediately
2. Purge input messages
3. Delete transactions
4. Clear buffers

**Correct Answer:** 1

---

## Question 169

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is CHNG call?

**Options:**
1. Change output destination
2. Change transaction
3. Change priority
4. Change format

**Correct Answer:** 1

---

## Question 170

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How is SPA size defined?

**Options:**
1. In transaction definition
2. At runtime
3. In program
4. System default

**Correct Answer:** 1

---

## Question 171

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** Can SPA be encrypted?

**Options:**
1. Program can encrypt data in SPA
2. Automatic encryption
3. No encryption possible
4. System encrypts SPA

**Correct Answer:** 1

---

## Question 172

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is MFS?

**Options:**
1. Message Format Service
2. Message File System
3. Multiple Format Structure
4. Master Format Service

**Correct Answer:** 1

---

## Question 173

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is the purpose of MFS?

**Options:**
1. Format messages for screen display
2. Store messages
3. Route messages
4. Validate messages

**Correct Answer:** 1

---

## Question 174

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** How many parameters in ENTRY statement?

**Options:**
1. Varies, typically 2 or more
2. Always 1
3. Always 5
4. No parameters

**Correct Answer:** 1

---

## Question 175

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is PCB address list?

**Options:**
1. List of pointers to PCBs
2. PCB names
3. PCB contents
4. PCB structure

**Correct Answer:** 1

---

## Question 176

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is GA status code?

**Options:**
1. Segment not found at specified level
2. Get again
3. General access
4. Good answer

**Correct Answer:** 1

---

## Question 177

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is GE status code?

**Options:**
1. End of database
2. General error
3. Get error
4. Good end

**Correct Answer:** 1

---

## Question 178

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is IMS Test Tool?

**Options:**
1. Tool for testing IMS applications
2. Terminal test
3. Database test
4. Performance test

**Correct Answer:** 1

---

## Question 179

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How to generate test transactions?

**Options:**
1. Use terminal emulator or test tools
2. Manual entry only
3. Batch generation
4. Automatic generation

**Correct Answer:** 1

---

## Question 180

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What validation is critical for maintenance programs?

**Options:**
1. Authorization, data validity, referential integrity
2. Syntax only
3. Format only
4. Length only

**Correct Answer:** 1

---

## Question 181

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** Should inquiry programs use database updates?

**Options:**
1. No, read-only access
2. Yes, for logging
3. Sometimes
4. Not applicable

**Correct Answer:** 1

---

## Question 182

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is AOI in IMS DC?

**Options:**
1. Automated Operator Interface
2. Application Output Interface
3. Advanced Online Interface
4. Automatic Operation Initiator

**Correct Answer:** 1

---

## Question 183

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What are command codes?

**Options:**
1. Special indicators for DL/I processing options
2. Transaction codes
3. Security codes
4. Format codes

**Correct Answer:** 1

---

## Question 184

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is WFI time?

**Options:**
1. Wait-for-input timeout period
2. Work flow interval
3. Wait for initialization
4. Work finish indicator

**Correct Answer:** 1

---

## Question 185

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How does IMS handle transaction backlog?

**Options:**
1. Queues and schedules based on priority
2. Rejects new transactions
3. Increases resources automatically
4. Waits indefinitely

**Correct Answer:** 1

---

## Question 186

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is the IOPCB in COBOL programs?

**Options:**
1. First PCB for message I/O
2. Input Only PCB
3. Internal Operation PCB
4. Interactive Online PCB

**Correct Answer:** 1

---

## Question 187

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can programs define their own PCB structure?

**Options:**
1. No, must match IMS-provided structure
2. Yes, freely
3. Yes, with restrictions
4. Only in test

**Correct Answer:** 1

---

## Question 188

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is transaction step?

**Options:**
1. Unit of work within transaction
2. Transaction phase
3. Processing stage
4. Commit point

**Correct Answer:** 1

---

## Question 189

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is dynamic allocation in IMS DC?

**Options:**
1. Runtime resource assignment
2. Memory allocation
3. Terminal assignment
4. Database allocation

**Correct Answer:** 1

---

## Question 190

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is VTAM in IMS DC context?

**Options:**
1. Virtual Telecommunications Access Method
2. Virtual Terminal Access Manager
3. Variable Transaction Access Mode
4. Visual Terminal Application Manager

**Correct Answer:** 1

---

## Question 191

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is a PTERM?

**Options:**
1. Physical terminal
2. Program terminal
3. Primary terminal
4. Process terminal

**Correct Answer:** 1

---

## Question 192

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is the transaction manager in IMS?

**Options:**
1. Component that controls transaction execution
2. User manager
3. Database manager
4. Terminal manager

**Correct Answer:** 1

---

## Question 193

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can MPP programs be debugged online?

**Options:**
1. Yes, using appropriate debugging tools
2. No, batch only
3. Only in test environment
4. Not recommended

**Correct Answer:** 1

---

## Question 194

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is transaction response time?

**Options:**
1. Time from input to output delivery
2. Processing time only
3. Queue time only
4. Network time

**Correct Answer:** 1

---

## Question 195

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What factors affect transaction performance?

**Options:**
1. Program efficiency, database access, queue depth, system load
2. Program only
3. Database only
4. Network only

**Correct Answer:** 1

---

## Question 196

**Topic:** IMS DC - Message Queues  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is a shared queue?

**Options:**
1. Queue accessible by multiple regions
2. Common queue
3. Public queue
4. Open queue

**Correct Answer:** 1

---

## Question 197

**Topic:** IMS DC - Message Queues  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can messages expire in queues?

**Options:**
1. Yes, based on age or system limits
2. No, permanent
3. Only after 24 hours
4. Only manually

**Correct Answer:** 1

---

## Question 198

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What information does date/time field provide?

**Options:**
1. Current system date and time
2. Transaction timestamp
3. Message arrival time
4. Processing time

**Correct Answer:** 1

---

## Question 199

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is the user ID field in I/O PCB?

**Options:**
1. Identifies user or terminal
2. Program ID
3. Transaction ID
4. System ID

**Correct Answer:** 1

---

## Question 200

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is GCMD call?

**Options:**
1. Get Command - for message retrieval
2. General command
3. Get command mode
4. Global command

**Correct Answer:** 1

---

## Question 201

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** Can you issue database calls and message calls in same program?

**Options:**
1. Yes, using appropriate PCBs
2. No, separate programs
3. Only in batch
4. Not recommended

**Correct Answer:** 1

---

## Question 202

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is pseudo-conversational processing?

**Options:**
1. Simulates conversation without holding resources
2. Fake conversation
3. Test conversation
4. Virtual conversation

**Correct Answer:** 1

---

## Question 203

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** When is conversational mode appropriate?

**Options:**
1. When user interaction requires context
2. Never
3. Always
4. Only for testing

**Correct Answer:** 1

---

## Question 204

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is device format in MFS?

**Options:**
1. Screen layout definition
2. Terminal type
3. Message format
4. Data format

**Correct Answer:** 1

---

## Question 205

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is message input descriptor (MID)?

**Options:**
1. Defines input message format
2. Message ID
3. Message indicator
4. Message identification

**Correct Answer:** 1

---

## Question 206

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** How to declare message I/O area?

**Options:**
1. 01 level in WORKING-STORAGE
2. 05 level
3. 77 level
4. 88 level

**Correct Answer:** 1

---

## Question 207

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is the function code parameter?

**Options:**
1. First parameter specifying DL/I operation
2. Program function
3. Transaction code
4. Status code

**Correct Answer:** 1

---

## Question 208

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What does II status code mean?

**Options:**
1. Segment already exists (duplicate key)
2. Information incomplete
3. Invalid input
4. Insert ignored

**Correct Answer:** 1

---

## Question 209

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is AJ status code?

**Options:**
1. Invalid concatenated key
2. Automatic jump
3. After job
4. All joined

**Correct Answer:** 1

---

## Question 210

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is regression testing for IMS DC?

**Options:**
1. Retesting after changes
2. Performance testing
3. Load testing
4. Security testing

**Correct Answer:** 1

---

## Question 211

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How to test concurrent transaction processing?

**Options:**
1. Multi-user or load testing tools
2. Single user test
3. Not possible
4. Manual testing

**Correct Answer:** 1

---

## Question 212

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is a help transaction?

**Options:**
1. Provides user assistance information
2. System help
3. Technical support
4. Error help

**Correct Answer:** 1

---

## Question 213

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is audit trail in maintenance programs?

**Options:**
1. Logging of all changes made
2. Program trace
3. Debug log
4. Error log

**Correct Answer:** 1

---

## Question 214

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is OTMA?

**Options:**
1. Open Transaction Manager Access
2. Online Terminal Manager Access
3. Output Transaction Management
4. Operational Task Management

**Correct Answer:** 1

---

## Question 215

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is program restart capability?

**Options:**
1. Resume processing after failure
2. Rerun program
3. Reload program
4. Reset program

**Correct Answer:** 1

---

## Question 216

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is message region?

**Options:**
1. Region where MPPs execute
2. Message storage
3. Message area
4. Message buffer

**Correct Answer:** 1

---

## Question 217

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How many message regions can IMS support?

**Options:**
1. Multiple, based on configuration
2. Only one
3. Maximum 10
4. Unlimited

**Correct Answer:** 1

---

## Question 218

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is segment name field in DB PCB?

**Options:**
1. Name of last accessed segment
2. Current segment
3. Target segment
4. Root segment

**Correct Answer:** 1

---

## Question 219

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is key feedback area?

**Options:**
1. Contains concatenated key of current position
2. Error feedback
3. Status feedback
4. Result feedback

**Correct Answer:** 1

---

## Question 220

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is security profile in IMS DC?

**Options:**
1. Defines access authorizations
2. User profile
3. System profile
4. Network profile

**Correct Answer:** 1

---

## Question 221

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is terminal preemption?

**Options:**
1. Taking over terminal for urgent message
2. Terminal disconnect
3. Terminal reset
4. Terminal lock

**Correct Answer:** 1

---

## Question 222

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is the primary purpose of Message Format Services (MFS) in IMS DC?

**Options:**
1. Format messages between application programs and terminals
2. Store messages in databases
3. Route messages to appropriate programs
4. Compress message data

**Correct Answer:** 1

---

## Question 223

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Which MFS control block defines the physical terminal characteristics?

**Options:**
1. DIF (Device Input Format)
2. DOF (Device Output Format)
3. MID (Message Input Descriptor)
4. MOD (Message Output Descriptor)

**Correct Answer:** 1

---

## Question 224

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What does MOD stand for in MFS?

**Options:**
1. Message Output Descriptor
2. Module Definition
3. Message Organizational Data
4. Multiple Output Device

**Correct Answer:** 1

---

## Question 225

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Which MFS control block maps the application program's view of a message?

**Options:**
1. MID (Message Input Descriptor)
2. DIF (Device Input Format)
3. FMT (Format)
4. PCB (Program Communication Block)

**Correct Answer:** 1

---

## Question 226

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** In MFS, what is the purpose of the DFLD (Device Field) statement?

**Options:**
1. Define physical field location on screen
2. Define database field mapping
3. Define field validation rules
4. Define field compression

**Correct Answer:** 1

---

## Question 227

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What MFS statement defines the logical message field for the application?

**Options:**
1. MFLD (Message Field)
2. DFLD (Device Field)
3. LFLD (Logical Field)
4. AFLD (Application Field)

**Correct Answer:** 1

---

## Question 228

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Which attribute controls whether a field is protected or unprotected on a 3270 screen?

**Options:**
1. ATTR parameter
2. PROT parameter
3. FIELD parameter
4. SECURE parameter

**Correct Answer:** 1

---

## Question 229

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What does the FILL parameter in MFS specify?

**Options:**
1. Character to fill unused field positions
2. Default value for empty fields
3. Field justification
4. Field alignment

**Correct Answer:** 1

---

## Question 230

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Which MFS format is used for output messages?

**Options:**
1. DOF and MOD
2. DIF and MID
3. FMT and MSG
4. OUT and DISP

**Correct Answer:** 1

---

## Question 231

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What tool is used to compile MFS source definitions?

**Options:**
1. MFS Language Utility
2. IMS Compiler
3. COBOL Compiler
4. Assembler

**Correct Answer:** 1

---

## Question 232

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Where are compiled MFS formats stored?

**Options:**
1. IMS Format Library
2. IMS Database
3. Application Library
4. System Catalog

**Correct Answer:** 1

---

## Question 233

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is the purpose of the LITERAL parameter in DFLD?

**Options:**
1. Display constant text on screen
2. Define literal values for comparison
3. Create literal database fields
4. Generate literal documentation

**Correct Answer:** 1

---

## Question 234

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can MFS perform automatic data type conversion?

**Options:**
1. Yes, between character and numeric formats
2. No, program must do all conversions
3. Yes, but only for dates
4. Only with special hardware

**Correct Answer:** 1

---

## Question 235

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What does the JUSTIFY parameter control in MFLD?

**Options:**
1. Left or right justification of data in field
2. Vertical alignment on screen
3. Field validation method
4. Error message positioning

**Correct Answer:** 1

---

## Question 236

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What is the standard screen size for a 3270 terminal model 2?

**Options:**
1. 24 rows by 80 columns
2. 25 rows by 80 columns
3. 24 rows by 132 columns
4. 32 rows by 80 columns

**Correct Answer:** 1

---

## Question 237

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What does the MDT (Modified Data Tag) attribute indicate?

**Options:**
1. Field has been modified by user
2. Field contains master data
3. Field is mandatory
4. Field is for date entry

**Correct Answer:** 1

---

## Question 238

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Which 3270 attribute makes a field invisible to the user?

**Options:**
1. Dark/Non-display attribute
2. Hidden attribute
3. Protected attribute
4. Masked attribute

**Correct Answer:** 1

---

## Question 239

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What happens when a user presses ENTER on a 3270 screen?

**Options:**
1. Only fields with MDT on are transmitted
2. All fields are transmitted
3. Only unprotected fields are transmitted
4. Only modified unprotected fields are transmitted

**Correct Answer:** 1

---

## Question 240

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How can a program clear the entire screen?

**Options:**
1. Send ERASE WRITE command via MFS or control characters
2. Use CLEAR PCB call
3. Issue DELETE SCREEN command
4. Send blank message

**Correct Answer:** 1

---

## Question 241

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is cursor positioning in IMS DC screen handling?

**Options:**
1. Placing cursor at specific screen location for user input
2. Moving cursor automatically through fields
3. Cursor blinking control
4. Cursor shape definition

**Correct Answer:** 1

---

## Question 242

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Which MFS parameter positions the cursor on a screen?

**Options:**
1. CURSOR parameter
2. POSITION parameter
3. LOCATE parameter
4. POINT parameter

**Correct Answer:** 1

---

## Question 243

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What are extended highlighting attributes used for?

**Options:**
1. Color, blinking, reverse video, underline
2. Font size changes
3. Graphics display
4. Sound effects

**Correct Answer:** 1

---

## Question 244

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Easy  
**Type:** Single Choice

**Question:** What does a protected field prevent?

**Options:**
1. User from typing into the field
2. Field from being displayed
3. Field from being read by program
4. Field from being colored

**Correct Answer:** 1

---

## Question 245

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is the purpose of the ALARM parameter in screen formatting?

**Options:**
1. Sound terminal alarm/beep on error
2. Set time limit for user input
3. Alert operator of system error
4. Trigger security alarm

**Correct Answer:** 1

---

## Question 246

**Topic:** IMS DC - Message Field Editing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What MFS editing pattern would format a number with comma separators?

**Options:**
1. EDIT='999,999,999'
2. EDIT='FORMAT-COMMA'
3. EDIT='NUMBER-MASK'
4. EDIT='SEPARATE'

**Correct Answer:** 1

---

## Question 247

**Topic:** IMS DC - Message Field Editing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How does MFS handle leading zeros in numeric fields?

**Options:**
1. Can suppress with appropriate edit pattern
2. Always displays leading zeros
3. Always suppresses leading zeros
4. Requires program logic

**Correct Answer:** 1

---

## Question 248

**Topic:** IMS DC - Message Field Editing  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What does the 'Z' character in an edit pattern do?

**Options:**
1. Suppresses leading zeros
2. Represents zero value
3. Adds zero padding
4. Zones numeric field

**Correct Answer:** 1

---

## Question 249

**Topic:** IMS DC - Message Field Editing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How can MFS add a currency symbol to a field?

**Options:**
1. Include '$' in edit pattern
2. Use CURRENCY parameter
3. Requires program code
4. Use SYMBOL parameter

**Correct Answer:** 1

---

## Question 250

**Topic:** IMS DC - Message Field Editing  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What editing can MFS perform on date fields?

**Options:**
1. Reformatting, separator insertion, validation
2. Date arithmetic only
3. No date editing available
4. Century windowing only

**Correct Answer:** 1

---

## Question 251

**Topic:** IMS DC - Message Field Editing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What does the 'CR' notation in an edit pattern indicate?

**Options:**
1. Credit (negative) balance indicator
2. Carriage return control
3. Create record function
4. Current rate display

**Correct Answer:** 1

---

## Question 252

**Topic:** IMS DC - Message Field Editing  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** How does MFS handle field overflow during editing?

**Options:**
1. Can truncate, asterisk fill, or error
2. Always truncates silently
3. Always errors and abends
4. Automatically expands field

**Correct Answer:** 1

---

## Question 253

**Topic:** IMS DC - Message Field Editing  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can MFS perform uppercase/lowercase conversion?

**Options:**
1. Yes, via field attributes
2. No, requires program logic
3. Only for alphabetic fields
4. Only with special hardware

**Correct Answer:** 1

---

## Question 254

**Topic:** IMS DC - Multi-segment Messages  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is a multi-segment message in IMS DC?

**Options:**
1. Message broken into multiple logical segments
2. Message sent to multiple terminals
3. Message with multiple transaction codes
4. Message split across multiple screens

**Correct Answer:** 1

---

## Question 255

**Topic:** IMS DC - Multi-segment Messages  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How does a program retrieve multiple input message segments?

**Options:**
1. Issue multiple GU or GN calls to I/O PCB
2. Single GET-ALL call
3. Use RETRIEVE SEGMENTS call
4. Automatic concatenation by IMS

**Correct Answer:** 1

---

## Question 256

**Topic:** IMS DC - Multi-segment Messages  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What status code indicates no more message segments available?

**Options:**
1. QD status code
2. QC status code
3. GB status code
4. NM status code

**Correct Answer:** 1

---

## Question 257

**Topic:** IMS DC - Multi-segment Messages  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How does a program send a multi-segment output message?

**Options:**
1. Issue multiple ISRT calls to I/O PCB
2. Use SEND-MULTIPLE call
3. Concatenate segments in program
4. Use special MOD format

**Correct Answer:** 1

---

## Question 258

**Topic:** IMS DC - Multi-segment Messages  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What determines segment boundaries in multi-segment messages?

**Options:**
1. Segment size defined in MFS or program logic
2. Fixed 80-byte segments
3. Screen size limits
4. Transaction code definition

**Correct Answer:** 1

---

## Question 259

**Topic:** IMS DC - Multi-segment Messages  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can segments within a message have different formats?

**Options:**
1. Yes, each segment can have unique structure
2. No, all segments must be identical
3. Only in conversational transactions
4. Only with MFS support

**Correct Answer:** 1

---

## Question 260

**Topic:** IMS DC - Multi-segment Messages  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is message chaining in IMS DC?

**Options:**
1. Linking multiple messages for single transaction
2. Sending messages sequentially
3. Connecting terminals together
4. Database chain processing

**Correct Answer:** 1

---

## Question 261

**Topic:** IMS DC - Error Recovery  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What should a program do when receiving an unexpected status code?

**Options:**
1. Check PCB, log error, send user message, rollback if needed
2. Ignore and continue processing
3. Always abend immediately
4. Return to operating system

**Correct Answer:** 1

---

## Question 262

**Topic:** IMS DC - Error Recovery  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What IMS call can a program use to signal abnormal termination?

**Options:**
1. ROLL or ROLB call
2. ABEND call
3. TERM call
4. EXIT call

**Correct Answer:** 1

---

## Question 263

**Topic:** IMS DC - Error Recovery  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What does the ROLL call do?

**Options:**
1. Backs out database and message changes
2. Rolls forward transaction log
3. Rotates log datasets
4. Rolls back operating system

**Correct Answer:** 1

---

## Question 264

**Topic:** IMS DC - Error Recovery  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** After a ROLB call, what happens to the input message?

**Options:**
1. Can be requeued or discarded based on ROLB type
2. Always requeued for retry
3. Always discarded permanently
4. Sent to error queue

**Correct Answer:** 1

---

## Question 265

**Topic:** IMS DC - Error Recovery  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is the purpose of the SETS and SETO calls?

**Options:**
1. Set commit point for database and message changes
2. Set error recovery options
3. Set terminal output mode
4. Set security level

**Correct Answer:** 1

---

## Question 266

**Topic:** IMS DC - Error Recovery  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** How should a program handle a database deadlock?

**Options:**
1. Receive BA status, issue ROLB, retry or exit
2. Wait indefinitely for lock release
3. Force lock override
4. Abend immediately

**Correct Answer:** 1

---

## Question 267

**Topic:** IMS DC - Error Recovery  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What information should error messages to users include?

**Options:**
1. Clear description, action required, contact info if needed
2. Technical status codes only
3. Complete abend dump
4. Database structure details

**Correct Answer:** 1

---

## Question 268

**Topic:** IMS DC - Error Recovery  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What happens to output messages after a ROLB?

**Options:**
1. All output messages are discarded
2. Output messages are still sent
3. Only error messages are sent
4. Output is queued for manual review

**Correct Answer:** 1

---

## Question 269

**Topic:** IMS DC - Program Switching  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What DL/I call transfers control to another IMS program?

**Options:**
1. XRST (Transfer)
2. CALL
3. LINK
4. SWITCH

**Correct Answer:** 1

---

## Question 270

**Topic:** IMS DC - Program Switching  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What happens to database position after program switch (XRST)?

**Options:**
1. Position is maintained for called program
2. Position is reset to beginning
3. Position is lost completely
4. Depends on PCB type

**Correct Answer:** 1

---

## Question 271

**Topic:** IMS DC - Program Switching  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can a program switch return control to the calling program?

**Options:**
1. No, XRST is one-way transfer
2. Yes, automatically returns
3. Yes, with RETURN call
4. Only in conversational mode

**Correct Answer:** 1

---

## Question 272

**Topic:** IMS DC - Program Switching  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What data can be passed to the switched-to program?

**Options:**
1. Data in I/O area specified on XRST call
2. No data transfer possible
3. Complete working storage
4. Only transaction code

**Correct Answer:** 1

---

## Question 273

**Topic:** IMS DC - Program Switching  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Why use program switching instead of COBOL CALL?

**Options:**
1. XRST provides IMS context and PCB access
2. XRST is faster
3. XRST uses less memory
4. COBOL CALL not supported

**Correct Answer:** 1

---

## Question 274

**Topic:** IMS DC - Program Switching  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What security applies when switching programs?

**Options:**
1. Target program must be authorized for transaction
2. No security checks performed
3. Original program security carries over
4. User must reauthorize

**Correct Answer:** 1

---

## Question 275

**Topic:** IMS DC - Transaction Restart  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is transaction restart in IMS DC?

**Options:**
1. Automatic reprocessing of failed transaction
2. Manual transaction resubmission
3. System restart after crash
4. Transaction code redefinition

**Correct Answer:** 1

---

## Question 276

**Topic:** IMS DC - Transaction Restart  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** When does IMS automatically restart a transaction?

**Options:**
1. After certain abends or system failures
2. After every abend
3. Never automatically
4. Only during scheduled maintenance

**Correct Answer:** 1

---

## Question 277

**Topic:** IMS DC - Transaction Restart  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is a checkpoint in the context of transaction processing?

**Options:**
1. Point where transaction state is saved for recovery
2. End of transaction
3. Security validation point
4. Performance measurement point

**Correct Answer:** 1

---

## Question 278

**Topic:** IMS DC - Transaction Restart  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How can a program make itself non-restartable?

**Options:**
1. Issue ROLB call or define transaction as non-restartable
2. Cannot prevent restart
3. Set NORESTART flag
4. Use special PCB option

**Correct Answer:** 1

---

## Question 279

**Topic:** IMS DC - Transaction Restart  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What programming practice helps ensure clean transaction restart?

**Options:**
1. Design idempotent operations, avoid external side effects
2. Use global variables
3. Cache all data in memory
4. Disable all error checking

**Correct Answer:** 1

---

## Question 280

**Topic:** IMS DC - Transaction Restart  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What happens to database updates during automatic restart?

**Options:**
1. Rolled back and reapplied during restart
2. Lost permanently
3. Kept as-is from failed run
4. Manually recovered

**Correct Answer:** 1

---

## Question 281

**Topic:** IMS DC - Data Validation  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Where should input data validation occur?

**Options:**
1. As early as possible in application logic
2. Only at database update time
3. Only in batch programs
4. Validation not needed with MFS

**Correct Answer:** 1

---

## Question 282

**Topic:** IMS DC - Data Validation  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What types of validation should online programs perform?

**Options:**
1. Format, range, required fields, cross-field edits
2. Only numeric validation
3. Only database constraint checking
4. No validation needed

**Correct Answer:** 1

---

## Question 283

**Topic:** IMS DC - Data Validation  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** How should a program handle multiple validation errors?

**Options:**
1. Collect all errors and report together
2. Report first error only
3. Abend on first error
4. Ignore all but critical errors

**Correct Answer:** 1

---

## Question 284

**Topic:** IMS DC - COBOL Program Structure  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What special COBOL division is used for IMS programs?

**Options:**
1. No special division, standard COBOL structure
2. IMS DIVISION
3. DL/I DIVISION
4. TRANSACTION DIVISION

**Correct Answer:** 1

---

## Question 285

**Topic:** IMS DC - COBOL Program Structure  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Where are PCB masks defined in COBOL?

**Options:**
1. LINKAGE SECTION
2. WORKING-STORAGE SECTION
3. FILE SECTION
4. LOCAL-STORAGE SECTION

**Correct Answer:** 1

---

## Question 286

**Topic:** IMS DC - COBOL Program Structure  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What is the ENTRY parameter 'DLITCBL' used for?

**Options:**
1. Entry point for IMS to call COBOL program
2. Database entry definition
3. Transaction entry point
4. Error entry routine

**Correct Answer:** 1

---

## Question 287

**Topic:** IMS DC - COBOL Program Structure  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How does a COBOL program receive its PCB addresses?

**Options:**
1. Via ENTRY USING statement parameters
2. From WORKING-STORAGE
3. Through ACCEPT statement
4. From JCL parameters

**Correct Answer:** 1

---

## Question 288

**Topic:** IMS DC - COBOL Program Structure  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What COBOL statement issues DL/I calls?

**Options:**
1. CALL 'CBLTDLI' USING...
2. EXEC DLI
3. INVOKE DLI
4. DLI-CALL

**Correct Answer:** 1

---

## Question 289

**Topic:** IMS DC - COBOL Program Structure  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** How should a COBOL IMS program terminate normally?

**Options:**
1. GOBACK or STOP RUN statement
2. ROLLBACK statement
3. EXIT PROGRAM only
4. TERMINATE DLI

**Correct Answer:** 1

---

## Question 290

**Topic:** IMS DC - COBOL Program Structure  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** Can IMS COBOL programs use files (FILE SECTION)?

**Options:**
1. Generally no, should use DL/I for data access
2. Yes, fully supported
3. Only sequential files
4. Only for output

**Correct Answer:** 1

---

## Question 291

**Topic:** IMS DC - PCB Details  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What field in the I/O PCB contains the message sequence number?

**Options:**
1. Not standard in I/O PCB, may be in alternate PCB
2. MSG-SEQ-NUM field
3. SEQUENCE-FIELD
4. TRANS-SEQ field

**Correct Answer:** 1

---

## Question 292

**Topic:** IMS DC - PCB Details  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What does the LTERM field in I/O PCB identify?

**Options:**
1. Logical terminal name (8 characters)
2. Physical terminal address
3. User ID
4. Terminal type code

**Correct Answer:** 1

---

## Question 293

**Topic:** IMS DC - Status Codes  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What does status code 'QC' indicate?

**Options:**
1. No more input message segments (message complete)
2. Queue is closed
3. Query completed
4. Quick commit performed

**Correct Answer:** 1

---

## Question 294

**Topic:** IMS DC - Status Codes  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What status code indicates segment not found in database?

**Options:**
1. GE status code
2. NF status code
3. GB status code
4. NS status code

**Correct Answer:** 1

---

## Question 295

**Topic:** IMS DC - Status Codes  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** What does 'BA' status code mean?

**Options:**
1. Resource unavailable/deadlock detected
2. Bad address in call
3. Batch mode active
4. Buffer allocation failed

**Correct Answer:** 1

---

## Question 296

**Topic:** IMS DC - Status Codes  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What status indicates successful database update?

**Options:**
1. Blank or spaces status code
2. OK status code
3. 00 status code
4. SU status code

**Correct Answer:** 1

---

## Question 297

**Topic:** IMS DC - Best Practices  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** Why should online programs minimize database holds?

**Options:**
1. Reduce contention and improve concurrency
2. Save memory
3. Improve screen response
4. Reduce network traffic

**Correct Answer:** 1

---

## Question 298

**Topic:** IMS DC - Best Practices  
**Difficulty:** Medium  
**Type:** Single Choice

**Question:** What is a common pitfall in IMS DC programming?

**Options:**
1. Not checking status codes after every DL/I call
2. Using too many comments
3. Making programs too modular
4. Testing too thoroughly

**Correct Answer:** 1

---

## Question 299

**Topic:** IMS DC - Real-world Application  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** In a customer inquiry transaction, what's the recommended approach?

**Options:**
1. Retrieve data, format output, send to user, no database holds
2. Hold database locks during user review
3. Update database with inquiry timestamp
4. Always use conversational mode

**Correct Answer:** 1

---

## Question 300

**Topic:** IMS DC - Real-world Application  
**Difficulty:** Hard  
**Type:** Single Choice

**Question:** For a complex update transaction requiring validation from multiple sources, what's best?

**Options:**
1. Gather all data, validate completely, then update atomically
2. Update as you go, validating each piece
3. Skip validation to improve performance
4. Use separate transactions for each piece

**Correct Answer:** 1

---

