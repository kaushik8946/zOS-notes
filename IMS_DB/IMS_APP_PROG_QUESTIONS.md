# IMS Application Programmer Questions

**Total Questions: 300**

---

### Q1. Which IMS component provides a central point of control and access to application data?

**Type:** Single Choice

**A.** IMS Message Queue Interface

**B.** IMS Database Manager

**C.** IMS Channel Initiator

**D.** IMS Transaction Manager

**Correct Answer:** B

---

### Q2. Which data model is used by IMS Database Manager as its basic storage method?

**Type:** Single Choice

**A.** Document model

**B.** Network model

**C.** Relational model

**D.** Hierarchical model

**Correct Answer:** D

---

### Q3. In IMS hierarchical design, entity types are implemented as what?

**Type:** Single Choice

**A.** Rows

**B.** Partitions

**C.** Segments

**D.** Pages

**Correct Answer:** C

---

### Q4. What is the basic building element of an IMS hierarchical data structure?

**Type:** Single Choice

**A.** Parent/child relationship

**B.** Table/view relationship

**C.** Primary/foreign key pair

**D.** Schema/catalog relationship

**Correct Answer:** A

---

### Q5. According to the Redbook, what is the maximum number of segment types in one IMS hierarchical data structure?

**Type:** Single Choice

**A.** 127

**B.** 255

**C.** 512

**D.** 99

**Correct Answer:** B

---

### Q6. According to the Redbook, what is the maximum number of segment levels in one IMS hierarchical data structure?

**Type:** Single Choice

**A.** 12

**B.** 32

**C.** 15

**D.** 10

**Correct Answer:** C

---

### Q7. How does IMS describe hierarchical traversal sequence?

**Type:** Single Choice

**A.** Front to back, right to left, bottom to top

**B.** Top to bottom, left to right, front to back

**C.** Left to right, top to bottom, back to front

**D.** Bottom to top, left to right, front to back

**Correct Answer:** B

---

### Q8. The hierarchy shown to an IMS application program represents what?

**Type:** Single Choice

**A.** Logical database record view

**B.** Tape block sequence

**C.** Exact physical disk layout

**D.** JES spool structure

**Correct Answer:** A

---

### Q9. The IMS Database Manager allows multiple batch or online tasks to update data while retaining:

**Type:** Single Choice

**A.** Only throughput

**B.** Data integrity

**C.** Only response time

**D.** Only catalog statistics

**Correct Answer:** B

---

### Q10. Which capability is explicitly listed for IMS Database Manager?

**Type:** Single Choice

**A.** TCP socket termination

**B.** UNIX shell scheduling

**C.** HTML rendering

**D.** Database backup and recovery facilities

**Correct Answer:** D

---

### Q11. IMS Database Manager tuning includes which actions?

**Type:** Single Choice

**A.** Replacing all segments with XML

**B.** Auto-generating SQL views only

**C.** Eliminating all logs

**D.** Reorganizing and restructuring databases

**Correct Answer:** D

---

### Q12. IMS databases are organized internally using:

**Type:** Single Choice

**A.** Only z/OS UNIX files

**B.** Only relational clustering indexes

**C.** IMS database organization access methods

**D.** Only VSAM KSDS

**Correct Answer:** C

---

### Q13. IMS database data is stored on disk using:

**Type:** Single Choice

**A.** Only queue manager files

**B.** Normal operating system access methods

**C.** Only IMS proprietary hardware microcode

**D.** Only APPC buffers

**Correct Answer:** B

---

### Q14. In IMS terminology, a "database" commonly describes:

**Type:** Single Choice

**A.** Only the logging subsystem

**B.** A queue manager instance

**C.** Implementation of one hierarchy

**D.** All hierarchies in the enterprise at once

**Correct Answer:** C

---

### Q15. Compared with the relational model, one IMS database is approximately equivalent to:

**Type:** Single Choice

**A.** A trigger

**B.** A table

**C.** A plan

**D.** A schema

**Correct Answer:** B

---

### Q16. The core of an IMS subsystem runs in which region?

**Type:** Single Choice

**A.** Spool region

**B.** Utility region

**C.** Sort region

**D.** Control region

**Correct Answer:** D

---

### Q17. Dependent IMS address spaces primarily:

**Type:** Single Choice

**A.** Provide services and run application programs

**B.** Store only JES output

**C.** Host only TCP stacks

**D.** Replace the control region

**Correct Answer:** A

---

### Q18. Some IMS applications/utilities can run in separate batch address spaces that are:

**Type:** Single Choice

**A.** Separate and with no connection to control region

**B.** Limited to APPC only

**C.** Always connected to control region

**D.** Required to be in CSA

**Correct Answer:** A

---

### Q19. In IMS documentation, the term "region" is commonly used as a synonym for:

**Type:** Single Choice

**A.** Control interval

**B.** JCL procedure

**C.** z/OS address space

**D.** Job step

**Correct Answer:** C

---

### Q20. A stated IMS use of z/OS is to run in:

**Type:** Single Choice

**A.** Single thread only

**B.** Multiple address spaces

**C.** Only virtual machine guests

**D.** Only one dependent task

**Correct Answer:** B

---

### Q21. IMS communication between its address spaces uses:

**Type:** Single Choice

**A.** Cross-memory services

**B.** Only TSO pipes

**C.** Only FTP channels

**D.** Only JES readers

**Correct Answer:** A

---

### Q22. IMS stores frequently accessed control blocks in CSA to:

**Type:** Single Choice

**A.** Minimize impact of multiple address spaces

**B.** Disable sysplex support

**C.** Replace all logs

**D.** Increase page faults

**Correct Answer:** A

---

### Q23. IMS dynamically registers as a z/OS subsystem mainly to:

**Type:** Single Choice

**A.** Create SQL triggers

**B.** Eliminate control blocks

**C.** Format COBOL copybooks

**D.** Detect dependent space failures and interact with subsystems

**Correct Answer:** D

---

### Q24. IMS can exploit z/OS sysplex to allow:

**Type:** Single Choice

**A.** Removal of all logging

**B.** Only one subsystem total

**C.** Multiple subsystems accessing same IMS databases

**D.** Exclusive batch-only operation

**Correct Answer:** C

---

### Q25. One sysplex benefit cited for IMS is:

**Type:** Single Choice

**A.** Increased availability via switch in/out without service interruption

**B.** No need for control region

**C.** Reduced data integrity

**D.** Removal of dependent regions

**Correct Answer:** A

---

### Q26. Another sysplex benefit for IMS is:

**Type:** Single Choice

**A.** Automatic SQL normalization

**B.** No use of address spaces

**C.** Increased processing capacity through multiple subsystems

**D.** Lower aggregate processing volume

**Correct Answer:** C

---

### Q27. The Redbook figure labels IMS DB/DC subsystem with DBRC and RECONs together with:

**Type:** Single Choice

**A.** Only HTML repositories

**B.** Only RACF exits

**C.** IMS message queues and logs

**D.** Only JVM classpaths

**Correct Answer:** C

---

### Q28. According to the z/OS Basics Redbook, Which IMS component provides a central point of control and access to application data?

**Type:** Single Choice

**A.** IMS Channel Initiator

**B.** IMS Database Manager

**C.** IMS Transaction Manager

**D.** IMS Message Queue Interface

**Correct Answer:** B

---

### Q29. According to the z/OS Basics Redbook, Which data model is used by IMS Database Manager as its basic storage method?

**Type:** Single Choice

**A.** Relational model

**B.** Hierarchical model

**C.** Network model

**D.** Document model

**Correct Answer:** B

---

### Q30. According to the z/OS Basics Redbook, In IMS hierarchical design, entity types are implemented as what?

**Type:** Single Choice

**A.** Segments

**B.** Pages

**C.** Partitions

**D.** Rows

**Correct Answer:** A

---

### Q31. According to the z/OS Basics Redbook, What is the basic building element of an IMS hierarchical data structure?

**Type:** Single Choice

**A.** Primary/foreign key pair

**B.** Schema/catalog relationship

**C.** Table/view relationship

**D.** Parent/child relationship

**Correct Answer:** D

---

### Q32. According to the z/OS Basics Redbook, According to the Redbook, what is the maximum number of segment types in one IMS hierarchical data structure?

**Type:** Single Choice

**A.** 99

**B.** 127

**C.** 255

**D.** 512

**Correct Answer:** C

---

### Q33. According to the z/OS Basics Redbook, According to the Redbook, what is the maximum number of segment levels in one IMS hierarchical data structure?

**Type:** Single Choice

**A.** 12

**B.** 32

**C.** 10

**D.** 15

**Correct Answer:** D

---

### Q34. According to the z/OS Basics Redbook, How does IMS describe hierarchical traversal sequence?

**Type:** Single Choice

**A.** Top to bottom, left to right, front to back

**B.** Front to back, right to left, bottom to top

**C.** Left to right, top to bottom, back to front

**D.** Bottom to top, left to right, front to back

**Correct Answer:** A

---

### Q35. According to the z/OS Basics Redbook, The hierarchy shown to an IMS application program represents what?

**Type:** Single Choice

**A.** Logical database record view

**B.** JES spool structure

**C.** Tape block sequence

**D.** Exact physical disk layout

**Correct Answer:** A

---

### Q36. According to the z/OS Basics Redbook, The IMS Database Manager allows multiple batch or online tasks to update data while retaining:

**Type:** Single Choice

**A.** Only response time

**B.** Only throughput

**C.** Data integrity

**D.** Only catalog statistics

**Correct Answer:** C

---

### Q37. According to the z/OS Basics Redbook, Which capability is explicitly listed for IMS Database Manager?

**Type:** Single Choice

**A.** HTML rendering

**B.** TCP socket termination

**C.** Database backup and recovery facilities

**D.** UNIX shell scheduling

**Correct Answer:** C

---

### Q38. According to the z/OS Basics Redbook, IMS Database Manager tuning includes which actions?

**Type:** Single Choice

**A.** Auto-generating SQL views only

**B.** Reorganizing and restructuring databases

**C.** Eliminating all logs

**D.** Replacing all segments with XML

**Correct Answer:** B

---

### Q39. According to the z/OS Basics Redbook, IMS databases are organized internally using:

**Type:** Single Choice

**A.** Only z/OS UNIX files

**B.** IMS database organization access methods

**C.** Only relational clustering indexes

**D.** Only VSAM KSDS

**Correct Answer:** B

---

### Q40. According to the z/OS Basics Redbook, IMS database data is stored on disk using:

**Type:** Single Choice

**A.** Only queue manager files

**B.** Normal operating system access methods

**C.** Only IMS proprietary hardware microcode

**D.** Only APPC buffers

**Correct Answer:** B

---

### Q41. According to the z/OS Basics Redbook, In IMS terminology, a "database" commonly describes:

**Type:** Single Choice

**A.** Only the logging subsystem

**B.** Implementation of one hierarchy

**C.** All hierarchies in the enterprise at once

**D.** A queue manager instance

**Correct Answer:** B

---

### Q42. According to the z/OS Basics Redbook, Compared with the relational model, one IMS database is approximately equivalent to:

**Type:** Single Choice

**A.** A plan

**B.** A table

**C.** A schema

**D.** A trigger

**Correct Answer:** B

---

### Q43. According to the z/OS Basics Redbook, The core of an IMS subsystem runs in which region?

**Type:** Single Choice

**A.** Spool region

**B.** Utility region

**C.** Sort region

**D.** Control region

**Correct Answer:** D

---

### Q44. According to the z/OS Basics Redbook, Dependent IMS address spaces primarily:

**Type:** Single Choice

**A.** Provide services and run application programs

**B.** Replace the control region

**C.** Store only JES output

**D.** Host only TCP stacks

**Correct Answer:** A

---

### Q45. According to the z/OS Basics Redbook, Some IMS applications/utilities can run in separate batch address spaces that are:

**Type:** Single Choice

**A.** Required to be in CSA

**B.** Always connected to control region

**C.** Limited to APPC only

**D.** Separate and with no connection to control region

**Correct Answer:** D

---

### Q46. According to the z/OS Basics Redbook, In IMS documentation, the term "region" is commonly used as a synonym for:

**Type:** Single Choice

**A.** Control interval

**B.** z/OS address space

**C.** JCL procedure

**D.** Job step

**Correct Answer:** B

---

### Q47. According to the z/OS Basics Redbook, A stated IMS use of z/OS is to run in:

**Type:** Single Choice

**A.** Multiple address spaces

**B.** Only virtual machine guests

**C.** Single thread only

**D.** Only one dependent task

**Correct Answer:** A

---

### Q48. According to the z/OS Basics Redbook, IMS communication between its address spaces uses:

**Type:** Single Choice

**A.** Only JES readers

**B.** Only FTP channels

**C.** Only TSO pipes

**D.** Cross-memory services

**Correct Answer:** D

---

### Q49. According to the z/OS Basics Redbook, IMS stores frequently accessed control blocks in CSA to:

**Type:** Single Choice

**A.** Disable sysplex support

**B.** Minimize impact of multiple address spaces

**C.** Replace all logs

**D.** Increase page faults

**Correct Answer:** B

---

### Q50. According to the z/OS Basics Redbook, IMS dynamically registers as a z/OS subsystem mainly to:

**Type:** Single Choice

**A.** Detect dependent space failures and interact with subsystems

**B.** Eliminate control blocks

**C.** Create SQL triggers

**D.** Format COBOL copybooks

**Correct Answer:** A

---

### Q51. According to the z/OS Basics Redbook, IMS can exploit z/OS sysplex to allow:

**Type:** Single Choice

**A.** Only one subsystem total

**B.** Exclusive batch-only operation

**C.** Removal of all logging

**D.** Multiple subsystems accessing same IMS databases

**Correct Answer:** D

---

### Q52. According to the z/OS Basics Redbook, One sysplex benefit cited for IMS is:

**Type:** Single Choice

**A.** Reduced data integrity

**B.** Removal of dependent regions

**C.** No need for control region

**D.** Increased availability via switch in/out without service interruption

**Correct Answer:** D

---

### Q53. According to the z/OS Basics Redbook, Another sysplex benefit for IMS is:

**Type:** Single Choice

**A.** Automatic SQL normalization

**B.** Lower aggregate processing volume

**C.** No use of address spaces

**D.** Increased processing capacity through multiple subsystems

**Correct Answer:** D

---

### Q54. According to the z/OS Basics Redbook, The Redbook figure labels IMS DB/DC subsystem with DBRC and RECONs together with:

**Type:** Single Choice

**A.** IMS message queues and logs

**B.** Only RACF exits

**C.** Only HTML repositories

**D.** Only JVM classpaths

**Correct Answer:** A

---

### Q55. In IMS context described by the Redbook, Which IMS component provides a central point of control and access to application data?

**Type:** Single Choice

**A.** IMS Transaction Manager

**B.** IMS Database Manager

**C.** IMS Message Queue Interface

**D.** IMS Channel Initiator

**Correct Answer:** B

---

### Q56. In IMS context described by the Redbook, Which data model is used by IMS Database Manager as its basic storage method?

**Type:** Single Choice

**A.** Hierarchical model

**B.** Network model

**C.** Document model

**D.** Relational model

**Correct Answer:** A

---

### Q57. In IMS context described by the Redbook, In IMS hierarchical design, entity types are implemented as what?

**Type:** Single Choice

**A.** Segments

**B.** Partitions

**C.** Rows

**D.** Pages

**Correct Answer:** A

---

### Q58. In IMS context described by the Redbook, What is the basic building element of an IMS hierarchical data structure?

**Type:** Single Choice

**A.** Schema/catalog relationship

**B.** Primary/foreign key pair

**C.** Table/view relationship

**D.** Parent/child relationship

**Correct Answer:** D

---

### Q59. In IMS context described by the Redbook, According to the Redbook, what is the maximum number of segment types in one IMS hierarchical data structure?

**Type:** Single Choice

**A.** 127

**B.** 255

**C.** 512

**D.** 99

**Correct Answer:** B

---

### Q60. In IMS context described by the Redbook, According to the Redbook, what is the maximum number of segment levels in one IMS hierarchical data structure?

**Type:** Single Choice

**A.** 32

**B.** 15

**C.** 10

**D.** 12

**Correct Answer:** B

---

### Q61. In IMS context described by the Redbook, How does IMS describe hierarchical traversal sequence?

**Type:** Single Choice

**A.** Top to bottom, left to right, front to back

**B.** Bottom to top, left to right, front to back

**C.** Left to right, top to bottom, back to front

**D.** Front to back, right to left, bottom to top

**Correct Answer:** A

---

### Q62. In IMS context described by the Redbook, The hierarchy shown to an IMS application program represents what?

**Type:** Single Choice

**A.** Exact physical disk layout

**B.** Logical database record view

**C.** Tape block sequence

**D.** JES spool structure

**Correct Answer:** B

---

### Q63. In IMS context described by the Redbook, The IMS Database Manager allows multiple batch or online tasks to update data while retaining:

**Type:** Single Choice

**A.** Only catalog statistics

**B.** Only throughput

**C.** Data integrity

**D.** Only response time

**Correct Answer:** C

---

### Q64. In IMS context described by the Redbook, Which capability is explicitly listed for IMS Database Manager?

**Type:** Single Choice

**A.** TCP socket termination

**B.** Database backup and recovery facilities

**C.** HTML rendering

**D.** UNIX shell scheduling

**Correct Answer:** B

---

### Q65. In IMS context described by the Redbook, IMS Database Manager tuning includes which actions?

**Type:** Single Choice

**A.** Auto-generating SQL views only

**B.** Replacing all segments with XML

**C.** Reorganizing and restructuring databases

**D.** Eliminating all logs

**Correct Answer:** C

---

### Q66. In IMS context described by the Redbook, IMS databases are organized internally using:

**Type:** Single Choice

**A.** Only z/OS UNIX files

**B.** IMS database organization access methods

**C.** Only relational clustering indexes

**D.** Only VSAM KSDS

**Correct Answer:** B

---

### Q67. In IMS context described by the Redbook, IMS database data is stored on disk using:

**Type:** Single Choice

**A.** Only IMS proprietary hardware microcode

**B.** Only queue manager files

**C.** Normal operating system access methods

**D.** Only APPC buffers

**Correct Answer:** C

---

### Q68. In IMS context described by the Redbook, In IMS terminology, a "database" commonly describes:

**Type:** Single Choice

**A.** Implementation of one hierarchy

**B.** All hierarchies in the enterprise at once

**C.** Only the logging subsystem

**D.** A queue manager instance

**Correct Answer:** A

---

### Q69. In IMS context described by the Redbook, Compared with the relational model, one IMS database is approximately equivalent to:

**Type:** Single Choice

**A.** A schema

**B.** A table

**C.** A plan

**D.** A trigger

**Correct Answer:** B

---

### Q70. In IMS context described by the Redbook, The core of an IMS subsystem runs in which region?

**Type:** Single Choice

**A.** Control region

**B.** Spool region

**C.** Utility region

**D.** Sort region

**Correct Answer:** A

---

### Q71. In IMS context described by the Redbook, Dependent IMS address spaces primarily:

**Type:** Single Choice

**A.** Host only TCP stacks

**B.** Store only JES output

**C.** Replace the control region

**D.** Provide services and run application programs

**Correct Answer:** D

---

### Q72. In IMS context described by the Redbook, Some IMS applications/utilities can run in separate batch address spaces that are:

**Type:** Single Choice

**A.** Required to be in CSA

**B.** Always connected to control region

**C.** Limited to APPC only

**D.** Separate and with no connection to control region

**Correct Answer:** D

---

### Q73. In IMS context described by the Redbook, In IMS documentation, the term "region" is commonly used as a synonym for:

**Type:** Single Choice

**A.** Control interval

**B.** Job step

**C.** z/OS address space

**D.** JCL procedure

**Correct Answer:** C

---

### Q74. In IMS context described by the Redbook, A stated IMS use of z/OS is to run in:

**Type:** Single Choice

**A.** Only virtual machine guests

**B.** Only one dependent task

**C.** Multiple address spaces

**D.** Single thread only

**Correct Answer:** C

---

### Q75. In IMS context described by the Redbook, IMS communication between its address spaces uses:

**Type:** Single Choice

**A.** Only JES readers

**B.** Only FTP channels

**C.** Only TSO pipes

**D.** Cross-memory services

**Correct Answer:** D

---

### Q76. In IMS context described by the Redbook, IMS stores frequently accessed control blocks in CSA to:

**Type:** Single Choice

**A.** Increase page faults

**B.** Replace all logs

**C.** Minimize impact of multiple address spaces

**D.** Disable sysplex support

**Correct Answer:** C

---

### Q77. In IMS context described by the Redbook, IMS dynamically registers as a z/OS subsystem mainly to:

**Type:** Single Choice

**A.** Create SQL triggers

**B.** Format COBOL copybooks

**C.** Eliminate control blocks

**D.** Detect dependent space failures and interact with subsystems

**Correct Answer:** D

---

### Q78. In IMS context described by the Redbook, IMS can exploit z/OS sysplex to allow:

**Type:** Single Choice

**A.** Removal of all logging

**B.** Only one subsystem total

**C.** Exclusive batch-only operation

**D.** Multiple subsystems accessing same IMS databases

**Correct Answer:** D

---

### Q79. In IMS context described by the Redbook, One sysplex benefit cited for IMS is:

**Type:** Single Choice

**A.** Reduced data integrity

**B.** Removal of dependent regions

**C.** Increased availability via switch in/out without service interruption

**D.** No need for control region

**Correct Answer:** C

---

### Q80. In IMS context described by the Redbook, Another sysplex benefit for IMS is:

**Type:** Single Choice

**A.** Lower aggregate processing volume

**B.** Automatic SQL normalization

**C.** Increased processing capacity through multiple subsystems

**D.** No use of address spaces

**Correct Answer:** C

---

### Q81. In IMS context described by the Redbook, The Redbook figure labels IMS DB/DC subsystem with DBRC and RECONs together with:

**Type:** Single Choice

**A.** Only JVM classpaths

**B.** Only RACF exits

**C.** IMS message queues and logs

**D.** Only HTML repositories

**Correct Answer:** C

---

### Q82. From the IMS sections of the Redbook, Which IMS component provides a central point of control and access to application data?

**Type:** Single Choice

**A.** IMS Channel Initiator

**B.** IMS Message Queue Interface

**C.** IMS Transaction Manager

**D.** IMS Database Manager

**Correct Answer:** D

---

### Q83. From the IMS sections of the Redbook, Which data model is used by IMS Database Manager as its basic storage method?

**Type:** Single Choice

**A.** Hierarchical model

**B.** Document model

**C.** Relational model

**D.** Network model

**Correct Answer:** A

---

### Q84. From the IMS sections of the Redbook, In IMS hierarchical design, entity types are implemented as what?

**Type:** Single Choice

**A.** Rows

**B.** Pages

**C.** Segments

**D.** Partitions

**Correct Answer:** C

---

### Q85. From the IMS sections of the Redbook, What is the basic building element of an IMS hierarchical data structure?

**Type:** Single Choice

**A.** Parent/child relationship

**B.** Schema/catalog relationship

**C.** Table/view relationship

**D.** Primary/foreign key pair

**Correct Answer:** A

---

### Q86. From the IMS sections of the Redbook, According to the Redbook, what is the maximum number of segment types in one IMS hierarchical data structure?

**Type:** Single Choice

**A.** 512

**B.** 255

**C.** 99

**D.** 127

**Correct Answer:** B

---

### Q87. From the IMS sections of the Redbook, According to the Redbook, what is the maximum number of segment levels in one IMS hierarchical data structure?

**Type:** Single Choice

**A.** 15

**B.** 10

**C.** 32

**D.** 12

**Correct Answer:** A

---

### Q88. From the IMS sections of the Redbook, How does IMS describe hierarchical traversal sequence?

**Type:** Single Choice

**A.** Bottom to top, left to right, front to back

**B.** Left to right, top to bottom, back to front

**C.** Front to back, right to left, bottom to top

**D.** Top to bottom, left to right, front to back

**Correct Answer:** D

---

### Q89. From the IMS sections of the Redbook, The hierarchy shown to an IMS application program represents what?

**Type:** Single Choice

**A.** Tape block sequence

**B.** JES spool structure

**C.** Logical database record view

**D.** Exact physical disk layout

**Correct Answer:** C

---

### Q90. From the IMS sections of the Redbook, The IMS Database Manager allows multiple batch or online tasks to update data while retaining:

**Type:** Single Choice

**A.** Only catalog statistics

**B.** Only response time

**C.** Only throughput

**D.** Data integrity

**Correct Answer:** D

---

### Q91. From the IMS sections of the Redbook, Which capability is explicitly listed for IMS Database Manager?

**Type:** Single Choice

**A.** HTML rendering

**B.** TCP socket termination

**C.** UNIX shell scheduling

**D.** Database backup and recovery facilities

**Correct Answer:** D

---

### Q92. From the IMS sections of the Redbook, IMS Database Manager tuning includes which actions?

**Type:** Single Choice

**A.** Reorganizing and restructuring databases

**B.** Eliminating all logs

**C.** Replacing all segments with XML

**D.** Auto-generating SQL views only

**Correct Answer:** A

---

### Q93. From the IMS sections of the Redbook, IMS databases are organized internally using:

**Type:** Single Choice

**A.** Only relational clustering indexes

**B.** Only VSAM KSDS

**C.** IMS database organization access methods

**D.** Only z/OS UNIX files

**Correct Answer:** C

---

### Q94. From the IMS sections of the Redbook, IMS database data is stored on disk using:

**Type:** Single Choice

**A.** Only APPC buffers

**B.** Only queue manager files

**C.** Normal operating system access methods

**D.** Only IMS proprietary hardware microcode

**Correct Answer:** C

---

### Q95. From the IMS sections of the Redbook, In IMS terminology, a "database" commonly describes:

**Type:** Single Choice

**A.** Implementation of one hierarchy

**B.** A queue manager instance

**C.** Only the logging subsystem

**D.** All hierarchies in the enterprise at once

**Correct Answer:** A

---

### Q96. From the IMS sections of the Redbook, Compared with the relational model, one IMS database is approximately equivalent to:

**Type:** Single Choice

**A.** A plan

**B.** A table

**C.** A trigger

**D.** A schema

**Correct Answer:** B

---

### Q97. From the IMS sections of the Redbook, The core of an IMS subsystem runs in which region?

**Type:** Single Choice

**A.** Sort region

**B.** Control region

**C.** Spool region

**D.** Utility region

**Correct Answer:** B

---

### Q98. A team is reviewing IMS architecture. Statement A: Which IMS component provides a central point of control and access to application data. Statement B: The hierarchy shown to an IMS application program represents what. Which design decision best aligns with this Redbook guidance?

**Type:** Single Choice

**A.** Neither statement is supported by Redbook IMS sections.

**B.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**C.** Both statements are consistent with Redbook IMS explanations.

**D.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**Correct Answer:** C

---

### Q99. A team is reviewing IMS architecture. Statement A: Which data model is used by IMS Database Manager as its basic storage method. Statement B: IMS Database Manager tuning includes which actions. Which interpretation is most accurate?

**Type:** Single Choice

**A.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**B.** Both statements are consistent with Redbook IMS explanations.

**C.** Neither statement is supported by Redbook IMS sections.

**D.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**Correct Answer:** B

---

### Q100. A team is reviewing IMS architecture. Statement A: In IMS hierarchical design, entity types are implemented as what. Statement B: In IMS terminology, a "database" commonly describes. Which conclusion follows most directly?

**Type:** Single Choice

**A.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**B.** Both statements are consistent with Redbook IMS explanations.

**C.** Neither statement is supported by Redbook IMS sections.

**D.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**Correct Answer:** B

---

### Q101. A team is reviewing IMS architecture. Statement A: What is the basic building element of an IMS hierarchical data structure. Statement B: Dependent IMS address spaces primarily. Which option best reflects IMS architecture behavior?

**Type:** Single Choice

**A.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**B.** Both statements are consistent with Redbook IMS explanations.

**C.** Neither statement is supported by Redbook IMS sections.

**D.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**Correct Answer:** B

---

### Q102. A team is reviewing IMS architecture. Statement A: According to the Redbook, what is the maximum number of segment types in one IMS hierarchical data structure. Statement B: A stated IMS use of z/OS is to run in. Which design decision best aligns with this Redbook guidance?

**Type:** Single Choice

**A.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**B.** Neither statement is supported by Redbook IMS sections.

**C.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**D.** Both statements are consistent with Redbook IMS explanations.

**Correct Answer:** D

---

### Q103. A team is reviewing IMS architecture. Statement A: According to the Redbook, what is the maximum number of segment levels in one IMS hierarchical data structure. Statement B: IMS stores frequently accessed control blocks in CSA to. Which interpretation is most accurate?

**Type:** Single Choice

**A.** Neither statement is supported by Redbook IMS sections.

**B.** Both statements are consistent with Redbook IMS explanations.

**C.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**D.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**Correct Answer:** B

---

### Q104. A team is reviewing IMS architecture. Statement A: How does IMS describe hierarchical traversal sequence. Statement B: One sysplex benefit cited for IMS is. Which conclusion follows most directly?

**Type:** Single Choice

**A.** Neither statement is supported by Redbook IMS sections.

**B.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**C.** Both statements are consistent with Redbook IMS explanations.

**D.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**Correct Answer:** C

---

### Q105. A team is reviewing IMS architecture. Statement A: The hierarchy shown to an IMS application program represents what. Statement B: Which IMS component provides a central point of control and access to application data. Which option best reflects IMS architecture behavior?

**Type:** Single Choice

**A.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**B.** Both statements are consistent with Redbook IMS explanations.

**C.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**D.** Neither statement is supported by Redbook IMS sections.

**Correct Answer:** B

---

### Q106. A team is reviewing IMS architecture. Statement A: The IMS Database Manager allows multiple batch or online tasks to update data while retaining. Statement B: What is the basic building element of an IMS hierarchical data structure. Which design decision best aligns with this Redbook guidance?

**Type:** Single Choice

**A.** Neither statement is supported by Redbook IMS sections.

**B.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**C.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**D.** Both statements are consistent with Redbook IMS explanations.

**Correct Answer:** D

---

### Q107. A team is reviewing IMS architecture. Statement A: Which capability is explicitly listed for IMS Database Manager. Statement B: How does IMS describe hierarchical traversal sequence. Which interpretation is most accurate?

**Type:** Single Choice

**A.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**B.** Neither statement is supported by Redbook IMS sections.

**C.** Both statements are consistent with Redbook IMS explanations.

**D.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**Correct Answer:** C

---

### Q108. A team is reviewing IMS architecture. Statement A: IMS Database Manager tuning includes which actions. Statement B: Which capability is explicitly listed for IMS Database Manager. Which conclusion follows most directly?

**Type:** Single Choice

**A.** Neither statement is supported by Redbook IMS sections.

**B.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**C.** Both statements are consistent with Redbook IMS explanations.

**D.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**Correct Answer:** C

---

### Q109. A team is reviewing IMS architecture. Statement A: IMS databases are organized internally using. Statement B: IMS database data is stored on disk using. Which option best reflects IMS architecture behavior?

**Type:** Single Choice

**A.** Both statements are consistent with Redbook IMS explanations.

**B.** Neither statement is supported by Redbook IMS sections.

**C.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**D.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**Correct Answer:** A

---

### Q110. A team is reviewing IMS architecture. Statement A: IMS database data is stored on disk using. Statement B: The core of an IMS subsystem runs in which region. Which design decision best aligns with this Redbook guidance?

**Type:** Single Choice

**A.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**B.** Both statements are consistent with Redbook IMS explanations.

**C.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**D.** Neither statement is supported by Redbook IMS sections.

**Correct Answer:** B

---

### Q111. A team is reviewing IMS architecture. Statement A: In IMS terminology, a "database" commonly describes. Statement B: In IMS documentation, the term "region" is commonly used as a synonym for. Which interpretation is most accurate?

**Type:** Single Choice

**A.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**B.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**C.** Neither statement is supported by Redbook IMS sections.

**D.** Both statements are consistent with Redbook IMS explanations.

**Correct Answer:** D

---

### Q112. A team is reviewing IMS architecture. Statement A: Compared with the relational model, one IMS database is approximately equivalent to. Statement B: IMS communication between its address spaces uses. Which conclusion follows most directly?

**Type:** Single Choice

**A.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**B.** Neither statement is supported by Redbook IMS sections.

**C.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**D.** Both statements are consistent with Redbook IMS explanations.

**Correct Answer:** D

---

### Q113. A team is reviewing IMS architecture. Statement A: The core of an IMS subsystem runs in which region. Statement B: IMS can exploit z/OS sysplex to allow. Which option best reflects IMS architecture behavior?

