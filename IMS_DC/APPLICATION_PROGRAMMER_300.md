# IMS DC Application Programmer - 300 Questions

This file contains 300 questions covering IMS DC (Data Communications) topics for application programmers.

---

## Question 1

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What does IMS DC stand for?

**Options:**
1. Direct Connection
2. Database Control
3. Data Center
4. Data Communications

**Correct Answer:** 4

---

## Question 2

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is the primary purpose of IMS DC?

**Options:**
1. Network routing
2. File management
3. Online transaction processing
4. Batch processing only

**Correct Answer:** 3

---

## Question 3

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Which component manages message flow in IMS DC?

**Options:**
1. Message Processing Region
2. Transaction Manager
3. Batch Message Processing
4. IMS Control Region

**Correct Answer:** 2

---

## Question 4

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is a terminal in IMS DC context?

**Options:**
1. Only physical terminals
2. Logical unit of work
3. Any input/output device
4. Database connection

**Correct Answer:** 3

---

## Question 5

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** IMS DC supports which processing modes?

**Options:**
1. Batch only
2. Both online and batch
3. Real-time only
4. Online only

**Correct Answer:** 2

---

## Question 6

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is the IMS DC environment primarily designed for?

**Options:**
1. Report generation
2. File transfers
3. Data warehousing
4. High-volume transaction processing

**Correct Answer:** 4

---

## Question 7

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Which layer handles communication with terminals?

**Options:**
1. Database layer
2. Communication layer
3. Application layer
4. Control layer

**Correct Answer:** 2

---

## Question 8

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What does LTERM represent?

**Options:**
1. Last terminal
2. Link terminal
3. Logical terminal
4. Local terminal

**Correct Answer:** 3

---

## Question 9

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is the purpose of transaction codes?

**Options:**
1. Identify and route transactions to appropriate programs
2. Validate user credentials
3. Encrypt messages
4. Store transaction history

**Correct Answer:** 1

---

## Question 10

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** IMS DC can process how many transactions?

**Options:**
1. Tens per hour
2. One at a time
3. Thousands per second
4. Hundreds per minute

**Correct Answer:** 3

---

## Question 11

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What does MPP stand for in IMS DC?

**Options:**
1. Master Program Processor
2. Multiple Program Processing
3. Message Protocol Program
4. Message Processing Program

**Correct Answer:** 4

---

## Question 12

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is the primary function of an MPP?

**Options:**
1. Manage security
2. Backup databases
3. Generate reports
4. Process online transactions

**Correct Answer:** 4

---

## Question 13

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How does an MPP receive input?

**Options:**
1. Command line
2. Direct terminal access
3. Through message queues
4. File input

**Correct Answer:** 3

---

## Question 14

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** Can an MPP update databases?

**Options:**
1. Only with special authorization
2. Only in batch mode
3. No, read-only access
4. Yes, using DL/I calls

**Correct Answer:** 4

---

## Question 15

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What happens when an MPP completes processing?

**Options:**
1. Sends response to output queue
2. Terminates immediately
3. Restarts the system
4. Waits for next transaction

**Correct Answer:** 1

---

## Question 16

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Which PCB does an MPP use for message I/O?

**Options:**
1. Express PCB
2. I/O PCB
3. Alternate PCB
4. DB PCB

**Correct Answer:** 2

---

## Question 17

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Can multiple MPPs process the same transaction code?

**Options:**
1. No, only one MPP per transaction
2. Only with system approval
3. Only in test environments
4. Yes, for load balancing

**Correct Answer:** 4

---

## Question 18

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is the main difference between MPP and BMP?

**Options:**
1. MPP is faster
2. No difference
3. MPP processes online messages, BMP runs in batch
4. BMP has priority

**Correct Answer:** 3

---

## Question 19

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How does IMS DC schedule MPPs?

**Options:**
1. Alphabetically by name
2. Random selection
3. First-come, first-served
4. Based on message queue depth and priority

**Correct Answer:** 4

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
2. 16 characters
3. 32 characters
4. 4 characters

**Correct Answer:** 1

---

## Question 22

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** Where is the transaction code placed in a message?

**Options:**
1. At the beginning
2. Anywhere
3. In the middle
4. At the end

**Correct Answer:** 1

---

## Question 23

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What determines which program processes a transaction?

**Options:**
1. Message content
2. User preference
3. Terminal ID
4. Transaction code definition

**Correct Answer:** 4

---

## Question 24

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Can a transaction code be associated with multiple programs?

**Options:**
1. Yes, but not recommended
2. Only in test mode
3. No, one-to-one relationship
4. Yes, many-to-many

**Correct Answer:** 3

---

## Question 25

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is transaction priority?

**Options:**
1. Message size limit
2. Determines processing order
3. Security level
4. Response time requirement

**Correct Answer:** 2

---

## Question 26

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What happens if an invalid transaction code is entered?

**Options:**
1. System crash
2. Default program executed
3. Error message returned to terminal
4. Transaction ignored

**Correct Answer:** 3

---

## Question 27

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Can transaction codes be defined dynamically?

**Options:**
1. Only by system administrator
2. Yes, by any user
3. Yes, at runtime
4. No, must be pre-defined in system definition

**Correct Answer:** 4

---

## Question 28

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is a conversational transaction?

**Options:**
1. Processes multiple messages
2. Requires user confirmation
3. Maintains state between messages
4. Uses conversation API

**Correct Answer:** 3

---

## Question 29

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is transaction class?

**Options:**
1. Program language
2. Security classification
3. Groups transactions for scheduling
4. Message format type

**Correct Answer:** 3

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
1. Memory buffer
2. Input message queue
3. Log file
4. Database

**Correct Answer:** 2

---

## Question 32

**Topic:** IMS DC - Message Queues  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What determines message processing order?

**Options:**
1. Priority and arrival time
2. Random selection
3. Alphabetical order
4. Message size

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
1. No, all equal priority
2. Only in batch mode
3. Yes, 0-9 or 0-15 depending on system
4. Yes, low/medium/high only

**Correct Answer:** 3

---

## Question 35

**Topic:** IMS DC - Message Queues  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is message queuing?

**Options:**
1. Sorting messages
2. Encrypting messages
3. Temporarily storing messages for processing
4. Archiving messages

**Correct Answer:** 3

---

## Question 36

**Topic:** IMS DC - Message Queues  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Where are queues physically stored?

**Options:**
1. In memory only
2. On tape
3. In user files
4. In IMS queue datasets

**Correct Answer:** 4

---

## Question 37

**Topic:** IMS DC - Message Queues  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is a scratch pad area (SPA)?

**Options:**
1. Temporary work area
2. Storage for conversational transaction data
3. Message buffer
4. Error log

**Correct Answer:** 2

---

## Question 38

**Topic:** IMS DC - Message Queues  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Can messages be retrieved from queues non-destructively?

**Options:**
1. Yes, using browse functions
2. Only in test mode
3. No, always destructive
4. Only by operators

**Correct Answer:** 1

---

## Question 39

**Topic:** IMS DC - Message Queues  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is message flooding?

**Options:**
1. Multiple duplicate messages
2. Queue overflow condition
3. Message corruption
4. Rapid message arrival

**Correct Answer:** 2

---

## Question 40

**Topic:** IMS DC - Message Queues  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How long can messages remain in queues?

**Options:**
1. Until system restart
2. Maximum 24 hours
3. Maximum 1 hour
4. Until processed or expired

**Correct Answer:** 4

---

## Question 41

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What does I/O PCB stand for?

