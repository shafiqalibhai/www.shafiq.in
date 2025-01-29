---
title: Online Temperature Monitoring System
author: Shafiq Alibhai
date: 2013-06-07T09:52:57+00:00
categories:
  - Development

---
# Download : [PROJ\_FORMAT\_][1]

1. Introduction

2. Working environment

2.1 Hardware Requirement Specification

i. Microcontroller AT89c52  
ii. ADC ADC0808  
iii. <a class="zem_slink" title="Real-time clock" href="http://en.wikipedia.org/wiki/Real-time_clock" target="_blank" rel="wikipedia">Real Time Clock</a> DS1307  
iv. Serial EEPROM AT24c08  
v. Serial Transceiver MAX232  
vi. LCD 16&#215;2

2.2 <a class="zem_slink" title="Requirement" href="http://en.wikipedia.org/wiki/Requirement" target="_blank" rel="wikipedia">Software Requirement</a> Specification

i. Programming Language ANSI C  
ii. Compiler KEIL

2.3 About the Hardware

2.3.1 Microcontroller (89C52)  
Key Features  
 Compatible with MCS-51™ Products  
 8K Bytes of In-System Reprogrammable <a class="zem_slink" title="Flash memory" href="http://en.wikipedia.org/wiki/Flash_memory" target="_blank" rel="wikipedia">Flash Memory</a>  
 Endurance: 1,000 Write/Erase Cycles  
 256 x 8-bit Internal RAM  
 32 Programmable I/O Lines  
 Three 16-bit Timer/Counters  
 Eight Interrupt Sources  
 Programmable Serial Channel

Description  
The AT89C52 is a low-power, high-performance CMOS 8-bit microcomputer with 8K bytes of Flash programmable and erasable read only memory (PEROM). The device is manufactured using <a class="zem_slink" title="NASDAQ: ATML" href="http://www.google.com/finance?q=NASDAQ:ATML" target="_blank" rel="googlefinance">Atmel</a>'s high-density nonvolatile memory technology. The on-chip Flash allows the program memory to be reprogrammed in-system or by a conventional nonvolatile memory programmer. By combining a versatile 8-bit CPU with Flash on a monolithic chip, the Atmel AT89C52 is a powerful microcomputer which provides a highly-flexible and cost-effective solution to many embedded control applications.

Pin Configurations

Pin Description  
• RST  
Reset input. A high on this pin for two machine cycles while the oscillator is running resets the device.  
• ALE/PROG  
Address Latch Enable is an output pulse for latching the low byte of the address during accesses to external memory. This pin is also the program pulse input (PROG) during <a class="zem_slink" title="Adobe Flash" href="http://www.adobe.com/flashplatform/" target="_blank" rel="homepage">Flash programming</a>.  
• PSEN  
Program Store Enable is the read strobe to external program memory. When the AT89C52 is executing code from external program memory, PSEN is activated twice each machine cycle, except that two PSEN activations are skipped during each access to external data memory.  
• EA/VPP  
External Access Enable. EA must be strapped to GND in order to enable the device to fetch code from external program memory locations starting at 0000H up to FFFFH.

Programming the Flash

To program the 89c52, take the following steps.  

1. Input the desired memory location on the address lines.  
2. Input the appropriate data on the data lines  
3. Activate the correct combination of control signals  
4. Raise EA/Vpp  
5. Pulse ALE/PROG once to program a byte in the Flash array or lock bits. The byte-write cycle is self-timed and typically takes no more than 1.5 ms. Repeat steps 1 through 5, changing the address and data for the entire array or until the end of the object file is reached.

2.3.2 ADC 0808  
Key Features:

2.3.3 Real time Clock (DS1307)  
Features  
 Real-time clock (RTC) counts seconds, minutes, hours, date of the month, month, day of the week, and year with leap-year compensation valid up to 2100  
 56-byte, battery-backed, nonvolatile (NV) RAM for data storage  
 <a class="zem_slink" title="I²C" href="http://en.wikipedia.org/wiki/I%C2%B2C" target="_blank" rel="wikipedia">Two-wire serial interface</a>  
 Automatic power-fail detects and switches circuitry

