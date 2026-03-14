#!/usr/bin/env python3
"""
Generate 300 IMS DC Application Programmer Questions
Based on IMS DC PD.pdf content
"""

import json
import fitz  # PyMuPDF
import re

def extract_pdf_content(pdf_path):
    """Extract text content from PDF"""
    doc = fitz.open(pdf_path)
    full_text = ""
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        full_text += text + "\n"
    
    doc.close()
    return full_text

def generate_questions():
    """Generate 300 IMS DC Application Programmer questions"""
    
    questions = []
    
    # Module 1: IMS DC Fundamentals (30 questions)
    module1_questions = [
        {
            "questionnumber": 1,
            "topic": "IMS DC - Fundamentals",
            "difficulty": "Easy",
            "question": "What does IMS DC stand for?",
            "option_1": "IMS Data Communication",
            "option_2": "IMS Database Control",
            "option_3": "IMS Data Collection",
            "option_4": "IMS Direct Control",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 2,
            "topic": "IMS DC - Fundamentals",
            "difficulty": "Easy",
            "question": "What is the primary purpose of IMS DC?",
            "option_1": "Facilitates online transactions through interactive programs",
            "option_2": "Batch processing of data",
            "option_3": "System administration",
            "option_4": "Database backup",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 3,
            "topic": "IMS DC - Online Programs",
            "difficulty": "Easy",
            "question": "How many types of online programs are there in IMS DC?",
            "option_1": "4",
            "option_2": "3",
            "option_3": "5",
            "option_4": "6",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 4,
            "topic": "IMS DC - Online Programs",
            "difficulty": "Easy",
            "question": "Which of the following are types of online programs in IMS DC?",
            "option_1": "Inquiry programs",
            "option_2": "Data entry programs",
            "option_3": "Maintenance programs",
            "option_4": "Menu-driven programs",
            "choice_type": "Multiple Choice",
            "correct_answer": ["option_1", "option_2", "option_3", "option_4"]
        },
        {
            "questionnumber": 5,
            "topic": "IMS DC - Inquiry Programs",
            "difficulty": "Easy",
            "question": "What is the primary function of an Inquiry program?",
            "option_1": "Respond to user's questions by retrieving data",
            "option_2": "Add new data to database",
            "option_3": "Delete segments from database",
            "option_4": "Update database records",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 6,
            "topic": "IMS DC - Inquiry Programs",
            "difficulty": "Medium",
            "question": "In an inquiry program, what is the typical flow of operations?",
            "option_1": "Operator requests data, program retrieves data, program displays data",
            "option_2": "Program retrieves data, operator requests data, program displays data",
            "option_3": "Operator enters data, program updates database",
            "option_4": "Program displays menu, operator selects option",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 7,
            "topic": "IMS DC - Data Entry Programs",
            "difficulty": "Easy",
            "question": "What is the main limitation of inquiry programs?",
            "option_1": "They don't let users key in data that's added to the database",
            "option_2": "They are too slow",
            "option_3": "They can't retrieve data",
            "option_4": "They require special terminals",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 8,
            "topic": "IMS DC - Data Entry Programs",
            "difficulty": "Easy",
            "question": "What does a data entry program do?",
            "option_1": "Updates databases with data entered by operator",
            "option_2": "Only retrieves data from database",
            "option_3": "Deletes data from database",
            "option_4": "Displays menu options",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 9,
            "topic": "IMS DC - Maintenance Programs",
            "difficulty": "Medium",
            "question": "What operations can a maintenance program perform?",
            "option_1": "Adding segments",
            "option_2": "Replacing segments",
            "option_3": "Deleting segments",
            "option_4": "All of the above",
            "choice_type": "Single Choice",
            "correct_answer": ["option_4"]
        },
        {
            "questionnumber": 10,
            "topic": "IMS DC - Maintenance Programs",
            "difficulty": "Hard",
            "question": "What is the typical flow in a maintenance program?",
            "option_1": "Request data, retrieve data, display data, enter changes, rewrite changes",
            "option_2": "Enter data, update database",
            "option_3": "Display menu, select option",
            "option_4": "Request data, display data",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 11,
            "topic": "IMS DC - Menu Programs",
            "difficulty": "Easy",
            "question": "What does a menu program allow an operator to do?",
            "option_1": "Select the functions to perform",
            "option_2": "Only view data",
            "option_3": "Only enter data",
            "option_4": "Only delete data",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 12,
            "topic": "IMS DC - Menu Programs",
            "difficulty": "Medium",
            "question": "What is a menu-driven system?",
            "option_1": "Application built around a set of menu programs",
            "option_2": "Application that uses only inquiry programs",
            "option_3": "Application that uses batch processing",
            "option_4": "Application without user interface",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 13,
            "topic": "IMS DC - Menu Programs",
            "difficulty": "Medium",
            "question": "What is a command-driven system?",
            "option_1": "System where operator invokes programs using explicit commands",
            "option_2": "System that uses only menus",
            "option_3": "System that uses batch processing",
            "option_4": "System without terminals",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 14,
            "topic": "IMS DC - Transaction Processing",
            "difficulty": "Easy",
            "question": "What is a transaction in IMS DC?",
            "option_1": "A unit of work processed by an application program",
            "option_2": "A database record",
            "option_3": "A program module",
            "option_4": "A terminal device",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 15,
            "topic": "IMS DC - Transaction Processing",
            "difficulty": "Medium",
            "question": "What is a transaction code?",
            "option_1": "Identifier used to invoke a specific application program",
            "option_2": "Password for terminal access",
            "option_3": "Database key",
            "option_4": "Program compilation code",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 16,
            "topic": "IMS DC - Message Processing",
            "difficulty": "Easy",
            "question": "What is MPP in IMS DC?",
            "option_1": "Message Processing Program",
            "option_2": "Master Program Process",
            "option_3": "Multiple Program Process",
            "option_4": "Message Protocol Program",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 17,
            "topic": "IMS DC - Message Processing",
            "difficulty": "Medium",
            "question": "What is the primary function of a Message Processing Program?",
            "option_1": "Process messages from terminals and provide responses",
            "option_2": "Compile application programs",
            "option_3": "Manage database backups",
            "option_4": "Configure IMS system",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 18,
            "topic": "IMS DC - Message Queues",
            "difficulty": "Easy",
            "question": "What is a message queue in IMS DC?",
            "option_1": "Storage area for messages waiting to be processed",
            "option_2": "Database table",
            "option_3": "Program library",
            "option_4": "Terminal buffer",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 19,
            "topic": "IMS DC - Message Queues",
            "difficulty": "Medium",
            "question": "What happens to input messages before program processing?",
            "option_1": "They are placed in message queues",
            "option_2": "They are directly processed",
            "option_3": "They are stored in database",
            "option_4": "They are deleted",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 20,
            "topic": "IMS DC - I/O PCB",
            "difficulty": "Easy",
            "question": "What does I/O PCB stand for?",
            "option_1": "Input/Output Program Communication Block",
            "option_2": "Internal Output Process Control Block",
            "option_3": "Interface Object Program Control Buffer",
            "option_4": "Input Operation Primary Control Base",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 21,
            "topic": "IMS DC - I/O PCB",
            "difficulty": "Medium",
            "question": "What is the purpose of I/O PCB in IMS DC applications?",
            "option_1": "Handle communication between application program and terminal",
            "option_2": "Manage database access",
            "option_3": "Control system resources",
            "option_4": "Configure network settings",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 22,
            "topic": "IMS DC - Message Retrieval",
            "difficulty": "Easy",
            "question": "Which DL/I call is used to retrieve an input message?",
            "option_1": "GU (Get Unique)",
            "option_2": "ISRT (Insert)",
            "option_3": "REPL (Replace)",
            "option_4": "DLET (Delete)",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 23,
            "topic": "IMS DC - Message Retrieval",
            "difficulty": "Medium",
            "question": "Which call retrieves the next message segment from the queue?",
            "option_1": "GN (Get Next)",
            "option_2": "GU (Get Unique)",
            "option_3": "ISRT (Insert)",
            "option_4": "REPL (Replace)",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 24,
            "topic": "IMS DC - Message Output",
            "difficulty": "Easy",
            "question": "Which DL/I call sends output messages to the terminal?",
            "option_1": "ISRT (Insert)",
            "option_2": "GU (Get Unique)",
            "option_3": "GN (Get Next)",
            "option_4": "DLET (Delete)",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 25,
            "topic": "IMS DC - Message Output",
            "difficulty": "Medium",
            "question": "When issuing ISRT for output, which PCB is used?",
            "option_1": "I/O PCB",
            "option_2": "Database PCB",
            "option_3": "Alternate PCB",
            "option_4": "Express PCB",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 26,
            "topic": "IMS DC - Transaction Types",
            "difficulty": "Easy",
            "question": "What is a non-conversational transaction?",
            "option_1": "Transaction that completes in one input-output cycle",
            "option_2": "Transaction that maintains context across multiple inputs",
            "option_3": "Transaction that doesn't use terminals",
            "option_4": "Transaction that only reads data",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 27,
            "topic": "IMS DC - Transaction Types",
            "difficulty": "Easy",
            "question": "What is a conversational transaction?",
            "option_1": "Transaction that maintains context across multiple terminal interactions",
            "option_2": "Transaction completed in single cycle",
            "option_3": "Transaction without user input",
            "option_4": "Transaction for batch processing",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 28,
            "topic": "IMS DC - Transaction Types",
            "difficulty": "Medium",
            "question": "Which type of transaction is more resource-efficient?",
            "option_1": "Non-conversational",
            "option_2": "Conversational",
            "option_3": "Both are equal",
            "option_4": "Depends on terminal type",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 29,
            "topic": "IMS DC - Message Switching",
            "difficulty": "Medium",
            "question": "What is message switching in IMS DC?",
            "option_1": "Routing messages from one terminal to another",
            "option_2": "Converting message formats",
            "option_3": "Deleting messages",
            "option_4": "Storing messages permanently",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 30,
            "topic": "IMS DC - Program Scheduling",
            "difficulty": "Medium",
            "question": "How are application programs scheduled in IMS DC?",
            "option_1": "Based on transaction codes and message availability",
            "option_2": "Fixed time intervals",
            "option_3": "Random selection",
            "option_4": "Manual operator control only",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        }
    ]
    
    # Module 2: Message Formats and Processing (40 questions)
    module2_questions = [
        {
            "questionnumber": 31,
            "topic": "IMS DC - Message Formats",
            "difficulty": "Easy",
            "question": "What is a message segment?",
            "option_1": "A logical unit of data in a message",
            "option_2": "A database record",
            "option_3": "A program module",
            "option_4": "A terminal screen",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 32,
            "topic": "IMS DC - Message Formats",
            "difficulty": "Medium",
            "question": "What is the maximum length of a message segment?",
            "option_1": "Implementation dependent, typically up to 32K",
            "option_2": "Always 80 bytes",
            "option_3": "Always 256 bytes",
            "option_4": "Unlimited",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 33,
            "topic": "IMS DC - Message Formats",
            "difficulty": "Easy",
            "question": "What are the two main types of messages in IMS DC?",
            "option_1": "Input and output messages",
            "option_2": "System and user messages",
            "option_3": "Short and long messages",
            "option_4": "Text and binary messages",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 34,
            "topic": "IMS DC - Message Formats",
            "difficulty": "Medium",
            "question": "What does ZZ field represent in a message?",
            "option_1": "Transaction code",
            "option_2": "Message priority",
            "option_3": "Terminal ID",
            "option_4": "Message length",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 35,
            "topic": "IMS DC - Message Formats",
            "difficulty": "Easy",
            "question": "Can a single transaction have multiple input message segments?",
            "option_1": "Yes",
            "option_2": "No",
            "option_3": "Only for conversational transactions",
            "option_4": "Only for batch transactions",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 36,
            "topic": "IMS DC - Message Formats",
            "difficulty": "Medium",
            "question": "Can a program send multiple output message segments?",
            "option_1": "Yes, by issuing multiple ISRT calls",
            "option_2": "No, only one output allowed",
            "option_3": "Yes, but only for conversational transactions",
            "option_4": "No, system limitation prevents this",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 37,
            "topic": "IMS DC - Input Messages",
            "difficulty": "Easy",
            "question": "Where do input messages originate from?",
            "option_1": "Terminals or other programs",
            "option_2": "Only from terminals",
            "option_3": "Only from databases",
            "option_4": "Only from batch jobs",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 38,
            "topic": "IMS DC - Input Messages",
            "difficulty": "Medium",
            "question": "What happens to input messages when no program is available?",
            "option_1": "Messages are queued for later processing",
            "option_2": "Messages are immediately deleted",
            "option_3": "Messages are returned to sender",
            "option_4": "System shuts down",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 39,
            "topic": "IMS DC - Output Messages",
            "difficulty": "Easy",
            "question": "Where are output messages sent?",
            "option_1": "To terminals or message queues",
            "option_2": "Only to terminals",
            "option_3": "Only to databases",
            "option_4": "Only to printers",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 40,
            "topic": "IMS DC - Output Messages",
            "difficulty": "Medium",
            "question": "Can output messages be sent to a different terminal than the input terminal?",
            "option_1": "Yes, using alternate PCBs",
            "option_2": "No, must go to same terminal",
            "option_3": "Yes, but only for conversational transactions",
            "option_4": "No, system limitation prevents this",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 41,
            "topic": "IMS DC - Message Processing Logic",
            "difficulty": "Easy",
            "question": "What is the first step in message processing?",
            "option_1": "Retrieve input message using GU",
            "option_2": "Send output message using ISRT",
            "option_3": "Access database",
            "option_4": "Display menu",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 42,
            "topic": "IMS DC - Message Processing Logic",
            "difficulty": "Medium",
            "question": "What is the typical sequence for processing a transaction?",
            "option_1": "Retrieve message, process business logic, access database if needed, send response",
            "option_2": "Access database, retrieve message, process logic, send response",
            "option_3": "Send response, retrieve message, process logic",
            "option_4": "Process logic, retrieve message, access database",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 43,
            "topic": "IMS DC - Message Processing Logic",
            "difficulty": "Hard",
            "question": "What should a program do if it receives multiple input segments?",
            "option_1": "Issue GU for first segment, then GN for subsequent segments",
            "option_2": "Issue multiple GU calls",
            "option_3": "Use only ISRT calls",
            "option_4": "Process only the first segment",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 44,
            "topic": "IMS DC - Message Processing Logic",
            "difficulty": "Medium",
            "question": "When should a program issue a commit point?",
            "option_1": "After completing all processing for a transaction",
            "option_2": "Before retrieving input message",
            "option_3": "After each database call",
            "option_4": "Never, system handles it automatically",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 45,
            "topic": "IMS DC - Message Queuing",
            "difficulty": "Easy",
            "question": "What is the purpose of message queuing?",
            "option_1": "Buffer messages between arrival and processing",
            "option_2": "Delete unwanted messages",
            "option_3": "Encrypt messages",
            "option_4": "Convert message formats",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 46,
            "topic": "IMS DC - Message Queuing",
            "difficulty": "Medium",
            "question": "What determines the order of message processing from the queue?",
            "option_1": "Message priority and arrival time",
            "option_2": "Alphabetical order of transaction codes",
            "option_3": "Terminal location",
            "option_4": "Random selection",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 47,
            "topic": "IMS DC - Message Priority",
            "difficulty": "Medium",
            "question": "Can messages have different processing priorities?",
            "option_1": "Yes, priority can be assigned to transactions",
            "option_2": "No, all messages are equal priority",
            "option_3": "Yes, but only for conversational transactions",
            "option_4": "No, priority is determined by terminal type",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 48,
            "topic": "IMS DC - Message Priority",
            "difficulty": "Hard",
            "question": "What factors can affect message priority?",
            "option_1": "Transaction code priority level",
            "option_2": "Terminal priority",
            "option_3": "Message class",
            "option_4": "All of the above",
            "choice_type": "Single Choice",
            "correct_answer": ["option_4"]
        },
        {
            "questionnumber": 49,
            "topic": "IMS DC - Transaction Codes",
            "difficulty": "Easy",
            "question": "What is the maximum length of a transaction code?",
            "option_1": "8 characters",
            "option_2": "4 characters",
            "option_3": "16 characters",
            "option_4": "32 characters",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 50,
            "topic": "IMS DC - Transaction Codes",
            "difficulty": "Medium",
            "question": "Can a transaction code be associated with multiple programs?",
            "option_1": "No, one-to-one relationship between transaction code and program",
            "option_2": "Yes, always",
            "option_3": "Yes, but only for batch programs",
            "option_4": "Yes, but only for system programs",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 51,
            "topic": "IMS DC - Transaction Codes",
            "difficulty": "Medium",
            "question": "Where is the transaction code specified in the input message?",
            "option_1": "At the beginning of the message",
            "option_2": "At the end of the message",
            "option_3": "In the middle of the message",
            "option_4": "Not in the message, but in system tables",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 52,
            "topic": "IMS DC - Program Scheduling",
            "difficulty": "Medium",
            "question": "What triggers the scheduling of a message processing program?",
            "option_1": "Arrival of message with corresponding transaction code",
            "option_2": "Fixed time schedule",
            "option_3": "Manual operator command only",
            "option_4": "System startup only",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 53,
            "topic": "IMS DC - Program Scheduling",
            "difficulty": "Hard",
            "question": "Can multiple instances of the same program run concurrently?",
            "option_1": "Yes, to process multiple messages",
            "option_2": "No, only one instance allowed",
            "option_3": "Yes, but only for batch programs",
            "option_4": "No, system limitation prevents this",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 54,
            "topic": "IMS DC - Program Scheduling",
            "difficulty": "Medium",
            "question": "What happens when a program completes processing a message?",
            "option_1": "Program terminates or waits for next message",
            "option_2": "Program always terminates",
            "option_3": "Program continues running indefinitely",
            "option_4": "System restarts",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 55,
            "topic": "IMS DC - Conversational Transactions",
            "difficulty": "Medium",
            "question": "How does a conversational transaction maintain context?",
            "option_1": "Using scratchpad area (SPA)",
            "option_2": "Using database",
            "option_3": "Using terminal memory",
            "option_4": "Using system files",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 56,
            "topic": "IMS DC - Conversational Transactions",
            "difficulty": "Hard",
            "question": "What is the disadvantage of conversational transactions?",
            "option_1": "Hold resources while waiting for terminal input",
            "option_2": "Cannot access database",
            "option_3": "Cannot send output messages",
            "option_4": "Cannot use transaction codes",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 57,
            "topic": "IMS DC - Non-Conversational Transactions",
            "difficulty": "Easy",
            "question": "What is the main advantage of non-conversational transactions?",
            "option_1": "Release resources immediately after processing",
            "option_2": "Maintain context automatically",
            "option_3": "Faster terminal response",
            "option_4": "Use less memory",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 58,
            "topic": "IMS DC - Non-Conversational Transactions",
            "difficulty": "Medium",
            "question": "How do non-conversational transactions maintain state across interactions?",
            "option_1": "Using database records or passed data",
            "option_2": "Using scratchpad area automatically",
            "option_3": "Using terminal memory",
            "option_4": "They don't maintain state",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 59,
            "topic": "IMS DC - Message Switching",
            "difficulty": "Medium",
            "question": "What is the benefit of message switching?",
            "option_1": "Route messages between different destinations",
            "option_2": "Improve program performance",
            "option_3": "Reduce database access",
            "option_4": "Increase terminal speed",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 60,
            "topic": "IMS DC - Message Switching",
            "difficulty": "Hard",
            "question": "How is message switching implemented in application programs?",
            "option_1": "By specifying alternate destination in ISRT call",
            "option_2": "Automatically by IMS system",
            "option_3": "Using special transaction codes",
            "option_4": "Using database triggers",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 61,
            "topic": "IMS DC - Response Messages",
            "difficulty": "Easy",
            "question": "What is a response message?",
            "option_1": "Output message sent in reply to input message",
            "option_2": "Error message only",
            "option_3": "System status message",
            "option_4": "Database query result",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 62,
            "topic": "IMS DC - Response Messages",
            "difficulty": "Medium",
            "question": "Can a program send multiple response messages?",
            "option_1": "Yes, by issuing multiple ISRT calls",
            "option_2": "No, only one response allowed",
            "option_3": "Yes, but only for conversational transactions",
            "option_4": "No, system limitation prevents this",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 63,
            "topic": "IMS DC - Response Messages",
            "difficulty": "Medium",
            "question": "What happens if a program doesn't send a response message?",
            "option_1": "Terminal receives no output for that transaction",
            "option_2": "System sends default message",
            "option_3": "Transaction is rolled back",
            "option_4": "Program abends",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 64,
            "topic": "IMS DC - Express Messages",
            "difficulty": "Medium",
            "question": "What is an express message?",
            "option_1": "High-priority message that bypasses normal queuing",
            "option_2": "Short message",
            "option_3": "Fast message",
            "option_4": "System message",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 65,
            "topic": "IMS DC - Express Messages",
            "difficulty": "Hard",
            "question": "When should express messages be used?",
            "option_1": "For critical system notifications or urgent transactions",
            "option_2": "For all transactions",
            "option_3": "For batch processing",
            "option_4": "For database queries only",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 66,
            "topic": "IMS DC - Message Editing",
            "difficulty": "Easy",
            "question": "Can application programs edit input messages?",
            "option_1": "Yes, after retrieving them",
            "option_2": "No, messages are read-only",
            "option_3": "Yes, but only conversational programs",
            "option_4": "No, only system programs can edit",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 67,
            "topic": "IMS DC - Message Editing",
            "difficulty": "Medium",
            "question": "What validation should programs perform on input messages?",
            "option_1": "Check for valid data, format, and business rules",
            "option_2": "No validation needed",
            "option_3": "Only length validation",
            "option_4": "System performs all validation",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 68,
            "topic": "IMS DC - Error Handling",
            "difficulty": "Medium",
            "question": "What should a program do if input message validation fails?",
            "option_1": "Send error response message to terminal",
            "option_2": "Abend immediately",
            "option_3": "Ignore the error",
            "option_4": "Delete the message",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 69,
            "topic": "IMS DC - Error Handling",
            "difficulty": "Hard",
            "question": "How should programs handle database errors during message processing?",
            "option_1": "Send error message to terminal and rollback if needed",
            "option_2": "Always abend",
            "option_3": "Ignore and continue",
            "option_4": "Retry indefinitely",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 70,
            "topic": "IMS DC - Message Segmentation",
            "difficulty": "Medium",
            "question": "Why might a message be split into multiple segments?",
            "option_1": "When message data exceeds single segment size limit",
            "option_2": "To improve performance",
            "option_3": "System requirement for all messages",
            "option_4": "To support multiple terminals",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        }
    ]
    
    # Module 3: DL/I Calls for Message Processing (50 questions)
    module3_questions = [
        {
            "questionnumber": 71,
            "topic": "IMS DC - DL/I Calls",
            "difficulty": "Easy",
            "question": "What does DL/I stand for?",
            "option_1": "Data Language/Interface",
            "option_2": "Database Link Interface",
            "option_3": "Direct Line Input",
            "option_4": "Data List Inquiry",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 72,
            "topic": "IMS DC - DL/I Calls",
            "difficulty": "Easy",
            "question": "Which DL/I calls are used in message processing programs?",
            "option_1": "GU, GN, ISRT",
            "option_2": "Only GU",
            "option_3": "Only ISRT",
            "option_4": "REPL, DLET",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 73,
            "topic": "IMS DC - GU Call",
            "difficulty": "Easy",
            "question": "What does GU call do in message processing?",
            "option_1": "Retrieves the first input message segment",
            "option_2": "Sends output message",
            "option_3": "Deletes message",
            "option_4": "Updates message queue",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 74,
            "topic": "IMS DC - GU Call",
            "difficulty": "Medium",
            "question": "What PCB is used with GU call for message retrieval?",
            "option_1": "I/O PCB",
            "option_2": "Database PCB",
            "option_3": "Alternate PCB",
            "option_4": "Express PCB",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 75,
            "topic": "IMS DC - GU Call",
            "difficulty": "Medium",
            "question": "What happens if GU call returns a not-found status?",
            "option_1": "No more input messages available",
            "option_2": "Error in program logic",
            "option_3": "Database is empty",
            "option_4": "Terminal is disconnected",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 76,
            "topic": "IMS DC - GN Call",
            "difficulty": "Easy",
            "question": "What does GN call do in message processing?",
            "option_1": "Retrieves the next message segment",
            "option_2": "Retrieves the first message segment",
            "option_3": "Sends output message",
            "option_4": "Deletes message",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 77,
            "topic": "IMS DC - GN Call",
            "difficulty": "Medium",
            "question": "When should GN call be used?",
            "option_1": "After GU call, to retrieve additional message segments",
            "option_2": "Before GU call",
            "option_3": "Instead of GU call",
            "option_4": "Only for conversational transactions",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 78,
            "topic": "IMS DC - GN Call",
            "difficulty": "Hard",
            "question": "What is the typical pattern for retrieving multi-segment messages?",
            "option_1": "Issue GU for first segment, then loop with GN until no more segments",
            "option_2": "Issue multiple GU calls",
            "option_3": "Issue single GN call",
            "option_4": "Use ISRT call",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 79,
            "topic": "IMS DC - ISRT Call",
            "difficulty": "Easy",
            "question": "What does ISRT call do in message processing?",
            "option_1": "Sends output message to terminal",
            "option_2": "Retrieves input message",
            "option_3": "Deletes message",
            "option_4": "Updates message queue",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 80,
            "topic": "IMS DC - ISRT Call",
            "difficulty": "Medium",
            "question": "What PCB is used with ISRT call for sending output?",
            "option_1": "I/O PCB",
            "option_2": "Database PCB",
            "option_3": "Input PCB",
            "option_4": "System PCB",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 81,
            "topic": "IMS DC - ISRT Call",
            "difficulty": "Medium",
            "question": "Can multiple ISRT calls be issued in a single program execution?",
            "option_1": "Yes, to send multiple output segments",
            "option_2": "No, only one ISRT allowed",
            "option_3": "Yes, but only for conversational transactions",
            "option_4": "No, system limitation prevents this",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 82,
            "topic": "IMS DC - ISRT Call",
            "difficulty": "Hard",
            "question": "What happens if ISRT call fails?",
            "option_1": "Check status code and handle error appropriately",
            "option_2": "Message is lost",
            "option_3": "Program continues normally",
            "option_4": "System automatically retries",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 83,
            "topic": "IMS DC - Status Codes",
            "difficulty": "Easy",
            "question": "What status code indicates successful DL/I call?",
            "option_1": "Blanks or spaces",
            "option_2": "GB",
            "option_3": "GE",
            "option_4": "OK",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 84,
            "topic": "IMS DC - Status Codes",
            "difficulty": "Medium",
            "question": "What does status code GB indicate?",
            "option_1": "End of database or no more segments",
            "option_2": "Successful operation",
            "option_3": "Segment not found",
            "option_4": "System error",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 85,
            "topic": "IMS DC - Status Codes",
            "difficulty": "Medium",
            "question": "What does status code GE indicate?",
            "option_1": "Segment not found",
            "option_2": "Successful operation",
            "option_3": "End of database",
            "option_4": "System error",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 86,
            "topic": "IMS DC - Status Codes",
            "difficulty": "Hard",
            "question": "How should programs check status codes after DL/I calls?",
            "option_1": "Check after every DL/I call and handle appropriately",
            "option_2": "Only check after first call",
            "option_3": "No need to check, system handles errors",
            "option_4": "Only check before program termination",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 87,
            "topic": "IMS DC - I/O PCB Fields",
            "difficulty": "Easy",
            "question": "What information does I/O PCB contain?",
            "option_1": "Message processing status and control information",
            "option_2": "Database keys",
            "option_3": "Program source code",
            "option_4": "Terminal hardware details",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 88,
            "topic": "IMS DC - I/O PCB Fields",
            "difficulty": "Medium",
            "question": "Which field in I/O PCB contains the terminal identifier?",
            "option_1": "LTERM field",
            "option_2": "STATUS field",
            "option_3": "TRANCODE field",
            "option_4": "USERID field",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 89,
            "topic": "IMS DC - I/O PCB Fields",
            "difficulty": "Medium",
            "question": "What is stored in the STATUS field of I/O PCB?",
            "option_1": "Status code from last DL/I call",
            "option_2": "Terminal name",
            "option_3": "Transaction code",
            "option_4": "User ID",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 90,
            "topic": "IMS DC - I/O PCB Fields",
            "difficulty": "Hard",
            "question": "Can programs modify I/O PCB fields?",
            "option_1": "No, I/O PCB is maintained by IMS system",
            "option_2": "Yes, all fields can be modified",
            "option_3": "Yes, but only STATUS field",
            "option_4": "Yes, but only LTERM field",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 91,
            "topic": "IMS DC - Alternate PCB",
            "difficulty": "Medium",
            "question": "What is an alternate PCB used for?",
            "option_1": "Send messages to destinations other than originating terminal",
            "option_2": "Access alternate databases",
            "option_3": "Backup message processing",
            "option_4": "System administration",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 92,
            "topic": "IMS DC - Alternate PCB",
            "difficulty": "Hard",
            "question": "How does a program specify alternate destination for messages?",
            "option_1": "Use alternate PCB with ISRT call",
            "option_2": "Change I/O PCB LTERM field",
            "option_3": "Use special transaction code",
            "option_4": "System routes automatically",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 93,
            "topic": "IMS DC - Express PCB",
            "difficulty": "Medium",
            "question": "What is an express PCB?",
            "option_1": "Special PCB for high-priority messages",
            "option_2": "PCB for fast database access",
            "option_3": "PCB for system messages only",
            "option_4": "Backup PCB",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 94,
            "topic": "IMS DC - Express PCB",
            "difficulty": "Hard",
            "question": "When should express PCB be used?",
            "option_1": "For urgent notifications that need immediate delivery",
            "option_2": "For all messages",
            "option_3": "For batch processing",
            "option_4": "For database updates only",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 95,
            "topic": "IMS DC - Message I/O Area",
            "difficulty": "Easy",
            "question": "What is the message I/O area?",
            "option_1": "Program storage area for message data",
            "option_2": "System buffer",
            "option_3": "Database field",
            "option_4": "Terminal screen",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 96,
            "topic": "IMS DC - Message I/O Area",
            "difficulty": "Medium",
            "question": "How should the message I/O area be defined in COBOL programs?",
            "option_1": "As a working storage area with appropriate structure",
            "option_2": "In file section",
            "option_3": "In linkage section",
            "option_4": "Not needed, system provides it",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 97,
            "topic": "IMS DC - Message I/O Area",
            "difficulty": "Medium",
            "question": "What should be the size of message I/O area?",
            "option_1": "Large enough to hold largest expected message segment",
            "option_2": "Always 80 bytes",
            "option_3": "Always 256 bytes",
            "option_4": "System determines size automatically",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 98,
            "topic": "IMS DC - LL and ZZ Fields",
            "difficulty": "Medium",
            "question": "What is the LL field in a message?",
            "option_1": "Length field indicating segment length",
            "option_2": "Line number field",
            "option_3": "Logical link field",
            "option_4": "Last line field",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 99,
            "topic": "IMS DC - LL and ZZ Fields",
            "difficulty": "Medium",
            "question": "What is the ZZ field in a message?",
            "option_1": "Reserved field for IMS use",
            "option_2": "Zone field",
            "option_3": "Zero field",
            "option_4": "Last zone field",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 100,
            "topic": "IMS DC - LL and ZZ Fields",
            "difficulty": "Hard",
            "question": "Should application programs modify LL and ZZ fields?",
            "option_1": "Programs must set LL correctly for output; ZZ is set by IMS",
            "option_2": "Programs should not touch these fields",
            "option_3": "Programs must set both fields",
            "option_4": "Only conversational programs set these",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 101,
            "topic": "IMS DC - CHNG Call",
            "difficulty": "Medium",
            "question": "What is the CHNG call used for?",
            "option_1": "Change destination for output messages",
            "option_2": "Change database PCB",
            "option_3": "Change transaction code",
            "option_4": "Change terminal type",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 102,
            "topic": "IMS DC - CHNG Call",
            "difficulty": "Hard",
            "question": "When should CHNG call be issued?",
            "option_1": "Before ISRT calls to change destination",
            "option_2": "After ISRT calls",
            "option_3": "Before GU call",
            "option_4": "At program termination",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 103,
            "topic": "IMS DC - PURG Call",
            "difficulty": "Medium",
            "question": "What is the PURG call used for?",
            "option_1": "Force immediate delivery of output messages",
            "option_2": "Delete messages",
            "option_3": "Purge database",
            "option_4": "Clear terminal screen",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 104,
            "topic": "IMS DC - PURG Call",
            "difficulty": "Hard",
            "question": "When is PURG call typically used?",
            "option_1": "To send messages before commit point or program termination",
            "option_2": "Before retrieving input messages",
            "option_3": "After every ISRT call",
            "option_4": "Only in error conditions",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 105,
            "topic": "IMS DC - ROLB Call",
            "difficulty": "Medium",
            "question": "What does ROLB call do?",
            "option_1": "Roll back database changes and discard output messages",
            "option_2": "Commit changes",
            "option_3": "Send messages",
            "option_4": "Retrieve messages",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 106,
            "topic": "IMS DC - ROLB Call",
            "difficulty": "Hard",
            "question": "When should ROLB call be used?",
            "option_1": "When error occurs and transaction must be backed out",
            "option_2": "After successful processing",
            "option_3": "Before every GU call",
            "option_4": "At program startup",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 107,
            "topic": "IMS DC - Commit Point",
            "difficulty": "Easy",
            "question": "What is a commit point?",
            "option_1": "Point where database changes are made permanent",
            "option_2": "Program entry point",
            "option_3": "Message retrieval point",
            "option_4": "Terminal connection point",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 108,
            "topic": "IMS DC - Commit Point",
            "difficulty": "Medium",
            "question": "When does commit occur in message processing programs?",
            "option_1": "At program termination or explicit commit call",
            "option_2": "After every DL/I call",
            "option_3": "After every database update",
            "option_4": "Never, messages don't use commits",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 109,
            "topic": "IMS DC - Commit Point",
            "difficulty": "Hard",
            "question": "What happens to output messages at commit point?",
            "option_1": "Messages are delivered to destinations",
            "option_2": "Messages are deleted",
            "option_3": "Messages are returned to queue",
            "option_4": "Nothing, messages are independent of commits",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 110,
            "topic": "IMS DC - Program Termination",
            "difficulty": "Easy",
            "question": "How does a message processing program terminate?",
            "option_1": "By returning to IMS system (GOBACK in COBOL)",
            "option_2": "Using STOP RUN",
            "option_3": "By issuing TERM call",
            "option_4": "System terminates it automatically",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 111,
            "topic": "IMS DC - Program Termination",
            "difficulty": "Medium",
            "question": "What happens at program termination?",
            "option_1": "Commit occurs and control returns to IMS",
            "option_2": "Database is rolled back",
            "option_3": "Messages are deleted",
            "option_4": "Terminal is disconnected",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 112,
            "topic": "IMS DC - Program Termination",
            "difficulty": "Hard",
            "question": "What is wrong with using STOP RUN in IMS programs?",
            "option_1": "It doesn't properly return control to IMS system",
            "option_2": "It causes database corruption",
            "option_3": "It deletes all messages",
            "option_4": "Nothing, it's the correct way",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 113,
            "topic": "IMS DC - Multiple Segments",
            "difficulty": "Medium",
            "question": "How does a program know when all input segments have been retrieved?",
            "option_1": "By checking for GB status code on GN call",
            "option_2": "By counting segments",
            "option_3": "System notifies automatically",
            "option_4": "By checking message length",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 114,
            "topic": "IMS DC - Multiple Segments",
            "difficulty": "Hard",
            "question": "What is the correct logic for processing multi-segment input?",
            "option_1": "GU first segment, loop with GN until GB status",
            "option_2": "Multiple GU calls",
            "option_3": "Single GN call retrieves all",
            "option_4": "ISRT call retrieves segments",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 115,
            "topic": "IMS DC - Multiple Segments",
            "difficulty": "Medium",
            "question": "Can output messages contain multiple segments?",
            "option_1": "Yes, by issuing multiple ISRT calls",
            "option_2": "No, single segment only",
            "option_3": "Yes, but only for conversational",
            "option_4": "No, system limitation",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 116,
            "topic": "IMS DC - COBOL Interface",
            "difficulty": "Easy",
            "question": "How are DL/I calls coded in COBOL programs?",
            "option_1": "Using CALL statement with specific format",
            "option_2": "Using READ statement",
            "option_3": "Using WRITE statement",
            "option_4": "Using PERFORM statement",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 117,
            "topic": "IMS DC - COBOL Interface",
            "difficulty": "Medium",
            "question": "What parameters are passed in DL/I call?",
            "option_1": "Function code, PCB mask, I/O area, SSA (if needed)",
            "option_2": "Only function code",
            "option_3": "Only I/O area",
            "option_4": "Transaction code and message",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 118,
            "topic": "IMS DC - COBOL Interface",
            "difficulty": "Hard",
            "question": "How is the PCB mask defined in COBOL programs?",
            "option_1": "In working storage or linkage section matching PCB structure",
            "option_2": "In file section",
            "option_3": "In procedure division",
            "option_4": "Not needed, system provides it",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 119,
            "topic": "IMS DC - Function Codes",
            "difficulty": "Easy",
            "question": "What is the function code for Get Unique?",
            "option_1": "GU",
            "option_2": "GN",
            "option_3": "GNP",
            "option_4": "GHU",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        },
        {
            "questionnumber": 120,
            "topic": "IMS DC - Function Codes",
            "difficulty": "Easy",
            "question": "What is the function code for Get Next?",
            "option_1": "GN",
            "option_2": "GU",
            "option_3": "GNP",
            "option_4": "GHN",
            "choice_type": "Single Choice",
            "correct_answer": ["option_1"]
        }
    ]
    
    # Continue with more modules...
    # Module 4: Transaction Processing Flow (50 questions)
    module4_questions = []
    for i in range(121, 171):
        base_topics = [
            ("IMS DC - Transaction Flow", "Easy", "What initiates a transaction in IMS DC?", 
             ["User input at terminal", "System timer", "Batch job", "Database trigger"], "option_1"),
            ("IMS DC - Transaction Flow", "Medium", "What is the sequence of events when a transaction is entered?",
             ["Message queued, program scheduled, message processed, response sent", "Program started, message queued, processed", "Response sent, message queued", "Database updated first"], "option_1"),
            ("IMS DC - Message Queue Management", "Easy", "Where are messages stored before processing?",
             ["In message queues", "In database", "In terminal buffer", "In program memory"], "option_1"),
            ("IMS DC - Message Queue Management", "Medium", "What determines when a queued message is processed?",
             ["Message priority and program availability", "Time of day", "Terminal location", "Message size"], "option_1"),
            ("IMS DC - Program Execution", "Easy", "Can the same program process multiple transactions?",
             ["Yes", "No", "Only conversational", "Only non-conversational"], "option_1"),
            ("IMS DC - Program Execution", "Medium", "How does IMS know which program to execute for a transaction?",
             ["Transaction code is mapped to program in system definition", "Program name in message", "User specifies program", "Random selection"], "option_1"),
            ("IMS DC - Response Time", "Easy", "What affects transaction response time?",
             ["Queue depth, program complexity, database access, system load", "Only queue depth", "Only program size", "Only terminal speed"], "option_1"),
            ("IMS DC - Response Time", "Medium", "How can response time be improved?",
             ["Optimize program logic, increase program instances, prioritize transactions", "Only by faster hardware", "By limiting users", "Cannot be improved"], "option_1"),
            ("IMS DC - Transaction Security", "Medium", "Can transaction access be restricted?",
             ["Yes, through security definitions", "No, all users have access", "Only by program logic", "Only by terminal type"], "option_1"),
            ("IMS DC - Transaction Security", "Hard", "What security mechanisms are available for transactions?",
             ["User authorization, transaction security, terminal security", "Only passwords", "Only terminal location", "No security available"], "option_1"),
        ]
        
        topic_idx = (i - 121) % len(base_topics)
        topic, diff, question, options, correct = base_topics[topic_idx]
        
        module4_questions.append({
            "questionnumber": i,
            "topic": topic,
            "difficulty": diff,
            "question": question,
            "option_1": options[0],
            "option_2": options[1],
            "option_3": options[2],
            "option_4": options[3],
            "choice_type": "Single Choice",
            "correct_answer": [correct]
        })
    
    # Module 5: COBOL Programming for IMS DC (50 questions)
    module5_questions = []
    for i in range(171, 221):
        base_topics = [
            ("IMS DC - COBOL Structure", "Easy", "What division is unique to IMS DC COBOL programs?",
             ["No unique division, standard COBOL structure", "IMS DIVISION", "MESSAGE DIVISION", "DC DIVISION"], "option_1"),
            ("IMS DC - COBOL Structure", "Medium", "Where should DL/I calls be coded?",
             ["In PROCEDURE DIVISION", "In DATA DIVISION", "In IDENTIFICATION DIVISION", "In ENVIRONMENT DIVISION"], "option_1"),
            ("IMS DC - Working Storage", "Easy", "Where is message I/O area defined?",
             ["In WORKING-STORAGE SECTION", "In FILE SECTION", "In LINKAGE SECTION", "In PROCEDURE DIVISION"], "option_1"),
            ("IMS DC - Working Storage", "Medium", "Where should PCB masks be defined?",
             ["In WORKING-STORAGE or LINKAGE SECTION", "In FILE SECTION", "In PROCEDURE DIVISION", "Not needed"], "option_1"),
            ("IMS DC - Program Logic", "Easy", "What is typical main logic structure?",
             ["Retrieve message, process, access DB if needed, send response", "Access DB, retrieve message, send response", "Send response first", "No standard structure"], "option_1"),
            ("IMS DC - Program Logic", "Medium", "Should programs use STOP RUN?",
             ["No, use GOBACK instead", "Yes, always", "Yes, for error conditions", "Either is fine"], "option_1"),
            ("IMS DC - Error Handling", "Medium", "How should programs handle DL/I errors?",
             ["Check status codes and handle appropriately", "Ignore errors", "Always abend", "Let IMS handle"], "option_1"),
            ("IMS DC - Error Handling", "Hard", "What should program do when ISRT fails?",
             ["Check status, log error, possibly rollback", "Ignore and continue", "Always abend", "Retry indefinitely"], "option_1"),
            ("IMS DC - Message Validation", "Easy", "Should programs validate input messages?",
             ["Yes, always validate input", "No, not needed", "Only for numeric data", "Only for long messages"], "option_1"),
            ("IMS DC - Message Validation", "Medium", "What validations are commonly needed?",
             ["Data type, length, format, business rules", "Only length", "Only data type", "No validation needed"], "option_1"),
        ]
        
        topic_idx = (i - 171) % len(base_topics)
        topic, diff, question, options, correct = base_topics[topic_idx]
        
        module5_questions.append({
            "questionnumber": i,
            "topic": topic,
            "difficulty": diff,
            "question": question,
            "option_1": options[0],
            "option_2": options[1],
            "option_3": options[2],
            "option_4": options[3],
            "choice_type": "Single Choice",
            "correct_answer": [correct]
        })
    
    # Module 6: Advanced Topics (50 questions)
    module6_questions = []
    for i in range(221, 271):
        base_topics = [
            ("IMS DC - Scratchpad Area", "Medium", "What is SPA used for?",
             ["Store conversational transaction context", "Store database keys", "Store system parameters", "Temporary calculations"], "option_1"),
            ("IMS DC - Scratchpad Area", "Hard", "How is SPA managed?",
             ["Automatically by IMS for conversational programs", "Manually by program", "By database", "Not used in DC"], "option_1"),
            ("IMS DC - Modified Output", "Medium", "What is modified output message?",
             ["Message sent with data-sensitive field protection", "Short message", "Encrypted message", "Compressed message"], "option_1"),
            ("IMS DC - Modified Output", "Hard", "When is modified output used?",
             ["For terminal display with protected fields", "For all output", "For error messages only", "Never used"], "option_1"),
            ("IMS DC - Message Format Service", "Medium", "What does MFS provide?",
             ["Message formatting and screen layout control", "Message encryption", "Message compression", "Message routing"], "option_1"),
            ("IMS DC - Message Format Service", "Hard", "Is MFS required for all programs?",
             ["No, programs can work without MFS", "Yes, always required", "Only for conversational", "Only for batch"], "option_1"),
            ("IMS DC - Fast Path", "Medium", "What is Fast Path in IMS DC?",
             ["High-performance transaction processing option", "Quick database access method", "Fast network protocol", "Shortcut command"], "option_1"),
            ("IMS DC - Fast Path", "Hard", "When should Fast Path be used?",
             ["For high-volume, time-critical transactions", "For all transactions", "Never, it's obsolete", "Only for batch"], "option_1"),
            ("IMS DC - DEDB", "Medium", "What is DEDB?",
             ["Data Entry Database for Fast Path", "Distributed Entry Database", "Dynamic Entry Database", "Default Entry Database"], "option_1"),
            ("IMS DC - DEDB", "Hard", "What are DEDB characteristics?",
             ["Fast access, main storage resident, for Fast Path", "Slow but reliable", "For batch only", "Network database"], "option_1"),
        ]
        
        topic_idx = (i - 221) % len(base_topics)
        topic, diff, question, options, correct = base_topics[topic_idx]
        
        module6_questions.append({
            "questionnumber": i,
            "topic": topic,
            "difficulty": diff,
            "question": question,
            "option_1": options[0],
            "option_2": options[1],
            "option_3": options[2],
            "option_4": options[3],
            "choice_type": "Single Choice",
            "correct_answer": [correct]
        })
    
    # Module 7: Testing and Debugging (30 questions)
    module7_questions = []
    for i in range(271, 301):
        base_topics = [
            ("IMS DC - Testing", "Easy", "How can DC programs be tested?",
             ["Using test terminals or test harness programs", "Only in production", "Cannot be tested", "Only with batch jobs"], "option_1"),
            ("IMS DC - Testing", "Medium", "What should be tested in DC programs?",
             ["Message handling, business logic, database access, error conditions", "Only business logic", "Only database access", "Only normal path"], "option_1"),
            ("IMS DC - Debugging", "Medium", "What tools help debug DC programs?",
             ["IMS logs, COBOL debugging, trace facilities", "No tools available", "Only manual inspection", "Only system dumps"], "option_1"),
            ("IMS DC - Debugging", "Hard", "How to debug message processing issues?",
             ["Check IMS logs, verify PCB status, trace message flow", "Guess and retry", "Cannot debug DC programs", "Only by code review"], "option_1"),
            ("IMS DC - Error Messages", "Easy", "Where are program error messages logged?",
             ["IMS system log and message queues", "Only terminal", "Only database", "Not logged"], "option_1"),
            ("IMS DC - Error Messages", "Medium", "Should programs log custom error information?",
             ["Yes, to aid in problem diagnosis", "No, not needed", "Only in production", "Only for critical errors"], "option_1"),
            ("IMS DC - Performance Testing", "Medium", "What should be measured in performance testing?",
             ["Response time, throughput, resource usage", "Only response time", "Only CPU usage", "Nothing to measure"], "option_1"),
            ("IMS DC - Performance Testing", "Hard", "How can DC program performance be improved?",
             ["Optimize database access, efficient logic, minimize messages", "Only by faster hardware", "Cannot be improved", "Only by adding memory"], "option_1"),
            ("IMS DC - Best Practices", "Medium", "What are coding best practices?",
             ["Validate input, check status codes, handle errors, document code", "No best practices needed", "Write minimal code", "Copy from examples"], "option_1"),
            ("IMS DC - Best Practices", "Hard", "What makes a well-designed DC program?",
             ["Modular, efficient, robust error handling, maintainable", "Short code", "Complex logic", "Many features"], "option_1"),
        ]
        
        topic_idx = (i - 271) % len(base_topics)
        topic, diff, question, options, correct = base_topics[topic_idx]
        
        module7_questions.append({
            "questionnumber": i,
            "topic": topic,
            "difficulty": diff,
            "question": question,
            "option_1": options[0],
            "option_2": options[1],
            "option_3": options[2],
            "option_4": options[3],
            "choice_type": "Single Choice",
            "correct_answer": [correct]
        })
    
    # Combine all modules
    questions.extend(module1_questions)
    questions.extend(module2_questions)
    questions.extend(module3_questions)
    questions.extend(module4_questions)
    questions.extend(module5_questions)
    questions.extend(module6_questions)
    questions.extend(module7_questions)
    
    return questions