**Options:**
1. Intelligent Output PCB
2. Interface Output Process Control Block
3. Input/Output Program Communication Block
4. Internal Operation PCB

**Correct Answer:** 3

---

## Question 42

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is the primary use of I/O PCB?

**Options:**
1. File operations
2. Database access
3. Message input and output
4. Program control

**Correct Answer:** 3

---

## Question 43

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Which field in I/O PCB contains the logical terminal name?

**Options:**
1. ID field
2. NAME field
3. TERM field
4. LTERM field

**Correct Answer:** 4

---

## Question 44

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What status code indicates successful message retrieval?

**Options:**
1. SUCCESS
2. Spaces or blank
3. OK
4. 00

**Correct Answer:** 2

---

## Question 45

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Which field indicates message length in I/O PCB?

**Options:**
1. Message length field
2. Segment length field
3. Size field
4. Data length field

**Correct Answer:** 2

---

## Question 46

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** Can I/O PCB be used for database operations?

**Options:**
1. Only for read operations
2. No, only for message I/O
3. Only with special setup
4. Yes, for any operation

**Correct Answer:** 2

---

## Question 47

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is the status code field length in I/O PCB?

**Options:**
1. 1 byte
2. 4 bytes
3. 8 bytes
4. 2 bytes

**Correct Answer:** 4

---

## Question 48

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Which field identifies the originating terminal?

**Options:**
1. Terminal ID
2. User ID
3. LTERM name
4. Source field

**Correct Answer:** 3

---

## Question 49

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What does QC status code indicate?

**Options:**
1. Query complete
2. No more messages in queue
3. Queue corrupted
4. Quick complete

**Correct Answer:** 2

---

## Question 50

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How many I/O PCBs can a program have?

**Options:**
1. Unlimited
2. Maximum of 5
3. Exactly one
4. Typically one, but can have alternate PCBs

**Correct Answer:** 4

---

## Question 51

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** Which DL/I call retrieves the input message?

**Options:**
1. REPL (Replace)
2. GN (Get Next)
3. ISRT (Insert)
4. GU (Get Unique)

**Correct Answer:** 4

---

## Question 52

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** Which DL/I call sends output to terminal?

**Options:**
1. REPL to I/O PCB
2. PUT to I/O PCB
3. GU from I/O PCB
4. ISRT to I/O PCB

**Correct Answer:** 4

---

## Question 53

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is the purpose of GU call against I/O PCB?

**Options:**
1. Retrieve input message from queue
2. Get unique record
3. General update
4. Get user information

**Correct Answer:** 1

---

## Question 54

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Can GN be used with I/O PCB?

**Options:**
1. Yes, to retrieve multiple message segments
2. Yes, but deprecated
3. Only in batch mode
4. No, only GU is allowed

**Correct Answer:** 1

---

## Question 55

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** How do you send a message to a specific terminal?

**Options:**
1. WRITE to terminal
2. ISRT with modified LTERM in I/O PCB
3. SEND command
4. GU to terminal

**Correct Answer:** 2

---

## Question 56

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What happens if ISRT fails on I/O PCB?

**Options:**
1. Status code set in I/O PCB
2. System restart
3. Program abends
4. Message lost

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
1. Open the PCB
2. Initialize message area
3. Set terminal ID
4. Nothing, just issue the call

**Correct Answer:** 4

---

## Question 59

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How many ISRT calls can send one logical message?

**Options:**
1. Maximum of 10
2. Depends on terminal type
3. Only one ISRT per message
4. Multiple ISRTs for multi-segment messages

**Correct Answer:** 4

---

## Question 60

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What indicates end of input message segments?

**Options:**
1. Zero length
2. QC status code on GN
3. Null segment
4. EOF indicator

**Correct Answer:** 2

---

## Question 61

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is a non-conversational transaction?

**Options:**
1. Requires multiple interactions
2. Has no output
3. Runs in background
4. Completes in single input/output cycle

**Correct Answer:** 4

---

## Question 62

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What characterizes a conversational transaction?

**Options:**
1. Requires no database
2. Uses less memory
3. Maintains data between interactions
4. Processes faster

**Correct Answer:** 3

---

## Question 63

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Where is conversation state stored?

**Options:**
1. Database
2. Terminal buffer
3. Scratch Pad Area (SPA)
4. Program memory

**Correct Answer:** 3

---

## Question 64

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Which mode is more resource efficient?

**Options:**
1. Non-conversational
2. Conversational
3. Depends on transaction
4. Both equal

**Correct Answer:** 1

---

## Question 65

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** How does SPA get passed between conversations?

**Options:**
1. Via global memory
2. IMS automatically includes it in messages
3. Stored in database
4. Program must explicitly pass it

**Correct Answer:** 2

---

## Question 66

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is a typical use for conversational transactions?

**Options:**
1. High-volume processing
2. Simple inquiries
3. Multi-screen data entry
4. Batch updates

**Correct Answer:** 3

---

## Question 67

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Can a program switch between conversational modes?

**Options:**
1. Yes, dynamically
2. Yes, with special flag
3. No, determined by transaction definition
4. Only once per session

**Correct Answer:** 3

---

## Question 68

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What happens if user abandons a conversation?

**Options:**
1. System error
2. Resources held indefinitely
3. Automatic rollback
4. SPA eventually purged by IMS

**Correct Answer:** 4

---

## Question 69

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How is SPA defined?

**Options:**
1. In the transaction definition
2. In terminal definition
3. In the program
4. At runtime

**Correct Answer:** 1

---

## Question 70

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is the disadvantage of conversational transactions?

**Options:**
1. Slower response time
2. Higher resource consumption
3. Less functionality
4. More complex programming

**Correct Answer:** 2

---

## Question 71

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is a message segment?

**Options:**
1. Terminal identifier
2. Transaction code
3. Timestamp
4. A logical unit of message data

**Correct Answer:** 4

---

## Question 72

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is the maximum message segment size?

**Options:**
1. 64KB
2. No limit
3. System dependent, typically up to 32KB
4. 1MB

**Correct Answer:** 3

---

## Question 73

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How are multi-segment messages identified?

**Options:**
1. Segment IDs
2. Message headers
3. By IMS internally, transparent to application
4. Sequence numbers

**Correct Answer:** 3

---

## Question 74

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is message edit/routing?

**Options:**
1. Encrypting data
2. Validating and directing messages
3. Compressing messages
4. Formatting output

**Correct Answer:** 2

---

## Question 75

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Can message format be defined?

**Options:**
1. Only for output
2. Yes, using MFS (Message Format Service)
3. No, always free format
4. Yes, but not recommended

**Correct Answer:** 2

---

## Question 76

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is the purpose of LL ZZ fields?

**Options:**
1. Load level zones
2. Location labels
3. Logical link zones
4. Length and reserved fields in message segments

**Correct Answer:** 4

---

## Question 77

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Where is transaction code in message structure?

**Options:**
1. At the end
2. Variable position
3. In message header
4. First field after LL ZZ

**Correct Answer:** 4

---

## Question 78

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is message switching?

**Options:**
1. Changing message format
2. Swapping message segments
3. Message encryption
4. Routing messages to different destinations

**Correct Answer:** 4

---

## Question 79

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Can a message contain binary data?

**Options:**
1. Yes, but requires proper handling
2. Yes, but not recommended
3. No, text only
4. Only in file transfers

**Correct Answer:** 1

---

## Question 80

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is message class?

**Options:**
1. Format type
2. Categorization for processing
3. Security classification
4. Priority level

**Correct Answer:** 2

---