Pin Configurations

Pin Description  
 SCL (Serial Clock Input) –SCL is used to synchronize data movement on the serial interface.  
 SDA (Serial Data Input/Output) – SDA is the input/output pin for the 2-wire serial interface.  
 SQW/OUT (Square Wave/Output Driver) – When enabled, the SQWE bit set to 1, the SQW/OUT pin outputs one of four square wave frequencies (1Hz, 4kHz, 8kHz, 32kHz).  
 X1, X2 – Connections for a standard 32.768kHz quartz crystal. The internal oscillator circuitry is designed for operation with a crystal having a specified load capacitance (CL) of 12.5pF.

Description  
The DS1307 Serial Real-Time Clock is a low-power; full binary-coded decimal (BCD) clock/calendar plus 56 bytes of NV SRAM. Address and data are transferred serially via a 2-wire, bi-directional bus. The clock/calendar provides seconds, minutes, hours, day, date, month, and year information. The end of the month date is automatically adjusted for months with fewer than 31 days, including corrections for leap year. The clock operates in either the 24-hour or 12-hour format with AM/PM indicator. The DS1307 has a built-in power sense circuit that detects power failures and automatically switches to the battery supply.

Operation  
The DS1307 operates as a slave device on the serial bus. Access is obtained by implementing a START condition and providing a device identification code followed by a register address. Subsequent registers can be accessed sequentially until a STOP condition is executed. When VCC falls below 1.25 x VBAT the device terminates an access in progress and resets the device address counter. Inputs to the device will not be recognized at this time to prevent erroneous data from being written to the device from an out of tolerance system. When VCC falls below VBAT the device switches into a low-current battery backup mode. Upon power-up, the device switches from battery to VCC when VCC is greater than VBAT + 0.2V and recognizes inputs when VCC is greater than 1.25 x VBAT.

2.3.4 Serial Transceiver (MAX232)

Features  
 High data rate - 250 <a class="zem_slink" title="Data rate units" href="http://en.wikipedia.org/wiki/Data_rate_units" target="_blank" rel="wikipedia">kbits/sec</a> under load  
 Operate from single +5V power  
 Uses small capacitors: 0.1 µF

Pin Configurations

Description

The DS232A is a dual RS-232 driver/receiver pair that generates RS-232 voltage levels from a single +5- volt power supply. Additional ±12-volt supplies are not needed since the DS232A uses on-board charge pumps to convert the +5-volt supply to ±10 volts. Driver slew rates and data rates are guaranteed up to 250k bits/sec. The DS232A operates with only 0.1 µF charge pump capacitors.

2.3.4 Serial EEPROM  
Features  
 Internally Organized 1024 x 8 (8K) memory  
 2-wire Serial Interface  
 Bi-directional Data Transfer Protocol  
 Write Protect Pin for Hardware Data Protection  
 8-byte Page (1K, 2K), 16-byte Page (4K, 8K, 16K) Write modes  
 Partial Page Writes are allowed

Pin Configurations

Description  
The AT24C08 provides 8192 bits of serial electrically erasable and programmable read-only memory (EEPROM) organized as 1024 words of 8 bits each. The device is optimized for use in many industrial and commercial applications where low-power and low-voltage operation are essential. The AT24C08 is accessed via a 2-wire serial interface.

2.3.5. Liquid Crystal Display  
Online Temperature Monitoring system uses the Liquid crystal display as the system end display, with the display of 16 x 2. It has the display capability of 16 characters of ASCII data with 2 lines, total of 32 characters  
2.4 About the Software

