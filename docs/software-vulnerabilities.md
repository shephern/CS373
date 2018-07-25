---
layout: post
title:  "Software Vulnerabilities"
date:   2018-07-23 12:01:12 -0700
categories: blog
permalink: /blog/software-vulnerabilities.html
---

### Topics

 - Vulnerability Types
 - Exploit Methods
 - GDB or WinDebug (Exploit Analysis)
 - Stack Overflow
 - Use after free

### Lecture

Our lecture this week went over vulnerabilities and how to exploit them.
The lecturer was a former judge of CTF competitions, which I have been interested in for a while.
In the lecture, we learned about the two basic types of vulnerabilities:
- Software Vulnerability
	- Failure on the part of the software, the system has a vulnerability
- Configuration vulnerability
  - Failure on the part of the setup, the user didn't choose the most secure options

This lecture followed mostly along with the exploit side of things, which is considered more offensive than defensive.
In this field, which can be referred to as software exploit analysis, the individual has to be careful how they use what they learn.
With the main goal being to better understand attackers, and as a result better protect against attacks, it is important to practice and learn in a separate environment.
This learning and practice has to also be done in a mature and ethical manner.

After learning the basics, we started into what to do once a vulnerability is known.
In many cases, a researcher would be given a known vulnerability to patch or exploit.
Once you know a vulnerability
  - you need to write an exploit
 - can do with WinDebug

WinDebug

 - Adds breakpoints
 - Registers
 - Look at memory locations
  - Look at strings
    - Will be in hex as addresses, can be formatted
- Register calculations
- Can view local variables
- Can take steps or steps into parts of program
- Can execute up to a memory location


#### Memory Corruption

Stack overflow
Accessing memory in a (invalid) unintended undefined way

If you can crash the program, you might be able to use the crash to your advantage

Exploitation is taking advantage
  - Often have to write an exploit, cause some condition

Vulnerability Trigger - Puts the program in an unstable state
Then deliver Payload

Shellcode is often the payload
 - In Windows calc is often used, which shows that you can execute arbitrary code

Stack is used to return to a previous state

Explanation of the stack

# Stack Overflow

Stack can be seen by using 'k' command
String overflow can write beyond string size if not checked
Once it overflows it can overwrite the saved EBP and ESP
  - This changes the addresses that the program will return to
  - If this address is overwritten with valid address it will start to execute
  - It can overwrite so far that it SEG Faults

Steps:
  1. Understand the crash
    - Do we have registers that we control
    - Triage
    - Trigger reliably
    - control of stack? Heap? registers?
    - With this one we have control over the stack
  2. What the stack is and what we control
    - Figure out bytes between buffer and return address

We will use JS, reliably send data to programs
In attack and defense we used Python

You can use non repeating strings to easily find what address is being executed
Use WinDebug to find offset

Fill up in between data with junk
Overwrite return address

What address to overwrite:
  - right where the shellcode starts
  - We need a jump to esp, which is 'ffe4' which is part of another instruction

There are securities
  - Stack canary/cookie has a secret pass as a variable, if it is changed then the stack is smashed

#### Use After Free Exploit
  - Allocate memory  
  - Free the memory
  - Replace the freed object
    - with some shellcode or payload
  - Use that memory

Popular in browsers
Enable low fragmentation heap, to make things easier
Once freed using that memory again will often crash the program
  - The data could still be there, just dereferenced
  - Could be wiped, or zeroed