## Question 81

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How is I/O PCB defined in COBOL?

**Options:**
1. In FILE SECTION
2. In LINKAGE SECTION
3. In PROCEDURE DIVISION
4. In WORKING-STORAGE

**Correct Answer:** 2

---

## Question 82

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is the ENTRY statement for IMS program?

**Options:**
1. DLITCBL for DL/I programs
2. START
3. MAIN
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
2. PERFORM DLI-CALL
3. EXEC DLI command
4. DLI statement

**Correct Answer:** 1

---

## Question 84

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What parameters are passed to CBLTDLI?

**Options:**
1. Function and I/O area
2. All PCBs
3. Function code, PCB, I/O area, SSAs
4. PCB only

**Correct Answer:** 3

---

## Question 85

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** How is message I/O area defined?

**Options:**
1. CONFIGURATION SECTION
2. SPECIAL-NAMES
3. In WORKING-STORAGE or LINKAGE
4. FILE SECTION

**Correct Answer:** 3

---

## Question 86

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What COBOL level for PCB mask?

**Options:**
1. 05 level
2. 88 level
3. 01 level
4. 77 level

**Correct Answer:** 3

---

## Question 87

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** How to check status code in COBOL?

**Options:**
1. CHECK STATUS statement
2. Test status field in PCB
3. IF DLI-STATUS
4. INSPECT STATUS

**Correct Answer:** 2

---

## Question 88

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is the PCB mask pointer?

**Options:**
1. PCB identifier
2. PCB flag
3. PCB counter
4. Address pointer to PCB in LINKAGE

**Correct Answer:** 4

---

## Question 89

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How to handle multiple output segments?

**Options:**
1. SEND-ALL
2. WRITE-MULTIPLE
3. Multiple ISRT calls
4. Single ISRT with array

**Correct Answer:** 3

---

## Question 90

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is GOBACK used for?

**Options:**
1. Return to caller
2. Return control to IMS
3. Exit program
4. Go back in processing

**Correct Answer:** 2

---

## Question 91

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What does blank status code mean?

**Options:**
1. Not processed
2. Successful operation
3. Unknown error
4. No status available

**Correct Answer:** 2

---

## Question 92

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What does QD status code mean?

**Options:**
1. Query denied
2. Quick delete
3. Queue destroyed
4. Message not found in queue

**Correct Answer:** 4

---

## Question 93

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is AI status code?

**Options:**
1. Automatic insert
2. All inserted
3. Indicates potential data integrity issue
4. Application interface error

**Correct Answer:** 3

---

## Question 94

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** How should programs handle error status codes?

**Options:**
1. Check after each call and take appropriate action
2. Let IMS handle all errors
3. Log and continue
4. Ignore non-critical errors

**Correct Answer:** 1

---

## Question 95

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What does AM status code indicate?

**Options:**
1. Message format error
2. Automatic mode
3. All messages processed
4. Access method error

**Correct Answer:** 1

---

## Question 96

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** When should program issue rollback?

**Options:**
1. Only at end of day
2. When unrecoverable error occurs
3. After every transaction
4. Never, IMS handles it

**Correct Answer:** 2

---

## Question 97

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is the purpose of checkpoint?

**Options:**
1. Verify data
2. Control program flow
3. Check program status
4. Save transaction state for recovery

**Correct Answer:** 4

---

## Question 98

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How to issue rollback call?

**Options:**
1. EXEC CICS ROLLBACK
2. UNDO command
3. ROLLBACK statement
4. CALL 'CBLTDLI' with ROLL function

**Correct Answer:** 4

---

## Question 99

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What happens on abnormal termination?

**Options:**
1. System restart required
2. Changes committed
3. IMS automatically backs out changes
4. Database locked

**Correct Answer:** 3

---

## Question 100

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is the best way to test DC programs?

**Options:**
1. Unit test only
2. Test in production
3. No testing needed
4. Use IMS test environment with test terminals

**Correct Answer:** 4

---

## Question 101

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How can you simulate terminal input?

**Options:**
1. Batch simulation
2. Manual typing only
3. Use test harness or automation tools
4. Not possible

**Correct Answer:** 3

---

## Question 102

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What debugging techniques are available?

**Options:**
1. Printf only
2. Source debuggers, dumps, and traces
3. Manual inspection
4. No debugging available

**Correct Answer:** 2

---

## Question 103

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How to trace DL/I calls?

**Options:**
1. Add DISPLAY statements
2. Enable IMS tracing facilities
3. Not possible
4. Use system logs

**Correct Answer:** 2

---

## Question 104

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is a common cause of program failures?

**Options:**
1. Message too small
2. Incorrect status code handling
3. Terminal disconnected
4. Too many ISRT calls

**Correct Answer:** 2

---

## Question 105

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** How to test error conditions?

**Options:**
1. Wait for real errors
2. Only in production
3. Not necessary
4. Simulate error scenarios

**Correct Answer:** 4

---

## Question 106

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is program isolation test?

**Options:**
1. Disconnected test
2. Testing program without affecting production
3. Testing in isolation ward
4. Solo testing

**Correct Answer:** 2

---

## Question 107

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How to verify message format?

**Options:**
1. Not necessary
2. Visual inspection
3. Inspect message segments with debugging tools
4. Automated check

**Correct Answer:** 3

---

## Question 108

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What should be tested for conversational transactions?

**Options:**
1. Output format
2. State preservation across interactions
3. Speed only
4. User interface

**Correct Answer:** 2

---

## Question 109

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How to test transaction load?

**Options:**
1. Production monitoring
2. One transaction at a time
3. Not necessary
4. Use load testing tools

**Correct Answer:** 4

---

## Question 110

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is an inquiry program?

**Options:**
1. Program that asks questions
2. Delete program
3. Read-only program that displays data
4. Update program

**Correct Answer:** 3

---

## Question 111

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What characterizes a data entry program?

**Options:**
1. Manages terminals
2. Displays reports
3. Accepts and validates input data
4. Processes batch files

**Correct Answer:** 3

---

## Question 112

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is a maintenance program?

**Options:**
1. Updates, inserts, or deletes data
2. Backs up data
3. Maintains terminals
4. Repairs databases

**Correct Answer:** 1

---

## Question 113

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is a menu-driven program?

**Options:**
1. Processes menu data
2. Presents options for user selection
3. Food ordering system
4. List display program

**Correct Answer:** 2

---

## Question 114

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is typical of high-volume programs?

**Options:**
1. Complex logic
2. Large messages
3. Long running
4. Optimized for performance

**Correct Answer:** 4

---

## Question 115

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is a composite transaction?

**Options:**
1. Multiple terminals
2. Long duration
3. Complex format
4. Combines multiple operations

**Correct Answer:** 4

---

## Question 116

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What security is needed for update programs?

**Options:**
1. Password only
2. None needed
3. Proper authorization and validation
4. Terminal lock

**Correct Answer:** 3

---

## Question 117

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What validation should data entry program perform?

**Options:**
1. User identity only
2. Field format, range, and business rules
3. Syntax only
4. No validation needed

**Correct Answer:** 2

---

## Question 118

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is a report program in DC?

**Options:**
1. Batch reporting
2. Logs activities
3. Generates formatted output for display
4. Prints reports

**Correct Answer:** 3

---

## Question 119

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is the difference between inquiry and maintenance?

**Options:**
1. Maintenance is simpler
2. Inquiry is faster
3. No difference
4. Inquiry reads only, maintenance updates

**Correct Answer:** 4

---

## Question 120

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is alternate PCB?