**Type:** Single Choice

**A.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**B.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**C.** Both statements are consistent with Redbook IMS explanations.

**D.** Neither statement is supported by Redbook IMS sections.

**Correct Answer:** C

---

### Q114. A team is reviewing IMS architecture. Statement A: Dependent IMS address spaces primarily. Statement B: The Redbook figure labels IMS DB/DC subsystem with DBRC and RECONs together with. Which design decision best aligns with this Redbook guidance?

**Type:** Single Choice

**A.** Neither statement is supported by Redbook IMS sections.

**B.** Both statements are consistent with Redbook IMS explanations.

**C.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**D.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**Correct Answer:** B

---

### Q115. A team is reviewing IMS architecture. Statement A: Some IMS applications/utilities can run in separate batch address spaces that are. Statement B: In IMS hierarchical design, entity types are implemented as what. Which interpretation is most accurate?

**Type:** Single Choice

**A.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**B.** Neither statement is supported by Redbook IMS sections.

**C.** Both statements are consistent with Redbook IMS explanations.

**D.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**Correct Answer:** C

---

### Q116. A team is reviewing IMS architecture. Statement A: In IMS documentation, the term "region" is commonly used as a synonym for. Statement B: According to the Redbook, what is the maximum number of segment levels in one IMS hierarchical data structure. Which conclusion follows most directly?

**Type:** Single Choice

**A.** Neither statement is supported by Redbook IMS sections.

**B.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**C.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**D.** Both statements are consistent with Redbook IMS explanations.

**Correct Answer:** D

---

### Q117. A team is reviewing IMS architecture. Statement A: A stated IMS use of z/OS is to run in. Statement B: The IMS Database Manager allows multiple batch or online tasks to update data while retaining. Which option best reflects IMS architecture behavior?

**Type:** Single Choice

**A.** Neither statement is supported by Redbook IMS sections.

**B.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**C.** Both statements are consistent with Redbook IMS explanations.

**D.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**Correct Answer:** C

---

### Q118. A team is reviewing IMS architecture. Statement A: IMS communication between its address spaces uses. Statement B: Compared with the relational model, one IMS database is approximately equivalent to. Which interpretation is most accurate?

**Type:** Single Choice

**A.** Both statements are consistent with Redbook IMS explanations.

**B.** Neither statement is supported by Redbook IMS sections.

**C.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**D.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**Correct Answer:** A

---

### Q119. A team is reviewing IMS architecture. Statement A: IMS stores frequently accessed control blocks in CSA to. Statement B: Some IMS applications/utilities can run in separate batch address spaces that are. Which conclusion follows most directly?

**Type:** Single Choice

**A.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**B.** Both statements are consistent with Redbook IMS explanations.

**C.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**D.** Neither statement is supported by Redbook IMS sections.

**Correct Answer:** B

---

### Q120. A team is reviewing IMS architecture. Statement A: IMS can exploit z/OS sysplex to allow. Statement B: IMS dynamically registers as a z/OS subsystem mainly to. Which design decision best aligns with this Redbook guidance?

**Type:** Single Choice

**A.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**B.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**C.** Both statements are consistent with Redbook IMS explanations.

**D.** Neither statement is supported by Redbook IMS sections.

**Correct Answer:** C

---

### Q121. A team is reviewing IMS architecture. Statement A: One sysplex benefit cited for IMS is. Statement B: Another sysplex benefit for IMS is. Which interpretation is most accurate?

**Type:** Single Choice

**A.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**B.** Neither statement is supported by Redbook IMS sections.

**C.** Both statements are consistent with Redbook IMS explanations.

**D.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**Correct Answer:** C

---

### Q122. A team is reviewing IMS architecture. Statement A: Another sysplex benefit for IMS is. Statement B: Which data model is used by IMS Database Manager as its basic storage method. Which conclusion follows most directly?

**Type:** Single Choice

**A.** Neither statement is supported by Redbook IMS sections.

**B.** Both statements are consistent with Redbook IMS explanations.

**C.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**D.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**Correct Answer:** B

---

### Q123. A team is reviewing IMS architecture. Statement A: The Redbook figure labels IMS DB/DC subsystem with DBRC and RECONs together with. Statement B: According to the Redbook, what is the maximum number of segment types in one IMS hierarchical data structure. Which option best reflects IMS architecture behavior?

**Type:** Single Choice

**A.** Neither statement is supported by Redbook IMS sections.

**B.** Only Statement B is consistent; Statement A contradicts Redbook IMS sections.

**C.** Both statements are consistent with Redbook IMS explanations.

**D.** Only Statement A is consistent; Statement B contradicts Redbook IMS sections.

**Correct Answer:** C

---

### Q124. A DBA needs access path continuity while preserving hierarchical design intent. Which actions align with Redbook IMS principles?

**Type:** Multiple Choice

**A.** Place frequently used IMS control blocks in CSA

**B.** Use a control region with dependent address spaces

**C.** Exploit sysplex to run multiple IMS subsystems against same databases

**D.** Treat physical storage layout as mandatory application-level concern

**Correct Answers:** A, B, C

---

### Q125. Two IMS subsystems in a sysplex need shared database availability. Which actions align with Redbook IMS principles?

**Type:** Multiple Choice

**A.** Exploit sysplex to run multiple IMS subsystems against same databases

**B.** Use a control region with dependent address spaces

**C.** Force all IMS execution into one address space to maximize isolation

**D.** Run IMS in multiple address spaces

**Correct Answers:** A, B, D

---

### Q126. What is the primary purpose of the GU (Get Unique) DL/I call in an IMS application program?

**Type:** Single Choice

**A.** To retrieve all segments in hierarchical sequence

**B.** To retrieve the first segment occurrence that satisfies the SSA criteria

**C.** To retrieve the next segment under the current parent

**D.** To retrieve all twin segments at once

**Correct Answer:** B

---

### Q127. When an IMS application program issues a GN (Get Next) call, what segment does it retrieve?

**Type:** Single Choice

**A.** The first segment in the database

**B.** The next segment occurrence under the same parent

**C.** The next segment in hierarchical sequence from current position

**D.** The next root segment only

**Correct Answer:** C

---

### Q128. How does GNP (Get Next within Parent) differ from GN in IMS application programming?

**Type:** Single Choice

**A.** GNP retrieves only root segments while GN retrieves all segments

**B.** GNP retrieves next segment under same parent while GN continues hierarchical sequence

**C.** GNP requires qualified SSA while GN requires unqualified SSA

**D.** GNP is faster but retrieves fewer segments than GN

**Correct Answer:** B

---

### Q129. What does the ISRT DL/I call do in an IMS application program?

**Type:** Single Choice

**A.** Deletes a segment from the database

**B.** Updates an existing segment

**C.** Inserts a new segment into the database

**D.** Retrieves a segment for processing

**Correct Answer:** C

---

### Q130. What is the purpose of the REPL DL/I call?

**Type:** Single Choice

**A.** To insert a new segment

**B.** To replace or update an existing segment

**C.** To delete a segment

**D.** To retrieve a segment

**Correct Answer:** B

---

### Q131. What happens when an IMS application program issues a DLET (Delete) call on a parent segment?

**Type:** Single Choice

**A.** Only the parent segment is deleted

**B.** The parent and all its dependent child segments are deleted

**C.** The operation fails with an error

**D.** Only the child segments are deleted

**Correct Answer:** B

---

### Q132. Before an IMS application program can issue a REPL call, what must it do first?

**Type:** Single Choice

**A.** Issue an ISRT call

**B.** Issue a DLET call

**C.** Issue a GU or GN call to establish position

**D.** Issue a GNP call

**Correct Answer:** C

---

### Q133. An IMS application needs to retrieve all ORDER segments for a specific CUSTOMER. Which DL/I calls should be used?

**Type:** Single Choice

**A.** GU for the CUSTOMER, then GN calls for each ORDER

**B.** GU for the CUSTOMER, then GNP calls for each ORDER

**C.** Multiple GU calls for each ORDER

**D.** GN calls only without initial GU

**Correct Answer:** B

---

### Q134. What does SSA stand for in IMS application programming?

**Type:** Single Choice

**A.** System Segment Address

**B.** Segment Search Argument

**C.** Sequential Storage Access

**D.** Structured Segment Array

**Correct Answer:** B

---

### Q135. What is the difference between a qualified and unqualified SSA in IMS?

**Type:** Single Choice

**A.** Qualified SSA includes field conditions, unqualified specifies only segment type

**B.** Qualified SSA is faster, unqualified is slower

**C.** Qualified SSA can only be used with GU, unqualified with GN

**D.** There is no difference

**Correct Answer:** A

---

### Q136. In an IMS application program, what is the format of a qualified SSA?

**Type:** Single Choice

**A.** SEGNAME

**B.** SEGNAME(FIELDNAME operator value)

**C.** SEGNAME.FIELDNAME=value

**D.** SEGNAME/FIELDNAME/value

**Correct Answer:** B

---

### Q137. An IMS COBOL program needs to retrieve a CUSTOMER segment where CUSTNO = 12345. Which SSA is correct?

**Type:** Single Choice

**A.** CUSTOMER

**B.** CUSTOMER(CUSTNO=12345)

**C.** CUSTOMER*CUSTNO*12345

**D.** CUSTOMER.CUSTNO.EQ.12345

**Correct Answer:** B

---

### Q138. What operators can be used in a qualified SSA in IMS application programs?

**Type:** Single Choice

**A.** Only = (equal)

**B.** =, >, <, >=, <=, ¬= (not equal)

**C.** Only = and <>

**D.** =, >, <, LIKE, IN

**Correct Answer:** B

---

### Q139. In an IMS hierarchical database, what is a root segment?

**Type:** Single Choice

**A.** The last segment in the hierarchy

**B.** The top-level segment in the hierarchy

**C.** Any segment with child segments

**D.** The segment with the most fields

**Correct Answer:** B

---

### Q140. What are twin segments in IMS?

**Type:** Single Choice

**A.** Two segments with identical data

**B.** Multiple occurrences of the same segment type under one parent

**C.** Segments at the same level in the hierarchy

**D.** Backup copies of segments

**Correct Answer:** B

---

### Q141. In IMS hierarchical processing, what sequence is used to traverse segments?

**Type:** Single Choice

**A.** Bottom to top, right to left, back to front

**B.** Top to bottom, left to right, front to back

**C.** Left to right, top to bottom, back to front

**D.** Random access based on key fields

**Correct Answer:** B

---

### Q142. What is a database record in IMS from an application programmer's perspective?

**Type:** Single Choice

**A.** A single segment occurrence

**B.** All segments of the same type

**C.** One root segment occurrence and all its dependent segments

**D.** A collection of related tables

**Correct Answer:** C

---

### Q143. In IMS, what determines the order of twin segments?

**Type:** Single Choice

**A.** The order they were inserted

**B.** The sequence field value

**C.** Alphabetical order of segment name

**D.** Random order

**Correct Answer:** B

---

### Q144. What does PCB stand for in IMS application programming?

**Type:** Single Choice

**A.** Program Control Block