2.4.1 Programming Language (ANSI C)  
The software for the project was written in the "C" higher level language, using KEIL compiler.  
Why "C"  
C has become the language of choice for the embedded programmers, because it has the benefit of processor independence. This processor independence allows the programmer to concentrate on algorithms and applications rather than on the details of the processor architecture. However many of its features apply equally to other high level languages as well. Perhaps the strength of the C is that it gives embedded programmers an extraordinary degree of direct hardware control with-out scarifying the benefits of high level languages.  
Compilers and cross-compilers are available for almost every processor with C. Any source code with in C or C++ or Assembly language must be converted it to an executable image that can be loaded into a ROM chip  
2.4.2 KEILCompiler  
Raisonance Integrated Development Environment  
About the KEIL Development Kits  
The Raisonance 8051, XA and ST6 Development Kits are a complete solution to creating software for the 8051 family, XA family and ST6 family of microcontrollers. The Development Kits comprise many different tools that allow projects ranging from simple to highly complex to be developed with relative ease. KEIL has been developing embedded tools since 1988 and has built up many years of experience.  
Development Tools  
• ANSI C Compiler  
The C Compiler is an ANSI compliant compiler that takes source files and generates object files. Extensions to the C language are used to enable features of the microcontroller to be used or controlled.  
• Assembler  
The Assembler takes source files written in assembler and generates object files.  
• Linker/Locator  
The Linker combines the object files generated by the Compiler and Linker and produces a different kind of object file. The Linker also decides where certain types of Data and Code are located in memory.  
• Object-to-HEX Converter  
The converter converts an object file generated by the linker and generates an Intel Hex file, compatible with most device programmers.  
• KEIL  
The KEIL Integrated Development Environment. KEIL is a Windows program that allows the user to create projects, easily call the Compiler, Assembler and Linker to build the project and either simulate or debug the project.  
• Library Manager  
The Library Manager can take object files generated by the Compiler or Assembler and create a library that is included in other projects.  
• Monitor  
The Monitor is a program that runs on hardware and transmits debugging information back to KEIL as the program executes. It also provides a means of controlling the execution of the program and debugging the program while it is executing on hardware  
Development Steps

1. RIDE provides an editor which allows the user to generate C source files (.c extension) and Assembler source files (.a51 extension for 8051, .axa extension for XA and .st6 extension for ST6).

2. Each source file is translated using the appropriate tool. The Compiler translates C source files. The Assembler translates assembler source files. Each tool generates a re-locatable object file (.obj extension). If a project has more than one C source file or more than one Assembler source file, then the Compiler and Assembler are executed as many times as required.

3. If a library file is being generated then the Library Manager takes all the re-locatable object files and combines them into a library file (.lib extension). The library file may then be linked in with other projects.

4. The Linker/Locator takes relocatable object files and library files and links them together resolving external references. The Linker/Locator then locates variables and code to specific addresses in the memory map. The Linker/Locator generates a single Absolute Object File (.aof extension). It also generates the same file with no extension.

5. The Absolute Object File may then be used by the simulator or debugger in KEIL, as the file can contain debugging information. Alternatively the Absolute Object File may be used with In-Circuit Emulators.

6. The Object-HEX Converter tool converts an Absolute Object File into an Intel HEX file (.hex extension) which is a representation of the pure binary code generated, without debugging information. The Intel HEX File is accepted by virtually all device programmers. In addition to being an editor, simulator and debugger, KEIL also controls and automates the entire build process. By selecting a single menu item, KEIL will execute the correct tools to generate either a library file or an Absolute Object File and Intel HEX File.

Minimum System Requirements

• Windows 9x/NT/2000  
• Pentium Processor  
• 20Mb Hard disk Space  
• 32 Mb RAM

2.4.3 Front End Tool  
2.4.4 Platform

3. Hardware Design & Description

Fig. 1 Block Diagram of the Online Temperature Monitoring system

System Description

. This I2C provides the reliable and faster communication between the master (Microcontroller) device and the other slave (Real Time Clock, Serial EEPROM) devices.

4. System analysis

The system analysis task consists of two sub-tasks.  
They are  

1. Data flow diagram  
2. Control flow diagram

1. Data flow diagram

A data flow diagram is a graphical representation that depicts information flow and the transforms that are applied as data move from input to output. The DFD may used to represent a system or software at any level of abstraction.