**Options:**
1. Secondary PCB
2. Alternative database PCB
3. Additional I/O PCB for message routing
4. Backup PCB

**Correct Answer:** 3

---

## Question 121

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is express PCB?

**Options:**
1. Quick response PCB
2. PCB for urgent high-priority messages
3. Expedited PCB
4. Fast processing PCB

**Correct Answer:** 2

---

## Question 122

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is program-to-program message switching?

**Options:**
1. One program sending message to another program
2. Program linking
3. Message forwarding
4. Inter-program communication

**Correct Answer:** 1

---

## Question 123

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is asynchronous output?

**Options:**
1. Non-blocking output
2. Output sent after program completion
3. Delayed output
4. Background output

**Correct Answer:** 2

---

## Question 124

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is command code usage in DC?

**Options:**
1. Transaction codes
2. Terminal commands
3. Special processing options for calls
4. System commands

**Correct Answer:** 3

---

## Question 125

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is dynamic transaction routing?

**Options:**
1. Automatic routing
2. Fast routing
3. Runtime determination of transaction destination
4. Backup routing

**Correct Answer:** 3

---

## Question 126

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is transaction affinity?

**Options:**
1. User preference
2. Terminal binding
3. Related transactions processed by same region
4. Transaction preference

**Correct Answer:** 3

---

## Question 127

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is a security exit in IMS DC?

**Options:**
1. Backup path
2. Custom security validation routine
3. Emergency exit
4. Logout function

**Correct Answer:** 2

---

## Question 128

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is message edit exit?

**Options:**
1. Message deletion
2. Message correction
3. Custom routine for message validation
4. Message formatting

**Correct Answer:** 3

---

## Question 129

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How does IMS schedule transactions?

**Options:**
1. Based on priority, class, and availability
2. Random
3. First-in-first-out
4. Alphabetical

**Correct Answer:** 1

---

## Question 130

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is transaction class scheduling?

**Options:**
1. User classification
2. Type classification
3. Priority classification
4. Groups transactions for resource management

**Correct Answer:** 4

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
1. Terminal queuing
2. Message queuing
3. Data queuing
4. Waiting for processing resources

**Correct Answer:** 4

---

## Question 133

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How can transaction performance be monitored?

**Options:**
1. IMS monitoring tools and statistics
2. Not possible
3. User feedback
4. Manual observation

**Correct Answer:** 1

---

## Question 134

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is transaction load balancing?

**Options:**
1. User distribution
2. Message distribution
3. Terminal balancing
4. Distributing work across regions

**Correct Answer:** 4

---

## Question 135

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is a transaction timeout?

**Options:**
1. Maximum execution time limit
2. User wait time
3. Response time
4. Queue wait time

**Correct Answer:** 1

---

## Question 136

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What happens when transaction times out?

**Options:**
1. Automatic retry
2. IMS may abend the transaction
3. Extended time granted
4. Nothing

**Correct Answer:** 2

---

## Question 137

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is parallel transaction processing?

**Options:**
1. Sequential processing
2. Multiple transactions executing simultaneously
3. Batch processing
4. Single threading

**Correct Answer:** 2

---

## Question 138

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is a PCB mask?

**Options:**
1. PCB template
2. PCB security
3. COBOL structure mapping PCB fields
4. PCB filter

**Correct Answer:** 3

---

## Question 139

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What fields are in I/O PCB mask?

**Options:**
1. Only status code
2. User information
3. All database fields
4. LTERM, status code, date/time, message length

**Correct Answer:** 4

---

## Question 140

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** Why define PCB mask in LINKAGE SECTION?

**Options:**
1. Better performance
2. IMS provides PCB address at runtime
3. Saves memory
4. Required by COBOL

**Correct Answer:** 2

---

## Question 141

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is the typical size of I/O PCB?

**Options:**
1. 148 bytes
2. 100 bytes
3. Variable
4. 200 bytes

**Correct Answer:** 1

---

## Question 142

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Can PCB mask be modified by program?

**Options:**
1. Only status code
2. Yes, freely
3. No, read-only
4. Should not modify, except for routing

**Correct Answer:** 4

---

## Question 143

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is the status code field type?

**Options:**
1. Character field (PIC XX)
2. Numeric field
3. Alphanumeric
4. Binary field

**Correct Answer:** 1

---

## Question 144

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** How to reference PCB fields in COBOL?

**Options:**
1. Through mask variable name
2. Not possible
3. Direct PCB reference
4. Using POINTER

**Correct Answer:** 1

---

## Question 145

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is PCB list?

**Options:**
1. PCB directory
2. PCB index
3. Collection of PCBs passed to program
4. Array of PCBs

**Correct Answer:** 3

---

## Question 146

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How many PCBs can a program access?

**Options:**
1. Only one
2. One I/O PCB plus multiple DB PCBs
3. Unlimited
4. Maximum 10

**Correct Answer:** 2

---

## Question 147

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is modifiable alternate PCB field?

**Options:**
1. User ID
2. LTERM for message routing
3. Status code
4. Date/time

**Correct Answer:** 2

---

## Question 148

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is a response mode transaction?

**Options:**
1. Interactive transaction
2. Transaction that sends response to originating terminal
3. Fast response transaction
4. Acknowledged transaction

**Correct Answer:** 2

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
2. Uses multiple PCBs
3. Has multiple functions
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
2. Checkpoint
3. Beginning of transaction
4. End of transaction

**Correct Answer:** 1

---

## Question 152

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is transaction recovery?

**Options:**
1. Restarting transaction
2. Restoring transaction state after failure
3. Fixing transaction errors
4. Getting transaction back

**Correct Answer:** 2

---

## Question 153

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is a WFI transaction?

**Options:**
1. Wait-for-input transaction
2. Write file input
3. Wait for initialization
4. Work flow item

**Correct Answer:** 1

---

## Question 154

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is transaction code security?

**Options:**
1. Code protection
2. Transaction encryption
3. Terminal security
4. Authorization control for transactions

**Correct Answer:** 4

---

## Question 155

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is transaction serialization?

**Options:**
1. Numbering transactions
2. Transaction logging
3. Ensuring sequential access to resources
4. Converting to serial format

**Correct Answer:** 3

---

## Question 156

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is transaction coupling?

**Options:**
1. Transaction joining
2. Transaction linking
3. Transaction dependency
4. Relationship between transactions

**Correct Answer:** 4

---

## Question 157

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is transaction integrity?

**Options:**
1. Data validation
2. ACID properties compliance
3. Security check
4. Error checking

**Correct Answer:** 2

---

## Question 158

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is the role of IMS Control Region?

**Options:**
1. Manages databases
2. Manages overall IMS DC operations
3. Controls terminals only
4. Handles security

**Correct Answer:** 2

---

## Question 159

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is a dependent region in IMS DC?

**Options:**
1. Region that processes applications
2. Secondary region
3. Backup region
4. Test region

**Correct Answer:** 1

---

## Question 160

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is BMP in IMS?

**Options:**
1. Best Message Processor
2. Backup Message Program
3. Batch Message Processing program
4. Basic MPP

**Correct Answer:** 3

---

## Question 161

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Can an MPP access multiple databases?

**Options:**
1. Yes, but not recommended
2. Only in batch mode
3. No, only one database
4. Yes, through multiple DB PCBs

**Correct Answer:** 4

---

## Question 162

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is a transaction synonym?

**Options:**
1. Alternate name for same transaction
2. Related transaction
3. Backup transaction
4. Similar transaction

**Correct Answer:** 1

---

## Question 163

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** Can transaction codes contain special characters?

