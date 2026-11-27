# CompTIA A+ episode plan

The order to write episodes in: Core 1 (exam 220-1201) first, then Core 2
(exam 220-1202), following the official objectives in order. One line is
one script in `episodes/`, about 15 minutes long. Tick the box when the
script is pushed.

The percentage after each domain is its share of that exam. The numbers
in brackets at the end of each line are the official objectives it
covers.

## Foundation

- [x] 001 The OSI model, layer by layer ([script](episodes/001-osi-model.txt))

## Core 1 (220-1201)

### Mobile Devices (13%)

- [x] 002 Laptop hardware: replacing RAM, storage, battery, keyboard; display types; biometrics [1.1, plus 3.1] ([script](episodes/002-laptop-hardware.txt))
- [x] 003 Mobile connectivity and accessories: Bluetooth, NFC, hotspot, docks, sync, SIM/eSIM, MDM (corporate vs BYOD, policy enforcement, corporate apps) [1.2, 1.3] ([script](episodes/003-mobile-connectivity.txt))

### Networking (23%)

- [ ] 004 TCP and UDP ports and protocols to memorize [2.1]
- [ ] 005 Wireless: 802.11 standards, 2.4/5/6 GHz bands, channels, Wi-Fi 6/6E/7, Bluetooth, RFID, NFC [2.2]
- [ ] 006 Server roles: DNS, DHCP, file share, print, mail, syslog, web, AAA, database, NTP [2.3]
- [ ] 007 Other networked hosts: spam gateways, UTM, load balancers, proxy servers, SCADA, IoT [2.3]
- [ ] 008 DNS records (A, AAAA, CNAME, MX, TXT with SPF, DKIM, DMARC) and DHCP leases, scopes, reservations and exclusions [2.4]
- [ ] 009 VLANs and VPNs [2.4]
- [ ] 010 Network hardware: switches, routers, APs, PoE, firewalls, patch panels, ONT, cable modem, DSL, NICs [2.5]
- [ ] 011 IPv4 and IPv6 addressing: public, private, APIPA, static vs dynamic, subnet mask, gateway, SOHO configuration [2.6]
- [ ] 012 Internet connection types, network types, and networking tools (crimper, cable stripper, toner probe, punchdown tool, cable tester, loopback plug, network tap, Wi-Fi analyzer) [2.7, 2.8]

### Hardware (25%)

Objective 3.1 (display types and attributes) is covered in 002.

- [ ] 013 Cables and connectors [3.2]
- [ ] 014 RAM and storage: DDR types, ECC, channels; HDD, SSD, NVMe, SAS, M.2; RAID levels; removable and optical storage [3.3, 3.4]
- [ ] 015 Motherboards, CPUs, BIOS/UEFI, Secure Boot, TPM, expansion cards, cooling [3.5]
- [ ] 016 Power supplies: input voltage, output voltages, 20+4 pin connector, redundant and modular PSUs, wattage, efficiency [3.6]
- [ ] 017 Printer and multifunction device setup: drivers (PCL vs PostScript), connections, sharing and print servers, settings, security (badging, audit logs, secured prints), network scanning [3.7]
- [ ] 018 Printer maintenance: laser, inkjet, thermal, impact [3.8]

### Virtualization and Cloud Computing (11%)

- [ ] 019 Virtualization: hypervisor types, VMs, containers, sandboxes, VDI [4.1]
- [ ] 020 Cloud computing: IaaS, PaaS, SaaS; public, private, hybrid, community; elasticity, metered use, multitenancy [4.2]

### Hardware and Network Troubleshooting (28%)

- [ ] 021 Troubleshooting motherboards, RAM, CPUs and power [5.1]
- [ ] 022 Troubleshooting drives, RAID, displays and projectors [5.2, 5.3]
- [ ] 023 Troubleshooting mobile devices [5.4]
- [ ] 024 Troubleshooting network problems [5.5]
- [ ] 025 Troubleshooting printers [5.6]

## Core 2 (220-1202)

### Operating Systems (28%)

- [ ] 026 Operating system types: Windows, macOS, Linux, ChromeOS, iOS, iPadOS, Android; file systems (NTFS, ReFS, FAT32, exFAT, ext4, XFS, APFS); end of life and compatibility [1.1]
- [ ] 027 Installing and upgrading Windows, and Windows editions: boot methods, install types including zero-touch, GPT vs MBR, upgrade considerations; Home, Pro, Pro for Workstations, Enterprise [1.2, 1.3]
- [ ] 028 Windows tools: Task Manager, MMC snap-ins, Event Viewer, Disk Management, System Configuration, Registry Editor [1.4]
- [ ] 029 Windows command line: ipconfig, ping, tracert, pathping, netstat, nslookup, net use, net user, chkdsk, sfc, diskpart, format, gpupdate, gpresult, robocopy [1.5]
- [ ] 030 Windows settings: Control Panel and the Settings app, power options, File Explorer options [1.6]
- [ ] 031 Windows networking: workgroup vs domain, shares, mapped drives, firewall, VPN and cellular connections, proxy settings, metered connections [1.7]
- [ ] 032 macOS and Linux basics and essential commands [1.8, 1.9]
- [ ] 033 Installing apps and cloud productivity tools [1.10, 1.11]