Key notations used in DFD and CFD

Context-level DFD for OTMS

A level 0 DFD also called a fundamental system model or a context model represents the entire software element as a single bubble with input and output data indicated by incoming and outgoing arrows respectively.  
As the DFD is refined into greater levels of details, the analyst performs an implicit functional decomposition of the system, thereby accomplishing the forth operational analysis for function. At the same time, the DFD refinement results in a corresponding refinement of data as it moves through the processes that embody the application.

Fig. 2 Context Level Data Flow Diagram

Level 1 DFD for OTMS

Fig. 3 Level 1 Data Flow Diagram

Data Flow Information  

1) User commands and data  
2) Configure request  
3) Configure data  
4) Start / Stop  
5) Sensor status  
6) Configuration data  
7) A/d message  
8) Configuration data  
9) Sensor information  
10) Display information  
11) Alarm type

Level 2 DFD of OTMS

Level 2 Data Flow Diagram refines the monitor sensors process

Fig. 1 Level 2 Data Flow Diagram

Data Flow Information

1. Sensor status  
2. Sensor ID, type  
3. Alarm data  
4. Configuration data  
5. Sensor ID, type, location  
6. sensor information  
7. Alarm type

Control flow Diagram

A large class application are "driven" by events rather than data; produce control information rather than that reports or displays, and process information with heavy concern for time and performance.

Fig. 1 Control Flow Diagram  
Data Flow Information

1. User commands and data  
2. Configure request  
3. Configure data  
4. Start / Stop  
5. Sensor status  
6. Configuration data  
7. A/d message  
8. Configuration data  
9. Sensor information  
10. Display information  
11. Alarm type  
5. Software Design  
The software design will includes two parts  
• C Program Design (Source)  
5.1 "C" program design  
This is the main program of Online Temperature Monitoring System. This is compiled with the RIDE (Raisonance Integrated Development Environment) compiler and the generated executable image will be dumped into the Microcontroller (AT 89c52) Chip. The complete Flow Charts for the program are given below  
The main program routine

Flow Chart for the "Control" Routine

Flow Chart for the "Write Time" Routine

1. I2C Protocol  
2. Serial Communication Protocol  
6.2 I2C Protocol Communication  
Overview  
In consumer electronics, telecommunications and industrial electronics, there are often many similarities between seemingly unrelated designs. For example, nearly every system includes: • Some intelligent control, usually a single-chip microcontroller• General-purpose circuits like LCD drivers, remote I/O ports, RAM, EEPROM, or data converters • Application-oriented circuits such as digital tuning and signal processing circuits for radio and video systems, or DTMF generators for telephones with tone dialing. To exploit these similarities to the benefit of both systems designers and equipment manufacturers, as well as to maximize hardware efficiency and circuit simplicity, Philips developed a simple bi-directional 2-wire bus for efficient inter-IC control. This bus is called the Inter IC or I2C-bus. At present, Philips' IC range includes more than 150 CMOS and bipolar I2C-bus compatible types for performing functions in all three of the previously mentioned categories. All I2C-bus compatible devices incorporate an on-chip interface which allows them to communicate directly with each other via the I2C-bus. This design concept solves the many interfacing problems encountered when designing digital control circuits.  
Features of the I2C-bus  
• Only two bus lines are required; a serial data line (SDA) and a serial clock line (SCL)  
• Each device connected to the bus is software addressable by a unique address and simple master/slave relationships exist at all times; masters can operate as master-transmitters or as master-receivers  
• It's a true multi-master bus including collision detection and arbitration to prevent data corruption if two or more masters simultaneously initiate data transfer  
• Serial, 8-bit oriented, bi-directional data transfers can be made at up to 100 kbit/s in the Standard-mode, up to 400 kbit/s in the Fast-mode, or up to 3.4 Mbit/s in the High-speed mode  
• On-chip filtering rejects spikes on the bus data line to preserve data integrity  
• The number of ICs that can be connected to the same bus is limited only by a maximum bus capacitance of 400 pF.