**Options:**
1. No, alphanumeric only
2. Only underscore
3. Yes, any character
4. Limited special characters allowed

**Correct Answer:** 4

---

## Question 164

**Topic:** IMS DC - Message Queues  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is the system queue in IMS DC?

**Options:**
1. Database queue
2. Terminal queue
3. User queue
4. IMS internal queue for messages

**Correct Answer:** 4

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
1. System default
2. User specification
3. From LTERM field in I/O PCB
4. Random assignment

**Correct Answer:** 3

---

## Question 168

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is PURG call used for?

**Options:**
1. Delete transactions
2. Flush output messages immediately
3. Purge input messages
4. Clear buffers

**Correct Answer:** 2

---

## Question 169

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is CHNG call?

**Options:**
1. Change output destination
2. Change transaction
3. Change format
4. Change priority

**Correct Answer:** 1

---

## Question 170

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How is SPA size defined?

**Options:**
1. In transaction definition
2. In program
3. System default
4. At runtime

**Correct Answer:** 1

---

## Question 171

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** Can SPA be encrypted?

**Options:**
1. System encrypts SPA
2. Automatic encryption
3. No encryption possible
4. Program can encrypt data in SPA

**Correct Answer:** 4

---

## Question 172

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is MFS?

**Options:**
1. Message Format Service
2. Multiple Format Structure
3. Master Format Service
4. Message File System

**Correct Answer:** 1

---

## Question 173

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is the purpose of MFS?

**Options:**
1. Store messages
2. Format messages for screen display
3. Validate messages
4. Route messages

**Correct Answer:** 2

---

## Question 174

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** How many parameters in ENTRY statement?

**Options:**
1. No parameters
2. Always 5
3. Varies, typically 2 or more
4. Always 1

**Correct Answer:** 3

---

## Question 175

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is PCB address list?

**Options:**
1. PCB names
2. List of pointers to PCBs
3. PCB contents
4. PCB structure

**Correct Answer:** 2

---

## Question 176

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is GA status code?

**Options:**
1. General access
2. Good answer
3. Segment not found at specified level
4. Get again

**Correct Answer:** 3

---

## Question 177

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is GE status code?

**Options:**
1. End of database
2. Get error
3. General error
4. Good end

**Correct Answer:** 1

---

## Question 178

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is IMS Test Tool?

**Options:**
1. Terminal test
2. Database test
3. Tool for testing IMS applications
4. Performance test

**Correct Answer:** 3

---

## Question 179

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How to generate test transactions?

**Options:**
1. Batch generation
2. Use terminal emulator or test tools
3. Manual entry only
4. Automatic generation

**Correct Answer:** 2

---

## Question 180

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What validation is critical for maintenance programs?

**Options:**
1. Format only
2. Authorization, data validity, referential integrity
3. Syntax only
4. Length only

**Correct Answer:** 2

---

## Question 181

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** Should inquiry programs use database updates?

**Options:**
1. No, read-only access
2. Not applicable
3. Yes, for logging
4. Sometimes

**Correct Answer:** 1

---

## Question 182

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is AOI in IMS DC?

**Options:**
1. Application Output Interface
2. Automated Operator Interface
3. Advanced Online Interface
4. Automatic Operation Initiator

**Correct Answer:** 2

---

## Question 183

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What are command codes?

**Options:**
1. Security codes
2. Transaction codes
3. Special indicators for DL/I processing options
4. Format codes

**Correct Answer:** 3

---

## Question 184

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is WFI time?

**Options:**
1. Wait for initialization
2. Wait-for-input timeout period
3. Work flow interval
4. Work finish indicator

**Correct Answer:** 2

---

## Question 185

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How does IMS handle transaction backlog?

**Options:**
1. Queues and schedules based on priority
2. Increases resources automatically
3. Rejects new transactions
4. Waits indefinitely

**Correct Answer:** 1

---

## Question 186

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is the IOPCB in COBOL programs?

**Options:**
1. Internal Operation PCB
2. First PCB for message I/O
3. Interactive Online PCB
4. Input Only PCB

**Correct Answer:** 2

---

## Question 187

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Can programs define their own PCB structure?

**Options:**
1. Yes, with restrictions
2. Only in test
3. Yes, freely
4. No, must match IMS-provided structure

**Correct Answer:** 4

---

## Question 188

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is transaction step?

**Options:**
1. Commit point
2. Transaction phase
3. Processing stage
4. Unit of work within transaction

**Correct Answer:** 4

---

## Question 189

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is dynamic allocation in IMS DC?

**Options:**
1. Terminal assignment
2. Runtime resource assignment
3. Database allocation
4. Memory allocation

**Correct Answer:** 2

---

## Question 190

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is VTAM in IMS DC context?

**Options:**
1. Visual Terminal Application Manager
2. Variable Transaction Access Mode
3. Virtual Terminal Access Manager
4. Virtual Telecommunications Access Method

**Correct Answer:** 4

---

## Question 191

**Topic:** IMS DC - Fundamentals and Concepts  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is a PTERM?

**Options:**
1. Process terminal
2. Program terminal
3. Physical terminal
4. Primary terminal

**Correct Answer:** 3

---

## Question 192

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is the transaction manager in IMS?

**Options:**
1. Component that controls transaction execution
2. Terminal manager
3. User manager
4. Database manager

**Correct Answer:** 1

---

## Question 193

**Topic:** IMS DC - Message Processing Programs  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Can MPP programs be debugged online?

**Options:**
1. Yes, using appropriate debugging tools
2. Not recommended
3. No, batch only
4. Only in test environment

**Correct Answer:** 1

---

## Question 194

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is transaction response time?

**Options:**
1. Queue time only
2. Network time
3. Processing time only
4. Time from input to output delivery

**Correct Answer:** 4

---

## Question 195

**Topic:** IMS DC - Transaction Codes and Processing  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What factors affect transaction performance?

**Options:**
1. Database only
2. Network only
3. Program only
4. Program efficiency, database access, queue depth, system load

**Correct Answer:** 4

---

## Question 196

**Topic:** IMS DC - Message Queues  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is a shared queue?

**Options:**
1. Common queue
2. Open queue
3. Public queue
4. Queue accessible by multiple regions

**Correct Answer:** 4

---

## Question 197

**Topic:** IMS DC - Message Queues  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Can messages expire in queues?

**Options:**
1. No, permanent
2. Only after 24 hours
3. Only manually
4. Yes, based on age or system limits

**Correct Answer:** 4

---

## Question 198

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What information does date/time field provide?

**Options:**
1. Transaction timestamp
2. Processing time
3. Message arrival time
4. Current system date and time

**Correct Answer:** 4

---

## Question 199

**Topic:** IMS DC - I/O PCB  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is the user ID field in I/O PCB?

**Options:**
1. Transaction ID
2. System ID
3. Identifies user or terminal
4. Program ID

**Correct Answer:** 3

---

## Question 200

**Topic:** IMS DC - DL/I Calls for Message Processing  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is GCMD call?

**Options:**
1. General command
2. Global command
3. Get command mode
4. Get Command - for message retrieval

**Correct Answer:** 4

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
1. Fake conversation
2. Virtual conversation
3. Simulates conversation without holding resources
4. Test conversation

**Correct Answer:** 3

---

## Question 203

**Topic:** IMS DC - Conversational vs Non-conversational  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** When is conversational mode appropriate?

**Options:**
1. Always
2. When user interaction requires context
3. Only for testing
4. Never

**Correct Answer:** 2

---

## Question 204

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is device format in MFS?

