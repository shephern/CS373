---
layout: post
title:  "Software Vulnerabilities"
date:   2018-07-23 12:01:12 -0700
categories: blog
permalink: /blog/software-vulnerabilities.html
---

### Topics

 -

### Lecture



#### 1. Blends in


 - Changes file names
 - Changes date/time stamp
 - Provide fake signatures
 - Attack antivirus systems
 - Bootkits or Rootkits
  - installed on lowest level of OS

#### 2. Persists

For the malware to be a threat it also needs to persist in the case of a reboot.
This can be done in the following ways:

   - System Startup, using register keys
   - Windows Startup, like our first lab
   - Application Startup, using DLL
   - Scheduled, Autorun
   - Can live as just script in memory space
   - Disable security systems

#### 3. Execution

Execution is the goal of any malware.
After protecting itself from destruction and discovery, malware will execute its goal.
Most often that entails harvesting information.
Information such as:
  - passwords
  - process infromation
  - log files
  - local files
After collecting information, the malware must make use of it by sending it back to the attackers.
This can be done in a couple different ways, but most often will require internet.
The information can be transmitted over ssh, http, or other over the wire services, as well as email.
This can be detected by searching for email addresses, or website domains.

#### Protection

Protecting agains malware is a large and varied field.
It has to be, because of the amount of variation in malware.
One step can be education, providing users with options to protect themselves.
These options can be in many forms, like web reputation, to judge the value of a site.
Other protections can come in the form of policy, such as analyzing flash drives before plugging them into a system.
Another protection suggested is physical protections, like epoxy.
This isn't as feasible as other protections as it doesn't discern between legitimate media and dangerous media.
Other protections try to find executing malware and kill it.
This protection can be behavioral, as in finding it based off of the execution of the process, or it can be based off of the binary structure of the file.
The best strategy is a layered protections with different levels and different methods at each layer.
This is a list of selected methods, at different layers:

1. Network Firewall, Network Intrusion Prevention
2. Message, Website, Network reputation
3. Host Firewall
4. Host IPS
5. Access Control, Anti-Malware


Larger companies, like Nord or Cloudflare, can implement larger protections like bot net detection.
This analyzes network connections over different network nodes.
Other methods, such as firewalls can be heavy handed, blocking the majority of incoming traffic, regardless of danger.
These catch all methods can be fine tuned using better data.
This is where cloud data would come in.
Cloud data can provide hashes or decompositions of malware and inform anti-malware the nature of programs.

#### Yara

Yara is a Open Source language used for malware detection.
It uses pattern matching scanning for files or memory to programs based off of rules.
Although it can generate rules based off of samples, it is often best to make your own.
This is because the generated rules are often large and overfit to the examples.
To make the rules you can search for weird lines and strings that stand out.
This can be websites or ip addresses used to send back data, or making changes to registers to persist over boots.

#### Sample set 1

```js
rule BadFile
{
  strings:
    $a="OFTWARE\\Boreland\\Delphi"
    $b="Jenna Jam"
    $c="OutOfMemory"
  condition:
    all of them
}
```
This found all 7 in the malware folder and 0 in the System32 folder.
This means that it is pretty good, and doesn't produce any false positives.
Delphi is just the language that it is written in, and could match a lot.
Not using "Jenna Jam" still gave me 0 false positives, so the other two rules are enough to target the bad files.
Just using OutOfMemory gave me 62 false positives, which means alone it wouldn't be a good rule.

#### Sample set 2
```js
rule BadFile
{
  strings:
    $a="DownloaderActiveX"
  condition:
    all of them
}
```

Flagged all samples, found none in System32, which means that it is a good rule set.
With Yara, especially hand written, it can be hard to manually search through and find similarities.
Machine learning can help with flagging and detection, by automatically finding similarities and reducing false positives.
ML can also be implemented to detect what the file is doing, during execution.

#### Automated Malware Analysis

With 300 million unique hashes of malware currently, it is infeasible to manually detect each one individually.
This number doesn't count infected innocent programs, which would greatly increase this number.

One tool used for malware detection is Cuckoo.
Cuckoo runs malware on multiple vms and reports the results.
These reports can be any of the following:
   - Queuing
   - Screenshots
   - Memory Dumps for volatilitys
   - Files created and downloaded by malware

This program can help define and detect interesting behavior.
As mentioned before, these behaviors are often common:
   1. Blend In
   2. Persist
   3. Execute