Designer benefits

• Functional blocks on the block diagram correspond with the actual ICs; designs proceed rapidly from block diagram to final schematic.  
• No need to design bus interfaces because the I2C-bus interface is already integrated on-chip.  
• Integrated addressing and data-transfer protocol allow systems to be completely software-defined  
• The same IC types can often be used in many different applications  
• Design-time reduces as designers quickly become familiar with the frequently used functional blocks represented by I2C-bus compatible ICs  
• ICs can be added to or removed from a system without affecting any other circuits on the bus  
• Fault diagnosis and debugging are simple; malfunctions can be immediately traced

The I2C-Bus Concept  
The I2C-bus contains two wires, serial data (SDA) and serial clock (SCL), carry information between the devices connected to the bus. Each device is recognized by a unique address (whether it's a microcontroller, LCD driver, memory or keyboard interface) and can operate as either a transmitter or receiver, depending on the function of the device. Obviously an LCD driver is only a receiver, whereas a memory can both receive and transmit data. In addition to transmitters and receivers, devices can also be considered as masters or slaves when performing data transfers

Definition of I2C-bus Terminology

Byte format  
Every byte put on the SDA line must be 8-bits long. The number of bytes that can be transmitted per transfer is unrestricted. Each byte has to be followed by an acknowledge bit. Data is transferred with the most significant bit (MSB) first (see Fig. a). If a slave can't receive or transmit another complete byte of data until it has performed some other function, for example servicing an internal interrupt, it can hold the clock line SCL LOW to force the master into a wait state. Data transfer then continues when the slave is ready for another byte of data and releases clock line SCL.

Fig a. Data transfer on I2C Bus

Acknowledge  
Data transfer with acknowledge is obligatory. The acknowledge-related clock pulse is generated by the master. The transmitter releases the SDA line (HIGH) during the acknowledge clock pulse. The receiver must pull down the SDA line during the acknowledge clock pulse so that it remains stable LOW during the HIGH period of this clock pulse (see Fig.).

Fig b. Acknowledge on I2C Bus

Formats with 7-Bit Addresses  
Data transfers follow the format shown in Fig.a After the START condition (S), a slave address is sent. This address is 7 bits long followed by an eighth bit which is a data direction bit (R/W) - a ‘zero' indicates a transmission (WRITE), a ‘one' indicates a request for data (READ). A data transfer is always terminated by a STOP condition (P) generated by the master. However, if a master still wishes to communicate on the bus, it can generate a repeated START condition (Sr) and address another slave without first generating a STOP condition. Various combinations of read/write formats are then possible within such a transfer.

Fig. a. complete data transfer.

Complete Data Transfer Format

S- START Condition  
P- STOP Condition  
A- Acknowledgement

3. Serial Communication Protocol  
The establishment of RS 232 and ASCCII coined with the development of multi-user computer organizations wherein a number of users of users were linked to a host mainframe via serial data links, and serial data was encoded in ASCII. Peripheral devices, such as printers, adopted the same standards in order to access the growing market for serial devices.  
Serial data transmission using ASCII become so universal that specialized integrated circuits, universal Asynchronous Receiver Transmitters (UARTS), were developed to perform the tasks of converting an 8-bit parallel data byte to a 10-bit serial stream and converting 10-bit serial stream to an 8-bit parallel byte.  
The 89c52 contains serial data transmission / reception circuitry that can be programmed to use four asynchronous data communication modes numbered from 0 to 3.

• Mode 0: High-Speed, 8-bit shift register; one baud rate of f/12  
• Mode 1: Standard 8-bit UART; variable baud rates  
• Mode 2 & Mode3 Multiprocessor 9-bit UART

Asynchronous 8-bit Character (Mode1)

7. Operational Specifications

8. Application Real Time

9. Conclusion  
9.1 Future Scope

9.2 Limitations  
.

10. Bibliography

 [1]:https://www.shafiq.in/wp-content/uploads/2013/06/proj_format_.doc
