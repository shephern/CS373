---
layout: post
title:  "Window Internals"
date:   2018-07-31 12:01:12 -0700
categories: blog
permalink: /blog/window-internals.html
---

### Topics

 - Agony Lab
 - Threads and Processes
 - Master Boot Record

### Agony Lab

This lab started with launching the Agony file on our VMs.
I moved the bin file to the desktop and renamed it evil.exe.
Using the analyzer.py we learned about a few files that were created, specifically wininit.sys.
As we learned in our last class, files with the .sys extension are hidden.
These are actually hidden in a different way then normal files, which means that kinda need to be specifically looking for the file to find it.
This hidden wininit.sys file hooks multiple apis.
These APIs are:
  - NtQueryDirectoryFile: Querying directory to explore files
  - NtEnumerateValueKey: Enumerate over value keys
  - NtQuerySystemInformation: Enumerate the processes

The Agony rootkit takes over these processes and filters out all references to itself, essentially hiding it from view.
In fact, it hasn't taken over these processes, just overwritten the addresses, to point to within the program.
This is most likely the first step in execution: hiding and persisting.
Using LiveKD we are able to fish around in the kernel memory, allowing us to view the specific module called by wininit.
Following the instruction, I found the address that were changed.
This was done using Tuluka, which shows different details of a running system, including the trustworthiness of keys and processes.
The APIs above were marked as untrustworthy, and they showed that the reference addresses had been changed.
At this point I was ready to run windbg and inspect these addresses.
Unfortunately when I tried using windbg, it wouldn't allow me to add break points at this address, and I wasn't able to find the issue.

### Lecture

In the lecture, we dipped into threads in regards to debugging.
I learned more about threads, which run processes.
Each program can have multiple threads which obviously leads to lots of threads.
This requires a method for thread scheduling.
A common thread scheduler method acts as a FIFO structure with the addition of quantum and priority.
A quantum is a time slice allowed to each thread, while priority determines how much and how often a process gets CPU energy.
Priorities in this method can be changed, based off of how long they have been waiting.
Although some research was spent with Hyperthreading, most computers currently have multiple cores, which means that stalling is less of a problem.
During swapping out threads, the context of the thread must be preserved.
Specifically the stack, heap, and registers get saved and stored.
To context switch and manipulate threads, the CPU refers to objects as handles.

One piece of malware we looked at was a key logger.
These types of programs monitor the key inputs of the victim.
This is done through injection into multiple pipelines, such as the hardware to software pipeline of keystrokes.
Injection into other processes is how many rootkits and bootkits work.
By injecting pointers and hooking the original program, the malware is able to tie itself to other programs.
Sometimes the fix for this is simple, and you can use Tuluka and windbg to patch addresses back to the original address.
However it can be much tougher, as a rootkit at kernel level can infect any API call.

Often bootkits modify launching to persist over boots.
They do this usually by modifying the master boot record
The Master Boot Record is Windows method of keeping track what programs are trusted and should be allowed at launch time.
It is basically a large table of programs, ending in 55AA, that is stored at the first sector on the boot disk.
To analyze this, a tool called Sect Editor can be used to display and read any sector on disc.

Although I have been using them interchangeably, rootkits and bootkits are not the same.
The main difference is a rootkit has a stealth component, trying to hide from a searching user or anti-virus, while a bootkit doesn't care.

To hide itself, a rootkit can use a variety of different methods.
One common long term method is to make testing and cracking the rootkit much harder.
Rootkits can do tricky things, just to throw off research, for example a rootkit:
  - only runs during the day
  - won't run with ProcMon or other viewing programs
  - won't run in VM

In addition to not running reliably, rootkits at the kernel level can try any of the following to obscure their persistence:
 - File Forging
 - Memory Forging
 - Self protection
 - Attack Anti-Virus
 - Disassociating memory from file-on-disk
 - Removing dependency on file
 - Untrusting the trusted

Also they can whitelist programs, to not allow the user to download any anti-virus software.
It was really interesting learning and witnessing rootkits in action.