**B.** Program Communication Block

**C.** Process Control Buffer

**D.** Primary Control Block

**Correct Answer:** B

---

### Q145. What information does a PCB provide to an IMS application program?

**Type:** Single Choice

**A.** Only the database name

**B.** Only the segment types

**C.** The database view including sensitive segments and processing options

**D.** Only the status codes

**Correct Answer:** C

---

### Q146. After a DL/I call, where does an IMS application program find the status code?

**Type:** Single Choice

**A.** In the segment I/O area

**B.** In the PCB status code field

**C.** In the DBD

**D.** In a global variable

**Correct Answer:** B

---

### Q147. What does a status code of 'GE' indicate in an IMS application program after a DL/I call?

**Type:** Single Choice

**A.** Segment found successfully

**B.** Segment not found (end of database)

**C.** Duplicate key error

**D.** Security violation

**Correct Answer:** B

---

### Q148. What processing options can be specified in a PCB for an IMS application program?

**Type:** Multiple Choice

**A.** Only G (Get)

**B.** G (Get), I (Insert), R (Replace), D (Delete)

**C.** Only I (Insert) and D (Delete)

**D.** Only G (Get) and R (Replace)

**Correct Answer:** B

---

### Q149. What does DBD stand for in IMS?

**Type:** Single Choice

**A.** Database Description

**B.** Database Definition

**C.** Data Block Description

**D.** Direct Block Definition

**Correct Answer:** A

---

### Q150. What does PSB stand for in IMS application programming?

**Type:** Single Choice

**A.** Program Storage Block

**B.** Program Specification Block

**C.** Process Segment Buffer

**D.** Primary System Block

**Correct Answer:** B

---

### Q151. What is the relationship between DBD and PSB in IMS?

**Type:** Single Choice

**A.** DBD describes physical structure; PSB describes program's view of database

**B.** DBD is for batch programs; PSB is for online programs

**C.** DBD and PSB are identical

**D.** DBD is created by programmers; PSB is created by DBAs

**Correct Answer:** A

---

### Q152. What are sensitive segments in an IMS PSB?

**Type:** Single Choice

**A.** Segments that contain confidential data

**B.** Segments that are accessible to the application program

**C.** Segments that cannot be modified

**D.** Segments that are encrypted

**Correct Answer:** B

---

### Q153. If an IMS application program tries to access a segment that is not defined as sensitive in its PSB, what happens?

**Type:** Single Choice

**A.** The segment is returned successfully

**B.** A status code error is returned

**C.** The program abends

**D.** The segment is returned but marked as read-only

**Correct Answer:** B

---

### Q154. What is a segment in IMS hierarchical database?

**Type:** Single Choice

**A.** A collection of related tables

**B.** A basic unit of data containing related fields

**C.** A database index

**D.** A pointer to another segment

**Correct Answer:** B

---

### Q155. What is a key field in an IMS segment?

**Type:** Single Choice

**A.** The first field in the segment

**B.** A field used to uniquely identify and sequence segment occurrences

**C.** A field that cannot be updated

**D.** A field that references another segment

**Correct Answer:** B

---

### Q156. Can an IMS segment exist without a key field?

**Type:** Single Choice

**A.** No, all segments must have a key field

**B.** Yes, key fields are optional in IMS segments

**C.** Only root segments require key fields

**D.** Only child segments require key fields

**Correct Answer:** B

---

### Q157. What is the purpose of a sequence field in IMS segments?

**Type:** Single Choice

**A.** To generate sequence numbers automatically

**B.** To determine the order in which twin segments are stored and retrieved

**C.** To count the number of segments

**D.** To validate segment data

**Correct Answer:** B

---

### Q158. In an IMS application program, how are segment fields accessed?

**Type:** Single Choice

**A.** Through SQL SELECT statements

**B.** Through the segment I/O area after a successful DL/I call

**C.** Through direct memory pointers

**D.** Through XML parsing

**Correct Answer:** B

---

### Q159. What happens to database position after a successful GU call in an IMS program?

**Type:** Single Choice

**A.** Position is set to the beginning of the database

**B.** Position is set to the retrieved segment

**C.** Position is not changed

**D.** Position is set to the root segment

**Correct Answer:** B

---

### Q160. An IMS program issues: GU on root, GN on child1, GN on child2. What is the next segment retrieved by another GN?

**Type:** Single Choice

**A.** Another child2 twin

**B.** The next segment in hierarchical sequence after child2

**C.** The root segment

**D.** Another child1 segment

**Correct Answer:** B

---

### Q161. What is sequential processing in IMS application programming?

**Type:** Single Choice

**A.** Processing segments in random order

**B.** Processing segments in hierarchical sequence

**C.** Processing only root segments

**D.** Processing segments in reverse order

**Correct Answer:** B

---

### Q162. An IMS program needs to process all ITEM segments under a specific ORDER. After GU to the ORDER, which approach is correct?

**Type:** Single Choice

**A.** Use GN calls until status code GE

**B.** Use GNP calls until status code GE

**C.** Use GU calls for each ITEM

**D.** Use ISRT calls

**Correct Answer:** B

---

### Q163. What status code indicates a successful DL/I call in an IMS program?

**Type:** Single Choice

**A.** OK

**B.** 00 (spaces)

**C.** GE

**D.** GA

**Correct Answer:** B

---

### Q164. What does the status code 'GB' mean in an IMS application program?

**Type:** Single Choice

**A.** Segment found successfully

**B.** End of database reached

**C.** End of database record (reached end of current path)

**D.** Duplicate key error

**Correct Answer:** C

---

### Q165. In an IMS program, what status code indicates a duplicate key error during ISRT?

**Type:** Single Choice

**A.** GE

**B.** II

**C.** DK

**D.** DA

**Correct Answer:** B

---

### Q166. Which programming languages can be used to write IMS application programs?

**Type:** Single Choice

**A.** Only COBOL

**B.** COBOL, Java, PL/I, C, C++, Assembler

**C.** Only COBOL and Assembler

**D.** Only Java

**Correct Answer:** B

---

### Q167. In a COBOL IMS program, where is the PCB defined?

**Type:** Single Choice

**A.** In the WORKING-STORAGE SECTION

**B.** In the LINKAGE SECTION

**C.** In the FILE SECTION

**D.** In the CONFIGURATION SECTION

**Correct Answer:** B

---

### Q168. In a COBOL IMS program, where is the segment I/O area typically defined?

**Type:** Single Choice

**A.** In the LINKAGE SECTION

**B.** In the WORKING-STORAGE SECTION

**C.** In the FILE SECTION

**D.** In the PROCEDURE DIVISION

**Correct Answer:** B

---

### Q169. What is the correct COBOL syntax for a DL/I call in an IMS program?

**Type:** Single Choice

**A.** EXEC DLI GU PCB SSA SEGMENT

**B.** CALL 'CBLTDLI' USING function, PCB, segment-io-area, SSA

**C.** PERFORM DLI-GU USING PCB SSA

**D.** INVOKE DLI-CALL WITH GU PCB SEGMENT

**Correct Answer:** B

---

### Q170. When an IMS application deletes a parent segment, what happens to its children?

**Type:** Single Choice

**A.** Children remain unchanged

**B.** Children are automatically deleted (cascade delete)

**C.** Children become root segments

**D.** Operation fails with an error

**Correct Answer:** B

---

### Q171. Before inserting a child segment in an IMS program, what must exist?

**Type:** Single Choice

**A.** The parent segment must already exist in the database

**B.** All sibling segments must exist

**C.** The root segment of a different hierarchy

**D.** No prerequisites are needed

**Correct Answer:** A

---

### Q172. An IMS program inserts segments in this order: ROOT, CHILDA, CHILDB. If CHILDA is under ROOT and CHILDB is under CHILDA, what is the result?

**Type:** Single Choice

**A.** All insertions succeed creating a 3-level hierarchy

**B.** CHILDB insertion fails because position is not set correctly

**C.** Only ROOT insertion succeeds

**D.** All insertions succeed but in wrong hierarchy level

**Correct Answer:** A

---

### Q173. What is a path call in IMS application programming?

**Type:** Single Choice

**A.** A call that retrieves only the root segment

**B.** A call that retrieves multiple segments in a path with a single DL/I call

**C.** A call that updates multiple segments

**D.** A call that defines the navigation path

**Correct Answer:** B

---

### Q174. When would an IMS application programmer use a path call instead of multiple GN calls?

**Type:** Single Choice

**A.** When better performance is needed by reducing DL/I call overhead

**B.** When only root segments are needed

**C.** When deleting segments

**D.** Path calls cannot be used in application programs

**Correct Answer:** A

---

### Q175. What is an IMS batch program?

**Type:** Single Choice

**A.** A program that runs online with user interaction

**B.** A program that accesses IMS databases offline without online requirements

**C.** A program that only reads data

**D.** A program that runs in the control region

**Correct Answer:** B

---

### Q176. What is a BMP (Batch Message Program) in IMS?

**Type:** Single Choice

**A.** A batch program with no message processing capability

**B.** A batch program that can also process messages

**C.** An online program only

**D.** A system utility program

**Correct Answer:** B

---

### Q177. Can IMS batch programs update the database?

**Type:** Single Choice

**A.** No, batch programs are read-only

**B.** Yes, if the PSB grants Insert, Replace, or Delete processing options

**C.** Only during offline hours

**D.** Only with special system permissions

**Correct Answer:** B

---

### Q178. What is the significance of hierarchical sequence in IMS application programming?

**Type:** Single Choice

**A.** It determines the physical storage location

**B.** It defines the order in which segments are retrieved during sequential processing

**C.** It has no significance for application programs

**D.** It only applies to batch programs

**Correct Answer:** B

---

### Q179. When an IMS application program retrieves a segment, where is the data placed?

**Type:** Single Choice

**A.** In the PCB

**B.** In the segment I/O area defined by the program

**C.** In the DBD

**D.** In the PSB

**Correct Answer:** B

---

### Q180. In IMS, what is the maximum number of segment levels in a hierarchical structure?

**Type:** Single Choice

**A.** 10

**B.** 15

**C.** 20

**D.** Unlimited

**Correct Answer:** B

---

### Q181. What is the maximum number of segment types in an IMS hierarchical structure?

**Type:** Single Choice

**A.** 127

**B.** 255

**C.** 512

**D.** 1024

**Correct Answer:** B

---

### Q182. What is the purpose of the DL/I interface in IMS application programs?

**Type:** Single Choice

**A.** To compile the program

**B.** To provide a standard interface for database access operations

**C.** To create the database

**D.** To manage system resources

**Correct Answer:** B

---

### Q183. If an IMS program issues a REPL call without first retrieving the segment, what happens?

**Type:** Single Choice

**A.** The replace succeeds on the last segment position

**B.** A status code error is returned (no current position)

**C.** A random segment is replaced

**D.** The program abends

**Correct Answer:** B

---

### Q184. Can an IMS application program access multiple databases in a single execution?

**Type:** Single Choice

**A.** No, only one database per program

**B.** Yes, if multiple PCBs are defined in the PSB

