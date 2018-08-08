---
layout: post
title:  "Network Security"
date:   2018-07-16 22:01:12 -0700
categories: blog
permalink: /blog/network-security.html
---

### Topics

 - Secure network
 - Threats

### Lecture

This week we went over many definitions and vocabulary for network security.
The lectures were on different aspects of network security, which was a change from the past term of working with specific operating systems.
The first topic we went over was reasons for a secure network.
One mentioned was the desire to create a safe space, to reduce the attack space and to create a trusted system.
Another reason is to make it harder for attackers to exfiltrate data using the internet.
Protecting vulnerable hosts who haven't updated or are just using legacy software and hardware is another reason for a secure network.
Also if you can prevent a system from getting infected, it can be much easier to detect and deter than trying to save an infected system.

Tying this into our previous lectures is easy because for much of malware, the internet is the attack vector.
This can be in the form of worms or trojans, and also botnets and DOS attacks.

#### Strategies
We also went over strategies for protection.
The following strategies will be further discussed below:

- Positive Policy
- Firewalls/security zones
- Defense in depth
- Intrusion Detection
- Honeynets/Intrusion Deception
- Quarantine
- Reputation

Positive Policy involves whitelisting trusted connections.
It also includes any policy enforcement, with the goal of clearly defining what you expect to happen.
This means that any connection not on the whitelist or any action not approved will be disallowed.

Following positive policy, Firewalls and Security Zones help enforce policy.
They specifically help separate incoming requests and actions, disallowing prohibited connections.
Firewalls can also help implement access control, making sure that certain users have certain powers, whereas others do not.

Security Zones work to further separate networks by using proxies and other methods.
The term DMZ came up, which I learned to be a defined area of higher or lower protections.
From the idea of separate zones of security comes the term defense in depth.
This means that the defenses are layered, so that each layer could defend if the outer layer fails.
This is likened to a castle, with multiple strong walls protecting each next wall.
The deeper the wall, the more protections, and the more trusted it is to protect higher priority data.
When designing a network or system, you need to develop the security with defense and depth in mind because this method covers the bases.

Although impenetrable walls is a nice idea, inevitably someone will manage to get through and thats where intrusion detection comes in.
Intrusion detection seeks to alert the system once before it has been compromised.
This method is good against known attacks as it can recognize them.
This can be useful for attacks that could be used in different spots or slightly reworked.
It can also help against systems that have not been updated, or aren't suspected such as imbedded systems.
It isn't very good against zero day attacks, because it can't recognize novel attacks.
Intrusion detection can also have the issue of stopping legitimate traffic, as a false positive.

Once detected attackers can be waylaid by Honeynets  via Intrusion Deception.
Honey nets return fake data at a slow rate, to trick attackers into thinking they've won.
This is a smart method, but isn't actually implemented that often, because it requires specific information crafted to only catch attackers and not waste users' time.

An alternative to honeynets is the act of quarantining an attack.
This method puts attackers in network all on their own, preventing them from attacking again, and giving the defenders a chance to analyze their behavior.

In addition to all of the above methods, a system can implement a reputation system.
Reputation just means that a system would keep track of who acts hostile on a network, and lowers their permissions or keeps a closer eye on their activity.
This is a good method, as it can be shared between multiple different systems, and can act to share information about attackers.

#### Threats

In addition to our lectures about prevention methods, we went into some depth about certain attacks and how to specifically protect against them.

In the Man in the Middle attack, the attacker takes packets from a communication, via interception.
This means, as a user, your messages don't go where you think they go, and as a result you can disclose information, be misinformed, and lose all of your privacy.
This attack can be done through ARP poisoning or TCP hijacking and involves intercepting packets and sending them on, changing their destination, meaning or just deleting them.
I was surprised to learn that MITM can be use non-maliciously, to remove malware from streams, stopping you from accidentally sending malware, or removing metacharacters from obfuscated urls.

Prevention can be done using cryptographic signatures, which, if implemented correctly, can verify that a message came from whoever signed it.
This often requires a trusted third party and asymmetrical cryptography to properly scale.

Another malicious attack we learned about was reconnaissance.
This is where an attacker gains information to prepare an attack on a system.
It is often done through scanning, which can be either passive or active:
- active: attacker scans ports for exploits, using tools like Nmap
- passive: attacker sits on network to watch people and communications

To defend against reconnaissance, you can create honeynets and use quarantining.

Spoofing is kinda like MITM, in that it disguises itself.
This method is described as masquerades as another system, and can be used to steal information or spread misinformation or malware.
It can be done legitimately, for example to fake a bunch of hosts or users to test systems.
It can be prevented using signatures or certificates.


Denial of Service or DOS is a really common attack.
It acts to overload the bandwidth of a system, functionally shutting it down.
There are several kinds, one of which is DDOS.
This stands for distributed denial of service and often includes a botnet or group sending requests to server.
Another DOS attack is the slow lorris which uses a few constantly open connections to slow down a network.
The reason this attack is so common is it is pretty hard to prevent, as any effort to stop traffic can turn into a self-directed denial of service.
Some methods include large overseers such as Cloudflare, which analyze networks using distributed nodes and redirect fake traffic.
Also simple firewalls and proxies can help, but they have to be configured correctly so as not to disallow real users.

From these lectures I learned that security is not total, and that all security additions only protect against certain attacks, and only to a certain extent.
In security, you have to think about precise meanings and constantly test and improve the security of a system. 
