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
 - GDB or Windbg (Exploit Analysis)
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
Once you know a vulnerability you need to exploit it.
This can be done in a few different ways mentioned in the class:

  - Buffer overflow
  - Use after free

With writing an exploit, it can be tough to see how your payload and exploit are effecting the system.
Tools like GDB and Windbg help with this.

In general an exploit follows a vulnerability.
In this lecture the exploits we looked at are defined as memory corruption exploits.
This just means accessing memory in an unintended, undefined way.
In this, as the attacker, it is good to keep in mind that if you can crash the program, you might be able to use the crash to your advantage.
This is the definition of exploit, after all.
Memory corruption exploits usually are in two parts:

- Vulnerability Trigger: Puts the program in an unstable state
- Payload: The goal of the exploit

In most cases shellcode is the payload.
Shellcode is called that because it allows the attacker to gain a shell, with heightened authority.
In Windows the ability to execute arbitrary code is proved by launching calc.exe.

#### Windbg

Windbg is what we will be using in this class.
Below are some of the functionalities of Windbg, and their uses.

- Adds breakpoints: To stop the program at certain points
- Registers: To look at internal variables and construction of program
- ESP Offsets: Can be used to look at program strings.  These can be formatted in different ways (HEX, BIN, ASCII)
- Register calculations: Can be used to calculate buffer lengths and program distances
- Can view local variables
- Can take steps or steps into parts of program
- Can execute up to a memory location

Using this we were able to execute both stack overflow attacks and use after free attacks.

##### Stack Overflow

In the lab we used Windbg to analyze a buffer overflow crash.
These sorts of crashes often cause the infamous 'SEG fault' when running loops over strings or something.
In Windbg, we use the 'k' command to print out the current stack.
The stack overflow attack uses the fact that the ESP and EBP are stored on the stack.
These registers are used when a program returns to the calling program.
If they are overwritten then the program control will pass to whatever program is referenced.

The steps to a stack overflow exploit are below:

  1. Understand the crash
    - Do we have registers that we control?
    - Triage different methods of crashing
    - Can we trigger it reliably?
    - Do we have control of the stack? Heap? registers?
  2. Calculate sizes of NOPs or junk strings
  3. Exploit with string and payload

In the lab we used JavaScript, as it can easily send data to the program.
In other classes I've used Python, but it seemed to work in a similar way.

In JS, you can use non repeating strings to easily find what address is being executed.
This helps when searching through the stack in Windbg, as you can easily count the offset based off of what string was overwriting the ESP.
With the right length of string figured out, you can then use a trampoline method.
In this method, you find 'ffe4' which is the opcode to jump to the process referenced in ESP.
With this, you can overwrite ESP with the address of our shellcode or malicious code.

There are some securities against stack overflow attacks, the most common being a stack canary.
The stack canary or stack cookie acts as a secret variable, if it is changed then the stack is considered smashed.

#### Use After Free Exploit

The other exploit that we explored was the use after free exploit.
It is done using the following steps:

  - Allocate memory  
  - Free the memory
  - Replace the freed object
    - with some shellcode or payload
  - Use that memory

This attack is popular in browsers, as they have access to memory, and take a wide variety of inputs.
To do it in class, we had to enable the low fragmentation heap, to easily reference the program during runtime.
In the use after free exploit, the key step is to replace the freed object.
Often, once freed using freed memory again will crash the program.
This was more of a demonstration, and also the sort of attack that can't really be executed in the wild.