**C.** Only in batch mode

**D.** Only with special system authorization

**Correct Answer:** B

---

### Q185. What is the entry point parameter in an IMS application program?

**Type:** Single Choice

**A.** The database name

**B.** The pointer to the PCB list

**C.** The program name

**D.** The segment name

**Correct Answer:** B

---

### Q186. An IMS program retrieves a parent segment and then issues ISRT for a child. The child ISRT uses a qualified SSA. What must be ensured?

**Type:** Single Choice

**A.** The SSA qualification matches the parent key

**B.** The parent segment was the last segment retrieved (position is established)

**C.** The child key field is unique

**D.** The database must be reorganized first

**Correct Answer:** B

---

### Q187. What happens if an IMS program tries to insert a root segment with a duplicate key?

**Type:** Single Choice

**A.** The insertion succeeds with a twin created

**B.** Status code 'II' is returned indicating duplicate key

**C.** The old segment is automatically replaced

**D.** The program abends

**Correct Answer:** B

---

### Q188. What are sensitive fields in an IMS PSB?

**Type:** Single Choice

**A.** Fields that contain sensitive data like passwords

**B.** Fields that the application program can access

**C.** Fields that cannot be modified

**D.** Fields that trigger security alerts

**Correct Answer:** B

---

### Q189. If a segment has 10 fields but only 5 are defined as sensitive in the PSB, what does the IMS program see?

**Type:** Single Choice

**A.** All 10 fields

**B.** Only the 5 sensitive fields

**C.** No fields

**D.** An error is returned

**Correct Answer:** B

---

### Q190. What is the purpose of checkpoint calls in IMS batch programs?

**Type:** Single Choice

**A.** To test the database connection

**B.** To save program position for potential restart after failure

**C.** To delete all processed segments

**D.** To create backups of the database

**Correct Answer:** B

---

### Q191. After an IMS batch program restart from a checkpoint, where does execution resume?

**Type:** Single Choice

**A.** At the beginning of the program

**B.** At the last checkpoint position

**C.** At a random position

**D.** At the end of the database

**Correct Answer:** B

---

### Q192. What are command codes in IMS SSAs?

**Type:** Single Choice

**A.** Codes that identify the DL/I call type

**B.** Special processing options specified in the SSA

**C.** Error codes returned by DL/I

**D.** Database security codes

**Correct Answer:** B

---

### Q193. What does the 'F' command code do in an IMS SSA?

**Type:** Single Choice

**A.** Forces a database reorganization

**B.** Indicates this is the first segment in the path

**C.** Skips to the first occurrence of the segment

**D.** Filters out deleted segments

**Correct Answer:** B

---

### Q194. What does the 'D' command code do in an IMS SSA?

**Type:** Single Choice

**A.** Deletes the segment

**B.** Specifies this is a dependent segment

**C.** Uses a path call to retrieve this segment and all its dependents

**D.** Disables security checking

**Correct Answer:** C

---

### Q195. What is the purpose of a secondary index in IMS from an application perspective?

**Type:** Single Choice

**A.** To create backup copies of data

**B.** To provide an alternate access path to segments using non-key fields

**C.** To improve system performance only

**D.** To encrypt sensitive data

**Correct Answer:** B

---

### Q196. When an IMS application uses a secondary index, how does it affect the program's view of the hierarchy?

**Type:** Single Choice

**A.** No effect, hierarchy remains the same

**B.** The indexed segment appears as the root in the program's view

**C.** All segments become root segments

**D.** The hierarchy is inverted

**Correct Answer:** B

---

### Q197. What is a logical relationship in IMS databases?

**Type:** Single Choice

**A.** A physical link between two segments

**B.** A logical connection between segments in different physical hierarchies

**C.** A parent-child relationship

**D.** A security relationship

**Correct Answer:** B

---

### Q198. From an IMS application programmer's perspective, how are logical relationships accessed?

**Type:** Single Choice

**A.** Through special system calls

**B.** Through normal DL/I calls as if they were physical children

**C.** Through SQL queries

**D.** They cannot be accessed by application programs

**Correct Answer:** B

---

### Q199. What is database positioning in IMS application programming?

**Type:** Single Choice

**A.** The physical location of data on disk

**B.** The current location in the hierarchy after the last successful DL/I call

**C.** The beginning of the database

**D.** The end of the database

**Correct Answer:** B

---

### Q200. If an IMS program issues GU for a root, then GN for a child, and the child GN fails with status 'GE', what is the position?

**Type:** Single Choice

**A.** At the root segment

**B.** Position is undefined after an unsuccessful call

**C.** At the beginning of the database

**D.** At the end of the database

**Correct Answer:** B

---

### Q201. What is a concatenated key in IMS?

**Type:** Single Choice

**A.** Two fields joined in one segment

**B.** The combination of key fields from the root down to a specific segment

**C.** A compound primary key

**D.** Multiple segments with the same key

**Correct Answer:** B

---

### Q202. Why are concatenated keys important for IMS application programmers?

**Type:** Single Choice

**A.** They are not important

**B.** They uniquely identify a segment occurrence in the entire database

**C.** They improve system performance

**D.** They reduce storage requirements

**Correct Answer:** B

---

### Q203. How does an IMS application program commit database changes?

**Type:** Single Choice

**A.** Explicitly with a COMMIT call

**B.** Changes are committed when the program terminates normally

**C.** With a SAVE call

**D.** Changes are committed immediately after each DL/I call

**Correct Answer:** B

---

### Q204. What happens to database changes if an IMS program abnormally terminates?

**Type:** Single Choice

**A.** All changes are committed

**B.** All changes are rolled back (backed out)

**C.** Changes are partially committed

**D.** The database becomes corrupted

**Correct Answer:** B

---

### Q205. In an IMS qualified SSA, what character is used to enclose the qualification statement?

**Type:** Single Choice

**A.** Square brackets []

**B.** Parentheses ()

**C.** Curly braces {}

**D.** Angle brackets <>

**Correct Answer:** B

---

### Q206. An IMS program needs to find CUSTOMER where CITY='NEW YORK' and STATE='NY'. How should the SSA be constructed?

**Type:** Single Choice

**A.** CUSTOMER(CITY='NEW YORK'&STATE='NY')

**B.** CUSTOMER(CITY='NEW YORK',STATE='NY')

**C.** Two separate SSAs are required

**D.** This cannot be done in one SSA

**Correct Answer:** A

---

### Q207. What character is used in IMS SSA to specify AND logic between multiple conditions?

**Type:** Single Choice

**A.** & (ampersand)

**B.** + (plus)

**C.** * (asterisk)

**D.** , (comma)

**Correct Answer:** A

---

### Q208. What character is used in IMS SSA to specify OR logic between multiple conditions?

**Type:** Single Choice

**A.** & (ampersand)

**B.** + (plus)

**C.** | (pipe)

**D.** , (comma)

**Correct Answer:** C

---

### Q209. In an IMS unqualified SSA, what information is specified?

**Type:** Single Choice

**A.** Only the segment name

**B.** Segment name and field values

**C.** Only field conditions

**D.** Database name and segment name

**Correct Answer:** A

---

### Q210. An IMS program issues GU for ROOT, then GNP for CHILD. If no CHILD exists, what status code is returned?

**Type:** Single Choice

**A.** GE (segment not found)

**B.** GB (end of database record)

**C.** GK (wrong segment type)

**D.** II (duplicate insert)

**Correct Answer:** A

---

### Q211. What is the function parameter for a GU call in CBLTDLI?

**Type:** Single Choice

**A.** 'GU' (with quotes)

**B.** GU (without quotes)

**C.** 'GU  ' (4-character field)

**D.** 1 (numeric code)

**Correct Answer:** C

---

### Q212. How many SSAs can be specified in a single DL/I call?

**Type:** Single Choice

**A.** Only one

**B.** Up to 15 (matching the maximum hierarchy depth)

**C.** Exactly two

**D.** Unlimited

**Correct Answer:** B

---

### Q213. In an IMS GU call with multiple SSAs, what does each SSA represent?

**Type:** Single Choice

**A.** Different databases

**B.** Different programs

**C.** A level in the hierarchical path to the target segment

**D.** Alternative search criteria

**Correct Answer:** C

---

### Q214. Which DL/I call would an IMS program use to retrieve the first CUSTOMER segment?

**Type:** Single Choice

**A.** GN

**B.** GU

**C.** GNP

**D.** ISRT

**Correct Answer:** B

---

### Q215. After successfully retrieving a segment with GU, which call retrieves the next segment in sequence?

**Type:** Single Choice

**A.** Another GU

**B.** GN

**C.** GNP

**D.** REPL

**Correct Answer:** B

---

### Q216. An IMS program processes orders: GU for CUSTOMER, then loop GNP for ORDER segments. What happens when no more ORDERs exist for that CUSTOMER?

**Type:** Single Choice

**A.** Status code 'GE' is returned

**B.** Status code 'GB' is returned

**C.** The program abends

**D.** The next CUSTOMER's orders are returned

**Correct Answer:** A

---

### Q217. Can an IMS application program issue multiple GU calls in succession?

**Type:** Single Choice

**A.** No, only one GU per program execution

**B.** Yes, GU can be issued multiple times

**C.** Only in batch programs

**D.** Only for root segments

**Correct Answer:** B

---

### Q218. In an IMS hierarchy, what is the relationship between a segment and the segment directly above it?

**Type:** Single Choice

**A.** Sibling relationship

**B.** Parent-child relationship

**C.** Twin relationship

**D.** Peer relationship

**Correct Answer:** B

---

### Q219. What are segments at the same level under the same parent called in IMS?

**Type:** Single Choice

**A.** Twins

**B.** Siblings

**C.** Peers

**D.** Cousins

**Correct Answer:** B

---

### Q220. In an IMS database with a root segment PATIENT, can there be multiple PATIENT occurrences?

**Type:** Single Choice

**A.** No, only one root allowed

**B.** Yes, there can be multiple root segment occurrences (database records)

**C.** Only if they have different keys

**D.** Only in batch mode

**Correct Answer:** B

---

### Q221. If an IMS hierarchy has segments A(root), B(child of A), C(child of B), what is C's relationship to A?

**Type:** Single Choice

**A.** Direct child

**B.** Grandchild (descendant)

**C.** Twin

**D.** No relationship

**Correct Answer:** B

---

### Q222. Can an IMS segment have more than one parent?

**Type:** Single Choice

**A.** Yes, segments can have multiple parents

**B.** No, each segment has only one physical parent

**C.** Only root segments can have multiple parents

**D.** Only with special configuration

**Correct Answer:** B

---

### Q223. What determines the hierarchical structure shown to an IMS application program?

**Type:** Single Choice

**A.** The physical storage method

**B.** The PSB definition (which segments are sensitive)

**C.** The program logic

**D.** The operating system

**Correct Answer:** B

---

### Q224. What is the typical size limit for an IMS segment?

**Type:** Single Choice

**A.** No limit

**B.** Maximum of several thousand bytes

**C.** Exactly 256 bytes

**D.** Maximum of 80 bytes