**Options:**
1. Data format
2. Message format
3. Terminal type
4. Screen layout definition

**Correct Answer:** 4

---

## Question 205

**Topic:** IMS DC - Message Formats and Structure  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is message input descriptor (MID)?

**Options:**
1. Message ID
2. Defines input message format
3. Message indicator
4. Message identification

**Correct Answer:** 2

---

## Question 206

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** How to declare message I/O area?

**Options:**
1. 05 level
2. 88 level
3. 77 level
4. 01 level in WORKING-STORAGE

**Correct Answer:** 4

---

## Question 207

**Topic:** IMS DC - COBOL Programming  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is the function code parameter?

**Options:**
1. Status code
2. Program function
3. Transaction code
4. First parameter specifying DL/I operation

**Correct Answer:** 4

---

## Question 208

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What does II status code mean?

**Options:**
1. Information incomplete
2. Insert ignored
3. Invalid input
4. Segment already exists (duplicate key)

**Correct Answer:** 4

---

## Question 209

**Topic:** IMS DC - Status Codes and Error Handling  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is AJ status code?

**Options:**
1. Invalid concatenated key
2. Automatic jump
3. All joined
4. After job

**Correct Answer:** 1

---

## Question 210

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is regression testing for IMS DC?

**Options:**
1. Security testing
2. Performance testing
3. Retesting after changes
4. Load testing

**Correct Answer:** 3

---

## Question 211

**Topic:** IMS DC - Testing and Debugging  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How to test concurrent transaction processing?

**Options:**
1. Manual testing
2. Not possible
3. Single user test
4. Multi-user or load testing tools

**Correct Answer:** 4

---

## Question 212

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is a help transaction?

**Options:**
1. Error help
2. Technical support
3. System help
4. Provides user assistance information

**Correct Answer:** 4

---

## Question 213

**Topic:** IMS DC - Online Program Types  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is audit trail in maintenance programs?

**Options:**
1. Program trace
2. Logging of all changes made
3. Debug log
4. Error log

**Correct Answer:** 2

---

## Question 214

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is OTMA?

**Options:**
1. Output Transaction Management
2. Online Terminal Manager Access
3. Open Transaction Manager Access
4. Operational Task Management

**Correct Answer:** 3

---

## Question 215

**Topic:** IMS DC - Advanced Features  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is program restart capability?

**Options:**
1. Resume processing after failure
2. Reload program
3. Rerun program
4. Reset program

**Correct Answer:** 1

---

## Question 216

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is message region?

**Options:**
1. Message buffer
2. Region where MPPs execute
3. Message storage
4. Message area

**Correct Answer:** 2

---

## Question 217

**Topic:** IMS DC - Transaction Scheduling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How many message regions can IMS support?

**Options:**
1. Unlimited
2. Maximum 10
3. Only one
4. Multiple, based on configuration

**Correct Answer:** 4

---

## Question 218

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is segment name field in DB PCB?

**Options:**
1. Name of last accessed segment
2. Target segment
3. Root segment
4. Current segment

**Correct Answer:** 1

---

## Question 219

**Topic:** IMS DC - PCB Masks  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is key feedback area?

**Options:**
1. Result feedback
2. Error feedback
3. Contains concatenated key of current position
4. Status feedback

**Correct Answer:** 3

---

## Question 220

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is security profile in IMS DC?

**Options:**
1. Network profile
2. User profile
3. Defines access authorizations
4. System profile

**Correct Answer:** 3

---

## Question 221

**Topic:** IMS DC - Additional Concepts  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is terminal preemption?

**Options:**
1. Taking over terminal for urgent message
2. Terminal reset
3. Terminal lock
4. Terminal disconnect

**Correct Answer:** 1

---

## Question 222

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is the primary purpose of Message Format Services (MFS) in IMS DC?

**Options:**
1. Format messages between application programs and terminals
2. Compress message data
3. Store messages in databases
4. Route messages to appropriate programs

**Correct Answer:** 1

---

## Question 223

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Which MFS control block defines the physical terminal characteristics?

**Options:**
1. DOF (Device Output Format)
2. MOD (Message Output Descriptor)
3. MID (Message Input Descriptor)
4. DIF (Device Input Format)

**Correct Answer:** 4

---

## Question 224

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What does MOD stand for in MFS?

**Options:**
1. Message Organizational Data
2. Module Definition
3. Multiple Output Device
4. Message Output Descriptor

**Correct Answer:** 4

---

## Question 225

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Which MFS control block maps the application program's view of a message?

**Options:**
1. DIF (Device Input Format)
2. MID (Message Input Descriptor)
3. FMT (Format)
4. PCB (Program Communication Block)

**Correct Answer:** 2

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
1. DFLD (Device Field)
2. LFLD (Logical Field)
3. MFLD (Message Field)
4. AFLD (Application Field)

**Correct Answer:** 3

---

## Question 228

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Which attribute controls whether a field is protected or unprotected on a 3270 screen?

**Options:**
1. SECURE parameter
2. PROT parameter
3. ATTR parameter
4. FIELD parameter

**Correct Answer:** 3

---

## Question 229

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What does the FILL parameter in MFS specify?

**Options:**
1. Character to fill unused field positions
2. Field justification
3. Field alignment
4. Default value for empty fields

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
3. System Catalog
4. Application Library

**Correct Answer:** 1

---

## Question 233

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is the purpose of the LITERAL parameter in DFLD?

**Options:**
1. Display constant text on screen
2. Generate literal documentation
3. Define literal values for comparison
4. Create literal database fields

**Correct Answer:** 1

---

## Question 234

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Can MFS perform automatic data type conversion?

**Options:**
1. Only with special hardware
2. Yes, but only for dates
3. Yes, between character and numeric formats
4. No, program must do all conversions

**Correct Answer:** 3

---

## Question 235

**Topic:** IMS DC - Message Format Services (MFS)  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What does the JUSTIFY parameter control in MFLD?

**Options:**
1. Vertical alignment on screen
2. Error message positioning
3. Left or right justification of data in field
4. Field validation method

**Correct Answer:** 3

---

## Question 236

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What is the standard screen size for a 3270 terminal model 2?

**Options:**
1. 24 rows by 132 columns
2. 32 rows by 80 columns
3. 24 rows by 80 columns
4. 25 rows by 80 columns

**Correct Answer:** 3

---

## Question 237

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What does the MDT (Modified Data Tag) attribute indicate?

**Options:**
1. Field has been modified by user
2. Field contains master data
3. Field is for date entry
4. Field is mandatory

**Correct Answer:** 1

---

## Question 238

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Which 3270 attribute makes a field invisible to the user?

**Options:**
1. Protected attribute
2. Hidden attribute
3. Masked attribute
4. Dark/Non-display attribute

**Correct Answer:** 4

---

## Question 239

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What happens when a user presses ENTER on a 3270 screen?

**Options:**
1. Only unprotected fields are transmitted
2. Only fields with MDT on are transmitted
3. Only modified unprotected fields are transmitted
4. All fields are transmitted

**Correct Answer:** 2

---

## Question 240

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How can a program clear the entire screen?

**Options:**
1. Use CLEAR PCB call
2. Send blank message
3. Send ERASE WRITE command via MFS or control characters
4. Issue DELETE SCREEN command

**Correct Answer:** 3

---

## Question 241

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is cursor positioning in IMS DC screen handling?

**Options:**
1. Moving cursor automatically through fields
2. Cursor shape definition
3. Placing cursor at specific screen location for user input
4. Cursor blinking control

**Correct Answer:** 3

---

