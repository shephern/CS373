---
layout: post
title:  "Web Security"
date:   2018-07-16 22:01:12 -0700
categories: blog
permalink: /blog/web-security.html
---

### Topics

 - Threats
 - Solutions

### Lecture

As with many of the practical security classes, the idea of learning attacks is if you know what the attackers can do, you can better protect against it.
With that in mind, we started our second to last lecture.
This lecture was about web security, which I thought would be very similar to network security but was more broad.
One of our first recommendations was to not try this stuff on a system you don't own, because it is often considered a felony.

With that said one of the big things about web security is that the web is everywhere.
Not only is it the internet and websites, but it also includes any sort of IOT.
To start learning about website security we went over briefly some history.

In early days of the internet many attacks were mostly harmless and had to do with script bombing or spam being sent out.
From that browsers started and realized that they needed to protect against attacks.
In response, the attackers learned to attack plugins instead of browsers, because that could reach more victims.
In addition to mechanical attacks phishing and spearphishing have always been effective.
With further protections from browsers, malware started showing customized browser exploits, which could be tailored to the system that they attacked.
I wasn't surprised to learn in this that 95% of malware is delivered via internet, which emphasizes the importance of browsers.

Although the web is used everywhere, many attacks are Windows centric as far as injections.
This is because of the mass of Windows machines being used currently, as a large number means that attackers can hit more people with the same attack.

One thing that I learned that I found interesting is that the web on a computer can be under attack from two directions:
  - malware trying to gain control/visibility from computer
  - malware trying to infiltrate the system

This means that browsers have to protect from both directions also, so as not to be the vector for new malware, or the vessel for transporting info from old malware.

During the infection of a computer, the malware uses the methods we've talked about earlier in this class.
That is the payloads are obfuscated, trying whatever methods to hide their intent.
This can mean being hidden in cookie, or url, or on separate servers, with only links to them.
The addition of javascript to a site can mean that the payload can be build on the fly.
This is because JS can pull code from different places, use packers to compress it or obfuscate, and also encode in a variety of ways.

Another thing we learned about were the users of web devices.
In the case of web security, users are the weakest link.
Many attacks on web are via social engineering, which entails getting users to do something willingly, with malicious intent.
The user is unaware that they are being manipulated, but can often pull malicious code into places the attacker wouldn't otherwise have access to.
Here are some methods used to attack the web via the user:
 - Phishing is broadly convincing the user to give information or download malware. Often a phishing site will look exactly like other websites and can even be signed if attackers pay for a certificate.
 - SEO Poisoning- Search Engine Optimization, malicious sites self-reference to game the search engine and have malware high on the lists
 - Fake AV is a program that would be downloaded and warns against viruses or malwares. It then offers to rid the computer of the fake problem for money. Sometimes fake AV programs have full support crews backing them to make them seem more trustworthy.
 - Homographic Attacks use seemingly same named urls to trick users.  Sites like "arnazon" or "rnicrosoft" are hard to discern in some fonts.
 - Social Media Attacks generally just uses social media as a vector for attacks. This can be by impersonation or catphishing, or just using it to find public information on someone, as a first stage of an attack.
 - Form Link Insertion infects forms or serves fake forms for users to just input their info.  This skips the step of infecting the machine.
 - Malvertising: Using advertising networks to advertise specifically to high paid CXOs.  The advertising network serves websites with malicious advertisement to specific audiences, without the attacker having to search at all.
 - DNS spoofing can be done with bad USBs, and is used to rewrite a users URL lookup, so they can search sites that will be directed to the attackers server.
 - Click jacking is the act of redirecting user actions to different parts of the screen, and can even be used to jack webcams.
 - SQL injection is possible raw sql data is used on a site. In SQL injection the attacker can manipulate the database, providing long term attack possibilities.
 - Blind injection is the same, but can be done without any readout via timing or error results.
 - CSS is a relatively new attack form and is broadly just attacking a site via another page that is open.

#### Solutions

These attacks can be countered with a proper set up.
The following are ways that can prevent some of the above attacks:
- URL reputation system
- Site certification
- Client and Gateway AV/AM
- Safe URL shorteners  
- Client and Developer Education 