**Correct Answer:** B

---

### Q225. Can an IMS segment contain repeating groups of fields?

**Type:** Single Choice

**A.** No, fields cannot repeat within a segment

**B.** Yes, segments can contain repeating field groups

**C.** Only in root segments

**D.** Only with special database options

**Correct Answer:** B

---

### Q226. In IMS, what is a segment occurrence?

**Type:** Single Choice

**A.** A segment type definition

**B.** One specific instance of a segment type with actual data

**C.** A segment that occurs only once

**D.** A deleted segment

**Correct Answer:** B

---

### Q227. Can different segment types in an IMS hierarchy have different lengths?

**Type:** Single Choice

**A.** No, all segments must be the same length

**B.** Yes, each segment type can have its own length

**C.** Only if they are at the same level

**D.** Only root segments can have different lengths

**Correct Answer:** B

---

### Q228. After each DL/I call, what should an IMS application program check first?

**Type:** Single Choice

**A.** The segment data

**B.** The status code in the PCB

**C.** The database name

**D.** The PSB name

**Correct Answer:** B

---

### Q229. What status code indicates that an IMS program tried to access a segment not defined in its PSB?

**Type:** Single Choice

**A.** GE

**B.** GK

**C.** GA

**D.** AM

**Correct Answer:** B

---

### Q230. What information is available in the PCB after a successful GU call?

**Type:** Single Choice

**A.** Only the status code

**B.** Status code, segment level, and key feedback area

**C.** Only the segment name

**D.** Only the database name

**Correct Answer:** B

---

### Q231. Where is the key feedback area located in IMS?

**Type:** Single Choice

**A.** In the segment I/O area

**B.** In the PCB

**C.** In the DBD

**D.** In the PSB

**Correct Answer:** B

---

### Q232. What is stored in the key feedback area after a successful retrieve call?

**Type:** Single Choice

**A.** The entire segment

**B.** The concatenated key of the retrieved segment

**C.** Only the root key

**D.** The status code

**Correct Answer:** B

---

### Q233. When inserting a new root segment, what must an IMS program provide?

**Type:** Single Choice

**A.** Parent segment key

**B.** The complete segment data in the I/O area

**C.** Previous root segment reference

**D.** Database password

**Correct Answer:** B

---

### Q234. To insert a new child segment, an IMS program must first establish position at which level?

**Type:** Single Choice

**A.** At the root segment

**B.** At the immediate parent of the segment to be inserted

**C.** At any segment in the hierarchy

**D.** Position is not required for insert

**Correct Answer:** B

---

### Q235. If multiple twin segments exist, where is a new twin inserted when ISRT is issued?

**Type:** Single Choice

**A.** At the beginning of the twin chain

**B.** In sequence based on the key field value

**C.** At the end of the twin chain

**D.** At a random position

**Correct Answer:** B

---

### Q236. Can an IMS program insert a segment without a key field?

**Type:** Single Choice

**A.** No, all segments must have keys

**B.** Yes, if the segment type is defined without a key in the DBD

**C.** Only root segments require keys

**D.** Only for batch programs

**Correct Answer:** B

---

### Q237. Before issuing a DLET call, what must an IMS program do?

**Type:** Single Choice

**A.** Issue a checkpoint

**B.** Successfully retrieve the segment to be deleted

**C.** Retrieve all child segments

**D.** Issue a REPL call first

**Correct Answer:** B

---

### Q238. An IMS program has a hierarchy: ROOT-CHILD1-CHILD2. If it deletes CHILD1, what happens to CHILD2?

**Type:** Single Choice

**A.** CHILD2 remains and becomes a child of ROOT

**B.** CHILD2 is also deleted (cascade delete)

**C.** The delete fails

**D.** CHILD2 becomes an orphan segment

**Correct Answer:** B

---

### Q239. Can an IMS program delete the root segment?

**Type:** Single Choice

**A.** No, root segments cannot be deleted

**B.** Yes, if the program has delete authority in its PSB

**C.** Only by system programmers

**D.** Only in batch mode

**Correct Answer:** B

---

### Q240. Can an IMS program use REPL to change a segment's key field?

**Type:** Single Choice

**A.** Yes, any field can be changed including the key

**B.** No, key fields cannot be changed with REPL

**C.** Only in root segments

**D.** Only if the key is not unique

**Correct Answer:** B

---

### Q241. To change a segment's key field, what should an IMS application program do?

**Type:** Single Choice

**A.** Use REPL with a special flag

**B.** Delete the segment and insert a new one with the new key

**C.** Use a special UPDKEY call

**D.** Key fields can never be changed

**Correct Answer:** B

---

### Q242. After a REPL call, what is the database position?

**Type:** Single Choice

**A.** At the root segment

**B.** At the replaced segment

**C.** Position is lost

**D.** At the next segment

**Correct Answer:** B

---

### Q243. What is sequential processing in an IMS application program?

**Type:** Single Choice

**A.** Processing segments in physical storage order

**B.** Processing segments one after another in hierarchical sequence

**C.** Processing segments in reverse order

**D.** Processing only root segments

**Correct Answer:** B

---

### Q244. What is direct access processing in IMS?

**Type:** Single Choice

**A.** Accessing segments without using DL/I

**B.** Accessing a specific segment directly using qualified SSAs

**C.** Accessing only root segments

**D.** Accessing segments in random order

**Correct Answer:** B

---

### Q245. An IMS program processes all segments sequentially using GN. How does it know when to stop?

**Type:** Single Choice

**A.** When the program counter reaches maximum

**B.** When status code 'GB' or 'GE' is returned

**C.** When 1000 segments are processed

**D.** The program must manually count segments

**Correct Answer:** B

---

### Q246. In a COBOL IMS program, what is CBLTDLI?

**Type:** Single Choice

**A.** The segment name

**B.** The DL/I interface module name for COBOL programs

**C.** A status code

**D.** A database name

**Correct Answer:** B

---

### Q247. In a COBOL IMS program, what length should the function parameter be?

**Type:** Single Choice

**A.** 2 characters

**B.** 4 characters

**C.** 8 characters

**D.** Variable length

**Correct Answer:** B

---

### Q248. In a COBOL IMS program, which data division section contains the PCB mask?

**Type:** Single Choice

**A.** WORKING-STORAGE SECTION

**B.** LINKAGE SECTION

**C.** FILE SECTION

**D.** LOCAL-STORAGE SECTION

**Correct Answer:** B

---

### Q249. In a COBOL IMS program, how is the entry parm (PCB list address) received?

**Type:** Single Choice

**A.** Through ACCEPT statement

**B.** Through the ENTRY statement parameter or PROCEDURE DIVISION USING

**C.** Through an environment variable

**D.** Through a file

**Correct Answer:** B

---

### Q250. What does DL/I stand for in IMS?

**Type:** Single Choice

**A.** Data Language Interface

**B.** Data Language/I (Input)

**C.** Database Language Interface

**D.** Data Link Interface

**Correct Answer:** B

---

### Q251. Can an IMS application program mix database and message processing?

**Type:** Single Choice

**A.** No, they must be separate programs

**B.** Yes, IMS programs can use both database and message PCBs

**C.** Only in batch programs

**D.** Only in online programs

**Correct Answer:** B

---

### Q252. If an IMS PSB has multiple database PCBs, how does the program access a specific database?

**Type:** Single Choice

**A.** By specifying the database name in each call

**B.** By using the appropriate PCB pointer/reference in the DL/I call

**C.** By issuing a SELECT DATABASE call first

**D.** All databases are accessed simultaneously

**Correct Answer:** B

---

### Q253. What is the I/O area in an IMS application program?

**Type:** Single Choice

**A.** A file buffer

**B.** The memory area where segment data is passed between program and DL/I

**C.** The PCB

**D.** The SSA

**Correct Answer:** B

---

### Q254. Must the I/O area in an IMS program match the segment length exactly?

**Type:** Single Choice

**A.** Yes, it must match exactly

**B.** No, it can be larger (only needed data is moved)

**C.** It can only be larger, never smaller

**D.** It must be exactly 256 bytes

**Correct Answer:** B

---

### Q255. In IMS, can a child segment exist without its parent?

**Type:** Single Choice

**A.** Yes, child segments are independent

**B.** No, a parent must exist before its children can be inserted

**C.** Only for root children

**D.** Only in batch mode

**Correct Answer:** B

---

### Q256. After retrieving segment A at level 2, an IMS program issues GN. Which segment is retrieved next?

**Type:** Single Choice

**A.** The next twin of A

**B.** The first child of A if it exists, otherwise the next segment in hierarchical sequence

**C.** The parent of A

**D.** The root segment

**Correct Answer:** B

---

### Q257. Can an IMS program issue DL/I calls against multiple databases in one execution?

**Type:** Single Choice

**A.** No, only one database per execution

**B.** Yes, if the PSB includes PCBs for multiple databases

**C.** Only if databases are in the same DBDGEN

**D.** Only in online mode

**Correct Answer:** B

---

### Q258. If a PCB has processing option 'G' only, which DL/I calls can the program use?

**Type:** Single Choice

**A.** All DL/I calls

**B.** Only GU, GN, and GNP (retrieval calls)

**C.** Only ISRT and DLET

**D.** Only REPL

**Correct Answer:** B

---

### Q259. What should an IMS application program do when it receives an unexpected status code?

**Type:** Single Choice

**A.** Ignore it and continue

**B.** Check the status code and handle the error appropriately

**C.** Always abend the program

**D.** Retry the call indefinitely

**Correct Answer:** B

---

### Q260. An IMS program needs to find an ORDER with ORDERNO=5000. If ORDERs are sequenced by ORDERNO, which is more efficient?

**Type:** Single Choice

**A.** GN calls until ORDERNO=5000 is found

**B.** GU with qualified SSA: ORDER(ORDERNO=5000)

**C.** Both are equally efficient

**D.** Sequential scan is always faster

**Correct Answer:** B

---

### Q261. In an IMS batch program, when are database updates physically written?

**Type:** Single Choice

**A.** Immediately after each DL/I call

**B.** At commit points (checkpoint or program termination)

**C.** Every 100 calls

**D.** Only when the database is closed

**Correct Answer:** B

---

### Q262. Who defines the length of an IMS segment?

**Type:** Single Choice

**A.** The application programmer in the program

**B.** The DBA in the DBD (Database Description)

**C.** It is always 256 bytes

**D.** The operating system

**Correct Answer:** B

---

### Q263. Can IMS segment fields contain different data types (numeric, character, etc.)?

**Type:** Single Choice

**A.** No, all fields must be character

**B.** Yes, fields can be various types (character, packed, binary, etc.)

**C.** Only numeric types

**D.** Only character types

**Correct Answer:** B

---

### Q264. How does an IMS application program specify which PSB to use?

**Type:** Single Choice

**A.** In the program code

**B.** Through JCL or scheduling parameters when the program is executed

**C.** It is hardcoded in the DBD

**D.** Through a configuration file

**Correct Answer:** B

---

### Q265. An IMS program needs to retrieve all segments in the database. Which approach is appropriate?