## Question 242

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Which MFS parameter positions the cursor on a screen?

**Options:**
1. POSITION parameter
2. CURSOR parameter
3. POINT parameter
4. LOCATE parameter

**Correct Answer:** 2

---

## Question 243

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What are extended highlighting attributes used for?

**Options:**
1. Font size changes
2. Graphics display
3. Color, blinking, reverse video, underline
4. Sound effects

**Correct Answer:** 3

---

## Question 244

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Easy
**Type:** Single Choice

**Question:** What does a protected field prevent?

**Options:**
1. User from typing into the field
2. Field from being colored
3. Field from being displayed
4. Field from being read by program

**Correct Answer:** 1

---

## Question 245

**Topic:** IMS DC - Screen Handling  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is the purpose of the ALARM parameter in screen formatting?

**Options:**
1. Alert operator of system error
2. Sound terminal alarm/beep on error
3. Set time limit for user input
4. Trigger security alarm

**Correct Answer:** 2

---

## Question 246

**Topic:** IMS DC - Message Field Editing  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What MFS editing pattern would format a number with comma separators?

**Options:**
1. EDIT='SEPARATE'
2. EDIT='NUMBER-MASK'
3. EDIT='FORMAT-COMMA'
4. EDIT='999,999,999'

**Correct Answer:** 4

---

## Question 247

**Topic:** IMS DC - Message Field Editing  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How does MFS handle leading zeros in numeric fields?

**Options:**
1. Always suppresses leading zeros
2. Always displays leading zeros
3. Requires program logic
4. Can suppress with appropriate edit pattern

**Correct Answer:** 4

---

## Question 248

**Topic:** IMS DC - Message Field Editing  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What does the 'Z' character in an edit pattern do?

**Options:**
1. Represents zero value
2. Adds zero padding
3. Suppresses leading zeros
4. Zones numeric field

**Correct Answer:** 3

---

## Question 249

**Topic:** IMS DC - Message Field Editing  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How can MFS add a currency symbol to a field?

**Options:**
1. Requires program code
2. Use SYMBOL parameter
3. Include '$' in edit pattern
4. Use CURRENCY parameter

**Correct Answer:** 3

---

## Question 250

**Topic:** IMS DC - Message Field Editing  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What editing can MFS perform on date fields?

**Options:**
1. Date arithmetic only
2. No date editing available
3. Century windowing only
4. Reformatting, separator insertion, validation

**Correct Answer:** 4

---

## Question 251

**Topic:** IMS DC - Message Field Editing  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What does the 'CR' notation in an edit pattern indicate?

**Options:**
1. Carriage return control
2. Credit (negative) balance indicator
3. Create record function
4. Current rate display

**Correct Answer:** 2

---

## Question 252

**Topic:** IMS DC - Message Field Editing  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** How does MFS handle field overflow during editing?

**Options:**
1. Can truncate, asterisk fill, or error
2. Always errors and abends
3. Always truncates silently
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
3. Only with special hardware
4. Only for alphabetic fields

**Correct Answer:** 1

---

## Question 254

**Topic:** IMS DC - Multi-segment Messages  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is a multi-segment message in IMS DC?

**Options:**
1. Message sent to multiple terminals
2. Message broken into multiple logical segments
3. Message split across multiple screens
4. Message with multiple transaction codes

**Correct Answer:** 2

---

## Question 255

**Topic:** IMS DC - Multi-segment Messages  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How does a program retrieve multiple input message segments?

**Options:**
1. Single GET-ALL call
2. Use RETRIEVE SEGMENTS call
3. Automatic concatenation by IMS
4. Issue multiple GU or GN calls to I/O PCB

**Correct Answer:** 4

---

## Question 256

**Topic:** IMS DC - Multi-segment Messages  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What status code indicates no more message segments available?

**Options:**
1. QC status code
2. QD status code
3. NM status code
4. GB status code

**Correct Answer:** 2

---

## Question 257

**Topic:** IMS DC - Multi-segment Messages  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How does a program send a multi-segment output message?

**Options:**
1. Use special MOD format
2. Concatenate segments in program
3. Issue multiple ISRT calls to I/O PCB
4. Use SEND-MULTIPLE call

**Correct Answer:** 3

---

## Question 258

**Topic:** IMS DC - Multi-segment Messages  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What determines segment boundaries in multi-segment messages?

**Options:**
1. Fixed 80-byte segments
2. Screen size limits
3. Transaction code definition
4. Segment size defined in MFS or program logic

**Correct Answer:** 4

---

## Question 259

**Topic:** IMS DC - Multi-segment Messages  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Can segments within a message have different formats?

**Options:**
1. Yes, each segment can have unique structure
2. Only in conversational transactions
3. No, all segments must be identical
4. Only with MFS support

**Correct Answer:** 1

---

## Question 260

**Topic:** IMS DC - Multi-segment Messages  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is message chaining in IMS DC?

**Options:**
1. Sending messages sequentially
2. Database chain processing
3. Linking multiple messages for single transaction
4. Connecting terminals together

**Correct Answer:** 3

---

## Question 261

**Topic:** IMS DC - Error Recovery  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What should a program do when receiving an unexpected status code?

**Options:**
1. Check PCB, log error, send user message, rollback if needed
2. Ignore and continue processing
3. Return to operating system
4. Always abend immediately

**Correct Answer:** 1

---

## Question 262

**Topic:** IMS DC - Error Recovery  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What IMS call can a program use to signal abnormal termination?

**Options:**
1. ABEND call
2. TERM call
3. ROLL or ROLB call
4. EXIT call

**Correct Answer:** 3

---

## Question 263

**Topic:** IMS DC - Error Recovery  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What does the ROLL call do?

**Options:**
1. Rolls forward transaction log
2. Backs out database and message changes
3. Rolls back operating system
4. Rotates log datasets

**Correct Answer:** 2

---

## Question 264

**Topic:** IMS DC - Error Recovery  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** After a ROLB call, what happens to the input message?

**Options:**
1. Always requeued for retry
2. Always discarded permanently
3. Can be requeued or discarded based on ROLB type
4. Sent to error queue

**Correct Answer:** 3

---

## Question 265

**Topic:** IMS DC - Error Recovery  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is the purpose of the SETS and SETO calls?

**Options:**
1. Set terminal output mode
2. Set commit point for database and message changes
3. Set security level
4. Set error recovery options

**Correct Answer:** 2

---

## Question 266

**Topic:** IMS DC - Error Recovery  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** How should a program handle a database deadlock?

**Options:**
1. Wait indefinitely for lock release
2. Force lock override
3. Abend immediately
4. Receive BA status, issue ROLB, retry or exit

**Correct Answer:** 4

---

## Question 267

**Topic:** IMS DC - Error Recovery  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What information should error messages to users include?

**Options:**
1. Clear description, action required, contact info if needed
2. Technical status codes only
3. Database structure details
4. Complete abend dump

**Correct Answer:** 1

---

## Question 268

**Topic:** IMS DC - Error Recovery  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What happens to output messages after a ROLB?

**Options:**
1. Only error messages are sent
2. Output messages are still sent
3. All output messages are discarded
4. Output is queued for manual review

**Correct Answer:** 3

---

## Question 269

**Topic:** IMS DC - Program Switching  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What DL/I call transfers control to another IMS program?

**Options:**
1. XRST (Transfer)
2. CALL
3. SWITCH
4. LINK

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
3. Depends on PCB type
4. Position is lost completely

**Correct Answer:** 1

---

## Question 271

**Topic:** IMS DC - Program Switching  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Can a program switch return control to the calling program?

