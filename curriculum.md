# CompTIA A+ episode plan

The order to write episodes in: Core 1 (exam 220-1201) first, then Core 2
(exam 220-1202). One line is one script in `episodes/`, about 15 minutes
long. Tick the box when the script is pushed.

The percentage after each domain is its share of that exam.

## Foundation

- [x] 001 The OSI model, layer by layer ([script](episodes/001-osi-model.txt))

## Core 1 (220-1201)

### Mobile Devices (13%)

- [x] 002 Laptop hardware: replacing RAM, storage, battery, keyboard; display types; biometrics ([script](episodes/002-laptop-hardware.txt))
- [ ] 003 Mobile connectivity and accessories: Bluetooth, NFC, hotspot, docks, sync, SIM/eSIM, MDM basics

### Networking (23%)

- [ ] 004 TCP and UDP ports and protocols to memorize
- [ ] 005 Network hardware: switches, routers, APs, PoE, firewalls, patch panels, ONT, cable modem
- [ ] 006 Wireless: 802.11 standards, 2.4/5/6 GHz bands, channels, Wi-Fi 6/6E/7, RFID, NFC
- [ ] 007 Network services: DNS records, DHCP scopes, reservations and exclusions, NTP, server roles
- [ ] 008 IPv4 and IPv6 addressing: public, private, APIPA, static vs dynamic, SOHO configuration
- [ ] 009 Internet connection types, network types, and networking tools (crimper, toner, Wi-Fi analyzer)

### Hardware (25%)

- [ ] 010 Cables and connectors
- [ ] 011 RAM and storage: DDR types, ECC, channels; HDD, SSD, NVMe, M.2; RAID levels
- [ ] 012 Motherboards, CPUs, BIOS/UEFI, Secure Boot, TPM, expansion cards, cooling
- [ ] 013 Power supplies and choosing PC components
- [ ] 014 Printers: the laser printing process, inkjet, thermal, impact, 3D; printer maintenance

### Virtualization and Cloud Computing (11%)

- [ ] 015 Virtualization: hypervisor types, VMs, containers, sandboxes
- [ ] 016 Cloud computing: IaaS, PaaS, SaaS; public, private, hybrid; elasticity; VDI

### Hardware and Network Troubleshooting (28%)

- [ ] 017 The CompTIA troubleshooting methodology, plus motherboard, RAM, CPU and power problems
- [ ] 018 Troubleshooting storage drives and displays
- [ ] 019 Troubleshooting mobile devices and printers
- [ ] 020 Troubleshooting network problems

## Core 2 (220-1202)

### Operating Systems (28%)

- [ ] 021 Windows editions, installs and upgrades, boot methods, partitions, file systems (NTFS, FAT32, exFAT, ReFS, ext4, XFS, APFS)
- [ ] 022 Windows tools: Task Manager, MMC snap-ins, Event Viewer, Disk Management, Settings
- [ ] 023 Windows command line: ipconfig, ping, tracert, netstat, nslookup, chkdsk, sfc, diskpart, gpupdate, gpresult, robocopy
- [ ] 024 Windows networking: workgroup vs domain, shares, mapped drives, firewall, proxy settings
- [ ] 025 macOS and Linux basics and essential commands
- [ ] 026 Installing apps, cloud productivity tools, deployment methods including zero-touch

### Security (28%)

- [ ] 027 Physical security and Active Directory basics: GPOs, OUs, login scripts, least privilege, MFA
- [ ] 028 Wireless security and authentication: WPA2, WPA3, RADIUS, TACACS+, Kerberos
- [ ] 029 Malware types, the malware removal process, and tools
- [ ] 030 Social engineering and attacks: phishing, vishing, tailgating, DoS, zero-day, SQL injection, XSS, supply chain, BEC
- [ ] 031 Securing Windows: Defender, firewall, users and groups, NTFS vs share permissions, UAC, BitLocker, EFS
- [ ] 032 Securing mobile devices and SOHO networks, browser security, data destruction

### Software Troubleshooting (23%)

- [ ] 033 Troubleshooting Windows: BSOD, slow systems, boot problems, services, profiles
- [ ] 034 Troubleshooting mobile OS and security issues

### Operational Procedures (21%)

- [ ] 035 Documentation, ticketing, asset and change management
- [ ] 036 Backups (3-2-1, full, incremental, differential), safety, ESD, environment
- [ ] 037 Professionalism, privacy and licensing, scripting basics, remote access, AI basics (bias, hallucinations, public vs private AI)

---

## Gaps against the official objectives

