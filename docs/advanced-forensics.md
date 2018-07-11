---
layout: post
title:  "Advanced Forensic Techniques"
date:   2018-07-09 16:14:12 -0700
categories: blog
permalink: /blog/advanced-forensics.html
---

### Topics

 - Incident Response
 - Timeline
 - FTK Imager
 - Memory Dump with Volatility

### Lecture

This week I learned about incident response and how to do a proper investigation.
One of the main focuses of forensic computing involves replicating and understanding an attack.
This is kind of what we went over last week, with the malware analysis in a virtual machine.
Modern analysis relies heavily on memory of a system.
This helps make a timeline of an attack, and is also crucial to fixing any damage done by the attack.
As part of our foray into forensics we learned reasons that a investigation might require cyber intelligence.

Common reasons for forensics:
 - Fraud
 - Intellectual Property Theft
 - Hacker intrusion, or data breach
 - Inappropriate use of internet
 - Child Exploitation
 - Criminal investigation

Some companies have started funding their own in-house cyber security team, which not only provides incident response, but can also train and improve the security of the system.

Often as a cyber forensic specialist you can be hired to assist in an investigation.
These investigations require that the specialist keep track of all of the events, and it is recommended to keep a journal.
Our instructor mentioned that pen and paper is the most reliable for various reasons.
While using a journal can help you solidify evidence in your brain, it can also be an important tool to keep an official document of the investigation.
This prevents tampering, and can provide additional evidence when presenting a case.
While investigating, I learned it is important not to be the judge, and just work at collecting lots of evidence.
If the investigator has already judged a suspect as guilty, than further investigation is unnecessarily biased.

In investigation, both on a company level and a governmental level, it is important to work systematically, so as not to miss anything.
Below are three major steps to any investigation.

1. Evidence Acquisition
2. Investigation and analysis
3. Recording and reporting results

#### Evidence Acquisition

For evidence acquisition it is important to keep track of everything that is done.
This is where the journal comes in handy.
We were recommended to record everything, especially including the following:
 - Real time
 - System time
 - Location

Along with just recording information, it is inevitable that you have to open up the computer or system and delve into the investigation.
I was somewhat surprised to learn that even just pulling the plug on a computer can invalidate the evidence on it.
Above most things, preserving data is a high priority.
This can be done by using hashes to check changes in a system, if it has been changed, than it can no longer be trusted.
Using techniques like Writeblockers can help prevent accidentally tampering evidence.
The Writeblocker will prevent any information from being sent to a hard drive, allowing the hard drive to be read, without damaging it.
Another cool technique is to freeze computers, and use electron microscopes to analyze bits on the machine.
In all of evidence acquisition, it is important to keep in mind the safety of others, no investigation is worth putting others in danger.

#### Investigation and Analysis
After evidence has been properly gathered, it needs to be analyzed and tested, to determine its significance.
During this analysis, there are three types of investigations that may take place:

  - Post-Mortem: After the fact of an incident
  - Live Forensics: Forensics conducted during an incident
  - Network based: Forensics conducted based off of Network records

#### Recording and Reporting
In recording and reporting, it is important to re-examine the evidence.
Over the course of the investigation it may become clear that some evidence wasn't important, or didn't have an effect on the outcome.
This is the point where one would decide what evidence could be admissible in court.
I learned that a triage is a way to prove a conclusion by using multiple different pieces of evidence.

#### Challenges in Forensic Computing
Along with the methods used in investigating, I learned a bit about the challenges one can face in modern cyber investigations.
These challenges mostly have to do with the average scale of data.
With large data bases, multiple log types, and terabytes of potentially corrupted data, it can be very hard to sift out the important information.
Not to mention that this all has to be done within a specific timeframe.
These challenges can be lessened by the use of tools, and preparation.
Tools like Writeblocker, as mentioned above, can make it possible to copy whole disks off of computers, allowing for closer inspection.
Discs can be indexed and searched via regex, to find more evidence.

I was surprised to learn that lots of response teams are made up of adhoc people, chosen in the moment, with limited experience with the specific system they need to work on.
To be prepared for challenges, it seems best for a company to invest in an in-house cyber forensic team.
This allows a team to familiarize themselves with a system before an incident, getting used to different tools and different log formats.