**Type:** Single Choice

**A.** Issue GU for first root, then GN calls until status GE

**B.** Multiple GU calls for each root

**C.** GNP calls only

**D.** ISRT calls

**Correct Answer:** A

---

### Q266. An IMS hierarchy has ROOT-LEVEL1-LEVEL2-LEVEL3. To retrieve a LEVEL3 segment directly, how many SSAs are needed in the GU call?

**Type:** Single Choice

**A.** One SSA for LEVEL3 only

**B.** Four SSAs (ROOT, LEVEL1, LEVEL2, LEVEL3)

**C.** Three SSAs (LEVEL1, LEVEL2, LEVEL3)

**D.** Two SSAs (ROOT and LEVEL3)

**Correct Answer:** B

---

### Q267. To update a segment field value, which sequence of DL/I calls should an IMS program use?

**Type:** Single Choice

**A.** ISRT the segment with new data

**B.** GU/GN to retrieve, modify in I/O area, then REPL

**C.** DLET then ISRT

**D.** Direct memory update

**Correct Answer:** B

---

### Q268. An IMS program retrieves a segment, modifies data in the I/O area, but doesn't issue REPL. What happens?

**Type:** Single Choice

**A.** Changes are automatically saved

**B.** No changes are made to the database

**C.** The segment is deleted

**D.** A status code error occurs

**Correct Answer:** B

---

### Q269. In what order must segments be inserted in IMS when building a new database record?

**Type:** Single Choice

**A.** Any order is acceptable

**B.** In hierarchical order (parent before children)

**C.** Bottom-up (children before parents)

**D.** Alphabetical order

**Correct Answer:** B

---

### Q270. Can an IMS program insert multiple root segments in one execution?

**Type:** Single Choice

**A.** No, only one root per execution

**B.** Yes, multiple root segments (database records) can be inserted

**C.** Only in batch mode

**D.** Only with special authorization

**Correct Answer:** B

---

### Q271. What type of SSA should be used to retrieve a specific segment by key value?

**Type:** Single Choice

**A.** Unqualified SSA

**B.** Qualified SSA with key field condition

**C.** No SSA needed

**D.** Command code SSA

**Correct Answer:** B

---

### Q272. An IMS program uses GU with SSA: ORDER(ORDERNO>1000). Which ORDER is retrieved?

**Type:** Single Choice

**A.** The first ORDER with ORDERNO>1000 in hierarchical sequence

**B.** All ORDERs with ORDERNO>1000

**C.** The last ORDER with ORDERNO>1000

**D.** A random ORDER with ORDERNO>1000

**Correct Answer:** A

---

### Q273. Can an IMS program mix retrieval and update operations in the same execution?

**Type:** Single Choice

**A.** No, separate executions required

**B.** Yes, programs can issue both retrieval (GU/GN) and update (ISRT/REPL/DLET) calls

**C.** Only in batch programs

**D.** Only with multiple PCBs

**Correct Answer:** B

---

### Q274. Does an IMS application program directly manage file I/O and storage?

**Type:** Single Choice

**A.** Yes, programs must manage physical storage

**B.** No, DL/I and IMS Database Manager handle physical storage

**C.** Only for batch programs

**D.** Only for root segments

**Correct Answer:** B

---

### Q275. Must an IMS application program open and close the database?

**Type:** Single Choice

**A.** Yes, like regular files

**B.** No, IMS handles database open/close automatically

**C.** Only batch programs must do this

**D.** Only for multiple databases

**Correct Answer:** B

---

### Q276. How does an IMS application program know which database it's accessing?

**Type:** Single Choice

**A.** From the JCL DD statements

**B.** From the PCB which identifies the database

**C.** From environment variables

**D.** From the program name

**Correct Answer:** B

---

### Q277. When a DL/I call fails, what information is available to help diagnose the problem?

**Type:** Single Choice

**A.** Only the status code

**B.** Status code, segment level, and sometimes key feedback area

**C.** An error message is displayed

**D.** Nothing, the program just abends

**Correct Answer:** B

---

### Q278. What should an IMS program do after a failed DL/I call (status not spaces)?

**Type:** Single Choice

**A.** Continue with the next call

**B.** Check the status code and handle the error condition

**C.** Abend immediately

**D.** Retry the same call indefinitely

**Correct Answer:** B

---

### Q279. Can an IMS program access a grandchild segment directly without retrieving intervening levels?

**Type:** Single Choice

**A.** No, must retrieve each level sequentially

**B.** Yes, by specifying SSAs for each level in the path including unqualified SSAs for intermediate levels

**C.** Only in batch mode

**D.** Never allowed

**Correct Answer:** B

---

### Q280. An IMS program needs a specific LEVEL3 segment but doesn't know the parent keys. What approach is needed?

**Type:** Single Choice

**A.** Cannot be done

**B.** Use qualified SSA for LEVEL3 with unqualified SSAs for parent levels

**C.** Use GN calls only

**D.** Use secondary index or sequential scan

**Correct Answer:** D

---

### Q281. If an IMS PSB has 3 database PCBs, how does the program distinguish between them?

**Type:** Single Choice

**A.** By database name in the DL/I call

**B.** By using the appropriate PCB pointer (PCB1, PCB2, PCB3)

**C.** By issuing a SELECT call first

**D.** All PCBs are accessed simultaneously

**Correct Answer:** B

---

### Q282. In an IMS batch program, what defines a transaction boundary (commit point)?

**Type:** Single Choice

**A.** Every 100 DL/I calls

**B.** Checkpoint calls or program termination

**C.** Every GU call

**D.** Every 10 seconds

**Correct Answer:** B

---

### Q283. In a COBOL IMS program, how are segment fields typically defined?

**Type:** Single Choice

**A.** As individual variables

**B.** As a group item in WORKING-STORAGE matching the segment layout

**C.** In the FILE SECTION

**D.** As SQL columns

**Correct Answer:** B

---

### Q284. After a successful retrieve call, how does the program access individual fields?

**Type:** Single Choice

**A.** Through SQL syntax

**B.** By referencing field names in the I/O area structure

**C.** Through pointer arithmetic

**D.** Fields are not accessible

**Correct Answer:** B

---

### Q285. An IMS program processes CUSTOMERs where BALANCE>1000. After retrieving one, how to get the next matching CUSTOMER?

**Type:** Single Choice

**A.** GU with the same qualified SSA

**B.** GN with qualified SSA: CUSTOMER(BALANCE>1000)

**C.** GNP with the same SSA

**D.** Must use sequential scan and test each

**Correct Answer:** B

---

### Q286. Before inserting ORDER segments under a CUSTOMER, what must an IMS program ensure?

**Type:** Single Choice

**A.** The database is empty

**B.** The CUSTOMER segment is the last segment retrieved (parentage established)

**C.** All other ORDERs are deleted

**D.** The program has read authority

**Correct Answer:** B

---

### Q287. Can an IMS program insert multiple child segments under one parent in a single execution?

**Type:** Single Choice

**A.** No, only one child per execution

**B.** Yes, after positioning at the parent, multiple ISRTs can be issued

**C.** Only with special calls

**D.** Only in batch mode

**Correct Answer:** B

---

### Q288. How does an IMS hierarchical segment compare to a relational table row?

**Type:** Single Choice

**A.** They are identical concepts

**B.** A segment is like a row, but exists within a hierarchy not a flat table

**C.** Segments are larger than rows

**D.** No comparison is possible

**Correct Answer:** B

---

### Q289. In a qualified SSA, how are character field values specified?

**Type:** Single Choice

**A.** Without quotes: CUSTNAME=SMITH

**B.** With single quotes: CUSTNAME='SMITH'

**C.** With double quotes: CUSTNAME="SMITH"

**D.** With backticks: CUSTNAME=`SMITH`

**Correct Answer:** B

---

### Q290. How many root segments can exist in one IMS database record?

**Type:** Single Choice

**A.** Exactly one per database record

**B.** Multiple roots per database record

**C.** No root needed

**D.** Depends on the DBD

**Correct Answer:** A

---

### Q291. Is there a limit on the number of child segments under one parent in IMS?

**Type:** Single Choice

**A.** Yes, maximum of 15

**B.** No limit except physical constraints

**C.** Yes, maximum of 255

**D.** Yes, maximum of 100

**Correct Answer:** B

---

### Q292. Is the DL/I interface specific to COBOL or available for other languages?

**Type:** Single Choice

**A.** Only for COBOL

**B.** Available for COBOL, PL/I, C, C++, Java, Assembler

**C.** Only for COBOL and Assembler

**D.** Only for Java

**Correct Answer:** B

---

### Q293. Is it mandatory to check the status code after every DL/I call?

**Type:** Single Choice

**A.** No, status check is optional

**B.** Yes, status should always be checked to ensure call success

**C.** Only for ISRT calls

**D.** Only for DLET calls

**Correct Answer:** B

---

### Q294. When should an IMS program use unqualified SSAs?

**Type:** Single Choice

**A.** Never, always use qualified

**B.** When retrieving segments in sequence without specific field criteria

**C.** Only for root segments

**D.** Only for batch programs

**Correct Answer:** B

---

### Q295. For an IMS application, which is generally more efficient for finding a specific segment?

**Type:** Single Choice

**A.** Sequential scan with GN calls

**B.** Direct access with GU and qualified SSA

**C.** Both are equally efficient

**D.** Depends only on database size

**Correct Answer:** B

---

### Q296. Can an IMS program retrieve a segment without modifying it?

**Type:** Single Choice

**A.** No, all retrieves require updates

**B.** Yes, GU and GN calls retrieve without modifying

**C.** Only with special PCB options

**D.** Only for root segments

**Correct Answer:** B

---

### Q297. After deleting a segment with DLET, what is the database position?

**Type:** Single Choice

**A.** At the deleted segment location

**B.** Position is undefined/lost after DLET

**C.** At the next segment

**D.** At the parent segment

**Correct Answer:** B

---

### Q298. An IMS program needs to insert a 3-level structure: ROOT, CHILD, GRANDCHILD. What is the minimum number of ISRT calls?

**Type:** Single Choice

**A.** One call can insert all levels

**B.** Three separate ISRT calls required

**C.** Two calls minimum

**D.** Depends on the database options

**Correct Answer:** B

---

### Q299. In a hierarchy with ROOT, CHILD-A, CHILD-B (both under ROOT), GRANDCHILD (under CHILD-A), what is the hierarchical sequence?

**Type:** Single Choice

**A.** ROOT, CHILD-A, CHILD-B, GRANDCHILD

**B.** ROOT, CHILD-A, GRANDCHILD, CHILD-B

**C.** ROOT, GRANDCHILD, CHILD-A, CHILD-B

**D.** ROOT, CHILD-B, CHILD-A, GRANDCHILD

**Correct Answer:** B

---

### Q300. How does an IMS program process all twin segments under a parent?

**Type:** Single Choice

**A.** One GU call retrieves all twins

**B.** Loop with GNP calls until status code GE

**C.** Twins are processed automatically

**D.** Use a special TWIN call

**Correct Answer:** B

---