**How this was checked.** The official objectives PDFs for 220-1201 and
220-1202 (V15) could not be downloaded: comptia.org, CompTIA's file
server and the mirror sites were all blocked by the network settings of
the cloud session that wrote this file. So this check uses search-result
excerpts from those documents and from study guides that follow their
numbering, plus the known structure of the V15 objectives. The domain
names and weights above agree across several sources. Objective numbers
below are approximate. Before relying on this list, compare it with the
current PDFs, linked from CompTIA's
[A+ V15 page](https://www.comptia.org/en/certifications/a/core-1-and-2-v15/).

### Core 1: missing from the list

- **VLANs and VPNs.** They share an objective with DNS and DHCP
  (network configuration concepts), but no episode covers them. Add them
  to 007, or to 008.
- **Other networked hosts.** Internet appliances (spam gateways, UTM,
  load balancers, proxy servers), legacy and embedded systems (SCADA),
  and IoT devices. Add them to 007 next to the server roles.
- **Multifunction devices and printer setup.** This is its own objective:
  drivers (PCL vs PostScript), USB, Ethernet and wireless connections,
  printer sharing and print servers, settings (duplex, orientation, trays,
  quality), security (user authentication, badging, audit logs, secured
  prints), and scan to email, SMB or cloud. 014 already has a lot to
  cover, so consider splitting it into two episodes: printer setup, then
  printer types and maintenance.

### Core 1: on the list, but give these airtime

- **DNS records (007):** A, AAAA, CNAME, MX and TXT, plus the email
  anti-spam records SPF, DKIM and DMARC.
- **Networking tools (009):** the full list also has cable stripper,
  punchdown tool, cable tester, loopback plug and network tap.
- **Display troubleshooting (018):** projectors are part of it.
  **Storage troubleshooting (018):** RAID arrays are part of it.
- **Display types and attributes** moved from Mobile Devices to Hardware
  in V15 (resolution, refresh rate, pixel density, color gamut, mini-LED).
  002 covers them for laptops. Repeat them briefly with monitors in 010
  or 018.
- **MDM (003):** reports on what changed in V15 say MDM and MAM were
  removed from the Core 1 mobile objectives. They are still tested in
  Core 2 (logical security and securing mobile devices), so spend more
  time on them in 027 and 032 than in 003.
- **Troubleshooting methodology (017):** the same V15 change reports say
  the six steps are printed in the 220-1201 objectives document but are
  no longer a numbered objective. They are still worth knowing, and
  Core 2 uses them, but keep that part of 017 short.
- **Wi-Fi 7 / 802.11be (006):** no source confirmed it is in the V15
  objectives. The 6 GHz band and Wi-Fi 6E are. Treat Wi-Fi 7 as a bonus.

### Core 2: missing from the list

- **Incident response.** It is in the same objective as privacy and
  licensing: chain of custody, order of volatility, making a copy of the
  drive (data integrity and preservation), documenting the incident, and
  informing management or law enforcement. That objective also covers
  regulated data: PII, credit card data, healthcare data,
  government-issued IDs, and data retention. 037 is already the most
  crowded episode, so consider splitting it in two: (a) professionalism,
  privacy, licensing and incident response; (b) scripting, remote access
  and AI.
- **Workstation hardening.** Password rules (length, complexity,
  expiration), BIOS/UEFI passwords, screen locks, account lockout after
  failed attempts, login-time restrictions, disabling the guest account,
  changing the default admin account, disabling AutoRun and AutoPlay, and
  encrypting data at rest. Add this to 031.
- **Logical security concepts.** Zero trust, ACLs, SSO, SAML,
  just-in-time access, PAM, DLP, IAM and directory services. Also the MFA
  methods (authenticator app, hardware token, SMS, voice call, TOTP and
  one-time passcodes, email), and physical controls like bollards, access
  control vestibules, badge readers, video surveillance, motion sensors
  and magnetometers. Add these to 027, which may need two episodes.
- **Other operating systems.** iOS, iPadOS, Android and ChromeOS, vendor
  life cycles (end of life, update limits), and compatibility concerns.
  Add them to 021 or 025.
- **PC and browser security symptoms.** Pop-ups, browser redirects,
  certificate warnings, false antivirus alerts, missing or renamed files,
  and failed OS updates. 034 only mentions mobile, so add these to it.

### Core 2: on the list, but give these airtime

- **Malware tools (029):** EDR, MDR, XDR, email security gateways and
  the recovery console. Malware types include cryptominers, stalkerware,
  fileless malware and PUPs.
- **Social engineering (030):** also smishing, QR code phishing, whaling,
  evil twin, on-path attacks, brute force and dictionary attacks, insider
  threats, and vulnerabilities like unpatched, end-of-life and BYOD
  devices.
- **Windows settings (022):** Control Panel vs Settings, power options
  (sleep, hibernate, fast startup, USB selective suspend), and File
  Explorer options (hidden files, file extensions).
- **Installing apps (026):** 32-bit vs 64-bit, integrated vs dedicated
  graphics and VRAM, and the impact on the device, network, operation and
  business. For cloud productivity tools: identity synchronization and
  license assignment.
- **SOHO and browser security (032):** UPnP, screened subnets, port
  forwarding, guest Wi-Fi, secure DNS, and checking downloads with hashes.
- **Backups (036):** synthetic full backups, the GFS rotation scheme,
  on-site vs off-site copies, and testing backups.
- **Environment (036):** safety data sheets, battery and toner disposal,
  temperature and humidity, surge suppressors and UPS.
- **Remote access (037):** RDP, VPN, VNC, SSH, RMM, Windows Remote
  Assistance, screen-sharing and file transfer tools, and the security
  risks of each.