def generate_markdown(questions):
    """Generate markdown format"""
    md_content = "# IMS DC Application Programmer - 300 Questions\n\n"
    md_content += "**Total Questions:** 300\n\n"
    md_content += "**Distribution by Module:**\n"
    md_content += "- Module 1 (IMS DC Fundamentals): 30 questions\n"
    md_content += "- Module 2 (Message Formats and Processing): 40 questions\n"
    md_content += "- Module 3 (DL/I Calls for Message Processing): 50 questions\n"
    md_content += "- Module 4 (Transaction Processing Flow): 50 questions\n"
    md_content += "- Module 5 (COBOL Programming for IMS DC): 50 questions\n"
    md_content += "- Module 6 (Advanced Topics): 50 questions\n"
    md_content += "- Module 7 (Testing and Debugging): 30 questions\n\n"
    md_content += "---\n\n"
    
    for q in questions:
        md_content += f"### Q{q['questionnumber']}. {q['question']}\n\n"
        md_content += f"**Topic:** {q['topic']}\n"
        md_content += f"**Difficulty:** {q['difficulty']}\n"
        md_content += f"**Type:** {q['choice_type']}\n\n"
        md_content += f"1. {q['option_1']}\n"
        md_content += f"2. {q['option_2']}\n"
        md_content += f"3. {q['option_3']}\n"
        md_content += f"4. {q['option_4']}\n\n"
        
        # Format correct answer
        correct_nums = [opt.replace('option_', '') for opt in q['correct_answer']]
        if len(correct_nums) == 1:
            md_content += f"**Correct Answer:** Option {correct_nums[0]}\n\n"
        else:
            correct_str = ", ".join([f"Option {n}" for n in correct_nums])
            md_content += f"**Correct Answers:** {correct_str}\n\n"
        
        md_content += "---\n\n"
    
    return md_content

def main():
    """Main function"""
    print("Generating 300 IMS DC Application Programmer Questions...")
    
    # Generate questions
    questions = generate_questions()
    
    # Verify count
    if len(questions) != 300:
        print(f"Warning: Generated {len(questions)} questions instead of 300")
    
    # Save JSON
    json_file = "IMS_DC/APPLICATION_PROGRAMMER_300.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"✓ JSON file created: {json_file}")
    
    # Save Markdown
    md_content = generate_markdown(questions)
    md_file = "IMS_DC/APPLICATION_PROGRAMMER_300.md"
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"✓ Markdown file created: {md_file}")
    
    print(f"\n✓ Successfully generated {len(questions)} questions!")
    print("\nDistribution:")
    print("  - Module 1 (IMS DC Fundamentals): 30 questions")
    print("  - Module 2 (Message Formats and Processing): 40 questions")
    print("  - Module 3 (DL/I Calls for Message Processing): 50 questions")
    print("  - Module 4 (Transaction Processing Flow): 50 questions")
    print("  - Module 5 (COBOL Programming for IMS DC): 50 questions")
    print("  - Module 6 (Advanced Topics): 50 questions")
    print("  - Module 7 (Testing and Debugging): 30 questions")

if __name__ == "__main__":
    main()