**Options:**
1. Yes, automatically returns
2. Yes, with RETURN call
3. No, XRST is one-way transfer
4. Only in conversational mode

**Correct Answer:** 3

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
1. XRST is faster
2. COBOL CALL not supported
3. XRST provides IMS context and PCB access
4. XRST uses less memory

**Correct Answer:** 3

---

## Question 274

**Topic:** IMS DC - Program Switching  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What security applies when switching programs?

**Options:**
1. User must reauthorize
2. Target program must be authorized for transaction
3. Original program security carries over
4. No security checks performed

**Correct Answer:** 2

---

## Question 275

**Topic:** IMS DC - Transaction Restart  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is transaction restart in IMS DC?

**Options:**
1. Manual transaction resubmission
2. Automatic reprocessing of failed transaction
3. Transaction code redefinition
4. System restart after crash

**Correct Answer:** 2

---

## Question 276

**Topic:** IMS DC - Transaction Restart  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** When does IMS automatically restart a transaction?

**Options:**
1. After certain abends or system failures
2. Never automatically
3. Only during scheduled maintenance
4. After every abend

**Correct Answer:** 1

---

## Question 277

**Topic:** IMS DC - Transaction Restart  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is a checkpoint in the context of transaction processing?

**Options:**
1. Performance measurement point
2. End of transaction
3. Point where transaction state is saved for recovery
4. Security validation point

**Correct Answer:** 3

---

## Question 278

**Topic:** IMS DC - Transaction Restart  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How can a program make itself non-restartable?

**Options:**
1. Set NORESTART flag
2. Cannot prevent restart
3. Issue ROLB call or define transaction as non-restartable
4. Use special PCB option

**Correct Answer:** 3

---

## Question 279

**Topic:** IMS DC - Transaction Restart  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What programming practice helps ensure clean transaction restart?

**Options:**
1. Design idempotent operations, avoid external side effects
2. Disable all error checking
3. Use global variables
4. Cache all data in memory

**Correct Answer:** 1

---

## Question 280

**Topic:** IMS DC - Transaction Restart  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What happens to database updates during automatic restart?

**Options:**
1. Lost permanently
2. Rolled back and reapplied during restart
3. Manually recovered
4. Kept as-is from failed run

**Correct Answer:** 2

---

## Question 281

**Topic:** IMS DC - Data Validation  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Where should input data validation occur?

**Options:**
1. As early as possible in application logic
2. Only in batch programs
3. Validation not needed with MFS
4. Only at database update time

**Correct Answer:** 1

---

## Question 282

**Topic:** IMS DC - Data Validation  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What types of validation should online programs perform?

**Options:**
1. Format, range, required fields, cross-field edits
2. Only database constraint checking
3. Only numeric validation
4. No validation needed

**Correct Answer:** 1

---

## Question 283

**Topic:** IMS DC - Data Validation  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** How should a program handle multiple validation errors?

**Options:**
1. Abend on first error
2. Ignore all but critical errors
3. Report first error only
4. Collect all errors and report together

**Correct Answer:** 4

---

## Question 284

**Topic:** IMS DC - COBOL Program Structure  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What special COBOL division is used for IMS programs?

**Options:**
1. No special division, standard COBOL structure
2. TRANSACTION DIVISION
3. IMS DIVISION
4. DL/I DIVISION

**Correct Answer:** 1

---

## Question 285

**Topic:** IMS DC - COBOL Program Structure  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Where are PCB masks defined in COBOL?

**Options:**
1. FILE SECTION
2. LOCAL-STORAGE SECTION
3. WORKING-STORAGE SECTION
4. LINKAGE SECTION

**Correct Answer:** 4

---

## Question 286

**Topic:** IMS DC - COBOL Program Structure  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What is the ENTRY parameter 'DLITCBL' used for?

**Options:**
1. Transaction entry point
2. Entry point for IMS to call COBOL program
3. Database entry definition
4. Error entry routine

**Correct Answer:** 2

---

## Question 287

**Topic:** IMS DC - COBOL Program Structure  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** How does a COBOL program receive its PCB addresses?

**Options:**
1. Via ENTRY USING statement parameters
2. From JCL parameters
3. Through ACCEPT statement
4. From WORKING-STORAGE

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
1. EXIT PROGRAM only
2. ROLLBACK statement
3. TERMINATE DLI
4. GOBACK or STOP RUN statement

**Correct Answer:** 4

---

## Question 290

**Topic:** IMS DC - COBOL Program Structure  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** Can IMS COBOL programs use files (FILE SECTION)?

**Options:**
1. Generally no, should use DL/I for data access
2. Only sequential files
3. Only for output
4. Yes, fully supported

**Correct Answer:** 1

---

## Question 291

**Topic:** IMS DC - PCB Details  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What field in the I/O PCB contains the message sequence number?

**Options:**
1. MSG-SEQ-NUM field
2. SEQUENCE-FIELD
3. Not standard in I/O PCB, may be in alternate PCB
4. TRANS-SEQ field

**Correct Answer:** 3

---

## Question 292

**Topic:** IMS DC - PCB Details  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What does the LTERM field in I/O PCB identify?

**Options:**
1. Terminal type code
2. Logical terminal name (8 characters)
3. User ID
4. Physical terminal address

**Correct Answer:** 2

---

## Question 293

**Topic:** IMS DC - Status Codes  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What does status code 'QC' indicate?

**Options:**
1. Queue is closed
2. No more input message segments (message complete)
3. Quick commit performed
4. Query completed

**Correct Answer:** 2

---

## Question 294

**Topic:** IMS DC - Status Codes  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What status code indicates segment not found in database?

**Options:**
1. NF status code
2. GB status code
3. GE status code
4. NS status code

**Correct Answer:** 3

---

## Question 295

**Topic:** IMS DC - Status Codes  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** What does 'BA' status code mean?

**Options:**
1. Batch mode active
2. Buffer allocation failed
3. Bad address in call
4. Resource unavailable/deadlock detected

**Correct Answer:** 4

---

## Question 296

**Topic:** IMS DC - Status Codes  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What status indicates successful database update?

**Options:**
1. Blank or spaces status code
2. 00 status code
3. SU status code
4. OK status code

**Correct Answer:** 1

---

## Question 297

**Topic:** IMS DC - Best Practices  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** Why should online programs minimize database holds?

**Options:**
1. Reduce contention and improve concurrency
2. Reduce network traffic
3. Save memory
4. Improve screen response

**Correct Answer:** 1

---

## Question 298

**Topic:** IMS DC - Best Practices  
**Difficulty:** Medium
**Type:** Single Choice

**Question:** What is a common pitfall in IMS DC programming?

**Options:**
1. Making programs too modular
2. Using too many comments
3. Not checking status codes after every DL/I call
4. Testing too thoroughly

**Correct Answer:** 3

---

## Question 299

**Topic:** IMS DC - Real-world Application  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** In a customer inquiry transaction, what's the recommended approach?

**Options:**
1. Update database with inquiry timestamp
2. Retrieve data, format output, send to user, no database holds
3. Always use conversational mode
4. Hold database locks during user review

**Correct Answer:** 2

---

## Question 300

**Topic:** IMS DC - Real-world Application  
**Difficulty:** Hard
**Type:** Single Choice

**Question:** For a complex update transaction requiring validation from multiple sources, what's best?

**Options:**
1. Skip validation to improve performance
2. Use separate transactions for each piece
3. Gather all data, validate completely, then update atomically
4. Update as you go, validating each piece

**Correct Answer:** 3

---