### Security (28%)

- [ ] 034 Physical security: bollards, access control vestibules, badge readers, surveillance, locks, key fobs, smart cards, biometrics [2.1]
- [ ] 035 Logical security: least privilege, zero trust, ACLs, MFA methods, SSO, SAML, just-in-time access and PAM, DLP, IAM, directory services [2.1]
- [ ] 036 Securing Windows: Defender, firewall, users and groups, log-in options, NTFS vs share permissions, UAC, BitLocker, EFS [2.2]
- [ ] 037 Active Directory: joining a domain, OUs, Group Policy, login scripts, home folders, folder redirection, security groups [2.2]
- [ ] 038 Wireless security and authentication: WPA2, WPA3, TKIP, AES, RADIUS, TACACS+, Kerberos [2.3]
- [ ] 039 Malware types and tools: from viruses to fileless malware; EDR, MDR, XDR, email security gateways [2.4]
- [ ] 040 Social engineering, threats and vulnerabilities: phishing, vishing, smishing, tailgating, DoS, evil twin, on-path, zero-day, SQL injection, XSS, supply chain, BEC [2.5]
- [ ] 041 The malware removal process, step by step [2.6]
- [ ] 042 Workstation hardening: password rules, BIOS/UEFI passwords, screen locks, account lockout, disabling guest accounts and AutoRun [2.7]
- [ ] 043 Securing mobile devices, data destruction, SOHO networks and browsers [2.8, 2.9, 2.10, 2.11]

### Software Troubleshooting (23%)

- [ ] 044 Troubleshooting Windows: BSOD, slow systems, boot problems, services, profiles, time drift [3.1]
- [ ] 045 Troubleshooting mobile OS and security issues [3.2, 3.3]
- [ ] 046 PC and browser security symptoms: pop-ups, redirects, certificate warnings, false antivirus alerts, renamed files, failed updates [3.4]

### Operational Procedures (21%)

- [ ] 047 Documentation, ticketing, asset and change management [4.1, 4.2]
- [ ] 048 Backups (3-2-1, full, incremental, differential, synthetic full, GFS), safety, ESD, environment [4.3, 4.4, 4.5]
- [ ] 049 Incident response, licensing and privacy: chain of custody, order of volatility, licenses and EULAs, NDAs, regulated data, acceptable use [4.6]
- [ ] 050 Professionalism and communication [4.7]
- [ ] 051 Scripting basics, remote access, AI basics (bias, hallucinations, public vs private AI) [4.8, 4.9, 4.10]

---

## Notes from the official objectives

Checked against the official CompTIA documents: *CompTIA A+ 220-1201
Exam Objectives, Version 2.0* and *CompTIA A+ Core 2 (220-1202) V15 Exam
Objectives, Version 3.0*. Every objective in both is covered above.
CompTIA has since published later versions of the Core 1 document.
These usually only fix wording, but compare with the newest one if you
have it.

- **Troubleshooting methodology: not tested.** The 220-1201 document
  prints the six steps but says the methodology "will not be tested" and
  "does not constitute a formal objective". The 220-1202 document doesn't
  mention it. Give it a minute in 021 as a work habit, nothing more.
- **Wi-Fi 7 isn't named.** Objective 2.2 lists "802.11 standards" and the
  2.4, 5 and 6 GHz bands, without naming generations. The 6 GHz band
  means Wi-Fi 6E. In 005, cover Wi-Fi 4 to 6E properly, and Wi-Fi 7
  (802.11be) as a bonus.
- **MDM is a Core 1 topic.** Objective 1.3 lists MDM device
  configurations (corporate and BYOD), policy enforcement and corporate
  applications. It comes back in Core 2 (2.1 and 2.8).
- **Display types and attributes are Hardware (3.1),** not Mobile
  Devices. 002 covers all of 3.1: LCD types (IPS, TN, VA), OLED,
  mini-LED, touch screen/digitizer, inverter, pixel density, refresh
  rate, resolution and color gamut.
- **Printers.** Objective 3.8 lists only maintenance tasks for laser,
  inkjet, thermal and impact printers. The laser imaging process isn't
  listed, so in 018 explain it only enough to make sense of print
  defects in 025 (speckling, echo images, faded prints). 3D printers
  aren't in any objective, but CompTIA's sample hardware list includes
  one, so a sentence on filament and resin is enough.
- **No "choosing PC components" objective.** That part was dropped
  from 016. Socket and multisocket compatibility are in 3.5, so they
  go in 015.
- **VDI is objective 4.1 (virtualization),** not 4.2 (cloud).
- **Ports (004):** SNMP isn't on the 220-1201 list. The list is 20-21
  FTP, 22 SSH, 23 Telnet, 25 SMTP, 53 DNS, 67/68 DHCP, 80 HTTP, 110 POP3,
  137-139 NetBIOS, 143 IMAP, 389 LDAP, 443 HTTPS, 445 SMB/CIFS and
  3389 RDP.
- **Busy episodes:** 032 (two long objectives) and 043 (four objectives)
  are dense. Split them if they won't fit in 15 minutes.
