p = [
    {
        "question": "A coworker is complaining that their tablet’s screen no longer auto-rotates when changing device orientation. The feature was working earlier in the day but suddenly stopped. Auto-rotate is enabled in the settings, but the issue persists. How would the user most likely be able to solve this issue?",
        "options": {
            "A": "Calibrate the device’s accelerometer and gyroscope sensors",
            "B": "Replace the tablet’s screen since it is causing software issues",
            "C": "Change the screen timeout settings to a longer timeout period",
            "D": "Perform a full device wipe and restore from backup"
        },
        "answer": "A",
        "explanation": "If the auto-rotate feature stops working, the sensors that detect movement may need recalibration. This is the simplest solution before trying extreme measures like wiping the device.",
        "objective": "Mobile device troubleshooting"
    },
    {
        "question": "Dion Training has an open wireless network called 'InstructorDemos' for instructors to use during class. They do not want any students connecting to this network. The network must remain open since some IoT devices do not support encryption. Which configuration setting should you use?",
        "options": {
            "A": "NAT",
            "B": "Signal strength",
            "C": "QoS",
            "D": "MAC filtering"
        },
        "answer": "D",
        "explanation": "MAC filtering allows only specific devices (by their hardware address) to connect to the network. This prevents students’ devices from joining while still allowing IoT devices that need the open connection.",
        "objective": "Wireless network access control"
    },
    {
        "question": "Which of the following types of attacks is conducted against a database server by inserting code into an entry field on a web application form to try and gain access?",
        "options": {
            "A": "On-path attack",
            "B": "Cross-site scripting",
            "C": "Zero-day attack",
            "D": "SQL injection"
        },
        "answer": "D",
        "explanation": "SQL injection happens when an attacker enters malicious code into a form field to trick the database into revealing or changing information.",
        "objective": "Database attack methods"
    },
    {
        "question": "A client complains that their smartphone is warm and the battery only lasts 4 hours a day. Settings show: Email (never), Maps (always), Calendar (while using), Messages (while using), Photos (never), App Store (while using), Bank (while using), Weather (while using). What should be changed to fix the problem?",
        "options": {
            "A": "Change the Email setting to while using",
            "B": "Change the App Store to never",
            "C": "Change the Maps setting to while using",
            "D": "Change the Weather setting to always"
        },
        "answer": "C",
        "explanation": "Having Maps set to 'always' drains battery because GPS constantly runs in the background. Changing it to 'while using' saves power.",
        "objective": "Mobile device power management"
    },
    {
        "question": "You are going to replace a power supply in a desktop computer. Which of the following actions should you take FIRST?",
        "options": {
            "A": "Remove any jewelry you are wearing",
            "B": "Dispose of the old power supply",
            "C": "Verify proper cable management is being used",
            "D": "Use a grounding probe to discharge the power supply"
        },
        "answer": "A",
        "explanation": "Jewelry can conduct electricity and cause injury when working inside a computer. Removing it is the safest first step.",
        "objective": "Workplace safety"
    },
    {
        "question": "Your friend is concerned that someone might be listening to her conversations when her smartphone is in her purse. Which of the following threats is this an example of?",
        "options": {
            "A": "Unintended Bluetooth pairing",
            "B": "Unauthorized microphone activation",
            "C": "Unauthorized account access",
            "D": "Unauthorized location tracking"
        },
        "answer": "B",
        "explanation": "If someone activates a phone’s microphone without permission, they can eavesdrop on private conversations.",
        "objective": "Mobile device security threats"
    },
    {
        "question": "You just finished installing a new workstation for a user. They need to be able to see other workstations in the company’s workgroup. Which setting should you ensure is enabled?",
        "options": {
            "A": "Enable an RDP connection",
            "B": "Enable network discovery",
            "C": "Enable BitLocker",
            "D": "Enable file and folder sharing"
        },
        "answer": "B",
        "explanation": "Network discovery lets a computer find other devices on the same network, which is needed in a workgroup setup.",
        "objective": "Windows networking configuration"
    },
    {
        "question": "Which of the following best describes how cloud-based spreadsheets enhance team collaboration?",
        "options": {
            "A": "Only the spreadsheet owner can view or modify the document",
            "B": "Each user must download and re-upload the file to apply their updates",
            "C": "Changes made by one user appear in real time for all users with access",
            "D": "Editing is locked while another user is working to prevent conflicts"
        },
        "answer": "C",
        "explanation": "Cloud spreadsheets allow real-time updates, so all team members see changes instantly without needing to re-upload files.",
        "objective": "Cloud collaboration"
    },
    {
        "question": "Which of the following is used to communicate data and preferences to child processes within a script or batch file?",
        "options": {
            "A": "Environmental variables",
            "B": "Constants",
            "C": "Comments",
            "D": "Variables"
        },
        "answer": "A",
        "explanation": "Environmental variables store settings that can be passed to other programs or processes when a script runs.",
        "objective": "Scripting concepts"
    },
    {
        "question": "Which partition of the hard drive is concealed from the user in File Explorer in Windows 10 and is only used when restoring the computer to factory default state?",
        "options": {
            "A": "Swap",
            "B": "Extended",
            "C": "Primary",
            "D": "Recovery"
        },
        "answer": "D",
        "explanation": "The recovery partition is hidden from users and contains files needed to restore the computer back to factory settings.",
        "objective": "Disk partitioning & recovery"
    },
    {
        "question": "Sally noticed she had several automated replies to emails she doesn’t remember sending. What type of attack was Sally MOST likely the victim of?",
        "options": {
            "A": "Spear phishing",
            "B": "Phishing",
            "C": "Hijacked email",
            "D": "Vishing"
        },
        "answer": "C",
        "explanation": "Her account was taken over (hijacked), and attackers used it to send spam or malicious messages.",
        "objective": "Email security threats"
    },
    {
        "question": "A co-worker sent you a macro-enabled Microsoft Word document. After opening it, your computer began deleting photos. What type of malware did you MOST likely receive?",
        "options": {
            "A": "Virus",
            "B": "Rootkit",
            "C": "Trojan",
            "D": "Worm"
        },
        "answer": "C",
        "explanation": "Macro-enabled files often hide Trojans, which trick users into running malicious code disguised as legitimate software.",
        "objective": "Malware identification"
    },
    {
        "question": "Employees frequently access confidential company information through web-based apps. To increase security, IT recommends disabling certain browser features. Which feature should be disabled?",
        "options": {
            "A": "Automatic updates for the browser",
            "B": "Automatic clearing of browsing history",
            "C": "Browser pop-up blocker",
            "D": "JavaScript execution"
        },
        "answer": "D",
        "explanation": "Disabling JavaScript helps prevent script-based attacks, which are a common way attackers exploit browsers.",
        "objective": "Browser security"
    },
    {
        "question": "A cybersecurity analyst finds that USB devices were inserted into servers and logs show failed login attempts. Which TWO actions are recommended?",
        "options": {
            "A": "Install the operating system security updates",
            "B": "Remove administrative permissions",
            "C": "Change the default credentials on the servers",
            "D": "Lockout the account after 3 failed login attempts",
            "E": "Modify the AutoRun settings",
            "F": "Install a host-based firewall on the servers"
        },
        "answer": [
            "C",
            "D"
        ],
        "explanation": "Changing default credentials prevents easy access, and locking out accounts after failed attempts stops brute-force attacks.",
        "objective": "Server hardening & account security"
    },
    {
        "question": "A technician wants to conduct a vulnerability scan on a server every morning at 3:00 am. Which tool should they use?",
        "options": {
            "A": "Task scheduler",
            "B": "PerfMon",
            "C": "Event viewer",
            "D": "MSConfig"
        },
        "answer": "A",
        "explanation": "Task Scheduler lets administrators run tasks like scans automatically at set times.",
        "objective": "System administration automation"
    },
    {
        "question": "During penetration test reconnaissance, you find that client employees use Android devices over a VPN. What method would MOST likely be the best for exploiting these?",
        "options": {
            "A": "Use a tool like ICSSPLOIT",
            "B": "Identify a jailbroken device for easy exploitation",
            "C": "Use social engineering to trick a user into opening a malicious APK",
            "D": "Use web-based exploits against device web interfaces"
        },
        "answer": "C",
        "explanation": "Social engineering tricks users into installing malicious apps (APKs), which is a common Android attack method.",
        "objective": "Penetration testing techniques"
    },
    {
        "question": "Which type of authentication method is commonly used with physical access systems that rely on RFID devices embedded into a token?",
        "options": {
            "A": "TOTP",
            "B": "Pre-Shared Key",
            "C": "Proximity cards",
            "D": "HOTP"
        },
        "answer": "C",
        "explanation": "Proximity cards use RFID to grant or deny access to physical locations, like office doors.",
        "objective": "Physical security authentication"
    },
    {
        "question": "Charlie’s operating system is corrupted, but personal files and applications are intact. You need to reinstall the OS without deleting data or programs. Which recovery method is BEST?",
        "options": {
            "A": "Image-based recovery",
            "B": "In-place recovery",
            "C": "File-level restore",
            "D": "Clean install"
        },
        "answer": "B",
        "explanation": "In-place recovery reinstalls the operating system while keeping user data and installed applications safe.",
        "objective": "Operating system recovery methods"
    },
    {
        "question": "During a training session, an IT instructor explains the purpose of valid website certificates. How should the instructor accurately describe a valid security certificate?",
        "options": {
            "A": "A browser plug-in ensuring that websites load as quickly as possible.",
            "B": "A software update issued regularly to enhance browser security settings.",
            "C": "A privacy setting preventing websites from tracking browsing activities.",
            "D": "A digital document confirming the website’s identity and secure connection."
        },
        "answer": "D",
        "explanation": "A valid website certificate is like an ID card for a website. It confirms the website's identity and ensures the connection is secure and encrypted.",
        "objective": "Web security & certificates"
    },
    {
        "question": "Jason's iPhone has not received any emails or SMS messages in the last 4 hours. Which of the following is the most likely cause of these issues?",
        "options": {
            "A": "Internet connectivity failure",
            "B": "Mail client error",
            "C": "OS update failure",
            "D": "Bluetooth connectivity failure"
        },
        "answer": "A",
        "explanation": "If both emails and text messages are not being received, the most likely cause is a problem with the phone’s internet connection.",
        "objective": "Mobile device troubleshooting"
    },
    {
        "question": "An offsite tape backup storage facility is involved with a forensic investigation. The facility has been told they cannot recycle their outdated tapes until the conclusion of the investigation. Which of the following is the MOST likely reason for this?",
        "options": {
            "A": "The process of discovery",
            "B": "A chain of custody breach",
            "C": "A data transport request",
            "D": "A notice of a legal hold"
        },
        "answer": "D",
        "explanation": "A legal hold requires organizations to keep data (like backup tapes) unchanged until an investigation or court case is finished.",
        "objective": "Data retention & legal compliance"
    },
    {
        "question": "You are a member of a project team contracted to install twenty new wireless access points (WAPs) for a college campus. The project cannot move forward with the installation until the change request is finalized and approved. Which of the following is the MOST important thing from the IT perspective to add to the scope of work and change request before its approval?",
        "options": {
            "A": "Risk analysis",
            "B": "End-user acceptance",
            "C": "Plan for change",
            "D": "Rollback plan"
        },
        "answer": "D",
        "explanation": "A rollback plan ensures that if the installation causes problems, the system can be quickly returned to its previous working state.",
        "objective": "Change management & planning"
    },
    {
        "question": "A network administrator set up a firewall but users cannot access websites. Which of the following should the administrator do to correct this issue?",
        "options": {
            "A": "Add a rule to the ACL to allow traffic on ports 143 and 22",
            "B": "Add a rule to the ACL to allow traffic on ports 139 and 445",
            "C": "Add a rule to the ACL to allow traffic on ports 110 and 389",
            "D": "Add a rule to the ACL to allow traffic on ports 80 and 53"
        },
        "answer": "D",
        "explanation": "Websites use port 80 (HTTP) and port 53 (DNS). Allowing these through the firewall lets users access web pages normally.",
        "objective": "Firewall configuration & troubleshooting"
    },
    {
        "question": "Karen lives in an area that is prone to hurricanes and other extreme weather conditions. She wants her computer protected from sudden power loss and to keep running long enough for a safe shutdown. Which of the following should you recommend?",
        "options": {
            "A": "Line conditioner",
            "B": "Uninterruptible power supply",
            "C": "Surge protector",
            "D": "Power distribution unit"
        },
        "answer": "B",
        "explanation": "A UPS provides backup battery power during outages, allowing time to save work and shut down safely.",
        "objective": "Power protection & continuity"
    },
    {
        "question": "Dion Training has set up a lab of 12 laptops. The instructor is worried that a student may try to steal one. Which of the following physical security measures should be used?",
        "options": {
            "A": "Biometric locks",
            "B": "Cable locks",
            "C": "Key fob",
            "D": "USB lock"
        },
        "answer": "B",
        "explanation": "Cable locks physically secure laptops to desks, making it much harder to steal them.",
        "objective": "Physical security"
    },
    {
        "question": "Which mitigation provides the best return on investment by addressing the most vulnerable attack vector in an enterprise network?",
        "options": {
            "A": "Provide end-user awareness training for office staff",
            "B": "Remove unneeded services running on servers",
            "C": "Update all antivirus definitions on workstations and servers",
            "D": "Enable biometrics and SSO for authentication"
        },
        "answer": "A",
        "explanation": "Humans are the weakest link in security. Training staff to recognize phishing and other threats reduces the biggest risks at low cost.",
        "objective": "Security awareness & training"
    },
    {
        "question": "Which of the following attacks occurs when an attacker sends targeted emails to a specific group within an organization to steal confidential information?",
        "options": {
            "A": "Spear phishing",
            "B": "Spoofing",
            "C": "Phishing",
            "D": "Zero-day"
        },
        "answer": "A",
        "explanation": "Spear phishing is a targeted phishing attack aimed at specific people or groups, making it more convincing than regular phishing.",
        "objective": "Cyberattack identification"
    },
    {
        "question": "What is the name of a program that monitors user activity and sends that information to someone else?",
        "options": {
            "A": "Keylogger",
            "B": "Spyware",
            "C": "Virus",
            "D": "Rootkit"
        },
        "answer": "B",
        "explanation": "Spyware secretly tracks user activity and shares it with others, often for malicious purposes.",
        "objective": "Malware identification"
    },
    {
        "question": "You are upgrading the memory of a laptop. After removing the old memory chips, where should you safely store them until reuse?",
        "options": {
            "A": "Cardboard box",
            "B": "Antistatic bag",
            "C": "Manila envelopes",
            "D": "Ziplock bags"
        },
        "answer": "B",
        "explanation": "Antistatic bags prevent damage from static electricity, keeping memory chips safe until reuse.",
        "objective": "Hardware handling & safety"
    },
    {
        "question": "Your Windows 10 machine just crashed. Where should you look to identify the cause of the system crash and how to fix it?",
        "options": {
            "A": "DDOS",
            "B": "MAC",
            "C": "POST",
            "D": "BSOD"
        },
        "answer": "D",
        "explanation": "The Blue Screen of Death (BSOD) shows error codes and details about why Windows crashed, helping diagnose the problem.",
        "objective": "System crash troubleshooting"
    },
    {
        "question": "Which physical security control would be most effective in preventing a vehicle attack through the front doors of a building?",
        "options": {
            "A": "Access control vestibule",
            "B": "Security guards",
            "C": "Bollards",
            "D": "Intrusion alarm"
        },
        "answer": "C",
        "explanation": "Bollards are strong posts placed outside buildings to physically block vehicles from ramming entrances.",
        "objective": "Physical security & perimeter defense"
    },
    {
        "question": "Which file system type is used to mount remote storage devices on a Linux system?",
        "options": {
            "A": "APFS",
            "B": "NTFS",
            "C": "NFS",
            "D": "exFAT"
        },
        "answer": "C",
        "explanation": "NFS (Network File System) is designed for Linux/Unix systems to access files over a network as if they were local.",
        "objective": "Linux & file systems"
    },
    {
        "question": "You have submitted a request to install a security patch on company servers. Which change request document would describe how the installation will be performed?",
        "options": {
            "A": "Risk analysis",
            "B": "Purpose",
            "C": "Plan",
            "D": "Scope"
        },
        "answer": "C",
        "explanation": "The plan describes the step-by-step process for how the patch will be installed during maintenance.",
        "objective": "Change management documentation"
    },
    {
        "question": "You attempt to boot a Windows 10 laptop and see 'Operating System Not Found'. The hard disk is listed in BIOS. Which command should you use to repair the boot sector?",
        "options": {
            "A": "bootrec /fixboot",
            "B": "bootrec /fixmbr",
            "C": "diskpart list",
            "D": "bootrec /rebuildbcd"
        },
        "answer": "A",
        "explanation": "The command 'bootrec /fixboot' repairs the boot sector, which is often the cause of 'Operating System Not Found' errors.",
        "objective": "Windows boot troubleshooting"
    },
    {
        "question": "After a company rolls out software updates, Ann can no longer use lab equipment due to driver incompatibility. Which should the technician do to get her working again quickly?",
        "options": {
            "A": "Downgrade the PC to a working patch level",
            "B": "Restore Ann's PC to the last known good configuration",
            "C": "Rollback the drivers to the previous version",
            "D": "Reset Ann's equipment configuration from a backup"
        },
        "answer": "C",
        "explanation": "Rolling back the drivers to the previous version quickly restores compatibility without affecting the rest of the system.",
        "objective": "Driver & update troubleshooting"
    },
    {
        "question": "Several users report receiving emails from a well-known bank asking them to reset their passwords, even though they are not customers of that bank. What type of attack is this?",
        "options": {
            "A": "Spear phishing",
            "B": "Brute force",
            "C": "Whaling",
            "D": "Phishing"
        },
        "answer": "D",
        "explanation": "This is general phishing — a broad attack designed to trick many users into clicking links or giving up information.",
        "objective": "Email security & social engineering"
    },
    {
        "question": "You are working as a service desk analyst. This morning, you have received multiple calls from users reporting that they cannot access websites from their work computers. You decide to troubleshoot the issue by running a program to determine where the network connectivity outage is occurring. Which tool should you use to determine if the issue is on the intranet portion of your corporate network or if it is occurring due to a problem with your ISP?",
        "options": {
            "A": "netstat",
            "B": "nslookup",
            "C": "tracert",
            "D": "ping"
        },
        "answer": "C",
        "explanation": "The tracert (traceroute) command shows each hop between your computer and the destination, helping identify where the connection fails. This makes it useful to distinguish between local network vs ISP issues.",
        "objective": "Network troubleshooting"
    },
    {
        "question": "A company rolls out a cloud-based application that syncs constantly with remote servers. Employees report slow internet speeds after the installation. What is the most likely reason?",
        "options": {
            "A": "The application is using too much bandwidth for data transfers",
            "B": "The local network is too outdated for the application",
            "C": "The firewall is blocking cloud traffic, slowing the internet",
            "D": "Employee computers are overloaded by the application"
        },
        "answer": "A",
        "explanation": "Cloud-syncing applications transfer a lot of data, which can overwhelm available bandwidth and slow down internet performance for everyone.",
        "objective": "Cloud application performance"
    },
    {
        "question": "A government agency is retiring hard drives containing classified data. Agency guidelines require an irreversible method that prevents data retrieval. Which method aligns with this guideline?",
        "options": {
            "A": "Storing retired drives securely in locked storage units",
            "B": "Removing files using a specialized secure deletion tool",
            "C": "Exposing the drives to a high-powered magnetic degausser device",
            "D": "Using standard formatting procedures on each hard drive"
        },
        "answer": "C",
        "explanation": "A degausser permanently erases data by disrupting the magnetic fields on the drive, making recovery impossible. Formatting or deletion tools may still allow recovery.",
        "objective": "Data destruction & security"
    },
    {
        "question": "Which of the following features allows a Linux server to provide file-sharing services to a company’s Windows 10 workstations?",
        "options": {
            "A": "Samba",
            "B": "Pathping",
            "C": "Yum",
            "D": "Keychain"
        },
        "answer": "A",
        "explanation": "Samba allows Linux systems to share files and printers with Windows machines, making cross-platform file sharing possible.",
        "objective": "Cross-platform file sharing"
    },
    {
        "question": "Which attack utilizes a wireless access point made to look as if it belongs to the network by mimicking the corporate network's SSID to eavesdrop on wireless traffic?",
        "options": {
            "A": "Shoulder surfing",
            "B": "Evil twin",
            "C": "WEP attack",
            "D": "Rogue access point"
        },
        "answer": "B",
        "explanation": "An Evil Twin attack creates a fake Wi-Fi network with the same name as the real one, tricking users into connecting so attackers can steal data.",
        "objective": "Wireless attack methods"
    },
    {
        "question": "A local business has outsourced its cloud storage to an external provider. The IT manager needs to ensure uptime, availability, and support response times are guaranteed and enforceable. Which of the following would BEST ensure this?",
        "options": {
            "A": "BCP",
            "B": "EULA",
            "C": "SLA",
            "D": "SLO"
        },
        "answer": "C",
        "explanation": "A Service Level Agreement (SLA) is a formal contract that defines service guarantees such as uptime and response times, making them legally enforceable.",
        "objective": "Vendor management & SLAs"
    },
    {
        "question": "Jack has asked you for a recommendation on which word processing software they should install so their son can create school reports. Which of the following would MOST likely be the best option?",
        "options": {
            "A": "Enterprise",
            "B": "Personal",
            "C": "Open-source",
            "D": "Business"
        },
        "answer": "B",
        "explanation": "Since the software is for home and school use, the personal license is the most cost-effective and appropriate choice.",
        "objective": "Software licensing"
    },
    {
        "question": "Your IT administrator has proposed a new method for deploying security patches to company servers. Before the change is approved, another senior administrator reviews the plan. Which of the following BEST describes this step?",
        "options": {
            "A": "Implementation",
            "B": "Change freeze",
            "C": "Standard change",
            "D": "Peer review"
        },
        "answer": "D",
        "explanation": "Peer review involves having another qualified person check the plan for risks, compliance, and best practices before approval.",
        "objective": "Change management process"
    },
    {
        "question": "Tim has requested to install a security update to a web server during the next maintenance window. After approval from the change board, what should be documented as a result?",
        "options": {
            "A": "Risk level of the change",
            "B": "Affected systems/impact of the change",
            "C": "Date and time of the change",
            "D": "Purpose of the change"
        },
        "answer": "C",
        "explanation": "Once a change is approved, the date and time are scheduled to ensure proper planning and communication across teams.",
        "objective": "Change documentation"
    },
    {
        "question": "Another technician tells you they are PXE booting a computer. What is the technician MOST likely doing?",
        "options": {
            "A": "Installing an image to the computer over the network",
            "B": "An in-place upgrade of the OS",
            "C": "Using a multiboot configuration",
            "D": "Conducting a system repair"
        },
        "answer": "A",
        "explanation": "PXE (Preboot Execution Environment) allows a computer to boot from a network and install an operating system image remotely.",
        "objective": "Remote installation methods"
    },
    {
        "question": "You are troubleshooting a network issue and need to determine the packet's flow path from your system to the remote server. Which tool would best help?",
        "options": {
            "A": "nbtstat",
            "B": "ipconfig",
            "C": "netstat",
            "D": "tracert"
        },
        "answer": "D",
        "explanation": "Tracert shows the route packets take, hop by hop, which helps identify where the connection slows or breaks.",
        "objective": "Network diagnostics"
    },
    {
        "question": "Dion Training wants to implement WPA3 in their offices. Which feature of WPA3 provides password-based authentication using the dragonfly handshake instead of the WPA2 4-way handshake?",
        "options": {
            "A": "Enhanced open",
            "B": "AES GCMP",
            "C": "Management protection frames",
            "D": "SAE"
        },
        "answer": "D",
        "explanation": "Simultaneous Authentication of Equals (SAE) is the WPA3 feature that replaces WPA2's 4-way handshake, providing stronger protection against brute-force attacks.",
        "objective": "Wi-Fi security protocols"
    },
    {
        "question": "Which of the following backup types requires the LEAST time to complete?",
        "options": {
            "A": "Incremental",
            "B": "Differential",
            "C": "Synthetic",
            "D": "Full"
        },
        "answer": "A",
        "explanation": "Incremental backups only save changes since the last backup, making them much faster than full or differential backups.",
        "objective": "Backup strategies"
    },
    {
        "question": "A customer's Android smartphone is only 6 months old but is slowing down after installing a new stock market app. What should you do to troubleshoot?",
        "options": {
            "A": "Factory reset the smartphone and reinstall all apps",
            "B": "Perform a hard reboot of the smartphone",
            "C": "Uninstall the app, reboot the phone, and reinstall the app",
            "D": "Replace the phone with a newer model"
        },
        "answer": "C",
        "explanation": "The problem started after installing a specific app, so uninstalling and reinstalling it is the best first troubleshooting step.",
        "objective": "Mobile device troubleshooting"
    },
    {
        "question": "A company is integrating an AI-powered virtual assistant into its communication system. The legal team is concerned about sensitive information being accessible externally. What is the MOST important concern?",
        "options": {
            "A": "System update frequency",
            "B": "User interface design",
            "C": "Data privacy",
            "D": "Software licensing terms"
        },
        "answer": "C",
        "explanation": "Data privacy is the primary concern because sensitive business information could be exposed if the AI system stores or shares data insecurely.",
        "objective": "AI integration & security"
    },
    {
        "question": "A school district plans to repurpose classroom computers for general public use. To quickly prepare the drives without using specialized software, which method should they use?",
        "options": {
            "A": "Performing standard formatting on the hard drives",
            "B": "Running antivirus software to clean malware",
            "C": "Using advanced encryption to protect stored data",
            "D": "Physically drilling into the drives before reuse"
        },
        "answer": "A",
        "explanation": "A quick format removes access to existing data and prepares drives for reuse, though data may still be recoverable if specialized recovery tools are used.",
        "objective": "Data sanitization for reuse"
    },
    {
        "question": "Which command-line tool is used on a Windows system to display a list of files and directories within the current path?",
        "options": {
            "A": "ls",
            "B": "dir",
            "C": "chkdsk",
            "D": "sfc"
        },
        "answer": "B",
        "explanation": "The 'dir' command lists files and folders in the current directory on Windows systems. 'ls' is used on Linux/Mac.",
        "objective": "Windows command-line basics"
    },
    {
        "question": "You receive a ticket where a user reports frequent 'Low Memory' warnings on a Windows 10 laptop with 4 GB RAM while multitasking. What is the BEST solution?",
        "options": {
            "A": "Increase the laptop's virtual memory (paging file)",
            "B": "Reinstall the operating system",
            "C": "Upgrade the physical RAM in the laptop",
            "D": "Close unused applications and browser tabs"
        },
        "answer": "C",
        "explanation": "Adding more physical RAM provides a long-term fix that allows smoother multitasking compared to temporary workarounds like closing tabs.",
        "objective": "PC hardware troubleshooting"
    },
    {
        "question": "Which Linux command displays the current working directory’s full pathname to the screen?",
        "options": {
            "A": "pwd",
            "B": "passwd",
            "C": "chown",
            "D": "chmod"
        },
        "answer": "A",
        "explanation": "The 'pwd' (print working directory) command shows the absolute path of the current directory.",
        "objective": "Linux command basics"
    },
    {
        "question": "A smartphone user notices their phone gets very hot and the battery drains quickly, even when not in use. What is the most likely problem?",
        "options": {
            "A": "The charging port is faulty",
            "B": "The battery is depleted",
            "C": "The smartphone is using a lot of processing power",
            "D": "The touchscreen is faulty"
        },
        "answer": "C",
        "explanation": "Excessive processing (apps running in the background, malware, or heavy apps) causes overheating and fast battery drain.",
        "objective": "Smartphone troubleshooting"
    },
    {
        "question": "During a penetration test, four passwords were found: Pa55w0rd, P@$$WORD, P@$$w0rd, and pa55word. Which is the weakest and should be changed FIRST?",
        "options": {
            "A": "Pa55w0rd",
            "B": "P@$$WORD",
            "C": "P@$$w0rd",
            "D": "pa55word"
        },
        "answer": "D",
        "explanation": "The password 'pa55word' is weak because it is all lowercase letters with minimal substitutions, making it easy to crack.",
        "objective": "Password security"
    },
    {
        "question": "Dion Training uses Windows 10 Pro workstations in a domain environment. The company wants users to encrypt local hard drives for security. Which setting can be used?",
        "options": {
            "A": "Encrypting File System",
            "B": "BitLocker to Go",
            "C": "FileVault",
            "D": "BitLocker"
        },
        "answer": "D",
        "explanation": "BitLocker is a Windows feature that encrypts entire hard drives to protect data if the computer is lost or stolen. FileVault is for Mac.",
        "objective": "Data encryption"
    },
    {
        "question": "A user cannot change their iPad display from landscape to portrait when they are on the home screen. Which of the following is MOST likely the reason for this issue?",
        "options": {
            "A": "Developer mode is enabled",
            "B": "Autorotate is disabled",
            "C": "Smartphone has overheated",
            "D": "NFC is disabled"
        },
        "answer": "B",
        "explanation": "If autorotate is turned off, the iPad won’t switch between landscape and portrait view. The other options don’t affect screen rotation.",
        "objective": "Mobile device troubleshooting"
    },
    {
        "question": "Dion Training uses DHCP to assign private Class A IP addresses to its Windows 10 workstations. Which of the following IP addresses is a Class A address?",
        "options": {
            "A": "169.254.1.52",
            "B": "192.168.3.5",
            "C": "172.18.21.252",
            "D": "10.1.2.3"
        },
        "answer": "D",
        "explanation": "Class A private addresses range from 10.0.0.0 to 10.255.255.255. Only option D falls into that range.",
        "objective": "IP addressing"
    },
    {
        "question": "Ahmed, a software developer, enables Developer Mode on his Windows 11 machine to test a custom-built application. After enabling the mode, he notices increased battery drain and occasional security prompts. What would be the best solution for him to maintain security while allowing continued app testing?",
        "options": {
            "A": "Turn off security warnings in Windows Security settings",
            "B": "Disable Developer Mode when not actively testing the application",
            "C": "Ignore the warnings and proceed with testing",
            "D": "Reinstall Windows 11 to remove risks"
        },
        "answer": "B",
        "explanation": "Leaving Developer Mode on can lower security. Turning it off when not needed balances safety and functionality.",
        "objective": "System configuration & security"
    },
    {
        "question": "A user with an older laptop running Windows 7 that has only 2 GB of RAM, 32 GB of SSD, and a 1.7 GHz 64-bit processor would like to upgrade. Which operating system should the technician recommend?",
        "options": {
            "A": "Windows 11",
            "B": "Windows 10",
            "C": "Windows 8",
            "D": "Windows 8.1"
        },
        "answer": "D",
        "explanation": "Windows 8.1 has lower hardware requirements and works better on older, low-resource laptops compared to Windows 10 or 11.",
        "objective": "OS compatibility & performance"
    },
    {
        "question": "Sarah is installing Windows 10 (64-bit) in a virtual machine. The installation fails with her settings: dual-core 950 MHz CPU, 4 GB RAM, 64 GB hard drive, 1280x720 screen resolution. Which item should be increased?",
        "options": {
            "A": "The amount of RAM is insufficient",
            "B": "The processor is insufficient",
            "C": "The screen resolution is insufficient",
            "D": "The amount of storage space is insufficient"
        },
        "answer": "B",
        "explanation": "Windows 10 requires at least a 1 GHz CPU. The 950 MHz CPU is too slow, so the processor needs upgrading.",
        "objective": "System requirements"
    },
    {
        "question": "An IT administrator needs to upgrade several computers running an operating system that has reached its End-of-Life (EOL). Which should be the FIRST step?",
        "options": {
            "A": "Disable security features to speed up the process",
            "B": "Back up critical files and settings",
            "C": "Migrate all data to the cloud",
            "D": "Uninstall unnecessary software"
        },
        "answer": "B",
        "explanation": "Before upgrading an operating system, always back up important data in case something goes wrong.",
        "objective": "Upgrade preparation"
    },
    {
        "question": "Which of the tools should a technician NOT use with a solid-state device on a workstation?",
        "options": {
            "A": "Device manager",
            "B": "Performance monitor",
            "C": "Disk defragmenter",
            "D": "Disk cleanup"
        },
        "answer": "C",
        "explanation": "Defragmenting an SSD can wear it out faster and is unnecessary, since SSDs don’t benefit from defragmentation.",
        "objective": "Storage device maintenance"
    },
    {
        "question": "A home user says applications are slow and emails aren’t coming in. The technician finds CPU normal, router reachable, but web pages load slowly and the remote session keeps dropping. What should the technician do NEXT?",
        "options": {
            "A": "Empty browser cache and send test email",
            "B": "Enable TPM in BIOS and do a System Restore",
            "C": "Uninstall last OS update and run CHKDSK",
            "D": "Update antivirus, run a full scan, and verify browser/email settings"
        },
        "answer": "D",
        "explanation": "Slow internet with email issues and dropped connections can indicate malware or altered settings. Scanning for malware and checking configurations is the next step.",
        "objective": "Troubleshooting performance & connectivity"
    },
    {
        "question": "What information should be recorded on a chain of custody form during a forensic investigation?",
        "options": {
            "A": "The list of former owners/operators of the workstation",
            "B": "Any individual who worked with evidence during the investigation",
            "C": "The law enforcement agent first on the scene",
            "D": "The list of individuals who made contact with files"
        },
        "answer": "B",
        "explanation": "A chain of custody form documents everyone who handles the evidence to maintain its integrity in legal proceedings.",
        "objective": "Forensics procedures"
    },
    {
        "question": "Your network administrator hands you documentation showing which switch ports on a patch panel to connect with a CAT 5e patch cable. What document is this?",
        "options": {
            "A": "Process flow diagram",
            "B": "Logical network diagram",
            "C": "Inventory management plan",
            "D": "Physical network diagram"
        },
        "answer": "D",
        "explanation": "A physical network diagram shows actual hardware connections like switches, patch panels, and cables.",
        "objective": "Network documentation"
    },
    {
        "question": "Which Control Panel option should a technician configure to automatically adjust sound volume when the computer is used for calls?",
        "options": {
            "A": "Sound",
            "B": "Programs and Features",
            "C": "USB selective suspend",
            "D": "Ease of Access"
        },
        "answer": "A",
        "explanation": "Sound settings include communication options to automatically adjust audio levels during calls.",
        "objective": "Windows configuration"
    },
    {
        "question": "Which command is used on a Linux system to edit a text file?",
        "options": {
            "A": "vi",
            "B": "chown",
            "C": "ps",
            "D": "pwd"
        },
        "answer": "A",
        "explanation": "The `vi` editor is used to edit text files. Other commands manage ownership, processes, or show the current directory.",
        "objective": "Linux commands"
    },
    {
        "question": "Which command is used to create a new disk partition on a Windows system?",
        "options": {
            "A": "diskpart",
            "B": "dd",
            "C": "chkdsk",
            "D": "format"
        },
        "answer": "A",
        "explanation": "Diskpart is the Windows utility for creating and managing partitions. The others are for copying, checking, or formatting drives.",
        "objective": "Disk management"
    },
    {
        "question": "A computer is infected with malware that hides in the Windows kernel. Which type of malware MOST likely infected this computer?",
        "options": {
            "A": "Rootkit",
            "B": "Botnet",
            "C": "Ransomware",
            "D": "Trojan"
        },
        "answer": "A",
        "explanation": "Rootkits hide deep inside the system, often in the kernel, to avoid detection.",
        "objective": "Malware identification"
    },
    {
        "question": "A user says Microsoft Excel crashed while updating their spreadsheet. Which log file should be reviewed?",
        "options": {
            "A": "Setup",
            "B": "Security log",
            "C": "Application log",
            "D": "System log"
        },
        "answer": "C",
        "explanation": "The Application log records events from programs like Excel, including crashes and errors.",
        "objective": "Windows event logs"
    },
    {
        "question": "A workstation at Dion Training is taking a long time to boot. Which tool can be used to diagnose and fix boot issues?",
        "options": {
            "A": "msconfig.exe",
            "B": "resmon.exe",
            "C": "perfmon.msc",
            "D": "msinfo32.exe"
        },
        "answer": "A",
        "explanation": "Msconfig lets you control startup programs and services to speed up boot time.",
        "objective": "Windows troubleshooting"
    },
    {
        "question": "Jason’s 2018 work laptop is very slow and has a cracked screen. He needs it for a 45-day trip because of the built-in security key. What should you recommend?",
        "options": {
            "A": "Purchase a new laptop",
            "B": "Sell him an external 15\" tablet/monitor",
            "C": "Replace the display and charge for repairs",
            "D": "Replace the display and contact manufacturer"
        },
        "answer": "B",
        "explanation": "Since he’ll be issued a new laptop soon, an external monitor is the cheapest temporary fix while still keeping access to the security key.",
        "objective": "Hardware troubleshooting"
    },
    {
        "question": "A new bank security employee wants to scan for unauthorized devices at 2 AM daily. Which programming language is best to script this?",
        "options": {
            "A": "C#",
            "B": "ASP.NET",
            "C": "PHP",
            "D": "Python"
        },
        "answer": "D",
        "explanation": "Python is commonly used for automation and scripting, and has libraries for network scanning.",
        "objective": "Scripting & automation"
    },
    {
        "question": "Your smartphone shows a notification that a new pair of headphones connected to it. Which threat is this?",
        "options": {
            "A": "Unauthorized microphone activation",
            "B": "Unauthorized account access",
            "C": "Unintended Bluetooth pairing",
            "D": "Unauthorized location tracking"
        },
        "answer": "C",
        "explanation": "This is an example of unintended Bluetooth pairing, which can be a security risk.",
        "objective": "Mobile security"
    },
    {
        "question": "You cannot access your company’s internal shared drive, but websites like DionTraining.com work. Which command should you use to check if the drive is mapped?",
        "options": {
            "A": "ping",
            "B": "net use",
            "C": "chkdsk",
            "D": "tracert"
        },
        "answer": "B",
        "explanation": "The `net use` command shows if network drives are connected and working.",
        "objective": "Network troubleshooting"
    },
    {
        "question": "Which mobile device strategy is most likely to introduce vulnerable devices to a corporate network?",
        "options": {
            "A": "CYOD",
            "B": "BYOD",
            "C": "MDM",
            "D": "COPE"
        },
        "answer": "B",
        "explanation": "Bring Your Own Device (BYOD) allows personal devices that may not be secure to connect to the network.",
        "objective": "Mobile device management"
    },
    {
        "question": "Which of the following components presents the largest risk of electrical shock to a technician?",
        "options": {
            "A": "CRT monitor",
            "B": "Hard drive",
            "C": "LCD monitor",
            "D": "Laptop battery"
        },
        "answer": "A",
        "explanation": "CRT monitors hold very high voltages even after being unplugged, making them dangerous.",
        "objective": "Safety"
    },
    {
        "question": "Maria is asked to enter her username and password to log into webmail. Which type of authentication is she using?",
        "options": {
            "A": "Multifactor",
            "B": "Single-factor",
            "C": "TACACS+",
            "D": "RADIUS"
        },
        "answer": "B",
        "explanation": "A username and password is only one factor (something you know), so it’s single-factor authentication.",
        "objective": "Authentication methods"
    },
    {
        "question": "Dion Training wants to use full disk encryption on their 2 TB internal drives in Windows 10 Professional. Which security setting can do this?",
        "options": {
            "A": "FileVault",
            "B": "BitLocker to Go",
            "C": "BitLocker",
            "D": "Encrypting File System"
        },
        "answer": "C",
        "explanation": "BitLocker encrypts the entire internal drive. FileVault is for Macs, BitLocker to Go is for USB drives, and EFS encrypts only files.",
        "objective": "Encryption"
    },
    {
        "question": "Which best describes the difference between a dedicated graphics card and an integrated graphics solution?",
        "options": {
            "A": "Dedicated graphics is required for basic tasks; integrated is for gaming",
            "B": "Dedicated graphics uses less power, better for laptops",
            "C": "Dedicated graphics is built into the CPU; integrated operates separately",
            "D": "Dedicated graphics has its own memory; integrated shares system RAM"
        },
        "answer": "D",
        "explanation": "Dedicated graphics cards come with their own memory, while integrated graphics borrow system RAM, making them slower for heavy tasks.",
        "objective": "Hardware components"
    },
    {
        "question": "Every new employee must sign a document that explains what they can and cannot do on company computers. Which document is this?",
        "options": {
            "A": "MOU",
            "B": "AUP",
            "C": "SLA",
            "D": "SOW"
        },
        "answer": "B",
        "explanation": "An Acceptable Use Policy (AUP) defines the rules for how employees can use company systems.",
        "objective": "Policies & compliance"
    },
    {
        "question": "Which command is used on a Linux system to run a program with another user's permissions?",
        "options": {
            "A": "grep",
            "B": "chown",
            "C": "passwd",
            "D": "sudo"
        },
        "answer": "D",
        "explanation": "`sudo` allows you to run commands as another user, usually root. The others are unrelated.",
        "objective": "Linux permissions"
    },
    {
        "question": "A company is using an operating system that has reached End-of-Life (EOL). Which is the MOST significant risk?",
        "options": {
            "A": "Loss of user customization options",
            "B": "Reduced performance efficiency",
            "C": "Increased security vulnerabilities",
            "D": "Decreased hardware compatibility"
        },
        "answer": "C",
        "explanation": "The biggest risk is security vulnerabilities, since the OS no longer receives security updates.",
        "objective": "System lifecycle & risks"
    },
    {
        "question": "You are working as a service desk analyst. Multiple users report they cannot access websites. You run a program that shows each hop in the network path to find where the issue is occurring. Which tool should you use?",
        "options": {
            "A": "netstat",
            "B": "nslookup",
            "C": "tracert",
            "D": "ping"
        },
        "answer": "C",
        "explanation": "Tracert shows the path packets take to reach a destination and identifies where delays or failures occur. This helps you determine if the problem is inside your network or with your ISP.",
        "objective": "Network troubleshooting tools"
    },
    {
        "question": "A company rolls out a cloud-based application that constantly syncs with remote servers. Employees report slower internet speeds after installation. What is the most likely reason?",
        "options": {
            "A": "The application is using too much bandwidth for data transfers.",
            "B": "The local network is too outdated for the application.",
            "C": "The firewall is blocking cloud traffic, slowing the internet.",
            "D": "Employee computers are overloaded by the application."
        },
        "answer": "A",
        "explanation": "Constant syncing with cloud servers consumes a large amount of bandwidth, slowing down the internet for everyone else.",
        "objective": "Cloud application performance impact"
    },
    {
        "question": "A government agency is retiring hard drives containing classified data. Agency guidelines require an irreversible method that prevents data retrieval. Which method aligns with this guideline?",
        "options": {
            "A": "Storing retired drives securely in locked, monitored storage units.",
            "B": "Removing files using a specialized secure deletion software tool.",
            "C": "Exposing the drives to a high-powered magnetic degausser device.",
            "D": "Using standard formatting procedures on each retired hard drive."
        },
        "answer": "C",
        "explanation": "A magnetic degausser completely destroys the magnetic fields on a drive, making data recovery impossible. Formatting or deleting is not truly permanent.",
        "objective": "Secure data disposal"
    },
    {
        "question": "Which feature allows a Linux server to provide file-sharing services to a company's Windows 10 workstations?",
        "options": {
            "A": "Samba",
            "B": "Pathping",
            "C": "Yum",
            "D": "Keychain"
        },
        "answer": "A",
        "explanation": "Samba is software that allows Linux/Unix systems to share files and printers with Windows systems using SMB/CIFS protocol.",
        "objective": "File-sharing interoperability"
    },
    {
        "question": "Which attack uses a wireless access point made to look like a legitimate corporate access point by copying its SSID to trick users and capture data?",
        "options": {
            "A": "Shoulder surfing",
            "B": "Evil twin",
            "C": "WEP attack",
            "D": "Rogue access point"
        },
        "answer": "B",
        "explanation": "An Evil Twin attack creates a fake wireless access point with the same SSID as the real network, tricking users into connecting so attackers can capture traffic.",
        "objective": "Wireless security threats"
    },
    {
        "question": "A business outsources its cloud storage to a provider and needs to guarantee uptime, data availability, and support response times. Which document BEST ensures these expectations are enforceable?",
        "options": {
            "A": "BCP",
            "B": "EULA",
            "C": "SLA",
            "D": "SLO"
        },
        "answer": "C",
        "explanation": "A Service Level Agreement (SLA) is a formal contract that defines performance standards like uptime, availability, and remedies if the provider fails to meet them.",
        "objective": "Cloud service agreements"
    },
    {
        "question": "A user has reported that their workstation is running very slowly. A technician determines that the user has recently downloaded a new application from the internet and may have become infected with malware. Which of the following types of infections does the workstation MOST likely have?",
        "options": {
            "A": "Keylogger",
            "B": "Ransomware",
            "C": "Trojan",
            "D": "Rootkit"
        },
        "answer": "C",
        "explanation": "A Trojan pretends to be a safe program but secretly runs harmful processes in the background, slowing the computer. Other options like keyloggers or ransomware are more specialized and don’t usually cause general slowness.",
        "objective": "Malware identification"
    },
    {
        "question": "A user's personal settings are not showing up on their computer. You suspect their profile has become corrupted in Windows. You attempt to look at their profile file but cannot find it in their profile directory. Which option do you need to configure to see this file?",
        "options": {
            "A": "Display Settings",
            "B": "Internet Options",
            "C": "User Accounts",
            "D": "Folder Options"
        },
        "answer": "D",
        "explanation": "Some files in Windows are hidden by default. You must change the Folder Options to show hidden files and folders so the profile can be located.",
        "objective": "Windows troubleshooting"
    },
    {
        "question": "Which Windows tool can a technician use to gather information about a workstation and create a full list of hardware, system components, and software environment?",
        "options": {
            "A": "dxdiag.exe",
            "B": "resmon.exe",
            "C": "msinfo32.exe",
            "D": "devmgmt.msc"
        },
        "answer": "C",
        "explanation": "MSINFO32 shows detailed system information like memory, hardware, and drivers. The other tools focus on smaller areas like graphics, performance, or device management.",
        "objective": "Windows diagnostic tools"
    },
    {
        "question": "A user has been using Microsoft Excel for twenty minutes when it crashes. You can recover their data, but you cannot figure out why the app crashed. Which of the following actions should you take?",
        "options": {
            "A": "Uninstall and reinstall the application",
            "B": "Disable any unneeded applications configured to automatically startup",
            "C": "Remove a recently added hardware device",
            "D": "Verify that disabling one service has not affected others"
        },
        "answer": "B",
        "explanation": "Unnecessary background programs can use up memory and cause apps like Excel to crash. Disabling unneeded startup apps often fixes stability issues without reinstalling.",
        "objective": "Application troubleshooting"
    },
    {
        "question": "Edward returns from vacation and notices that he cannot see the shared Customer Service inbox folder in his email client, even though his account still works. What MOST likely happened?",
        "options": {
            "A": "The internet security options in his email client have been modified",
            "B": "The operating system was updated",
            "C": "The network file share's permission has been modified",
            "D": "Edward's user account permission has changed"
        },
        "answer": "D",
        "explanation": "The shared folder is missing because Edward’s permissions were changed while he was away. If his account still works normally otherwise, this is the most likely cause.",
        "objective": "Permission & access troubleshooting"
    },
    {
        "question": "You want to ensure that only one person can enter or leave the server room at a time. Which physical security device would BEST meet this requirement?",
        "options": {
            "A": "Cipher lock",
            "B": "Thumbprint reader",
            "C": "Video monitoring",
            "D": "Access control vestibule"
        },
        "answer": "D",
        "explanation": "An access control vestibule, also called a mantrap, only allows one person in or out at a time. Locks, cameras, and fingerprint readers can control access, but they do not physically enforce the 'one person at a time' rule.",
        "objective": "Physical security controls"
    },
    {
        "question": "Tim has created a new iOS application and wants to install it on his iPad without going through the official App Store. He has not purchased a developer certificate. Which option would allow him to install this unofficial app?",
        "options": {
            "A": "Rooted device",
            "B": "APK installer",
            "C": "Jailbroken device",
            "D": "Developer mode"
        },
        "answer": "C",
        "explanation": "On iOS, a jailbroken device removes Apple’s restrictions and allows apps to be installed without the App Store. Rooting and APKs apply to Android, not iOS.",
        "objective": "Mobile OS security"
    },
    {
        "question": "Which command is used on a Linux system to test if your computer can reach diontraining.com?",
        "options": {
            "A": "ping",
            "B": "dig",
            "C": "netstat",
            "D": "apt-get"
        },
        "answer": "A",
        "explanation": "The 'ping' command checks if a system can connect to a website or server by sending test signals. The other commands are for DNS lookups, network stats, or installing software.",
        "objective": "Linux network troubleshooting"
    },
    {
        "question": "When connecting multiple USB devices, a user gets a 'USB Controller Resource Exceeded' warning. Some devices stop working. What is the best solution?",
        "options": {
            "A": "Use a powered USB hub for the external devices",
            "B": "Disable USB devices in BIOS to free up resources",
            "C": "Update the computer's operating system to reallocate resources",
            "D": "Replace the motherboard with one that has more USB ports"
        },
        "answer": "A",
        "explanation": "A powered USB hub provides extra power and resources so all devices can work. Updating or disabling devices won’t fix the limitation, and replacing the motherboard is unnecessary.",
        "objective": "Peripheral troubleshooting"
    },
    {
        "question": "Which editions of Windows 10 can you connect to using Remote Desktop?",
        "options": {
            "A": "Home",
            "B": "Pro",
            "C": "Education",
            "D": "Enterprise"
        },
        "answer": "B, C, D",
        "explanation": "Windows 10 Home cannot be used as a Remote Desktop host. Only Pro, Education, and Enterprise editions support inbound Remote Desktop connections.",
        "objective": "Windows edition features"
    },
    {
        "question": "Which MacOS feature allows you to use multiple desktops or spaces on a single system?",
        "options": {
            "A": "Mission Control",
            "B": "Boot Camp",
            "C": "Finder",
            "D": "Dock"
        },
        "answer": "A",
        "explanation": "Mission Control lets Mac users create and switch between multiple desktops or 'spaces.' Boot Camp is for Windows, Finder is for files, and the Dock launches apps.",
        "objective": "MacOS features"
    },
    {
        "question": "Employees must verify the security of websites before submitting confidential client data. Which browser indicator BEST confirms that the website has a valid security certificate?",
        "options": {
            "A": "The browser’s history and cookies have recently been cleared",
            "B": "The site URL begins clearly with 'http://'",
            "C": "Browser displays a closed padlock icon next to the website address",
            "D": "Pop-up blocker is enabled, preventing unwanted advertisements"
        },
        "answer": "C",
        "explanation": "The closed padlock shows the website uses HTTPS with a valid security certificate. This means the connection is secure. Clearing history, using HTTP, or blocking pop-ups does not confirm security.",
        "objective": "Web security basics"
    },
    {
        "question": "You are trying to open your company's internal shared drive from your Windows 10 laptop but cannot reach it. You open your web browser and can connect to DionTraining.com without any issues. Which of the following commands should you use to determine if the internal shared drive is mapped to your computer properly?",
        "options": {
            "A": "net use",
            "B": "chkdsk",
            "C": "tracert",
            "D": "ping"
        },
        "answer": "A",
        "explanation": "The 'net use' command shows network drive connections. It tells you if your shared drive is mapped to your computer. The other commands check disks or network connections, but not drive mappings.",
        "objective": "Windows networking & troubleshooting"
    },
    {
        "question": "Which of the following is considered a trusted app source for APK files?",
        "options": {
            "A": "Android Central",
            "B": "App Store",
            "C": "Play Store",
            "D": "Windows Store"
        },
        "answer": "C",
        "explanation": "The Google Play Store is the official and trusted source for Android apps (APK files). Other stores are either for different platforms or not trusted distribution sources.",
        "objective": "Mobile security & app sources"
    },
    {
        "question": "Dion Training wants to provide governance for how employees can utilize the corporate network, email, and laptops while working for the company. Within which of the following should this be documented?",
        "options": {
            "A": "Password policy",
            "B": "Asset management policy",
            "C": "Knowledge base",
            "D": "Acceptable use policy"
        },
        "answer": "D",
        "explanation": "An Acceptable Use Policy (AUP) defines the rules for using company resources such as email, networks, and devices. The other options focus on specific topics but not general usage rules.",
        "objective": "Security policy & governance"
    },
    {
        "question": "A technician needs to add new features to an existing router on the network. Which of the following should be performed to add the new features?",
        "options": {
            "A": "Vulnerability patching",
            "B": "Clone the router",
            "C": "Migrating to IPv6",
            "D": "Firmware update"
        },
        "answer": "D",
        "explanation": "Firmware updates often add new features or improve performance on routers. Patching fixes bugs, cloning copies settings, and IPv6 changes the protocol but doesn’t add features.",
        "objective": "Router administration"
    },
    {
        "question": "A manager wants employees to enter data in a shared spreadsheet but needs to prevent accidental modifications to formulas. What is the best way to achieve this?",
        "options": {
            "A": "Lock the formula cells while keeping data entry fields editable",
            "B": "Convert the spreadsheet to a static file format, preventing further edits",
            "C": "Require employees to submit data separately for manual entry",
            "D": "Set the entire spreadsheet to read-only mode so no changes can be made"
        },
        "answer": "A",
        "explanation": "Locking the formula cells keeps important calculations safe while still allowing employees to enter their data. The other choices either block editing completely or create more work.",
        "objective": "File & data protection"
    },
    {
        "question": "You are working for a government contractor who requires all users to use a PIV device when sending digitally signed and encrypted emails. Which of the following physical security measures is being implemented?",
        "options": {
            "A": "Biometric reader",
            "B": "Key fob",
            "C": "Cable lock",
            "D": "Smart card"
        },
        "answer": "D",
        "explanation": "A PIV device is a government-issued smart card used for secure email signing, encryption, and authentication. It is not a fingerprint reader, fob, or physical lock.",
        "objective": "Authentication & access control"
    },
    {
        "question": "A workstation was patched last night with the latest operating system security update. This morning, the workstation only displays a blank screen. You restart the computer, but the operating system fails to load. What is the NEXT step you should attempt to boot this workstation?",
        "options": {
            "A": "Reboot the workstation into safe mode, open RegEdit, and repair the Windows Registry",
            "B": "Reboot the workstation into the BIOS and reconfigure boot options",
            "C": "Reboot the workstation into safe mode and disable Windows services/applications",
            "D": "Reboot the workstation into safe mode and roll back the recent security update"
        },
        "answer": "D",
        "explanation": "Booting into Safe Mode and rolling back the update fixes the system by removing the change that caused the problem. Editing the registry or BIOS won’t directly solve an update issue.",
        "objective": "Troubleshooting OS boot issues"
    },
    {
        "question": "Dion Consulting Group has been hired by a large security operations center (SOC) to build a Windows 2019 domain environment. The SOC has a total of 150 Windows 10 Professional edition workstations that will connect to the domain for authentication, administration, and access to networked resources. Which of the following types of network models is being used by this security operations center in the domain environment?",
        "options": {
            "A": "Mesh",
            "B": "Hub-and-spoke",
            "C": "Peer-to-peer",
            "D": "Client/server"
        },
        "answer": "D",
        "explanation": "A domain environment uses the client/server model, where all workstations connect to a central server (Domain Controller) for authentication and resource access.",
        "objective": "Network models & authentication domains"
    },
    {
        "question": "An IT professional is training employees about browser settings. How should they describe the primary function of a pop-up blocker?",
        "options": {
            "A": "It prevents automatic redirection from secure to unsecured websites",
            "B": "It restricts websites from storing tracking cookies on the user's device",
            "C": "It stops unwanted new windows or advertisements from opening automatically",
            "D": "It automatically deletes the browsing history after each session ends"
        },
        "answer": "C",
        "explanation": "Pop-up blockers stop unwanted ads or extra windows from opening automatically. They don’t handle cookies, redirects, or browsing history.",
        "objective": "Browser security settings"
    },
    {
        "question": "Which of the following is the purpose of an ESD mat?",
        "options": {
            "A": "Protects equipment against accidental static discharge",
            "B": "Protects the technician from accidental shocks",
            "C": "Protects equipment from dust or dirt",
            "D": "Protects casings from scratches and dents"
        },
        "answer": "A",
        "explanation": "An ESD mat grounds both the technician and the equipment, preventing damage from static electricity. It doesn’t protect people from electrical shocks or from physical dust/scratches.",
        "objective": "Safety & equipment handling"
    },
    {
        "question": "A government agency is retiring hard drives containing classified data. Agency guidelines require an irreversible method that prevents data retrieval. Which method aligns with this guideline?",
        "options": {
            "A": "Removing files using a specialized secure deletion software tool",
            "B": "Exposing the drives to a high-powered magnetic degausser device",
            "C": "Using standard formatting procedures on each retired hard drive",
            "D": "Storing retired drives securely in locked, monitored storage units"
        },
        "answer": "B",
        "explanation": "Degaussing permanently erases data on magnetic drives by disrupting the magnetic field. Formatting and deletion can often be reversed, and locking drives does not destroy the data.",
        "objective": "Data sanitization methods"
    },
    {
        "question": "Which of the following types of mobile device screen locks uses biometrics to securely unlock the device?",
        "options": {
            "A": "TouchID",
            "B": "Passcode",
            "C": "FaceID",
            "D": "Swipe"
        },
        "answer": "A, C",
        "explanation": "TouchID (fingerprint) and FaceID (facial recognition) use unique physical traits, making them biometric methods. Passcodes and swipes are not biometrics.",
        "objective": "Mobile security & authentication"
    },
    {
        "question": "Your friend is concerned that someone might be listening to her daily conversations when her smartphone is still in her purse. Which of the following threats is this an example of?",
        "options": {
            "A": "Unauthorized location tracking",
            "B": "Unintended Bluetooth pairing",
            "C": "Unauthorized microphone activation",
            "D": "Unauthorized account access"
        },
        "answer": "C",
        "explanation": "If someone is listening in without permission, it means the phone’s microphone has been turned on secretly. This is called unauthorized microphone activation.",
        "objective": "Mobile device security threats"
    },
    {
        "question": "The physical security manager is concerned that during a power outage the server room might be targeted for attack. Which of the following security controls would still be usable?",
        "options": {
            "A": "Video surveillance",
            "B": "Motion detectors",
            "C": "Biometric scanners",
            "D": "Door locks"
        },
        "answer": "D",
        "explanation": "Most electronic security systems need electricity to work, but a standard door lock will still function even during a power outage.",
        "objective": "Physical security & access control"
    },
    {
        "question": "Peter is attempting to print to his office printer, but nothing comes out. Yesterday, his printer worked fine and there are no error messages. What should Peter check FIRST?",
        "options": {
            "A": "Cancel all documents and print them again",
            "B": "Check the status of the print server queue",
            "C": "Check that the printer is not offline",
            "D": "Check to ensure the printer selected is the default printer"
        },
        "answer": "C",
        "explanation": "The simplest first step is to make sure the printer is online and ready. If it is offline, nothing will print.",
        "objective": "Basic troubleshooting steps"
    },
    {
        "question": "A user’s browser keeps redirecting to a different search engine and shows pop-up ads after installing free software. What is the best next step to fix this issue?",
        "options": {
            "A": "Clear the browser's cache and cookies, then reboot the browser",
            "B": "Check and ensure that the browser is running the latest version",
            "C": "Run a full malware scan and remove unwanted browser extensions",
            "D": "Perform a complete system restore to a previous state before the software was added"
        },
        "answer": "C",
        "explanation": "This is most likely caused by malware (adware or a browser hijacker). The best solution is to run a malware scan and remove harmful extensions.",
        "objective": "Malware troubleshooting"
    },
    {
        "question": "Which of the following best describes a benefit of cloud-based word processing tools?",
        "options": {
            "A": "Multiple users can edit documents at the same time",
            "B": "Users must download and re-upload files to make changes",
            "C": "Documents can only be edited by one person at a time",
            "D": "Changes are only saved when the file is closed"
        },
        "answer": "A",
        "explanation": "Cloud-based tools let multiple people edit the same document at once in real time, making collaboration easier.",
        "objective": "Cloud collaboration benefits"
    },
    {
        "question": "You have been asked to classify a hospital's medical records as regulated data. Which of the following best describes this data type?",
        "options": {
            "A": "PCI",
            "B": "PHI",
            "C": "GDPR",
            "D": "PII"
        },
        "answer": "B",
        "explanation": "Hospital medical records are considered Protected Health Information (PHI), which is regulated under HIPAA in the U.S.",
        "objective": "Data classification & compliance"
    },
    {
        "question": "You connected your laptop using a CAT 5e cable but received an IP address of 169.254.13.52 and cannot connect to the internet. What is most likely the cause?",
        "options": {
            "A": "Duplicate IP address",
            "B": "Poisoned ARP cache",
            "C": "Failed DNS resolution",
            "D": "DHCP failure"
        },
        "answer": "D",
        "explanation": "An address starting with 169.254 means the computer could not get an IP address from the DHCP server, so it assigned itself one.",
        "objective": "Networking basics & DHCP"
    },
    {
        "question": "Your boss asks you to set up a wireless network for visitors that does not require any setup on their devices. Which encryption should you choose?",
        "options": {
            "A": "WPA2-TKIP",
            "B": "WEP",
            "C": "WPA-CCMP",
            "D": "WPA",
            "E": "Open"
        },
        "answer": "E",
        "explanation": "An open wireless network allows visitors to connect without entering a password or changing any settings, which meets the requirement.",
        "objective": "Wireless security settings"
    },
    {
        "question": "An employee can receive but not send messages in a workplace chat app. Other network services work fine. What is the most likely cause?",
        "options": {
            "A": "The employee lacks permission to send messages",
            "B": "The app only allows users to receive messages",
            "C": "The internet connection is completely down",
            "D": "A network outage has taken the app offline"
        },
        "answer": "A",
        "explanation": "Since the employee can receive messages and the network is working, the issue is most likely a permission setting preventing them from sending.",
        "objective": "User permissions troubleshooting"
    },
    {
        "question": "Dion Training replaced the batteries in their UPS. How should the depleted batteries be disposed of?",
        "options": {
            "A": "Research local regulations for toxic waste disposal in their area",
            "B": "Place the batteries in the recycle bin behind their office building",
            "C": "Wrap the batteries in plastic and place them in the trash",
            "D": "Place them in the proper recycling containers"
        },
        "answer": "D",
        "explanation": "UPS batteries are hazardous and must be disposed of in proper recycling containers designed for batteries.",
        "objective": "Environmental safety & disposal"
    },
    {
        "question": "Your company wants to block all USB storage devices across workstations while still allowing keyboards and printers. Which command-line tool should be used to update Group Policy?",
        "options": {
            "A": "gpresult",
            "B": "sfc",
            "C": "diskpart",
            "D": "gpupdate"
        },
        "answer": "D",
        "explanation": "The gpupdate command forces an update to Group Policy, applying new rules like blocking USB storage devices across all workstations.",
        "objective": "Windows system administration"
    },
    {
        "question": "Jonathan's father is visually impaired and needs help using the Magnifier feature in Windows 10. Which Control Panel section should the technician use?",
        "options": {
            "A": "Sound",
            "B": "File Explorer Options",
            "C": "Ease of Access",
            "D": "Indexing Options"
        },
        "answer": "C",
        "explanation": "The Magnifier tool is part of the 'Ease of Access' section, which is designed to help users with disabilities adjust Windows settings.",
        "objective": "Accessibility settings in Windows"
    },
    {
        "question": "What is the term for a piece of software which no longer has technical support, software updates, or security updates?",
        "options": {
            "A": "Retired",
            "B": "End-of-life",
            "C": "Limited",
            "D": "Past due"
        },
        "answer": "B",
        "explanation": "When software reaches 'end-of-life,' the company stops providing fixes or updates. Using it becomes risky because it will not get security patches.",
        "objective": "Software lifecycle & support"
    },
    {
        "question": "You are working as a server administrator and use your badge to unlock the server room. Another person slips in behind you without scanning their badge. What social engineering technique did this person use?",
        "options": {
            "A": "Impersonation",
            "B": "Tailgating",
            "C": "Shoulder surfing",
            "D": "Spoofing"
        },
        "answer": "B",
        "explanation": "Tailgating is when someone follows an authorized person into a secure area without using their own access card.",
        "objective": "Physical security & social engineering"
    },
    {
        "question": "Jason logs in to his bank using a key fob that generates random numbers synced with the server. What device is this?",
        "options": {
            "A": "Biometric lock",
            "B": "Smart card",
            "C": "Hardware token",
            "D": "PIV card"
        },
        "answer": "C",
        "explanation": "A hardware token is a small device that generates temporary codes for secure logins.",
        "objective": "Authentication methods"
    },
    {
        "question": "Your Security Operations Center detects that workstations on your network are being used to launch a DDoS attack. What type of malware are these workstations most likely infected with?",
        "options": {
            "A": "Ransomware",
            "B": "Botnet",
            "C": "Spyware",
            "D": "Rootkit"
        },
        "answer": "B",
        "explanation": "A botnet is a group of infected computers controlled by an attacker, often used for large-scale attacks like DDoS.",
        "objective": "Malware types & attacks"
    },
    {
        "question": "An employee says their smartphone can’t connect to the internet or make calls, but apps still work fine. What’s the most likely issue?",
        "options": {
            "A": "The cellular radio is broken",
            "B": "Airplane mode is enabled",
            "C": "The Bluetooth connection is disabled",
            "D": "The VPN password was entered incorrectly"
        },
        "answer": "B",
        "explanation": "When airplane mode is on, the phone can’t use mobile data or calls, but apps that don’t need internet can still open.",
        "objective": "Mobile troubleshooting"
    },
    {
        "question": "Which command-line tool in Linux is used to move upward one directory in the system’s folder structure?",
        "options": {
            "A": "ls",
            "B": "cd ..",
            "C": "dir",
            "D": "cd ."
        },
        "answer": "B",
        "explanation": "The 'cd ..' command moves you up one folder level in Linux or Unix systems.",
        "objective": "Linux navigation commands"
    },
    {
        "question": "June’s tablet is slow, shows fake 'click to fix' warnings, and redirects to odd websites. What’s the best action?",
        "options": {
            "A": "Locate and remove affected apps, run a scan, and verify app permissions",
            "B": "Clear the browser cache, disable pop-ups, and reboot",
            "C": "Perform a soft reset to clear temporary files",
            "D": "Ignore the warnings and continue using the device"
        },
        "answer": "A",
        "explanation": "This looks like malware. Removing bad apps, scanning the device, and checking app permissions is the safest fix.",
        "objective": "Mobile malware troubleshooting"
    },
    {
        "question": "Which type of threat actor can accidentally cause a security problem inside an organization?",
        "options": {
            "A": "Organized Crime",
            "B": "Hacktivist",
            "C": "APT",
            "D": "Insider threat"
        },
        "answer": "D",
        "explanation": "An insider threat can be malicious or accidental. Employees might cause harm by mistake, like clicking a phishing link.",
        "objective": "Threat actors"
    },
    {
        "question": "How can a company best prevent employees from logging into someone else’s workstation without permission?",
        "options": {
            "A": "Install cameras in secure areas",
            "B": "Enforce 30-day password changes",
            "C": "Require biometric identification for logins",
            "D": "Require username and password for logins"
        },
        "answer": "C",
        "explanation": "Biometrics like fingerprint or face ID ensure only the authorized person can log in to their computer.",
        "objective": "Access control"
    },
    {
        "question": "Which command can be used to find devices between a client and destination and check for network delays?",
        "options": {
            "A": "net use",
            "B": "ping",
            "C": "netstat",
            "D": "pathping"
        },
        "answer": "D",
        "explanation": "Pathping shows the path packets take across the network and measures delays at each step.",
        "objective": "Network troubleshooting"
    },
    {
        "question": "You try to open an important encrypted work email on your phone, but it won’t open. What should you do?",
        "options": {
            "A": "Ask your boss to resend to Gmail",
            "B": "Verify the digital certificate is installed",
            "C": "Open it in a web browser",
            "D": "Ask your boss to resend unencrypted"
        },
        "answer": "B",
        "explanation": "Encrypted emails require a digital certificate on your device. Without it, the email cannot be read.",
        "objective": "Email security"
    },
    {
        "question": "Users get fake bank emails asking them to 'click here' to reset passwords, even if they aren’t bank customers. What type of attack is this?",
        "options": {
            "A": "Whaling",
            "B": "Brute force",
            "C": "Spear phishing",
            "D": "Phishing"
        },
        "answer": "D",
        "explanation": "Phishing is when attackers send fake emails to many people, trying to trick them into revealing personal info.",
        "objective": "Social engineering attacks"
    },
    {
        "question": "Which tool analyzes your hard drive to find unused files that can be safely removed?",
        "options": {
            "A": "Disk defragmenter",
            "B": "Performance monitor",
            "C": "Device manager",
            "D": "Disk cleanup"
        },
        "answer": "D",
        "explanation": "Disk Cleanup finds temporary files and other unnecessary data to free up space on your computer.",
        "objective": "System maintenance"
    },
    {
        "question": "Which policy explains what employees can and cannot do when using company computers or networks?",
        "options": {
            "A": "Acceptable use policy",
            "B": "Zero trust",
            "C": "Defense in depth",
            "D": "Least privilege"
        },
        "answer": "A",
        "explanation": "An acceptable use policy sets the rules for proper use of company resources.",
        "objective": "IT policies"
    },
    {
        "question": "Where in the Control Panel can you roll back a driver for a graphics card?",
        "options": {
            "A": "Devices and Printers",
            "B": "System",
            "C": "Device Manager",
            "D": "Programs and Features"
        },
        "answer": "C",
        "explanation": "Device Manager lets you manage, update, or roll back hardware drivers.",
        "objective": "Windows troubleshooting"
    },
    {
        "question": "John wants to stop users from changing the boot order and loading an unauthorized operating system. What feature should be enabled?",
        "options": {
            "A": "Full disk encryption",
            "B": "RAM integrity checking",
            "C": "Secure Boot",
            "D": "BIOS password required"
        },
        "answer": "D",
        "explanation": "A BIOS password prevents changes to startup settings, stopping unauthorized booting.",
        "objective": "System security"
    },
    {
        "question": "A programmer wants others to understand his script logic when reading the code. What should he use?",
        "options": {
            "A": "Loop",
            "B": "Constant",
            "C": "Comment",
            "D": "Variable"
        },
        "answer": "C",
        "explanation": "Comments are notes written into the code to explain what it does without affecting the program.",
        "objective": "Programming basics"
    },
    {
        "question": "Jason’s laptop is old, has a cracked screen, and contains a hardware key he needs for work while traveling. What’s the best temporary fix?",
        "options": {
            "A": "Replace the display and charge him",
            "B": "Purchase a new laptop",
            "C": "Replace display and contact manufacturer",
            "D": "Sell him an external monitor as a workaround"
        },
        "answer": "D",
        "explanation": "An external monitor allows Jason to keep using the laptop with the needed hardware key until a replacement is issued.",
        "objective": "Hardware troubleshooting"
    },
    {
        "question": "Employees frequently access confidential company information through web-based applications. To increase security, IT recommends disabling certain browser features. Which browser feature would be most appropriate to disable for enhanced security?",
        "options": {
            "A": "Automatic clearing of browsing history after each session",
            "B": "JavaScript execution to limit potential script-based attacks",
            "C": "Browser pop-up blocker to allow all necessary notifications",
            "D": "Automatic updates for the browser to avoid unexpected changes"
        },
        "answer": "B",
        "explanation": "JavaScript is often used by attackers to run harmful code on websites. Turning it off (or limiting it) reduces the risk of these attacks. The other options would either reduce security or remove important protections.",
        "objective": "Browser security hardening"
    },
    {
        "question": "A user reports that after logging into their Windows 11 computer, they are met with a black screen and a movable cursor. They add that no desktop icons or taskbar are visible. Which of the following is the best initial method for attempting to fix this?",
        "options": {
            "A": "Boot into Safe Mode and perform a system restore",
            "B": "Restart the Windows Explorer process using Task Manager",
            "C": "Check the monitor cable connections and replace the cable if necessary",
            "D": "Reinstall the graphics driver from Device Manager"
        },
        "answer": "B",
        "explanation": "This problem usually happens when Windows Explorer (the part of Windows that shows the desktop and taskbar) fails to load. Restarting it through Task Manager often fixes the issue right away.",
        "objective": "Windows troubleshooting"
    },
    {
        "question": "Users connecting to an SSID appear to be unable to authenticate to the captive portal. Which of the following is the MOST likely cause of the issue?",
        "options": {
            "A": "WPA2 security key",
            "B": "SSL certificates",
            "C": "CSMA/CA",
            "D": "RADIUS"
        },
        "answer": "D",
        "explanation": "Captive portals often use a RADIUS server to check usernames and passwords. If the RADIUS server is down or not set up correctly, users won’t be able to log in.",
        "objective": "Wireless authentication issues"
    },
    {
        "question": "Your company is concerned about the possibility of power fluctuations that may occur and cause a small dip in the input power to their server room for an extended period of time. What condition is this known as?",
        "options": {
            "A": "Power spikes",
            "B": "Under-voltage event",
            "C": "Power failure",
            "D": "Power surge"
        },
        "answer": "B",
        "explanation": "An under-voltage event (also called a brownout) is when the power level drops below normal for a while. This can cause computers and servers to act strangely or even crash.",
        "objective": "Power fluctuation conditions"
    },
    {
        "question": "A technician at Dion Training wants to identify which version and build of Windows 10 is installed on a laptop. Which of the following commands should the technician enter at the command line?",
        "options": {
            "A": "gpresult",
            "B": "net user",
            "C": "pathping",
            "D": "winver"
        },
        "answer": "D",
        "explanation": "The 'winver' command shows which version and build of Windows is running. The other commands are for checking policies, user accounts, or network paths.",
        "objective": "Windows command-line tools"
    },
    {
        "question": "Mark's laptop is running Windows 10 and appears to become slower and slower over time with use. You decide to check the current CPU utilization and observe that it remains in the 95% to 100% range fairly consistently. You close three of Mark's open applications and recheck the CPU utilization. You notice the utilization dropped to the 30% to 35% range. A week later, Mark calls you again and says the computer is extremely slow. Which of the following tools can you use to check the CPU utilization and manage any high-resource processes?",
        "options": {
            "A": "Msconfig",
            "B": "PerfMon",
            "C": "Task Manager",
            "D": "RDS"
        },
        "answer": "C",
        "explanation": "Task Manager shows what programs are using the most CPU power and allows you to close them. This makes it the quickest tool for fixing slow performance caused by heavy apps.",
        "objective": "Resource monitoring & management"
    },
    {
        "question": "You are working in a doctor's office and have been asked to set up a kiosk to allow customers to check in for their appointments. The kiosk should be secured, and only customers to access a single application used for the check-in process. You must also ensure that the computer will automatically log in whenever the system is powered on or rebooted. Which of the following types of accounts should you configure for this kiosk?",
        "options": {
            "A": "Remote Desktop User",
            "B": "Power User",
            "C": "Guest",
            "D": "Administrator"
        },
        "answer": "C",
        "explanation": "A Guest account is the safest choice for a kiosk because it limits what people can do on the computer. This keeps the system secure while still allowing access to the check-in program.",
        "objective": "Account security & least privilege"
    },
    {
        "question": "Which of the following should be configured on a macOS system to enable the Smart Zoom feature on a user's MacBook trackpad?",
        "options": {
            "A": "Motions",
            "B": "Movements",
            "C": "Gestures",
            "D": "Signals"
        },
        "answer": "C",
        "explanation": "Smart Zoom is a trackpad gesture on macOS. It’s turned on in the Gestures settings and lets you double-tap with two fingers to zoom in and out.",
        "objective": "macOS input configuration"
    },
    {
        "question": "A customer runs frantically into your computer repair store. He says that his smartphone fell into a puddle, and now it won't turn on. He excitedly tells you that he needs the smartphone working again 'right now' and cannot wait. What should you do?",
        "options": {
            "A": "Explain to the customer that the repairs may take several days",
            "B": "Tell the customer to calm down because it is just a phone",
            "C": "Offer the customer the option to replace his phone",
            "D": "Post about the experience on Facebook after the customer leaves"
        },
        "answer": "A",
        "explanation": "The professional response is to calmly explain that water damage takes time to fix. Telling the customer to calm down, replacing the phone, or posting online are not appropriate.",
        "objective": "Customer service professionalism"
    },
    {
        "question": "You are working as a defense contractor for the U.S. Army. The Army is looking to purchase Microsoft Office for all of its employees to use. Which of the following licenses would be BEST for this sized organization to purchase?",
        "options": {
            "A": "Personal",
            "B": "Business",
            "C": "Open-source",
            "D": "Enterprise"
        },
        "answer": "D",
        "explanation": "Large organizations like the Army need enterprise licenses. This option supports many users and includes advanced security and compliance features.",
        "objective": "Licensing models for organizations"
    },
    {
        "question": "Jack has asked you for a recommendation on which word processing software they should install. There are four different software packages they are considering, and each uses a different licensing type. Jack states he wants to get a copy of Microsoft Word so their son can create reports for school. Which of the following would MOST likely be the best option for them?",
        "options": {
            "A": "Business",
            "B": "Enterprise",
            "C": "Personal",
            "D": "Open-source"
        },
        "answer": "C",
        "explanation": "Since the software is just for home and school use, a Personal license is the right choice. Business or Enterprise licenses are for companies.",
        "objective": "Software licensing types"
    },
    {
        "question": "Which of the following remote access tools is a command-line terminal emulation program operating on port 23?",
        "options": {
            "A": "Telnet",
            "B": "RDP",
            "C": "VNC",
            "D": "SSH"
        },
        "answer": "A",
        "explanation": "Telnet is a remote command-line tool that uses port 23. It’s older and less secure than SSH, which uses port 22. RDP and VNC are for graphical remote desktops.",
        "objective": "Remote access protocols"
    },
    {
        "question": "A user is complaining that the touchscreen on their smartphone is not responding to their touch. What is the FIRST step you recommend to solve this issue?",
        "options": {
            "A": "Have the user restart the device",
            "B": "Enable and disable airplane mode",
            "C": "Replace the defective touchscreen",
            "D": "Reinstall the OS"
        },
        "answer": "A",
        "explanation": "Restarting the device is the simplest first step. It often clears temporary glitches without needing costly repairs or reinstallations.",
        "objective": "Basic troubleshooting"
    },
    {
        "question": "Your company is implementing a new customer relationship management (CRM) system. The IT department must ensure the CRM communicates seamlessly with billing and inventory software to reduce manual data errors. Which option BEST addresses this requirement?",
        "options": {
            "A": "Application integration",
            "B": "Virtualization",
            "C": "Software patch management",
            "D": "Endpoint protection"
        },
        "answer": "A",
        "explanation": "Application integration allows different software systems to talk to each other automatically, eliminating the need for duplicate manual data entry.",
        "objective": "System integration"
    },
    {
        "question": "An AI assistant provides detailed instructions for fixing a networking issue, but the steps include settings and commands that don’t actually exist. Which BEST describes this problem?",
        "options": {
            "A": "Inaccurate findings",
            "B": "Bias",
            "C": "Misconfiguration",
            "D": "Hallucination"
        },
        "answer": "D",
        "explanation": "Hallucination is when AI confidently makes up information that isn’t real. This is different from a misconfiguration or bias.",
        "objective": "AI reliability"
    },
    {
        "question": "Which of the following data types would be used to store a user's name?",
        "options": {
            "A": "Boolean",
            "B": "Integers",
            "C": "Floating point",
            "D": "String"
        },
        "answer": "D",
        "explanation": "A name is text, so it must be stored as a string. Numbers (integers or floating point) or true/false values (boolean) would not fit.",
        "objective": "Data types"
    },
    {
        "question": "An employee’s inbox is full of spam after their password was compromised. Many of the emails are from addresses ending in spamyour.com. What should you do to reduce this spam?",
        "options": {
            "A": "Establish an allow list of trusted senders",
            "B": "Create a domain-based email filter",
            "C": "Click the unsubscribe button of each email",
            "D": "Mark each email as spam or junk"
        },
        "answer": "B",
        "explanation": "A domain-based filter blocks all emails from that spam domain. Unsubscribing could make things worse and manually marking emails takes too long.",
        "objective": "Email security & filtering"
    },
    {
        "question": "A technician is installing Windows 11 (64-bit) in a virtual machine with 1.2 GHz dual-core CPU, 4 GB memory, 32 GB hard drive, and 1920x1080 screen resolution. The installation fails. What should be increased to fix this?",
        "options": {
            "A": "Amount of hard drive space",
            "B": "The screen resolution",
            "C": "Number of CPU cores",
            "D": "Amount of memory"
        },
        "answer": "D",
        "explanation": "Windows 11 (64-bit) requires at least 8 GB of memory. The 4 GB assigned isn’t enough, so increasing RAM fixes the problem.",
        "objective": "System requirements"
    },
    {
        "question": "Your company’s firewall fails, leaving the network exposed. The IT team must urgently replace it without going through the standard approval process. Which type of change is this?",
        "options": {
            "A": "Emergency change",
            "B": "Standard change",
            "C": "Unauthorized change",
            "D": "Normal change"
        },
        "answer": "A",
        "explanation": "An emergency change is unplanned and requires immediate action to restore critical security or services.",
        "objective": "Change management"
    },
    {
        "question": "A programmer needs to store the amount of disk space required for a daily backup in a placeholder that can change as the script runs. Which should they use?",
        "options": {
            "A": "Comment",
            "B": "Constant",
            "C": "Variable",
            "D": "Loop"
        },
        "answer": "C",
        "explanation": "A variable is a storage location in a program that can hold data and be updated while the program runs.",
        "objective": "Programming basics"
    },
    {
        "question": "A system administrator is performing a 5-step change. At step five, the change fails after 90 minutes of a 120-minute window. What should they do?",
        "options": {
            "A": "Return the system to the original state before the change",
            "B": "Request additional time since the change is near completion",
            "C": "Leave the change as is and inform users of a workaround",
            "D": "Return the system to step four since this was the last working step"
        },
        "answer": "A",
        "explanation": "Rollback means restoring the system to the original stable state, not leaving it partly changed.",
        "objective": "Change management rollback"
    },
    {
        "question": "A company issues tablets for employees used in public areas. To prevent unauthorized access, which biometric method is the most practical and secure?",
        "options": {
            "A": "Facial recognition",
            "B": "Retina scanning",
            "C": "Swipe pattern",
            "D": "Voice recognition"
        },
        "answer": "A",
        "explanation": "Facial recognition is fast, convenient, and secure for everyday use. Retina scanning is too complex, and swipe or voice are less secure.",
        "objective": "Mobile security"
    },
    {
        "question": "You need to reset a workstation’s BIOS password but the user forgot it. What should you do?",
        "options": {
            "A": "Remove and replace the CMOS battery",
            "B": "Conduct a brute force attack",
            "C": "Unplug and reconnect the mainboard power cable",
            "D": "Conduct a dictionary attack"
        },
        "answer": "A",
        "explanation": "Removing the CMOS battery clears BIOS settings including the password. Brute force or dictionary attacks aren’t practical here.",
        "objective": "BIOS troubleshooting"
    },
    {
        "question": "Which file system is used on Linux to mount remote storage devices?",
        "options": {
            "A": "NTFS",
            "B": "NFS",
            "C": "APFS",
            "D": "exFAT"
        },
        "answer": "B",
        "explanation": "NFS (Network File System) is a Linux/Unix protocol for accessing and mounting remote storage devices across a network.",
        "objective": "Linux storage systems"
    },
    {
        "question": "You are replacing a swollen battery in a customer's smartphone. Which of the following should you use? (Select TWO)",
        "options": {
            "A": "Compressed air",
            "B": "Safety goggles",
            "C": "Gloves",
            "D": "Air filter mask"
        },
        "answer": [
            "B",
            "C"
        ],
        "explanation": "When handling a swollen battery, safety goggles protect your eyes from chemicals and gloves protect your hands from burns or leaks. Compressed air and masks are not helpful in this case.",
        "objective": "Safety when handling hardware"
    },
    {
        "question": "A small doctor's office has asked you to configure their network to use the highest levels of wireless security and desktop authentication. Which TWO should you implement?",
        "options": {
            "A": "SSO",
            "B": "WEP",
            "C": "Multifactor",
            "D": "WPA2",
            "E": "RADIUS",
            "F": "WPS"
        },
        "answer": [
            "C",
            "D"
        ],
        "explanation": "WPA2 is the strongest wireless security option available here, and multifactor authentication adds extra protection by requiring more than just a password.",
        "objective": "Wireless and authentication security"
    },
    {
        "question": "You attempt to boot a Windows 10 laptop and receive an 'Operating System Not Found' error. Which command should you use to repair the boot sector of the hard disk?",
        "options": {
            "A": "bootrec /fixboot",
            "B": "diskpart list",
            "C": "bootrec /rebuildbcd",
            "D": "bootrec /fixmbr"
        },
        "answer": "D",
        "explanation": "The command 'bootrec /fixmbr' repairs the Master Boot Record, which often fixes the 'OS not found' error. The other commands have different purposes such as listing disks or rebuilding boot data.",
        "objective": "Windows boot repair"
    },
    {
        "question": "Your company is expanding its operations in the European Union and must follow regulations when processing personal data. Which regulation applies?",
        "options": {
            "A": "PCI",
            "B": "PII",
            "C": "GDPR",
            "D": "PHI"
        },
        "answer": "C",
        "explanation": "GDPR (General Data Protection Regulation) is the EU law that protects personal data and privacy. PCI relates to credit cards, PII is just a data type, and PHI relates to health data.",
        "objective": "Data privacy regulations"
    },
    {
        "question": "During a penetration test, an assessor finds the following passwords. Which one is the weakest and should be changed first?",
        "options": {
            "A": "P@$$W0RD",
            "B": "Pa55w0rd",
            "C": "P@$$w0rd",
            "D": "pa55word"
        },
        "answer": "D",
        "explanation": "The password 'pa55word' is weakest because it is all lowercase except for numbers and lacks complexity. The others include uppercase, symbols, or both.",
        "objective": "Password complexity & security"
    },
    {
        "question": "Which Windows tool should a technician use to import and install data in the x.509 format?",
        "options": {
            "A": "RDS",
            "B": "Group policy editor",
            "C": "Certificate manager",
            "D": "Device manager"
        },
        "answer": "C",
        "explanation": "Certificate Manager is the tool for installing and managing digital certificates like x.509. The other tools handle unrelated system settings.",
        "objective": "Certificate management"
    },
    {
        "question": "Which low power mode in Windows 10 saves power but takes longer to resume where the user left off?",
        "options": {
            "A": "Hibernate",
            "B": "Power saver",
            "C": "Sleep",
            "D": "Balanced"
        },
        "answer": "A",
        "explanation": "Hibernate saves everything from memory to the hard drive, using almost no power, but it takes longer to resume compared to Sleep mode.",
        "objective": "Power management"
    },
    {
        "question": "A small real estate office with 4 Windows 10 computers is configured in a workgroup to share files. What type of network model is this?",
        "options": {
            "A": "Peer-to-peer",
            "B": "Domain",
            "C": "Mesh",
            "D": "Hub-and-spoke"
        },
        "answer": "A",
        "explanation": "A workgroup setup is a peer-to-peer model, where each computer manages its own accounts and resources without a central server.",
        "objective": "Network models"
    },
    {
        "question": "Which Linux command is used to print the full contents of a file to the screen at once?",
        "options": {
            "A": "cat",
            "B": "dig",
            "C": "grep",
            "D": "ls"
        },
        "answer": "A",
        "explanation": "The 'cat' command displays the full contents of a file. 'grep' searches within files, 'ls' lists files, and 'dig' queries DNS.",
        "objective": "Linux file commands"
    },
    {
        "question": "How would you categorize the following authentication factors: PIN, Smart Card, Fingerprint, Signature, GPS Coordinates?",
        "options": {
            "A": "Smart card, Signature, GPS Coordinates, PIN, Fingerprint",
            "B": "Fingerprint, PIN, GPS Coordinates, Smart Card, Signature",
            "C": "PIN, Signature, Fingerprint, Smart Card, GPS Coordinates",
            "D": "PIN, Smart Card, Fingerprint, Signature, GPS Coordinates"
        },
        "answer": "D",
        "explanation": "PIN is something you know, Smart Card is something you have, Fingerprint is something you are, Signature is something you do, and GPS is somewhere you are.",
        "objective": "Authentication factors"
    },
    {
        "question": "The paparazzi found private baby photos of a celebrity online that were only in their cloud backup. Which threat is this?",
        "options": {
            "A": "Unauthorized camera activation",
            "B": "Leaked personal files",
            "C": "Unintended Bluetooth pairing",
            "D": "Unauthorized root access"
        },
        "answer": "B",
        "explanation": "The photos were leaked from cloud storage, making it a case of leaked personal files. The other options describe different attack types not related to this case.",
        "objective": "Cloud security & privacy"
    },
    {
        "question": "Which type of Windows installation requires an XML text file with instructions for the Setup program?",
        "options": {
            "A": "In-place upgrade",
            "B": "Unattended installation",
            "C": "Repair installation",
            "D": "Remote network installation"
        },
        "answer": "B",
        "explanation": "Unattended installations use an XML answer file to automate the setup without user input. The other methods require manual steps.",
        "objective": "Windows installation methods"
    },
    {
        "question": "You are installing a new file server at the offices of Dion Training. The entire building has a diesel generator installed to protect it from power outages. The file server must have zero downtime once placed into production. Which of the following power sources should the file server utilize?",
        "options": {
            "A": "A surge protector",
            "B": "An uninterruptible power supply (UPS)",
            "C": "A surge protector connected to a UPS",
            "D": "A line conditioner"
        },
        "answer": "B",
        "explanation": "A UPS provides temporary battery power during outages, covering the gap until the generator starts, ensuring zero downtime. Surge protectors and line conditioners do not provide backup power.",
        "objective": "Power protection & redundancy"
    },
    {
        "question": "A user has repeatedly gotten malware infections on their home computer after visiting untrusted websites. You've completed the malware removal process. Which is the best practice you should educate the user about to minimize the likelihood of future infections?",
        "options": {
            "A": "Regularly update antivirus software definitions",
            "B": "Use public Wi-Fi networks cautiously",
            "C": "Avoid using email attachments",
            "D": "Frequently reinstall the operating system"
        },
        "answer": "A",
        "explanation": "Updating antivirus definitions ensures the system can detect and block the latest malware, which is the most effective preventive measure against repeat infections.",
        "objective": "Malware prevention & user education"
    },
    {
        "question": "You are trying to copy a 4.7 GB file from your Windows laptop to an external hard drive using USB 3. The external hard drive is formatted with FAT32. Every time you attempt this copy, you receive an error. What is MOST likely the issue?",
        "options": {
            "A": "USB 3 is too slow to transfer a file this large",
            "B": "The external hard drive must be formatted as APFS to support this transfer",
            "C": "Files over 4 GB cannot be stored on a FAT32 formatted drive",
            "D": "The laptop must be reformatted as FAT32 to support this transfer"
        },
        "answer": "C",
        "explanation": "FAT32 has a maximum file size limit of 4 GB, so the 4.7 GB file cannot be copied until the drive is reformatted to NTFS or exFAT.",
        "objective": "File systems & storage limits"
    },
    {
        "question": "An attacker is using a word list that contains 1 million possible passwords as they attempt to crack your Windows password. What type of password attack is this?",
        "options": {
            "A": "Dictionary",
            "B": "Hybrid",
            "C": "Rainbow table",
            "D": "Brute-force"
        },
        "answer": "A",
        "explanation": "A dictionary attack uses a predefined list of possible passwords. This is distinct from brute-force, which tries every possible combination, or rainbow tables, which use precomputed hashes.",
        "objective": "Password attacks"
    },
    {
        "question": "Dion Training just released a new corporate policy that dictates all access to network resources will be controlled based on the user's job functions and tasks within the organization. For example, only people working in Human Resources can access employee records, and only the people working in finance can access customer payment histories. Which of the following security concepts is BEST described by this new policy?",
        "options": {
            "A": "Defense in depth",
            "B": "Acceptable use policy",
            "C": "Least privilege",
            "D": "Zero trust"
        },
        "answer": "C",
        "explanation": "The principle of least privilege restricts access rights to only what users need to perform their jobs, which is exactly what this policy enforces.",
        "objective": "Access control models"
    },
    {
        "question": "Susan is installing several updates on a Windows computer. Nine of the updates were installed without any issues, but one update produced an error and failed to install. Susan restarts the computer as part of the troubleshooting process, and the computer automatically attempts to install the failed update again. Again, the update fails to install. What should Susan do NEXT?",
        "options": {
            "A": "Review the Event Viewer to determine the cause of the failure and address the findings",
            "B": "Manually download and install the failed update",
            "C": "Download the update from a third-party website like Source Forge and install it",
            "D": "Research the error number for the failed update and determine if there is a known issue with this update"
        },
        "answer": "A",
        "explanation": "The best next step is to check Event Viewer for detailed error logs, which can identify the cause of the failed update before attempting other fixes.",
        "objective": "Windows update troubleshooting"
    },
    {
        "question": "Your company's IT department routinely deploys software updates to employee workstations every month. These updates follow a predefined approval process, pose minimal risk to system stability, and require no special authorization beyond the usual change request workflow. The IT manager wants to ensure these updates are properly categorized in the change management process to streamline approval and implementation. Which of the following would BEST describe this type of change?",
        "options": {
            "A": "Normal change",
            "B": "Emergency change",
            "C": "Standard change",
            "D": "Major change"
        },
        "answer": "C",
        "explanation": "A standard change is pre-approved, low risk, and repeatable — such as routine software updates. This best matches the described scenario.",
        "objective": "Change management"
    },
    {
        "question": "Which of the following tools should a technician use to modify the HOSTS file on a Windows 10 system to solve a website address resolution issue?",
        "options": {
            "A": "Services",
            "B": "Regedit",
            "C": "Notepad",
            "D": "MMC"
        },
        "answer": "C",
        "explanation": "The HOSTS file is a plain text file that must be edited with a text editor such as Notepad (run as administrator). Other tools like Services, Regedit, and MMC cannot edit this file.",
        "objective": "Windows system files & troubleshooting"
    },
    {
        "question": "Which of the following commands is used to edit a text file on a Linux server?",
        "options": {
            "A": "grep",
            "B": "pwd",
            "C": "nano",
            "D": "cat"
        },
        "answer": "C",
        "explanation": "Nano is a command-line text editor for Linux, used to create or modify text files. grep searches text, pwd shows the current directory, and cat displays contents but cannot edit.",
        "objective": "Linux text editors"
    },
    {
        "question": "Which of the following should be configured on a macOS system to enable the Smart Zoom feature on a user's MacBook trackpad?",
        "options": {
            "A": "Signals",
            "B": "Movements",
            "C": "Gestures",
            "D": "Motions"
        },
        "answer": "C",
        "explanation": "Smart Zoom is enabled in macOS under Trackpad settings by configuring gestures, which control two-finger taps, swipes, and zoom actions.",
        "objective": "macOS trackpad configuration"
    },
    {
        "question": "Which of the following Windows tools should a technician use to import and install data in the x.509 format?",
        "options": {
            "A": "Group policy editor",
            "B": "Device manager",
            "C": "Certificate manager",
            "D": "RDS"
        },
        "answer": "C",
        "explanation": "The Certificate Manager (certmgr.msc) in Windows is used to import, install, and manage certificates, including X.509 formatted ones.",
        "objective": "Windows certificate management"
    },
    {
        "question": "A developer uses a MacBook Pro when working from home, but they need access to both a Windows and macOS system to test their programs. Which of the following tools should be used to allow both operating systems to exist on their MacBook Pro?",
        "options": {
            "A": "Terminal",
            "B": "Boot Camp",
            "C": "Mission Control",
            "D": "Device Manager"
        },
        "answer": "B",
        "explanation": "Boot Camp allows users to install Windows alongside macOS, creating a dual-boot environment on a MacBook.",
        "objective": "Dual-boot configuration on macOS"
    },
    {
        "question": "Which of the following Linux command-line options would shut down a Linux server 11 minutes from now?",
        "options": {
            "A": "shutdown @11",
            "B": "shutdown 11:00",
            "C": "shutdown +11",
            "D": "shutdown now"
        },
        "answer": "C",
        "explanation": "The 'shutdown +11' command tells Linux to schedule a shutdown 11 minutes from the current time.",
        "objective": "Linux system shutdown commands"
    },
    {
        "question": "Which of the following types of screen locks uses a secret PIN or password to prevent access to a mobile device?",
        "options": {
            "A": "Swipe",
            "B": "TouchID",
            "C": "FaceID",
            "D": "Passcode"
        },
        "answer": "D",
        "explanation": "A passcode uses a PIN or password to secure the device, unlike biometric or swipe methods.",
        "objective": "Mobile device security methods"
    },
    {
        "question": "During employee cybersecurity training, a technician explains browser extensions. Which statement accurately describes why a user might choose to disable browser extensions?",
        "options": {
            "A": "To temporarily improve browser performance or security.",
            "B": "To permanently stop browser updates from being installed.",
            "C": "To prevent websites from tracking cookies on the device.",
            "D": "To avoid having to clear browsing history after sessions."
        },
        "answer": "A",
        "explanation": "Disabling browser extensions can reduce slowdowns or security risks caused by potentially vulnerable or resource-heavy extensions.",
        "objective": "Browser security and performance"
    },
    {
        "question": "Which of the following types of installations would require the use of an XML text file containing the instructions that the Windows Setup program would need to complete the installation?",
        "options": {
            "A": "Repair installation",
            "B": "Remote network installation",
            "C": "Unattended installation",
            "D": "In-place upgrade"
        },
        "answer": "C",
        "explanation": "Unattended installations use an XML answer file (unattend.xml) to automate setup without user interaction.",
        "objective": "Windows installation methods"
    },
    {
        "question": "You are troubleshooting a workstation and need to enter the BIOS. Unfortunately, the user does not remember their BIOS password. What action should you take to rest the BIOS password?",
        "options": {
            "A": "Remove and replace the CMOS battery",
            "B": "Conduct a brute force attack",
            "C": "Conduct a dictionary attack",
            "D": "Unplug and reconnect the mainboard power cable"
        },
        "answer": "A",
        "explanation": "Removing and reinserting the CMOS battery clears CMOS memory, resetting BIOS settings including the password.",
        "objective": "BIOS password recovery"
    },
    {
        "question": "A user has reported that their workstation is running very slowly. A technician begins to investigate the issue and notices a lot of unknown processes running in the background. The technician determines that the user has recently downloaded a new application from the internet and may have become infected with malware. Which of the following types of infections does the workstation MOST likely have?",
        "options": {
            "A": "Ransomware",
            "B": "Keylogger",
            "C": "Trojan",
            "D": "Rootkit"
        },
        "answer": "C",
        "explanation": "A Trojan disguises itself as a legitimate program but installs malicious processes that slow the system and cause hidden damage.",
        "objective": "Types of malware infections"
    },
    {
        "question": "A system administrator needs to remotely execute PowerShell commands on multiple Windows servers without requiring direct remote desktop access. The solution should allow secure command-line management using standard web-based protocols. Which of the following tools would BEST meet this requirement?",
        "options": {
            "A": "RDP",
            "B": "SSH",
            "C": "SNMP",
            "D": "WinRM"
        },
        "answer": "D",
        "explanation": "WinRM (Windows Remote Management) uses WS-Management, a web-based protocol, to execute PowerShell commands securely across systems.",
        "objective": "Windows remote management tools"
    },
    {
        "question": "A company rolls out a cloud-based application that syncs constantly with remote servers. Employees report slow internet speeds after the installation. What is the most likely reason?",
        "options": {
            "A": "Employee computers are overloaded by the application.",
            "B": "The local network is too outdated for the application.",
            "C": "The application is using too much bandwidth for data transfers.",
            "D": "The firewall is blocking cloud traffic, slowing the internet."
        },
        "answer": "C",
        "explanation": "Constant syncing uses up large amounts of bandwidth, which slows internet performance for all employees.",
        "objective": "Cloud application troubleshooting"
    },
    {
        "question": "A company plans to dispose of numerous outdated laptops and hard drives containing customer financial records. To comply with regulatory requirements, what step must the company take during disposal?",
        "options": {
            "A": "Obtaining certificates of secure data destruction from disposal vendors.",
            "B": "Storing retired equipment indefinitely in secured warehouse storage.",
            "C": "Donating retired equipment directly to local schools.",
            "D": "Wiping the systems with a quick format before disposal."
        },
        "answer": "A",
        "explanation": "Certificates of secure data destruction ensure compliance with regulations and confirm that sensitive data has been irreversibly destroyed.",
        "objective": "Data security & regulatory compliance"
    },
    {
        "question": "Which of the following backup rotation schemes requires backups to be stored to at least two different types of media?",
        "options": {
            "A": "Grandfather-father-son",
            "B": "FIFO Backup",
            "C": "Tower of Hanoi",
            "D": "3-2-1 backup"
        },
        "answer": "D",
        "explanation": "The 3-2-1 backup strategy requires keeping three copies of data, on two different media types, with one copy stored offsite.",
        "objective": "Backup strategies"
    },
    {
        "question": "A laptop is running Windows 10 with Windows Defender on it. A user believes their laptop may have become infected with malware, so they install a second antivirus program that supposedly includes real-time protection. Now, the laptop is sluggish and sometimes non-responsive. Which of the following should you do FIRST to resolve this problem?",
        "options": {
            "A": "Install and run Spybot Search & Destroy on the laptop",
            "B": "Enable real-time protection in Windows Defender",
            "C": "Run the Windows Update utility",
            "D": "Uninstall the real-time protection antivirus"
        },
        "answer": "D",
        "explanation": "Running two antivirus programs with real-time protection causes system conflicts and slowdowns. The best first step is to uninstall the second antivirus.",
        "objective": "Windows malware troubleshooting"
    },
    {
        "question": "You need to move a 75-pound box with a rack-mounted UPS in it. Which of the following actions should you take?",
        "options": {
            "A": "Open the box and carry up the UPS in pieces",
            "B": "Ask a coworker to team lift it with you",
            "C": "Lift with your legs and not your back",
            "D": "Lift with your back and not your legs"
        },
        "answer": "B",
        "explanation": "OSHA guidelines recommend team lifting for loads above ~50 pounds. Asking a coworker is the safest option.",
        "objective": "Workplace safety & ergonomics"
    },
    {
        "question": "Mark is setting up a DHCP server on a segment of the corporate LAN. Which of the following options is NOT required in the DHCP scope to allow hosts on that LAN segment to be assigned a dynamic IP address and still be able to access the Internet and internal company servers?",
        "options": {
            "A": "Default gateway",
            "B": "Reservations",
            "C": "DNS servers",
            "D": "Subnet mask"
        },
        "answer": "B",
        "explanation": "Reservations are optional for DHCP (used for devices that need the same IP). Default gateway, DNS servers, and subnet mask are required.",
        "objective": "DHCP configuration"
    },
    {
        "question": "Which of the following types of information can be displayed by the top command in Linux?",
        "options": {
            "A": "User accounts ordered by the number of logins",
            "B": "Running processes ordered by CPU or RAM consumption",
            "C": "User groups ordered by the number of members",
            "D": "Amount of CPU cores, user groups, and free storage"
        },
        "answer": "B",
        "explanation": "The Linux top command shows real-time information about running processes, typically sorted by CPU or memory usage, along with their resource consumption.",
        "objective": "Linux monitoring & process management"
    },
    {
        "question": "Which of the following is the best reason for quarantining a system suspected of malware infection?",
        "options": {
            "A": "Speeds up system performance by stopping background processes.",
            "B": "Allows antivirus software to automatically remove the infection without user intervention.",
            "C": "Prevents the malware from spreading to other devices on the network.",
            "D": "Ensures that all user files are backed up before further action is taken."
        },
        "answer": "C",
        "explanation": "The purpose of quarantining is to isolate the system so the malware cannot spread across the network.",
        "objective": "Incident response containment"
    },
    {
        "question": "Which of the following will close all of a user's open programs and services before powering off their Windows 10 computer?",
        "options": {
            "A": "Shutdown",
            "B": "Sleep",
            "C": "Hibernate",
            "D": "Lock"
        },
        "answer": "A",
        "explanation": "Shutdown closes all programs and services before powering off. Sleep and Hibernate keep sessions active, and Lock only secures the session.",
        "objective": "Windows power management"
    },
    {
        "question": "An attacker attempts to crack your Windows password by repeatedly guessing until they either guess your password or try every possible combination. What type of password attack is this?",
        "options": {
            "A": "Dictionary",
            "B": "Brute-force",
            "C": "Hybrid",
            "D": "Rainbow table"
        },
        "answer": "B",
        "explanation": "A brute-force attack tries every possible character combination until the password is guessed.",
        "objective": "Password attack types"
    },
    {
        "question": "A home user brought their Windows 10 laptop to the electronics store where you work. They claim their computer has become infected with malware. You begin troubleshooting the issue by first pressing the power button, and the laptop loads properly without any issues. When you open Microsoft Edge, you notice that multiple pop-ups appear almost immediately. Which of the following actions should you take NEXT?",
        "options": {
            "A": "Document the pop-ups displayed and take a screenshot",
            "B": "Reinstall or reimage the operating system",
            "C": "Quarantine the machine and report it as infected to your company's cybersecurity department for investigation",
            "D": "Clear the browser's cookies and history, enable the pop-up blocker, and scan the system for malware"
        },
        "answer": "D",
        "explanation": "Since this is a home user, the next logical step is to clear browser data, enable protections, and run a malware scan before attempting drastic actions.",
        "objective": "Windows malware troubleshooting"
    },
    {
        "question": "Employees at a company report security warnings after a commonly used browser plug-in is identified as vulnerable. Which immediate action should IT staff instruct employees to take?",
        "options": {
            "A": "Perform regular antivirus scans on their computers daily.",
            "B": "Increase browser security settings to their maximum levels.",
            "C": "Clear browsing history and cookies to reset browser security.",
            "D": "Temporarily disable the vulnerable plug-in within browser settings."
        },
        "answer": "D",
        "explanation": "Disabling the vulnerable plug-in immediately removes the attack surface until a patch is available.",
        "objective": "Vulnerability management"
    },
    {
        "question": "An employee at Dion Training complains that every time airplane mode is enabled on their laptop, their external mouse and headphones stop working. Which of the following technologies is being disabled by airplane mode and likely causing the issues experienced by this user?",
        "options": {
            "A": "Cellular",
            "B": "Bluetooth",
            "C": "Wireless",
            "D": "GPS"
        },
        "answer": "B",
        "explanation": "External mice and headphones typically connect using Bluetooth. Airplane mode disables Bluetooth, which explains the issue.",
        "objective": "Wireless communication technologies"
    },
    {
        "question": "A facility would like to verify each individual's identity before allowing access to its server room and data center. Additionally, the building should ensure that users do not tailgate behind other users. What solution would BEST meet these requirements?",
        "options": {
            "A": "Implement a biometric reader at the datacenter entrance and require passage through an access control vestibule",
            "B": "Implement a biometric reader at the facility entrance and a proximity card at the data center entrance",
            "C": "Implement a security guard at the facility entrance and a keypad at the data center entrance",
            "D": "Implement a CCTV camera and a proximity reader at the data center entrance"
        },
        "answer": "A",
        "explanation": "Biometric authentication verifies individual identity, while an access control vestibule (mantrap) prevents tailgating. This combination provides the strongest security.",
        "objective": "Physical security controls"
    },
    {
        "question": "Which of the following technologies would you use to securely access the command line interface of a network's switches and routers remotely for configuration?",
        "options": {
            "A": "Telnet",
            "B": "SSH",
            "C": "HTTPS",
            "D": "RDP"
        },
        "answer": "B",
        "explanation": "SSH (Secure Shell) provides encrypted command-line access to network devices, making it the secure choice for remote configuration.",
        "objective": "Secure protocols"
    },
    {
        "question": "A penetration tester sends an email out to 100,000 random email addresses. In the email the attacker sent, it claims that 'Your Bank of America account is locked out. Please click here to reset your password.' Which of the following attack types is being used?",
        "options": {
            "A": "Vishing",
            "B": "Phishing",
            "C": "Whaling",
            "D": "Spear phishing"
        },
        "answer": "B",
        "explanation": "This is a large-scale phishing attack. It is not targeted like spear phishing or whaling, and it is not voice-based like vishing.",
        "objective": "Social engineering attacks"
    },
    {
        "question": "A macOS user is browsing the internet in Google Chrome when they see a notification that says, 'Windows Enterprise Defender: Your computer is infected with a virus, please click here to remove it!' What type of threat is this user experiencing?",
        "options": {
            "A": "Rogue anti-virus",
            "B": "Worm",
            "C": "Phishing",
            "D": "Pharming"
        },
        "answer": "A",
        "explanation": "Rogue anti-virus presents fake security alerts to trick users into installing malware or paying for fake solutions.",
        "objective": "Malware types"
    },
    {
        "question": "Dion Training wants to implement a new wireless network using WPA3 in their offices. Which of the following features of WPA3 is used to provide a password-based authentication using the dragonfly handshake instead of the older WPA 4-way handshake?",
        "options": {
            "A": "AES GCMP",
            "B": "SAE",
            "C": "Management protection frames",
            "D": "Enhanced open"
        },
        "answer": "B",
        "explanation": "SAE (Simultaneous Authentication of Equals) uses the dragonfly handshake in WPA3, providing stronger protection against brute-force attacks.",
        "objective": "Wireless security protocols"
    },
    {
        "question": "Which of the following is a connectionless protocol that utilizes on UDP?",
        "options": {
            "A": "FTP",
            "B": "HTTP",
            "C": "HTTPS",
            "D": "TFTP"
        },
        "answer": "D",
        "explanation": "TFTP (Trivial File Transfer Protocol) uses UDP and is connectionless, unlike FTP, HTTP, and HTTPS which all use TCP.",
        "objective": "Network protocols"
    },
    {
        "question": "You need to move a new desktop computer to another desk. Which of the following actions should you take?",
        "options": {
            "A": "Open the box and carry each piece individually",
            "B": "Ask a coworker to team lift it with you",
            "C": "Lift with your back and not your legs",
            "D": "Lift with your legs and not your back"
        },
        "answer": "D",
        "explanation": "The correct lifting technique is to bend your knees and lift with your legs, not your back, to avoid injury.",
        "objective": "Safety procedures"
    },
    {
        "question": "A user attempted to go to their favorite social media website this morning from their laptop. When they typed in Facebook.com, their browser redirected them to MalwareInfect.com instead. You asked the user to clear their cache, history, and cookies, but the problem remains. What should you do NEXT to solve this problem?",
        "options": {
            "A": "Upgrade their web browser",
            "B": "Check the host.ini file",
            "C": "Conduct an antivirus scan",
            "D": "Disable System Restore"
        },
        "answer": "B",
        "explanation": "A modified hosts file can redirect legitimate domains to malicious IP addresses. Checking and correcting it should be the next step.",
        "objective": "Malware remediation"
    },
    {
        "question": "A system administrator is assigned an approved change request with a change window of 120 minutes. After 90 minutes, the change is stuck on step five of a five-step change. The server manager decides to initiate a rollback. Which describes what the system administrator should do next?",
        "options": {
            "A": "Leave the change as is and inform users of a workaround",
            "B": "Return the system to the original state before the change",
            "C": "Request additional time since the change is near completion",
            "D": "Return the system to step four since this was the last working step"
        },
        "answer": "B",
        "explanation": "Rollback procedures return the system to its original, stable state before the change began, not to a halfway step.",
        "objective": "Change management"
    },
    {
        "question": "Your company wants to ensure that users cannot access USB mass storage devices. You have conducted some research online and found that if you modify the HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\UsbStor key, it will prevent USB storage devices from being used. Which of the following tools should you use to modify this key?",
        "options": {
            "A": "MMC",
            "B": "MSConfig",
            "C": "RDS",
            "D": "RegEdit"
        },
        "answer": "D",
        "explanation": "RegEdit (Registry Editor) is the tool used to view and modify registry keys such as UsbStor.",
        "objective": "System security configuration"
    },
    {
        "question": "You are working for an organization that plans to upgrade its company-wide VPN solution to improve security and performance. The upgrade requires thorough testing, stakeholder approval, and scheduled implementation to minimize business disruptions. Since this change is not routine but also not an emergency, it must go through the full change management process, including documentation and risk assessment. Which of the following would BEST categorize this type of change?",
        "options": {
            "A": "Emergency change",
            "B": "Normal change",
            "C": "Standard change",
            "D": "Unauthorized change"
        },
        "answer": "B",
        "explanation": "Normal changes are planned, non-routine changes that require the full change management process, including risk assessment and approvals.",
        "objective": "Change management categories"
    },
    {
        "question": "Your company is concerned about the possibility of power fluctuations that may occur and cause a small dip in the input power to their server room for an extended period of time. What condition is this known as?",
        "options": {
            "A": "Power failure",
            "B": "Power spikes",
            "C": "Under-voltage event",
            "D": "Power surge"
        },
        "answer": "C",
        "explanation": "An under-voltage event (brownout) is when power dips below normal for an extended period, affecting sensitive equipment.",
        "objective": "Environmental controls"
    },
    {
        "question": "A company plans to dispose of numerous outdated laptops and hard drives containing customer financial records. To comply with regulatory requirements, what step must the company take during disposal?",
        "options": {
            "A": "Obtaining certificates of secure data destruction from disposal vendors.",
            "B": "Storing retired equipment indefinitely in secured warehouse storage.",
            "C": "Donating retired equipment directly to local schools or non-profits.",
            "D": "Reformatting all equipment thoroughly before discarding in public bins."
        },
        "answer": "A",
        "explanation": "Certified data destruction ensures compliance with regulatory requirements and prevents sensitive data exposure.",
        "objective": "Data disposal and compliance"
    },
    {
        "question": "Which of the following backup rotation schemes requires backups to be stored to at least two different types of media?",
        "options": {
            "A": "Grandfather-father-son",
            "B": "FIFO Backup",
            "C": "Tower of Hanoi",
            "D": "3-2-1 backup"
        },
        "answer": "D",
        "explanation": "The 3-2-1 backup rule requires three copies of data, two stored on different media types, and one stored offsite.",
        "objective": "Backup strategies"
    },
    {
        "question": "A manager wants employees to enter data in a shared spreadsheet but needs to prevent accidental modifications to formulas. What is the best way to achieve this?",
        "options": {
            "A": "Set the entire spreadsheet to read-only mode so no changes can be made.",
            "B": "Convert the spreadsheet to a static file format, preventing further edits.",
            "C": "Lock the formula cells while keeping data entry fields editable.",
            "D": "Require employees to submit data separately for manual entry."
        },
        "answer": "C",
        "explanation": "Locking formula cells ensures critical formulas cannot be changed while still allowing users to enter data in designated fields.",
        "objective": "Spreadsheet protection and data integrity"
    },
    {
        "question": "Dion Training uses DHCP to assign private Class B IP addresses to its Windows 10 workstations. Which of the following IP addresses is a Class B address?",
        "options": {
            "A": "10.5.34.15",
            "B": "172.16.13.12",
            "C": "169.254.125.154",
            "D": "192.168.2.14"
        },
        "answer": "B",
        "explanation": "The private Class B range is 172.16.0.0 to 172.31.255.255, so 172.16.13.12 falls within this range.",
        "objective": "Networking fundamentals: IP addressing"
    },
    {
        "question": "Bruce is a user who has put in a ticket stating that their Windows 10 computer is running unusually slow after logging in. Task Manager shows high disk usage (>99%), primarily from a process named 'Antimalware Service Executable.' From the following choices, what would be the best way to solve this?",
        "options": {
            "A": "Restart the computer in Safe Mode and disable startup programs",
            "B": "Perform a full malware scan and schedule it for off-hours",
            "C": "Permanently disable their anti-malware program’s real-time protection",
            "D": "Update Windows Defender definitions and restart the system"
        },
        "answer": "D",
        "explanation": "High disk usage from Antimalware Service Executable often indicates outdated definitions. Updating Windows Defender ensures the service runs efficiently.",
        "objective": "Windows troubleshooting and performance optimization"
    },
    {
        "question": "A company is implementing enhanced user authentication for system administrators accessing the company's confidential servers. They intend to use two-factor authentication to accomplish this. Which of these BEST represents two-factor authentication?",
        "options": {
            "A": "Password and key fob",
            "B": "ID badge and keys",
            "C": "Fingerprint scanner and retina scan",
            "D": "Username and password"
        },
        "answer": "A",
        "explanation": "Two-factor authentication requires two different categories of authentication, such as something you know (password) and something you have (key fob).",
        "objective": "Authentication and access control"
    },
    {
        "question": "Eduardo is installing Windows 11 (64-bit) in a virtual machine on his macOS desktop. The installation is continually failing and producing an error. Eduardo has configured the virtual machine with a 2.2 GHz processor, 4 GB of memory, a 64 GB hard drive, and a 1280 x 720 screen resolution. Which item in the virtual machine should be increased to fix the installation issue experienced?",
        "options": {
            "A": "The screen resolution",
            "B": "Amount of hard drive space",
            "C": "Amount of memory",
            "D": "Number of CPU cores"
        },
        "answer": "C",
        "explanation": "Windows 11 requires more than 4 GB of RAM in practice for smooth installation. Increasing memory allocation resolves the issue.",
        "objective": "Virtual machine resource requirements"
    },
    {
        "question": "You are working as a mobile device technician for a large corporation's enterprise service desk. A user complains that every time they attempt to launch the company's mobile email application, it crashes and displays an error message of Code123. Which of the following should you do FIRST to attempt to solve this problem?",
        "options": {
            "A": "Rollback the app to an earlier version",
            "B": "Clear the app's cache",
            "C": "Reinstall the email app",
            "D": "Update the smartphone's OS"
        },
        "answer": "B",
        "explanation": "The first step in troubleshooting a crashing mobile app is to clear the cache, which often removes corrupted temporary data.",
        "objective": "Mobile device troubleshooting"
    },
    {
        "question": "A user attempts to visit a banking website and notices the browser displaying a security warning about an invalid certificate. What is the best action the user should take to protect sensitive information?",
        "options": {
            "A": "Avoid entering sensitive details until the certificate issue is resolved.",
            "B": "Continue browsing normally since the browser always shows this alert.",
            "C": "Update the browser’s software to see if it resolves the certificate warning.",
            "D": "Change browser privacy settings to disable future certificate warnings."
        },
        "answer": "A",
        "explanation": "An invalid certificate means the site may not be secure. The user should avoid entering sensitive details until the issue is resolved to prevent data theft.",
        "objective": "Web security & certificates"
    },
    {
        "question": "Which of the following is used to communicate data and preferences to child processes within a script or batch file?",
        "options": {
            "A": "Environmental variables",
            "B": "Constants",
            "C": "Variables",
            "D": "Comments"
        },
        "answer": "A",
        "explanation": "Environmental variables are inherited by child processes and allow configuration data to be passed from parent to child processes.",
        "objective": "Scripting & automation"
    },
    {
        "question": "Which of the following password policies defines the types of alphanumeric characters required to be utilized in a user's password?",
        "options": {
            "A": "Password complexity",
            "B": "Password length",
            "C": "Password expiration",
            "D": "Password history"
        },
        "answer": "A",
        "explanation": "Password complexity ensures users include uppercase, lowercase, numbers, and special characters for stronger security.",
        "objective": "Password policies"
    },
    {
        "question": "Which of the following types of software CANNOT be updated via the Windows Update program?",
        "options": {
            "A": "Driver updates",
            "B": "Firmware updates",
            "C": "Security patches",
            "D": "Critical fixes"
        },
        "answer": "B",
        "explanation": "Windows Update can install drivers, security patches, and critical fixes, but firmware updates typically require manufacturer tools.",
        "objective": "Windows updates & maintenance"
    },
    {
        "question": "Sally was checking her email when she noticed several automated replies from emails she doesn’t remember sending. What type of attack was Sally MOST likely the victim of?",
        "options": {
            "A": "Vishing",
            "B": "Phishing",
            "C": "Hijacked email",
            "D": "Spear phishing"
        },
        "answer": "C",
        "explanation": "Her email account was hijacked and used to send unauthorized messages. This is a sign of a compromised email account.",
        "objective": "Email security"
    },
    {
        "question": "An Android user recently cracked their screen and had it replaced. In a dark room, the phone works fine, but in normal light the display is dim and hard to read. What is MOST likely the problem?",
        "options": {
            "A": "Low battery",
            "B": "Auto-brightness is enabled",
            "C": "Faulty ambient light sensor",
            "D": "Defective display"
        },
        "answer": "C",
        "explanation": "The ambient light sensor controls auto-brightness. If damaged during screen replacement, it will misread light levels and adjust incorrectly.",
        "objective": "Mobile device troubleshooting"
    },
    {
        "question": "When Jason needs to log in to his bank, he must use a key fob to generate a random number code synchronized to a server for authentication. What type of device is Jason using?",
        "options": {
            "A": "Smart card",
            "B": "PIV card",
            "C": "Hardware token",
            "D": "Biometric lock"
        },
        "answer": "C",
        "explanation": "A hardware token generates one-time codes for two-factor authentication. The codes are synchronized with the server for verification.",
        "objective": "Authentication methods"
    },
    {
        "question": "Which of the following is an online storage solution provided by Apple that natively works with macOS and iOS devices?",
        "options": {
            "A": "OneDrive",
            "B": "Google Drive",
            "C": "iCloud",
            "D": "DropBox"
        },
        "answer": "C",
        "explanation": "iCloud is Apple’s native cloud storage that integrates with macOS and iOS devices.",
        "objective": "Cloud storage services"
    },
    {
        "question": "Which of the following is a primary advantage of the Android operating system compared to iOS?",
        "options": {
            "A": "It does not require updates or security patches",
            "B": "It uses the APFS file system for storage",
            "C": "It allows users to install apps from third-party sources",
            "D": "It exclusively supports proprietary hardware"
        },
        "answer": "C",
        "explanation": "Android allows sideloading apps from third-party sources, unlike iOS, which restricts apps to the App Store.",
        "objective": "Mobile OS comparison"
    },
    {
        "question": "Which of the following should be used to uniquely identify every piece of hardware installed on the corporate network, including servers, desktops, laptops, printers, and monitors?",
        "options": {
            "A": "Asset ID",
            "B": "MAC address",
            "C": "Location",
            "D": "IP address"
        },
        "answer": "A",
        "explanation": "Organizations assign unique asset IDs to track hardware across the network. MAC/IP can change, but asset IDs are permanent inventory identifiers.",
        "objective": "IT asset management"
    },
    {
        "question": "A user's computer is experiencing repeated BSODs and calls the service desk. The call is routed to Tier 2 support, and the technician is scheduled for a break in 2 minutes. Which of the following should the technician do?",
        "options": {
            "A": "Troubleshoot the issue for the user regardless of how long it takes",
            "B": "Ask another Tier 2 technician to answer the call",
            "C": "Ask the user to call back later",
            "D": "Answer the phone, put the user on hold, and help after break"
        },
        "answer": "A",
        "explanation": "Critical issues like repeated BSODs must be handled immediately, even if it delays the break. Customer impact takes priority.",
        "objective": "Help desk support procedures"
    },
    {
        "question": "The corporate network uses a centralized server to manage credentials for all its network devices. What type of server is MOST likely being used?",
        "options": {
            "A": "RADIUS",
            "B": "FTP",
            "C": "Kerberos",
            "D": "DNS"
        },
        "answer": "A",
        "explanation": "RADIUS provides centralized authentication for devices and users across a network.",
        "objective": "Network authentication"
    },
    {
        "question": "An IT trainer is explaining different types of screen locks to employees. Which description correctly identifies a primary characteristic of a PIN-based screen lock?",
        "options": {
            "A": "Requires drawing a predefined shape or pattern.",
            "B": "Uses a numeric code entered on a keypad.",
            "C": "Utilizes a physical fingerprint sensor to verify identity.",
            "D": "Relies on facial features captured by a camera."
        },
        "answer": "B",
        "explanation": "A PIN lock requires a numeric code, unlike pattern, fingerprint, or facial recognition methods.",
        "objective": "Mobile device security"
    },
    {
        "question": "You are configuring a SOHO network for a coffee shop and need to block a specific customer’s laptop from connecting by using its unique hardware identifier. Which configuration should you use?",
        "options": {
            "A": "Enforce a WPA2 password",
            "B": "MAC filtering",
            "C": "Port forwarding",
            "D": "Port filtering"
        },
        "answer": "B",
        "explanation": "MAC filtering blocks or allows network access based on the device’s unique MAC address.",
        "objective": "Network security"
    },
    {
        "question": "While troubleshooting why File Explorer is crashing on a Windows 10 machine, you determine that some system files may be corrupt. Which utility should you use?",
        "options": {
            "A": "gpupdate",
            "B": "sfc",
            "C": "regedit",
            "D": "dxdiag"
        },
        "answer": "B",
        "explanation": "System File Checker (sfc /scannow) scans and repairs corrupt system files in Windows.",
        "objective": "Windows troubleshooting"
    },
    {
        "question": "Which description accurately explains the function of clearing the browser cache?",
        "options": {
            "A": "It blocks potentially harmful websites from loading in the browser.",
            "B": "It prevents pop-up advertisements from displaying automatically.",
            "C": "It disables the tracking of user browsing history by websites.",
            "D": "It deletes stored copies of web pages to force fresh content loading."
        },
        "answer": "D",
        "explanation": "Clearing the cache removes saved versions of web pages, forcing the browser to load updated content from the server.",
        "objective": "Web browsing troubleshooting"
    },
    {
        "question": "A team is working on a shared document, but some edits are disappearing. What is the most likely cause?",
        "options": {
            "A": "The document automatically resets to an older version.",
            "B": "Multiple users are overwriting changes at the same time.",
            "C": "The file has reached its maximum number of saved edits.",
            "D": "The word processing tool is limited to viewing mode only."
        },
        "answer": "B",
        "explanation": "In shared environments, if multiple users edit simultaneously, changes may overwrite each other and cause edits to disappear.",
        "objective": "Collaboration tools"
    },
    {
        "question": "A user is trying to update their tablet’s operating system but keeps receiving 'Update failed' at 25% battery life. What is the best solution?",
        "options": {
            "A": "Switch to a cellular data connection instead of Wi-Fi",
            "B": "Plug the device into a charger and retry the update",
            "C": "Clear the cache partition from the device settings",
            "D": "Perform a factory reset before attempting the update again"
        },
        "answer": "B",
        "explanation": "Updates require the device to be plugged into a charger to ensure sufficient power during installation.",
        "objective": "Mobile device updates"
    },
    {
        "question": "Which of the following types of screen locks uses a secret pattern drawn on the screen to prevent access to a mobile device?",
        "options": {
            "A": "Passcode",
            "B": "TouchID",
            "C": "FaceID",
            "D": "Swipe"
        },
        "answer": "D",
        "explanation": "A swipe pattern lock uses a predefined drawn gesture for authentication, unlike PINs, fingerprints, or facial recognition.",
        "objective": "Mobile device security"
    },
    {
        "question": "Which of the following tools should you utilize to ensure you don't damage a laptop's SSD while replacing it?",
        "options": {
            "A": "ESD strap",
            "B": "Air filter mask",
            "C": "Antistatic bag",
            "D": "Latex gloves"
        },
        "answer": "A",
        "explanation": "An ESD strap prevents electrostatic discharge, protecting sensitive components like an SSD during handling.",
        "objective": "ESD protection & safety procedures"
    },
    {
        "question": "Which of the following file system formatting types should be used with a DVD?",
        "options": {
            "A": "CDFS",
            "B": "NTFS",
            "C": "FAT32",
            "D": "UDF"
        },
        "answer": "D",
        "explanation": "DVDs use the Universal Disk Format (UDF), which is designed for optical media.",
        "objective": "File systems for removable media"
    },
    {
        "question": "After upgrading their laptop from Windows 10 to Windows 11, a coworker now reports that several applications crash upon launch. The issue primarily affects older software used for work, while newer applications function normally. They need these legacy programs to work without constant crashes. What would be the best solution?",
        "options": {
            "A": "Reinstall Windows 10 to regain full compatibility with older software",
            "B": "Run the Disk Cleanup application and clear temporary files",
            "C": "Enable compatibility mode for the problematic applications",
            "D": "Increase the laptop’s RAM to improve application stability"
        },
        "answer": "C",
        "explanation": "Compatibility mode allows older software to run as if it were on an older version of Windows, preventing crashes.",
        "objective": "Windows application compatibility"
    },
    {
        "question": "You are configuring a new printer for a small real estate office with 4 computers connected to a single switch/router. No servers are available. Which method would BEST allow the users to print to the printer?",
        "options": {
            "A": "Configure the printer to support cloud printing",
            "B": "Configure a print server and connect the printer to it",
            "C": "Configure it as a shared printer connected to one of the four workstations",
            "D": "Configure the printer to support Bluetooth printing"
        },
        "answer": "C",
        "explanation": "Without a print server or network printer, the simplest solution is to connect the printer to one workstation and share it with the workgroup.",
        "objective": "Printer configuration in small networks"
    },
    {
        "question": "A user's personal settings are not showing up on their computer. You suspect that their profile has become corrupted within Windows. You attempt to look at their profile file but cannot find it in their profile directory. Which option should you configure to see this file?",
        "options": {
            "A": "User Accounts",
            "B": "Display Settings",
            "C": "Folder Options",
            "D": "Internet Options"
        },
        "answer": "C",
        "explanation": "Folder Options allows hidden files and system files to be viewed, which can reveal the corrupted profile data.",
        "objective": "Windows profile troubleshooting"
    },
    {
        "question": "A user's SOHO wireless network has slowed significantly. Normally they download at 900 Mbps, but now only 23 Mbps. The SSID shows WPA2 security. What is MOST likely the problem?",
        "options": {
            "A": "The WAN type needs to be upgraded to DSL or cable",
            "B": "Additional transmission power is needed for the wireless signal",
            "C": "WPA2 reduces download speeds and the user should switch to WPA3",
            "D": "Other users have connected to the WiFi due to a weak password"
        },
        "answer": "D",
        "explanation": "The sharp drop in speed suggests unauthorized users have connected to the WiFi due to a weak WPA2 password.",
        "objective": "Wireless network security troubleshooting"
    },
    {
        "question": "Jason checks the server room and finds it has only 10% humidity. Which of the following risks to the servers could occur due to this low humidity level?",
        "options": {
            "A": "Corrosion of the servers",
            "B": "Accidental static discharge",
            "C": "An under-voltage event",
            "D": "An over-voltage event"
        },
        "answer": "B",
        "explanation": "Low humidity increases the risk of static electricity, leading to accidental static discharge and hardware damage.",
        "objective": "Environmental risks in server rooms"
    },
    {
        "question": "Your coworker is creating a script to run on a Windows server using PowerShell. Which file format should the script use?",
        "options": {
            "A": ".bat",
            "B": ".sh",
            "C": ".py",
            "D": ".ps1"
        },
        "answer": "D",
        "explanation": "PowerShell scripts use the .ps1 extension for execution in Windows environments.",
        "objective": "Scripting and automation"
    },
    {
        "question": "Which of the following Control Panel sections would allow a technician to turn on Hyper-V on a Windows 10 Pro workstation?",
        "options": {
            "A": "Devices and Printers",
            "B": "System",
            "C": "Programs and Features",
            "D": "Device Manager"
        },
        "answer": "C",
        "explanation": "Hyper-V can be enabled through Programs and Features under 'Turn Windows features on or off.'",
        "objective": "Virtualization setup in Windows"
    },
    {
        "question": "An employee is complaining that every time they reboot their Windows 10 workstation, a music application loads automatically. Which tool would you use to disable this program from starting at boot?",
        "options": {
            "A": "Task manager",
            "B": "System information",
            "C": "Event viewer",
            "D": "User account control"
        },
        "answer": "A",
        "explanation": "Task Manager’s Startup tab allows disabling applications from automatically starting with Windows.",
        "objective": "Windows startup program management"
    },
    {
        "question": "Shirley is a project manager assigned to create internal training materials. She copies large sections from an external website without attribution. Which BEST describes this issue?",
        "options": {
            "A": "Copyright infringement",
            "B": "Data exfiltration",
            "C": "Plagiarism",
            "D": "Insider threat"
        },
        "answer": "C",
        "explanation": "Copying content without attribution is plagiarism. The emphasis is on unethical copying, not intellectual property theft.",
        "objective": "Professional ethics in IT"
    },
    {
        "question": "A user attempts to visit a banking website and the browser shows a security warning about an invalid certificate. What is the best action to protect sensitive information?",
        "options": {
            "A": "Avoid entering sensitive details until the certificate issue is resolved.",
            "B": "Continue browsing normally since the browser always shows this alert.",
            "C": "Update the browser’s software to see if it resolves the certificate warning.",
            "D": "Change browser privacy settings to disable future certificate warnings."
        },
        "answer": "A",
        "explanation": "The safest approach is to avoid entering sensitive information until the certificate issue is resolved.",
        "objective": "Web security & certificate validation"
    },
    {
        "question": "Which of the following best describes the benefit of instant messaging for workplace collaboration?",
        "options": {
            "A": "Conversations are stored permanently without deletion.",
            "B": "Messages are sent instantly, allowing quick communication.",
            "C": "Employees must be in the same location to send messages.",
            "D": "Messages only appear at scheduled update times."
        },
        "answer": "B",
        "explanation": "Instant messaging provides real-time communication, allowing teams to collaborate quickly without delays.",
        "objective": "Communication tools & collaboration"
    },
    {
        "question": "During the reconnaissance phase of a penetration test, which method would MOST likely be the best for exploiting Android devices connected via VPN?",
        "options": {
            "A": "Use a tool like ICSSPLOIT to target specific vulnerabilities",
            "B": "Use social engineering to trick a user into opening a malicious APK",
            "C": "Identify a jailbroken device for easy exploitation",
            "D": "Use web-based exploits against the device's web interfaces"
        },
        "answer": "B",
        "explanation": "Social engineering to trick users into installing a malicious APK is the most effective attack vector against Android devices.",
        "objective": "Penetration testing & mobile exploitation"
    },
    {
        "question": "Which type of encryption uses a 128-bit encryption key but is considered weak due to its use of a 24-bit initialization vector?",
        "options": {
            "A": "WEP",
            "B": "WPA",
            "C": "WPA2",
            "D": "WPS"
        },
        "answer": "A",
        "explanation": "WEP uses a 128-bit key but its 24-bit initialization vector makes it vulnerable to cracking.",
        "objective": "Wireless encryption & security"
    },
    {
        "question": "Which of the following is the MOST important thing from the IT perspective to add to the scope of work and change request before approval?",
        "options": {
            "A": "Rollback plan",
            "B": "Risk analysis",
            "C": "Plan for change",
            "D": "End-user acceptance"
        },
        "answer": "B",
        "explanation": "Risk analysis ensures potential security and performance issues are identified before implementing the change.",
        "objective": "Change management"
    },
    {
        "question": "What MOST likely happened during Edward's vacation that caused the missing inbox folders in his email client?",
        "options": {
            "A": "The network file share's permission has been modified",
            "B": "The internet security options in his email client have been modified",
            "C": "Edward's user account permission has changed",
            "D": "The operating system was updated"
        },
        "answer": "C",
        "explanation": "Since he can still send/receive email but lost access to the shared mailbox, his account permissions must have changed.",
        "objective": "Email permissions & account management"
    },
    {
        "question": "Your network administrator shows you documentation of switch ports on a patch panel for a network upgrade. What document are you MOST likely holding?",
        "options": {
            "A": "Physical network diagram",
            "B": "Inventory management plan",
            "C": "Logical network diagram",
            "D": "Process flow diagram"
        },
        "answer": "A",
        "explanation": "Physical network diagrams show cabling, switch ports, and patch panel connections.",
        "objective": "Networking documentation"
    },
    {
        "question": "A workstation runs extremely slow, CPU and network usage are near 100%, but only Microsoft Word is running. What is MOST likely the issue?",
        "options": {
            "A": "The application is not compatible with this OS",
            "B": "The computer has become a zombie",
            "C": "The computer is the victim of a DoS attack",
            "D": "The network's firewall is blocking outbound traffic"
        },
        "answer": "B",
        "explanation": "High CPU and network usage suggests the system is part of a botnet and acting as a zombie computer.",
        "objective": "Security threats & malware"
    },
    {
        "question": "During a data breach investigation, credentials from a terminated employee were found still active. What category does this breach fall under?",
        "options": {
            "A": "Zero-day",
            "B": "Known threat",
            "C": "Insider Threat",
            "D": "Advanced persistent threat"
        },
        "answer": "C",
        "explanation": "Because the breach involved a former employee account that was not disabled, it qualifies as an insider threat.",
        "objective": "Insider threats & account security"
    },
    {
        "question": "Which macOS feature is used to backup and restore files to an external hard disk?",
        "options": {
            "A": "Snapshot",
            "B": "Time Machine",
            "C": "Boot Camp",
            "D": "Remote disc"
        },
        "answer": "B",
        "explanation": "Time Machine is macOS's built-in tool for creating backups to external drives.",
        "objective": "Backup & recovery"
    },
    {
        "question": "The CFO asks for a way to reduce software licensing costs while still allowing remote access to applications. What should Maria recommend?",
        "options": {
            "A": "Use a Remote Desktop Protocol (RDP) application on a Windows 10 desktop",
            "B": "Use a Virtual Network Client (VNC) on a Windows 2019 server",
            "C": "Install and deploy thin clients without an operating system for each user",
            "D": "Install and deploy Windows 10 Home edition on each user's thick client"
        },
        "answer": "C",
        "explanation": "Thin clients reduce licensing and maintenance costs because applications run on centralized servers.",
        "objective": "Virtualization & thin client computing"
    },
    {
        "question": "Which tool should you use to avoid damaging a laptop's SSD during replacement?",
        "options": {
            "A": "ESD strap",
            "B": "Air filter mask",
            "C": "Antistatic bag",
            "D": "Latex gloves"
        },
        "answer": "A",
        "explanation": "An ESD strap prevents static electricity from damaging sensitive electronic components like SSDs.",
        "objective": "Hardware safety"
    },
    {
        "question": "Which file system formatting type should be used with a DVD?",
        "options": {
            "A": "CDFS",
            "B": "NTFS",
            "C": "FAT32",
            "D": "UDF"
        },
        "answer": "D",
        "explanation": "DVDs are formatted with UDF (Universal Disk Format), which is designed for optical media.",
        "objective": "File systems & media"
    },
    {
        "question": "After upgrading to Windows 11, older applications crash on launch. What is the best solution?",
        "options": {
            "A": "Reinstall Windows 10 to regain full compatibility",
            "B": "Run Disk Cleanup and clear temporary files",
            "C": "Enable compatibility mode for the problematic applications",
            "D": "Increase the laptop's RAM"
        },
        "answer": "C",
        "explanation": "Compatibility mode allows older applications to run properly on newer operating systems.",
        "objective": "Operating system troubleshooting"
    },
    {
        "question": "How should you configure a new printer in a small office with 4 computers connected to a single switch and no print server?",
        "options": {
            "A": "Configure the printer to support cloud printing",
            "B": "Configure a print server and connect the printer to it",
            "C": "Configure it as a shared printer connected to one of the four workstations",
            "D": "Configure the printer to support Bluetooth printing"
        },
        "answer": "C",
        "explanation": "The best solution in a small workgroup setup is to share the printer from one workstation.",
        "objective": "Printer configuration"
    },
    {
        "question": "A user's personal settings are missing because their Windows profile seems corrupted. What option should you configure to view the profile file?",
        "options": {
            "A": "User Accounts",
            "B": "Display Settings",
            "C": "Folder Options",
            "D": "Internet Options"
        },
        "answer": "C",
        "explanation": "Folder Options allows you to show hidden files and folders, which may include the user profile.",
        "objective": "Windows profile troubleshooting"
    },
    {
        "question": "A SOHO wireless network slows from 900 Mbps to 23 Mbps. What is the MOST likely cause?",
        "options": {
            "A": "The WAN type needs to be upgraded to DSL or cable",
            "B": "Additional transmission power is needed for the wireless signal",
            "C": "WPA2 reduces download speeds and the user should switch to WPA3",
            "D": "Other users have connected to the WiFi due to a weak password"
        },
        "answer": "D",
        "explanation": "A sudden slowdown usually indicates unauthorized users connected due to a weak WiFi password.",
        "objective": "Wireless troubleshooting & security"
    },
    {
        "question": "Which of the following types of information can be displayed by the top command in Linux?",
        "options": {
            "A": "User accounts ordered by the number of logins",
            "B": "Running processes ordered by CPU or RAM consumption",
            "C": "User groups ordered by the number of members",
            "D": "Amount of CPU cores, user groups, and free storage"
        },
        "answer": "B",
        "explanation": "The Linux top command shows real-time information about running processes, typically sorted by CPU or memory usage, along with their resource consumption.",
        "objective": "Linux monitoring & process management"
    },
    {
        "question": "Your supervisor has requested remote access to a particular server to check specific data and processes during evenings and weekends. You are concerned about security. Which action is the MOST important to take before granting remote access?",
        "options": {
            "A": "Disable internet access from the server outside of normal business hours",
            "B": "Educate your supervisor on safe internet browsing techniques",
            "C": "Set the server's antivirus to auto-update and run a full scan every Saturday night",
            "D": "Install the latest security updates and patches to the server"
        },
        "answer": "D",
        "explanation": "Ensuring the server is fully patched with the latest security updates reduces known vulnerabilities before exposing it to additional remote access.",
        "objective": "Server hardening & patch management"
    },
    {
        "question": "You submit an RFC to deploy a security patch to all Windows 2019 servers at 11 p.m. via an automated process. Which change-request document describes potential uncertainty or adverse effects during installation?",
        "options": {
            "A": "Purpose",
            "B": "Risk analysis",
            "C": "Plan",
            "D": "Scope"
        },
        "answer": "B",
        "explanation": "The risk analysis documents potential impacts, likelihood, and mitigation strategies for the change.",
        "objective": "Change management"
    },
    {
        "question": "Which Control Panel section should a technician use to configure Narrator so Windows 10 can read aloud the list of files to a user?",
        "options": {
            "A": "Ease of Access",
            "B": "Indexing Options",
            "C": "File Explorer Options",
            "D": "Sound"
        },
        "answer": "A",
        "explanation": "Narrator and other accessibility tools are configured under Ease of Access.",
        "objective": "Windows accessibility settings"
    },
    {
        "question": "After completing a three-day smartphone repair, a customer complains that it took too long and asks about the steps you performed. What should you do NEXT?",
        "options": {
            "A": "Provide documentation of the repair and thank them for their patience",
            "B": "Become defensive and explain why each step was necessary",
            "C": "Tell the customer it was their fault",
            "D": "Post about the encounter on social media"
        },
        "answer": "A",
        "explanation": "Professional communication includes providing clear repair documentation and showing appreciation for the customer’s patience.",
        "objective": "Professionalism & communication"
    },
    {
        "question": "Which Windows 10 utility is used to test the DirectX subsystem for video and sound-related problems?",
        "options": {
            "A": "msinfo32",
            "B": "taskschd",
            "C": "dxdiag",
            "D": "eventvwr"
        },
        "answer": "C",
        "explanation": "dxdiag (DirectX Diagnostic Tool) verifies DirectX functionality and drivers for audio/video.",
        "objective": "Windows diagnostic tools"
    },
    {
        "question": "A small office has four PCs connected to a single 4-port switch/router/cable-modem device and no servers. You must allow all four computers to print to one printer. What is the BEST approach?",
        "options": {
            "A": "Set up a dedicated print server",
            "B": "Enable Bluetooth printing on the printer",
            "C": "Use cloud printing",
            "D": "Share the printer from one of the workstations"
        },
        "answer": "D",
        "explanation": "In a tiny workgroup with no spare ports or servers, sharing the printer from one PC allows the others to print over the LAN when that PC is on.",
        "objective": "SOHO printing"
    },
    {
        "question": "A game lists 8 GB of RAM as the minimum and 16 GB as the recommended amount. The user plays only one game at a time. What is the best RAM recommendation?",
        "options": {
            "A": "Install less than the minimum to save money",
            "B": "Install only the minimum so the game launches",
            "C": "Upgrade to the recommended amount",
            "D": "Install far beyond the recommendation for maximum performance"
        },
        "answer": "C",
        "explanation": "Installing the recommended RAM provides better performance and reduces slowdowns compared to the bare minimum.",
        "objective": "PC hardware recommendations"
    },
    {
        "question": "You are working as a mobile device technician for a large corporation's enterprise service desk. A user complains that every time they attempt to launch the company's mobile email application, it crashes and displays an error message of Code123. Which of the following should you do FIRST to attempt to solve this problem?",
        "options": {
            "A": "Clear the app's cache",
            "B": "Rollback the app to an earlier version",
            "C": "Update the smartphone's OS",
            "D": "Reinstall the email app"
        },
        "answer": "A",
        "explanation": "When a single app repeatedly crashes, the least-invasive first step is to clear the app’s cache/data. If the problem persists, then consider reinstalling or updating.",
        "objective": "Mobile device troubleshooting"
    },
    {
        "question": "You are a technician assigned to troubleshoot a Windows 10 PC that fails to boot. After installing a secondary hard drive, the system displayed a 'BOOTMGR is missing' error on startup. Both drives are recognized in the BIOS. What command should you use next to try to restore boot functionality without reinstalling Windows?",
        "options": {
            "A": "sfc /scannow",
            "B": "bootrec /fixboot",
            "C": "diskpart",
            "D": "chkdsk /f"
        },
        "answer": "B",
        "explanation": "The BOOTMGR error indicates a damaged or missing boot sector/BCD. 'bootrec /fixboot' rewrites the boot sector and is the appropriate repair action.",
        "objective": "Windows startup repair"
    },
    {
        "question": "Which of the following file types are commonly used by network administrators to perform repetitive tasks using a Microsoft proprietary scripting language?",
        "options": {
            "A": ".vbs",
            "B": ".js",
            "C": ".py",
            "D": ".sh"
        },
        "answer": "A",
        "explanation": "VBScript (Visual Basic Script) is Microsoft’s proprietary scripting language; scripts typically use the .vbs file extension.",
        "objective": "Scripting & automation basics"
    },
    {
        "question": "Which of the following types of wireless encryption uses a 128-bit key but is considered weak due to its 24-bit initialization vector?",
        "options": {
            "A": "WEP",
            "B": "WPA",
            "C": "WPS",
            "D": "WPA2"
        },
        "answer": "A",
        "explanation": "WEP often advertises 64/128-bit keys (104-bit key + 24-bit IV). The small, reusable IV makes WEP vulnerable and insecure.",
        "objective": "Wireless security standards"
    },
    {
        "question": "Your company is concerned about power fluctuations that may cause a large increase in input power to the server room. What is this condition called?",
        "options": {
            "A": "Power failure",
            "B": "Under-voltage event",
            "C": "Blackout",
            "D": "Power spikes"
        },
        "answer": "D",
        "explanation": "A sudden, brief increase in voltage above normal is a power spike (surge). This can damage equipment and should be mitigated with surge protection/UPS.",
        "objective": "Power protection & safety"
    },
    {
        "question": "During a training session, an instructor explains the purpose of valid website certificates. How should a valid security certificate be accurately described?",
        "options": {
            "A": "A browser plug-in ensuring that websites load as quickly as possible.",
            "B": "A digital document confirming the website's identity and enabling a secure connection.",
            "C": "A privacy setting preventing websites from tracking browsing activities.",
            "D": "A software update issued regularly to enhance browser security settings."
        },
        "answer": "B",
        "explanation": "TLS/SSL certificates validate a site’s identity and enable encrypted (HTTPS) connections between the client and the server.",
        "objective": "Web security & PKI"
    },
    {
        "question": "Which file system type is used by default when installing macOS on a modern workstation?",
        "options": {
            "A": "NTFS",
            "B": "APFS",
            "C": "HFS+",
            "D": "FAT32"
        },
        "answer": "B",
        "explanation": "Modern versions of macOS default to APFS (Apple File System), optimized for SSDs and used since macOS High Sierra.",
        "objective": "macOS fundamentals"
    },
    {
        "question": "Which of the following describes the security method used when users enter their username and password only once and can access multiple applications?",
        "options": {
            "A": "Inheritance",
            "B": "Permission propagation",
            "C": "Multifactor authentication",
            "D": "SSO"
        },
        "answer": "D",
        "explanation": "Single sign-on (SSO) provides one authentication session that is trusted by multiple apps/services, so the user logs in once.",
        "objective": "Identity & access management"
    },
    {
        "question": "Which of the following file system formatting types should be used with a DVD?",
        "options": {
            "A": "NTFS",
            "B": "CDFS",
            "C": "FAT32",
            "D": "UDF"
        },
        "answer": "D",
        "explanation": "Optical media such as DVDs and Blu-ray discs use UDF (Universal Disk Format). CDFS is for CDs, not DVDs.",
        "objective": "Storage media & filesystems"
    },
    {
        "question": "Which of the following remote access protocols should you use to connect to a Windows Server 2019 host and control it with your mouse and keyboard from your workstation?",
        "options": {
            "A": "SSH",
            "B": "Telnet",
            "C": "RDP",
            "D": "VNC"
        },
        "answer": "C",
        "explanation": "Remote Desktop Protocol (RDP) provides a full graphical remote session to Windows systems, allowing keyboard and mouse control.",
        "objective": "Remote access tools"
    },
    {
        "question": "Eduardo has jailbroken his iPhone to install third-party apps and now experiences crashes and administrative-level apps. The device no longer receives official updates. What is the BEST solution to secure the device and prevent further issues?",
        "options": {
            "A": "Install a third-party antivirus app",
            "B": "Revoke the app’s permissions and continue using the device",
            "C": "Restore the device to factory settings to remove the jailbreak",
            "D": "Ignore the issue since the user intentionally modified the device"
        },
        "answer": "C",
        "explanation": "Jailbreaking compromises security and disables official updates. A factory reset reinstalls iOS and removes the jailbreak and unauthorized modifications.",
        "objective": "Mobile device security"
    },
    {
        "question": "A company is integrating an AI-powered virtual assistant into its internal communication system. The legal team is concerned that sensitive business information might be accessible by external entities depending on how the AI processes and stores data. What is the MOST important concern?",
        "options": {
            "A": "Data privacy",
            "B": "User interface design",
            "C": "System update frequency",
            "D": "Software licensing terms"
        },
        "answer": "A",
        "explanation": "When introducing AI services that process internal communications, the primary risk is data privacy—how data is collected, stored, shared, and protected from unauthorized access.",
        "objective": "Risk & compliance (data protection)"
    },
    {
        "question": "What does clearing a web browser’s cache do?",
        "options": {
            "A": "Blocks potentially harmful websites from loading",
            "B": "Disables tracking of user browsing history by websites",
            "C": "Prevents pop-up advertisements from displaying automatically",
            "D": "Deletes stored copies of web pages so fresh content loads"
        },
        "answer": "D",
        "explanation": "The cache stores local copies of page assets. Clearing it removes those files so the browser fetches the newest versions.",
        "objective": "Browser troubleshooting"
    },
    {
        "question": "A user with repeated BSODs calls the service desk. The call is routed to Tier 2, but the Tier 2 technician’s break is in about two minutes. What should the technician do?",
        "options": {
            "A": "Ask the user to call back later",
            "B": "Troubleshoot regardless of how long it takes",
            "C": "Answer, put the user on hold, then help after the break",
            "D": "Have another Tier 2 technician take the call"
        },
        "answer": "D",
        "explanation": "Follow help-desk procedures: avoid starting a long session you can’t complete and transfer to an available Tier 2 technician.",
        "objective": "Professionalism & escalation"
    },
    {
        "question": "An attacker uses a precomputed table of values to try to crack a Windows password. What type of attack is this?",
        "options": {
            "A": "Dictionary",
            "B": "Rainbow table",
            "C": "Hybrid",
            "D": "Brute-force"
        },
        "answer": "B",
        "explanation": "Rainbow tables are precomputed hash lookup tables used to reverse password hashes quickly.",
        "objective": "Security threats—password attacks"
    },
    {
        "question": "When airplane mode is enabled on a laptop, an external mouse and headphones stop working. Which technology being disabled most likely causes this?",
        "options": {
            "A": "GPS",
            "B": "Wireless (Wi-Fi)",
            "C": "Bluetooth",
            "D": "Cellular"
        },
        "answer": "C",
        "explanation": "Airplane mode disables radios, including Bluetooth—which many mice and headphones use.",
        "objective": "Mobile device connectivity"
    },
    {
        "question": "You receive an email stating “You won a free iPhone! Click the link to claim.” How should you classify this email?",
        "options": {
            "A": "Spoofing",
            "B": "Phishing",
            "C": "Spear phishing",
            "D": "Zero-day"
        },
        "answer": "B",
        "explanation": "It’s a broad, non-targeted attempt to trick users into clicking a malicious link and providing information—phishing.",
        "objective": "Social engineering & email security"
    },
    {
        "question": "Which term BEST describes the process of documenting everyone who has physical access to or possession of evidence?",
        "options": {
            "A": "Chain of custody",
            "B": "Financial responsibility",
            "C": "Secure copy protocol",
            "D": "Legal hold"
        },
        "answer": "A",
        "explanation": "Chain of custody records each person who handled evidence and when, preserving integrity and admissibility.",
        "objective": "Digital forensics & incident response"
    },
    {
        "question": "You are replacing a swollen battery in a customer's smartphone. Which of the following should you use? (Select TWO)",
        "options": {
            "A": "Compressed air",
            "B": "Air filter mask",
            "C": "Safety goggles",
            "D": "Gloves"
        },
        "answer": [
            "C",
            "D"
        ],
        "explanation": "Swollen lithium-ion batteries can rupture or leak caustic electrolyte. Wear safety goggles and gloves to protect eyes and skin while handling and replacing the battery.",
        "objective": "4.3 Safety procedures and environmental impacts"
    },
    {
        "question": "Which of the following devices should you NEVER disassemble during troubleshooting due to the risk of electrocution?",
        "options": {
            "A": "CRT display",
            "B": "Tablet",
            "C": "Printer",
            "D": "External hard drive enclosure"
        },
        "answer": "A",
        "explanation": "CRT monitors contain high-voltage capacitors that can retain a dangerous charge long after power is removed, so they should not be disassembled.",
        "objective": "4.3 Safety procedures and environmental impacts"
    },
    {
        "question": "A system administrator noticed that an employee's account has been attempting to log in to multiple workstations and servers across the network without success. The employee does not have access to these systems. Which action should the administrator take on this account in Active Directory?",
        "options": {
            "A": "Lock the user's account",
            "B": "Disable the user's account",
            "C": "Delete the user's account",
            "D": "Reset the password of the user's account"
        },
        "answer": "B",
        "explanation": "Disabling the account immediately prevents further logon attempts while the incident is investigated. Deleting removes auditing evidence, and locking is typically temporary/automatic.",
        "objective": "2.2 Identity and access management"
    },
    {
        "question": "After replacing a client’s security device that protects their screened subnet, external users can no longer connect remotely to the application. Which device was MOST likely misconfigured?",
        "options": {
            "A": "DHCP",
            "B": "DNS",
            "C": "Content filter",
            "D": "Firewall"
        },
        "answer": "D",
        "explanation": "A screened subnet (DMZ) is protected by firewalls. If external access to services in that subnet stops after replacement, the firewall rules/NAT are likely misconfigured.",
        "objective": "2.4 Network security devices"
    },
    {
        "question": "Which of the following tools will automatically analyze your hard disk drive or solid-state device to identify any unused files for removal?",
        "options": {
            "A": "Disk defragmenter",
            "B": "Disk Cleanup",
            "C": "Device Manager",
            "D": "Performance Monitor"
        },
        "answer": "B",
        "explanation": "Disk Cleanup scans drives for unnecessary files (temporary files, recycle bin, system files) and offers to remove them automatically.",
        "objective": "3.3 Windows maintenance tools"
    },
    {
        "question": "Before approving a new method for deploying security patches, another senior administrator is assigned to review the plan to ensure it follows best practices, minimizes risks, and aligns with policies. Which change-management step BEST describes this?",
        "options": {
            "A": "Implementation",
            "B": "Standard change",
            "C": "Peer review",
            "D": "Change freeze"
        },
        "answer": "C",
        "explanation": "Having another qualified administrator examine the plan for completeness and risk is a peer review step in change management.",
        "objective": "4.1 Change management and documentation"
    },
    {
        "question": "You are replacing a swollen battery in a customer's smartphone. Which of the following should you use? (Select TWO)",
        "options": {
            "A": "Compressed air",
            "B": "Air filter mask",
            "C": "Safety goggles",
            "D": "Gloves"
        },
        "answer": [
            "C",
            "D"
        ],
        "explanation": "Swollen lithium-ion batteries can rupture or leak caustic electrolyte. Wear safety goggles and gloves to protect eyes and skin while handling and replacing the battery.",
        "objective": "4.3 Safety procedures and environmental impacts"
    },
    {
        "question": "Which of the following devices should you NEVER disassemble during troubleshooting due to the risk of electrocution?",
        "options": {
            "A": "CRT display",
            "B": "Tablet",
            "C": "Printer",
            "D": "External hard drive enclosure"
        },
        "answer": "A",
        "explanation": "CRT monitors contain high-voltage capacitors that can retain a dangerous charge long after power is removed, so they should not be disassembled.",
        "objective": "4.3 Safety procedures and environmental impacts"
    },
    {
        "question": "A system administrator noticed that an employee's account has been attempting to log in to multiple workstations and servers across the network without success. The employee does not have access to these systems. Which action should the administrator take on this account in Active Directory?",
        "options": {
            "A": "Lock the user's account",
            "B": "Disable the user's account",
            "C": "Delete the user's account",
            "D": "Reset the password of the user's account"
        },
        "answer": "B",
        "explanation": "Disabling the account immediately prevents further logon attempts while the incident is investigated. Deleting removes auditing evidence, and locking is typically temporary/automatic.",
        "objective": "2.2 Identity and access management"
    },
    {
        "question": "After replacing a client’s security device that protects their screened subnet, external users can no longer connect remotely to the application. Which device was MOST likely misconfigured?",
        "options": {
            "A": "DHCP",
            "B": "DNS",
            "C": "Content filter",
            "D": "Firewall"
        },
        "answer": "D",
        "explanation": "A screened subnet (DMZ) is protected by firewalls. If external access to services in that subnet stops after replacement, the firewall rules/NAT are likely misconfigured.",
        "objective": "2.4 Network security devices"
    },
    {
        "question": "Which of the following tools will automatically analyze your hard disk drive or solid-state device to identify any unused files for removal?",
        "options": {
            "A": "Disk defragmenter",
            "B": "Disk Cleanup",
            "C": "Device Manager",
            "D": "Performance Monitor"
        },
        "answer": "B",
        "explanation": "Disk Cleanup scans drives for unnecessary files (temporary files, recycle bin, system files) and offers to remove them automatically.",
        "objective": "3.3 Windows maintenance tools"
    },
    {
        "question": "Before approving a new method for deploying security patches, another senior administrator is assigned to review the plan to ensure it follows best practices, minimizes risks, and aligns with policies. Which change-management step BEST describes this?",
        "options": {
            "A": "Implementation",
            "B": "Standard change",
            "C": "Peer review",
            "D": "Change freeze"
        },
        "answer": "C",
        "explanation": "Having another qualified administrator examine the plan for completeness and risk is a peer review step in change management.",
        "objective": "4.1 Change management and documentation"
    },
    {
        "question": "Which command identifies devices (hops) between a client and a destination that are experiencing network latency?",
        "options": {
            "A": "pathping",
            "B": "net use",
            "C": "netstat",
            "D": "ping"
        },
        "answer": "A",
        "explanation": "pathping combines ping and tracert to show per-hop latency and packet loss to diagnose where delays occur along a route.",
        "objective": "2.x Network troubleshooting tools"
    },
    {
        "question": "The border router shows very high traffic during non-working hours, causing outages for the company’s web servers. What is the MOST likely cause?",
        "options": {
            "A": "Distributed DoS",
            "B": "Session hijacking",
            "C": "Evil twin",
            "D": "ARP spoofing"
        },
        "answer": "A",
        "explanation": "A distributed denial-of-service flood generates excessive traffic—often off-hours—overwhelming the router and web servers.",
        "objective": "2.x Security threats and attacks"
    },
    {
        "question": "Which Linux command changes the permissions of a file?",
        "options": {
            "A": "sudo",
            "B": "chown",
            "C": "pwd",
            "D": "chmod"
        },
        "answer": "D",
        "explanation": "chmod modifies read, write, and execute permissions on files and directories in Linux.",
        "objective": "1.9 Linux basics and commands"
    },
    {
        "question": "A macOS user browsing the web gets a pop-up that says: 'Windows Enterprise Defender: Your computer is infected with a virus, click here to remove it!' What type of threat is this?",
        "options": {
            "A": "Phishing",
            "B": "Rogue anti-virus",
            "C": "Pharming",
            "D": "Worm"
        },
        "answer": "B",
        "explanation": "Fake anti-virus (rogue AV) pop-ups try to trick users into installing malware or paying for bogus software.",
        "objective": "2.x Social engineering and malware"
    },
    {
        "question": "Which Windows command-line tool erases all data on a hard disk and prepares it to accept new Windows files?",
        "options": {
            "A": "format /fs:NTFS",
            "B": "sfc /now",
            "C": "chkdsk /f",
            "D": "diskpart list disk"
        },
        "answer": "A",
        "explanation": "The format command creates a filesystem (e.g., NTFS) on a disk, wiping existing data and preparing it for new files.",
        "objective": "3.x Windows command-line utilities"
    },
    {
        "question": "A Windows 10 laptop connected by USB to a known-good printer cannot print. Which action should you try FIRST?",
        "options": {
            "A": "Disable/enable the wireless network adapter",
            "B": "Restart the print spooler service",
            "C": "Restart Windows Defender",
            "D": "Rollback the USB drivers"
        },
        "answer": "B",
        "explanation": "If the printer and connection are OK, restarting the Print Spooler service often resolves stuck or failed print jobs.",
        "objective": "4.x Print and peripheral troubleshooting"
    },
    {
        "question": "Which Linux command can overwrite an entire hard drive with zeros?",
        "options": {
            "A": "dd",
            "B": "mv",
            "C": "cp",
            "D": "rm"
        },
        "answer": "A",
        "explanation": "The dd utility can write raw data to a device (e.g., dd if=/dev/zero of=/dev/sdX) to overwrite it. mv moves files, cp copies files, and rm deletes files.",
        "objective": "Linux basics & shell commands"
    },
    {
        "question": "You are replacing a computer’s hard drive. What should you do FIRST to prevent an electrical hazard while working on the computer?",
        "options": {
            "A": "Place the computer on a grounded workbench",
            "B": "Disconnect the power before servicing the computer",
            "C": "Connect an ESD strap to yourself to prevent shock",
            "D": "Place the computer and its components on an ESD mat"
        },
        "answer": "B",
        "explanation": "The top safety step before servicing any computer is to remove power (and disconnect the battery if applicable) to prevent electrical shock. ESD strap/mat protect components from static, not you from electrical hazards.",
        "objective": "Safety procedures for PC repair"
    },
    {
        "question": "After seizing an employee’s laptop for suspected illegal activity and preparing to hand it to law enforcement, what should you do?",
        "options": {
            "A": "Maintain the chain of custody",
            "B": "Quarantine the system",
            "C": "Document the changes the employee made",
            "D": "Preserve the evidence"
        },
        "answer": "A",
        "explanation": "Maintaining a complete chain-of-custody log ensures the evidence’s integrity and admissibility by documenting who handled the device and when.",
        "objective": "Incident response & documentation"
    },
    {
        "question": "Which remote access tool is a command-line terminal emulator that operates on TCP port 23?",
        "options": {
            "A": "Telnet",
            "B": "RDP",
            "C": "SSH",
            "D": "VNC"
        },
        "answer": "A",
        "explanation": "Telnet is a plaintext terminal emulation protocol that uses TCP port 23. RDP uses 3389, SSH uses 22, and VNC commonly uses 5900/5901.",
        "objective": "Remote access protocols"
    },
    {
        "question": "An application becomes unresponsive in Windows. Which Task Manager feature should be used to terminate it?",
        "options": {
            "A": "Performance",
            "B": "Processes",
            "C": "Startup",
            "D": "Services"
        },
        "answer": "B",
        "explanation": "Use the Processes tab to select the hung application and choose “End task.” Performance and Services are for monitoring and service management; Startup controls startup apps.",
        "objective": "Windows troubleshooting tools"
    },
    {
        "question": "A new iPhone can get online, but a user’s AirPods won’t work. What is the MOST likely cause?",
        "options": {
            "A": "Wi-Fi is not enabled",
            "B": "Bluetooth is not enabled",
            "C": "The phone is in airplane mode",
            "D": "Cellular is not enabled"
        },
        "answer": "B",
        "explanation": "AirPods connect via Bluetooth. The phone’s ability to get online indicates Wi-Fi/cellular are fine, so the most probable cause is that Bluetooth is disabled.",
        "objective": "Mobile device connectivity troubleshooting"
    },
    {
        "question": "After upgrading a laptop from Windows 10 to Windows 11, several older work applications now crash while newer apps run fine. What is the BEST step to keep those legacy apps working without constant crashes?",
        "options": {
            "A": "Reinstall Windows 10 to regain full compatibility with older software",
            "B": "Enable compatibility mode for the problematic applications",
            "C": "Run the Disk Cleanup application and clear temporary files",
            "D": "Increase the laptop’s RAM to improve application stability"
        },
        "answer": "B",
        "explanation": "Windows' Compatibility Mode allows legacy applications to run with settings that emulate earlier versions of Windows, which is ideal when older apps crash after an OS upgrade.",
        "objective": "Windows OS troubleshooting"
    },
    {
        "question": "You need to access a workstation’s BIOS but the user forgot the BIOS password. What action should you take to reset the BIOS password?",
        "options": {
            "A": "Remove and replace the CMOS battery",
            "B": "Conduct a dictionary attack",
            "C": "Conduct a brute force attack",
            "D": "Unplug and reconnect the mainboard power cable"
        },
        "answer": "A",
        "explanation": "Removing (or shorting the reset jumper for) the CMOS battery clears the CMOS/BIOS settings, which resets a forgotten BIOS password.",
        "objective": "PC hardware & BIOS/UEFI"
    },
    {
        "question": "After software updates, a lab researcher’s PC can no longer use lab equipment. The vendor confirms the latest driver is incompatible. What should the technician do to get the researcher back to work quickly?",
        "options": {
            "A": "Rollback the drivers to the previous version",
            "B": "Reset the equipment configuration from a backup",
            "C": "Restore the PC to the last known good configuration",
            "D": "Downgrade the PC to a working patch level"
        },
        "answer": "A",
        "explanation": "Since the vendor identified the new driver as the issue, rolling back to the previous (working) driver version is the fastest way to restore functionality.",
        "objective": "Windows drivers & updates"
    },
    {
        "question": "A user connects an Android phone to an airport Wi-Fi network named FreeAirportWiFi. A question-mark appears next to the Wi-Fi icon and web pages won’t load, though phone calls work. What is the MOST likely issue?",
        "options": {
            "A": "The smartphone can only support 3G data networks",
            "B": "The smartphone is connected to the Wi-Fi but is not authenticated yet",
            "C": "The smartphone's SIM card is deactivated",
            "D": "The smartphone does not have a valid data plan enabled"
        },
        "answer": "B",
        "explanation": "The question-mark typically indicates no internet access because a captive portal (authentication/acceptance page) hasn’t been completed even though the device is associated to the Wi-Fi.",
        "objective": "Mobile device connectivity"
    },
    {
        "question": "While troubleshooting a newly installed NIC, you want to ping the NIC’s loopback address. Which IPv4 address should you ping?",
        "options": {
            "A": "172.16.1.1",
            "B": "127.0.0.1",
            "C": "10.0.0.1",
            "D": "192.168.1.1"
        },
        "answer": "B",
        "explanation": "127.0.0.1 is the IPv4 loopback address used to test the local TCP/IP stack.",
        "objective": "Networking fundamentals"
    },
    {
        "question": "Why should System Restore be disabled before removing malware from a Windows Home system?",
        "options": {
            "A": "Turning off System Restore speeds up system performance during scans.",
            "B": "Disabling System Restore removes all installed applications and user data.",
            "C": "System Restore must be off to allow antivirus software to detect threats.",
            "D": "Malware can hide in restore points and reinfect the system after removal."
        },
        "answer": "D",
        "explanation": "Malicious files can be stored in restore points. If System Restore remains enabled, the system could restore infected files and reinfect the machine.",
        "objective": "Malware remediation"
    },
    {
        "question": "You must deploy a policy to block USB storage on all corporate workstations using the command line. Which command applies Group Policy changes?",
        "options": {
            "A": "gpresult",
            "B": "gpupdate",
            "C": "sfc",
            "D": "diskpart"
        },
        "answer": "B",
        "explanation": "gpupdate refreshes and applies Group Policy settings on a system. gpresult only reports resultant set of policy; sfc and diskpart are unrelated.",
        "objective": "3.2 Windows administration commands"
    },
    {
        "question": "An IT administrator needs to upgrade several computers running an operating system at End-of-Life (EOL). What should be the FIRST step?",
        "options": {
            "A": "Migrate all data to the cloud",
            "B": "Back up critical files and settings",
            "C": "Uninstall unnecessary software",
            "D": "Disable security features to speed up the process"
        },
        "answer": "B",
        "explanation": "Always create a verified backup of critical data and settings before performing OS upgrades.",
        "objective": "3.4 OS installation and upgrade planning"
    },
    {
        "question": "You’re configuring a neighbor’s SOHO network so friends can access their Minecraft server over the Internet. Where should you place the server?",
        "options": {
            "A": "Perimeter network (DMZ)",
            "B": "MAN",
            "C": "WAN",
            "D": "LAN"
        },
        "answer": "A",
        "explanation": "Public-facing services should be placed in a perimeter network (DMZ) to isolate them from the internal LAN.",
        "objective": "1.7 Network architecture concepts"
    },
    {
        "question": "When using an MBR disk, which partition type is limited to at most four per disk?",
        "options": {
            "A": "Swap",
            "B": "Primary",
            "C": "Logical",
            "D": "Extended"
        },
        "answer": "B",
        "explanation": "MBR supports up to four primary partitions (or three primary plus one extended that holds multiple logical partitions).",
        "objective": "3.3 Disk partitions and formats"
    },
    {
        "question": "Which statement accurately describes the degaussing process for securely destroying data on storage devices?",
        "options": {
            "A": "A method that applies strong magnetic fields to erase drive data",
            "B": "Software procedures that repeatedly overwrite sensitive data",
            "C": "A chemical technique that dissolves the platters inside the drive",
            "D": "A mechanical process that slices hard drives into small pieces"
        },
        "answer": "A",
        "explanation": "Degaussing uses a powerful magnetic field to disrupt magnetic domains on media, erasing data. The other answers describe different destruction/sanitization methods.",
        "objective": "4.5 Data destruction and disposal"
    },
    {
        "question": "After using a café’s Wi-Fi, your laptop later boots to a full-screen lock with a demand for 0.1 BTC to regain access to personal files. What type of malware is this?",
        "options": {
            "A": "Ransomware",
            "B": "Rootkit",
            "C": "Spyware",
            "D": "Trojan"
        },
        "answer": "A",
        "explanation": "A lock screen with a ransom demand is characteristic of ransomware, which encrypts or locks access to data until payment is made.",
        "objective": "4.3 Malware types and symptoms"
    },
    {
        "question": "Which technology should you use to securely access the command-line interface of network switches and routers remotely for configuration?",
        "options": {
            "A": "SSH",
            "B": "HTTPS",
            "C": "Telnet",
            "D": "RDP"
        },
        "answer": "A",
        "explanation": "Secure Shell (SSH) provides encrypted remote terminal access to network devices. Telnet is insecure, HTTPS is for web-based GUIs, and RDP is a Windows desktop protocol.",
        "objective": "2.4 Remote access and management"
    },
    {
        "question": "An employee moved from Human Resources to Sales. To ensure the user no longer has access to HR share drives, what should you check?",
        "options": {
            "A": "Credential Manager",
            "B": "Home Folder",
            "C": "Group Policy",
            "D": "Security Groups"
        },
        "answer": "D",
        "explanation": "Access to file shares is typically granted through group memberships. Removing the user from the HR security group will revoke permissions to the HR shares.",
        "objective": "3.5 User and group permissions"
    },
    {
        "question": "You are setting up a check-in kiosk at a doctor's office that must auto-logon and run only a single application. Which account type is most appropriate?",
        "options": {
            "A": "Power User",
            "B": "Guest",
            "C": "Remote Desktop User",
            "D": "Administrator"
        },
        "answer": "B",
        "explanation": "Kiosks should run with the least privilege possible. A Guest (or other standard/kiosk) account with assigned access provides minimal rights and can be set to auto-logon.",
        "objective": "3.6 Account types and least privilege"
    },
    {
        "question": "A user gets an error when trying to open a 4-GB .dmg file on a Windows 10 workstation. What should you tell the user?",
        "options": {
            "A": "You must be an administrator to open that file.",
            "B": "You need to use macOS to open DMG files.",
            "C": "Your hard drive doesn't have enough free space.",
            "D": "Your workstation needs 16 GB of RAM to open the file."
        },
        "answer": "B",
        "explanation": ".dmg is a macOS disk-image format that Windows does not natively open. Use macOS or third-party tools.",
        "objective": "1.9 File types and OS compatibility"
    },
    {
        "question": "Your Wi-Fi network is running slowly and you discover a neighbor's laptop connected even though you never shared the password. What action will prevent connections without the proper WPA password?",
        "options": {
            "A": "Disable SSID broadcast",
            "B": "Enable WEP",
            "C": "Disable WPS",
            "D": "Disable WPA3"
        },
        "answer": "C",
        "explanation": "Wi-Fi Protected Setup (WPS) can be abused (PIN brute force) to join a network without knowing the passphrase. Disabling WPS prevents this vector.",
        "objective": "2.2 Wireless security"
    },
    {
        "question": "Which Windows 10 power state saves power but takes longer to resume where the user left off?",
        "options": {
            "A": "Sleep",
            "B": "Power saver",
            "C": "Hibernate",
            "D": "Balanced"
        },
        "answer": "C",
        "explanation": "Hibernate writes RAM contents to disk and powers down, saving more power than Sleep but resuming more slowly.",
        "objective": "3.2 Power settings and management"
    },
    {
        "question": "You are troubleshooting a workstation and want to check if any S.M.A.R.T. errors are being reported. Which Windows tool should you open?",
        "options": {
            "A": "DxDiag",
            "B": "Performance Monitor",
            "C": "Disk Management",
            "D": "Task Scheduler"
        },
        "answer": "C",
        "explanation": "S.M.A.R.T. status for storage devices is surfaced to Windows through the storage stack and can be viewed from Disk Management, which shows drive health/state. DxDiag and Task Scheduler are unrelated, and Performance Monitor does not directly report S.M.A.R.T. health.",
        "objective": "Operating systems — Windows tools and utilities"
    },
    {
        "question": "Dion Training uses DHCP to assign private Class A addresses to Windows 10 workstations. Which of the following is a Class A private IP address?",
        "options": {
            "A": "192.168.3.5",
            "B": "10.1.2.3",
            "C": "169.254.1.52",
            "D": "172.18.21.252"
        },
        "answer": "B",
        "explanation": "Private Class A addresses are in the 10.0.0.0/8 range. 192.168.0.0/16 is Class C private, 172.16.0.0–172.31.255.255 is Class B private, and 169.254.0.0/16 is APIPA/link-local.",
        "objective": "Networking fundamentals — IP addressing"
    },
    {
        "question": "After deploying an AI-driven documentation tool, techs report the instructions sometimes include wrong commands or outdated procedures, causing failed fixes. What BEST describes this issue?",
        "options": {
            "A": "Inaccuracies",
            "B": "Hallucination",
            "C": "Bias",
            "D": "Misconfiguration"
        },
        "answer": "B",
        "explanation": "In the AI context, a “hallucination” is when a model produces plausible-sounding but incorrect information (e.g., non-existent commands). That is the specific problem described.",
        "objective": "Operational procedures — documentation/AI limitations"
    },
    {
        "question": "A user is trying to copy a 5-GB video to a USB flash drive formatted with FAT32, but the copy fails. What is the BEST fix?",
        "options": {
            "A": "Convert the file system to exFAT without reformatting",
            "B": "Enable compression on the file before transferring",
            "C": "Split the file into multiple smaller files",
            "D": "Format the USB drive to NTFS"
        },
        "answer": "D",
        "explanation": "FAT32 has a maximum single-file size of 4 GB. Reformatting to a file system that supports larger files (NTFS or exFAT) resolves the problem; NTFS is a clear built-in option.",
        "objective": "Operating systems — File systems (FAT32 vs. NTFS)"
    },
    {
        "question": "A Windows 10 PC is very slow after logon. Task Manager shows >99% disk usage driven by the process 'Antimalware Service Executable'. What action is BEST?",
        "options": {
            "A": "Update Windows Defender definitions and restart",
            "B": "Perform a full malware scan and schedule it for off-hours",
            "C": "Restart in Safe Mode and disable startup programs",
            "D": "Permanently disable the anti-malware real-time protection"
        },
        "answer": "B",
        "explanation": "High disk use from the Defender service usually indicates a scan. Running a full scan and scheduling scans for off-hours addresses performance impact without sacrificing protection. Disabling protection is not recommended.",
        "objective": "Software troubleshooting — malware symptoms and remediation"
    },
    {
        "question": "A customer’s Android phone became very slow soon after installing a new stock-tracking app. What should you do FIRST to troubleshoot?",
        "options": {
            "A": "Perform a hard reboot of the smartphone",
            "B": "Factory reset the smartphone and reinstall all apps",
            "C": "Uninstall the app, reboot the phone, and reinstall the app",
            "D": "Replace the phone with a newer model"
        },
        "answer": "C",
        "explanation": "When performance issues begin right after installing an app, first remove the suspected app and reboot. If the user still needs it, reinstalling lets you confirm whether it was the cause before resorting to more drastic steps.",
        "objective": "Mobile device troubleshooting — app and performance issues"
    },
    {
        "question": "You are assisting the security team during incident response. Which Windows command-line tool shows the list of TCP connections currently established on the workstation?",
        "options": {
            "A": "tracert",
            "B": "arp",
            "C": "route",
            "D": "netstat"
        },
        "answer": "D",
        "explanation": "netstat displays active TCP/UDP connections and listening ports (e.g., netstat -an). tracert, arp, and route do not show current socket connections.",
        "objective": "2.3 Windows command-line tools and networking"
    },
    {
        "question": "Which command would a Linux user run to change their own password?",
        "options": {
            "A": "passwd",
            "B": "ps",
            "C": "chown",
            "D": "pwd"
        },
        "answer": "A",
        "explanation": "passwd updates a user’s account password. ps lists processes, chown changes ownership, and pwd prints the working directory.",
        "objective": "1.9 Linux basics"
    },
    {
        "question": "After deploying an updated audio driver to all workstations, multiple users report their website usernames and passwords were stolen. What malicious component was MOST likely bundled in the driver package?",
        "options": {
            "A": "Ransomware",
            "B": "Worm",
            "C": "Keylogger",
            "D": "Virus"
        },
        "answer": "C",
        "explanation": "A keylogger captures keystrokes and can exfiltrate credentials. The symptoms (stolen logins) align directly with keylogging activity.",
        "objective": "3.3 Malware types and symptoms"
    },
    {
        "question": "A Windows 10 laptop already using Windows Defender has another antivirus with real-time protection installed. The system is now sluggish and intermittently unresponsive. What should you do FIRST to resolve the problem?",
        "options": {
            "A": "Install and run Spybot Search & Destroy",
            "B": "Enable real-time protection in Windows Defender",
            "C": "Uninstall the real-time protection antivirus",
            "D": "Run Windows Update utility"
        },
        "answer": "C",
        "explanation": "Running two real-time AV engines commonly causes heavy contention and performance issues. Remove the additional real-time product (or disable one) before further troubleshooting.",
        "objective": "2.4 Troubleshooting Windows performance and security software"
    },
    {
        "question": "Your public website allows user posts. Users now see pop-ups requesting credentials, and the security team notes a spike in compromised accounts. What attack is MOST likely?",
        "options": {
            "A": "SQL injection",
            "B": "Rootkit",
            "C": "Cross-site scripting (XSS)",
            "D": "Cross-site request forgery (CSRF)"
        },
        "answer": "C",
        "explanation": "XSS allows attackers to inject scripts into web pages viewed by other users, often producing credential-stealing pop-ups and account compromise.",
        "objective": "3.5 Secure web applications and threats"
    },
    {
        "question": "Which backup type reconstructs the recovered data by combining a previous full backup with one or more later partial backups without rereading the source data?",
        "options": {
            "A": "Full",
            "B": "Differential",
            "C": "Synthetic",
            "D": "Incremental"
        },
        "answer": "C",
        "explanation": "A synthetic full backup is built by merging an earlier full with subsequent incrementals/differentials to create a new full image without pulling all data from the original source.",
        "objective": "4.2 Backup strategies and restoration"
    },
    {
        "question": "You are configuring a SOHO network and want only specific IP addresses to access the network while blocking any addresses that are not on the list. Which should be implemented?",
        "options": {
            "A": "Blocklist",
            "B": "Port forwarding",
            "C": "Allow list",
            "D": "MAC filtering"
        },
        "answer": "C",
        "explanation": "An allow list (whitelist) explicitly specifies which IP addresses are permitted. All other IPs are denied by default. A blocklist allows everything except listed entries, MAC filtering works at Layer 2 and is easy to spoof, and port forwarding is unrelated.",
        "objective": "Network security controls (firewall/ACLs)"
    },
    {
        "question": "Which of the following remote access protocols should you use to connect to a Linux server securely over the internet?",
        "options": {
            "A": "FTP",
            "B": "Telnet",
            "C": "SSH",
            "D": "RDP"
        },
        "answer": "C",
        "explanation": "SSH provides encrypted remote shell access (port 22) and is the standard secure method to administer Linux over untrusted networks. Telnet and FTP are unencrypted; RDP is primarily for Windows GUIs.",
        "objective": "Remote access protocols and secure administration"
    },
    {
        "question": "Dion Training wants to implement a new wireless network using WPA3. Which feature of WPA3 provides password-based authentication using the dragonfly handshake instead of the older WPA 4-way handshake?",
        "options": {
            "A": "Management protection frames",
            "B": "SAE",
            "C": "AES GCMP",
            "D": "Enhanced open"
        },
        "answer": "B",
        "explanation": "WPA3 uses SAE (Simultaneous Authentication of Equals) with the dragonfly key exchange for password-based authentication, resisting offline dictionary attacks. Management frame protection and Enhanced Open are other WPA3 features, while AES-GCMP is an encryption algorithm.",
        "objective": "Wireless security (WPA3 features)"
    },
    {
        "question": "A network administrator receives a call asking for help connecting to the network. The caller requests the IP address, subnet mask, and VLAN required to gain access. What type of attack is this most likely?",
        "options": {
            "A": "Spoofing",
            "B": "Social engineering",
            "C": "Zero-day attack",
            "D": "VLAN hopping"
        },
        "answer": "B",
        "explanation": "The caller is attempting to obtain sensitive configuration details by manipulating a person rather than exploiting technology—classic social engineering. Spoofing forges identities, zero-days exploit unknown flaws, and VLAN hopping abuses switching configurations.",
        "objective": "Threats and vulnerabilities (social engineering)"
    },
    {
        "question": "A user reports the browser keeps redirecting to unfamiliar sites and the homepage changed without permission. What is the BEST first step in diagnosing the issue?",
        "options": {
            "A": "Disable the network connection",
            "B": "Restart the computer to reset all browser settings automatically",
            "C": "Replace the browser with a different one",
            "D": "Check for unwanted browser extensions or settings changes"
        },
        "answer": "D",
        "explanation": "Unwanted extensions or altered settings commonly cause redirects; inspect and remove them first.",
        "objective": "Browser troubleshooting"
    },
    {
        "question": "After installing a new photo-sharing app, you hear the shutter sound when taking a picture but no new photos appear. What should you do first?",
        "options": {
            "A": "Uninstall and reinstall the app",
            "B": "Verify the app has the correct permissions",
            "C": "Perform a firmware update",
            "D": "Update all the smartphone’s apps"
        },
        "answer": "B",
        "explanation": "The app likely lacks Camera/Photos (storage) permissions, preventing saving images.",
        "objective": "Mobile OS/app permissions"
    },
    {
        "question": "As a file server administrator, you find inappropriate media files on a corporate share clearly violating the company's AUP. What should you do FIRST?",
        "options": {
            "A": "Copy the files to an external hard drive",
            "B": "Contact the user and ask them to remove the files",
            "C": "Notify your immediate supervisor",
            "D": "Delete the files immediately"
        },
        "answer": "C",
        "explanation": "Follow policy and escalate to management/HR. Preserve evidence and avoid deleting or confronting the user directly without direction.",
        "objective": "Policies & incident response"
    },
    {
        "question": "A school district’s iPads are running an iPadOS version that has reached End-of-Life (EOL). What is the MOST significant risk of continuing to use them?",
        "options": {
            "A": "Reduced touchscreen responsiveness",
            "B": "Inability to install new apps from the App Store",
            "C": "Decreased battery life over time",
            "D": "Increased vulnerability to security threats"
        },
        "answer": "D",
        "explanation": "EOL devices no longer receive security patches, making them more vulnerable to exploits and malware.",
        "objective": "Mobile device lifecycle & risk"
    },
    {
        "question": "Which remote access technology should NOT be used in a network due to its lack of security?",
        "options": {
            "A": "SSH",
            "B": "Telnet",
            "C": "VPN",
            "D": "RDP"
        },
        "answer": "B",
        "explanation": "Telnet transmits data in plaintext and should not be used on modern networks; SSH is the secure alternative.",
        "objective": "2.4 Secure protocols"
    },
    {
        "question": "A corporate workstation was infected with malware, which then began spreading using stolen credentials. IT wants to prevent a recurrence. Which option would BEST prevent this from reoccurring across the organization?",
        "options": {
            "A": "Install an anti-virus/anti-malware solution that uses heuristic analysis",
            "B": "Monitor login failures and forward to a centralized SYSLOG server",
            "C": "Install a host-based intrusion detection system (HIDS) on all corporate workstations",
            "D": "Install a UTM system on the network to monitor for suspicious traffic"
        },
        "answer": "C",
        "explanation": "A host-based IDS on all endpoints looks for suspicious behavior and credential-stealing activity at the source, providing broad endpoint coverage to stop lateral movement.",
        "objective": "4.4 Endpoint protection and hardening"
    },
    {
        "question": "Which setting should be configured on a macOS system to enable the Smart Zoom feature on a user's MacBook trackpad?",
        "options": {
            "A": "Movements",
            "B": "Motions",
            "C": "Gestures",
            "D": "Signals"
        },
        "answer": "C",
        "explanation": "Smart Zoom is a trackpad gesture setting in macOS (Trackpad → Point & Click/Scroll & Zoom).",
        "objective": "1.9 macOS basics and features"
    },
    {
        "question": "Which Windows command-line tool displays the resulting set of policy settings enforced on a computer for a specified user when they logged on?",
        "options": {
            "A": "dism",
            "B": "gpupdate",
            "C": "gpresult",
            "D": "sfc"
        },
        "answer": "C",
        "explanation": "gpresult shows the Resultant Set of Policy (RSoP) for a user/computer, detailing GPOs that applied.",
        "objective": "3.3 Windows tools"
    },
    {
        "question": "Which option allows users to save the current session to disk and then power down their Windows 10 laptop so they can resume exactly where they left off?",
        "options": {
            "A": "Lock",
            "B": "Shutdown",
            "C": "Sleep",
            "D": "Hibernate"
        },
        "answer": "D",
        "explanation": "Hibernate writes RAM contents to disk and powers off, allowing the session to resume later without power drain.",
        "objective": "3.1 Windows OS features and power options"
    },
    {
        "question": "A workstation takes a long time to boot. After it finally reaches the Windows 10 desktop, which tool can a technician use to diagnose and fix startup issues?",
        "options": {
            "A": "msconfig.exe",
            "B": "resmon.exe",
            "C": "perfmon.msc",
            "D": "msinfo32.exe"
        },
        "answer": "A",
        "explanation": "MSConfig is used to manage startup items, services, and boot options to troubleshoot slow startup problems.",
        "objective": "3.3 Windows tools and startup troubleshooting"
    },
    {
        "question": "You want to ensure that only one person can enter or leave the server room at a time. Which of the following physical security devices would BEST help you meet this requirement?",
        "options": {
            "A": "Thumbprint reader",
            "B": "Cipher lock",
            "C": "Video monitoring",
            "D": "Access control vestibule"
        },
        "answer": "D",
        "explanation": "An access control vestibule (mantrap) enforces single-person entry/exit by using two interlocked doors, ensuring only one person passes at a time. Biometrics, cipher locks, and cameras help with identification and logging but do not physically restrict entry to a single person.",
        "objective": "3.5 Physical security controls"
    },
    {
        "question": "David is a new help desk technician. He needs to install programs and printers but should not have full access to change everything on a Windows workstation. Which type of user account should David be given?",
        "options": {
            "A": "Administrator",
            "B": "Power User",
            "C": "Guest",
            "D": "Remote Desktop User"
        },
        "answer": "B",
        "explanation": "A Power User (or a standard user with appropriate elevated permissions) can install common peripherals and some software without full administrative control. Administrator is excessive, Guest is too limited, and Remote Desktop User only grants RDP rights, not local install rights.",
        "objective": "3.1 Windows accounts and permissions"
    },
    {
        "question": "Which of the following types of remote access technologies should NOT be used in a network due to its lack of security?",
        "options": {
            "A": "SSH",
            "B": "Telnet",
            "C": "VPN",
            "D": "RDP"
        },
        "answer": "B",
        "explanation": "Telnet sends data in cleartext and provides no encryption, making it insecure on modern networks. SSH and VPN provide encrypted sessions; RDP can be secured with modern settings.",
        "objective": "1.9 Secure protocols"
    },
    {
        "question": "A corporate workstation was infected with malware that accessed the credential store, stole usernames and passwords, and then infected other workstations using those credentials. Which of the following would BEST prevent this from reoccurring?",
        "options": {
            "A": "Install an anti-virus or anti-malware solution that uses heuristic analysis",
            "B": "Monitor all workstations for failed login attempts and forward them to a centralized SYSLOG server",
            "C": "Install a host-based intrusion detection system on all of the corporate workstations",
            "D": "Install a Unified Threat Management system on the network to monitor for suspicious traffic"
        },
        "answer": "A",
        "explanation": "Heuristic/behavior-based anti-malware is designed to stop new and unknown threats, including credential-stealing malware, before they execute successfully. HIDS and UTM help with detection and alerting, and log monitoring is useful for investigation, but none of those alone prevents the malware from executing like a modern behavior-based endpoint solution can.",
        "objective": "2.4 Malware prevention and remediation"
    },
    {
        "question": "Which of the following should you use to configure a network adapter's duplex setting manually in Windows 10?",
        "options": {
            "A": "Device Manager",
            "B": "Internet Options",
            "C": "System",
            "D": "Windows Defender Firewall"
        },
        "answer": "A",
        "explanation": "Duplex and speed settings are configured on the NIC via Device Manager.",
        "objective": "3.5 Windows troubleshooting"
    },
    {
        "question": "A user is complaining about slow data speeds when they are at home in a large apartment building. The user uses Wi-Fi when they get home, and the device works fine on other wireless networks. Which action should the user take to increase their data speeds?",
        "options": {
            "A": "Upgrade to a new smartphone",
            "B": "Turn off Wi-Fi and rely on cellular data",
            "C": "Increase the Wi-Fi signal being transmitted by their WAP",
            "D": "Enable MAC filtering on their WAP"
        },
        "answer": "C",
        "explanation": "In a congested environment, stronger signal output can help overcome interference. (Changing channels would also help, but it isn’t offered.)",
        "objective": "2.4 Wireless networking"
    },
    {
        "question": "During a telework rollout, the CIO allows employees to use their personal laptops and smartphones when conducting work at home. Which TWO policies/technologies should be implemented to provide security guidance on the use of these devices?",
        "options": {
            "A": "DRM",
            "B": "ACL",
            "C": "BYOD",
            "D": "EULA",
            "E": "MDM",
            "F": "COPE"
        },
        "answer": "CE",
        "explanation": "A BYOD policy defines acceptable use for personal devices, and MDM enforces controls such as encryption and remote wipe.",
        "objective": "5.3 Policies and best practices"
    },
    {
        "question": "A computer was infected with malware. Without any user intervention, the malware is now spreading throughout the corporate network and infecting other computers. Which type of malware MOST likely infected these computers?",
        "options": {
            "A": "Ransomware",
            "B": "Trojan",
            "C": "Worm",
            "D": "Virus"
        },
        "answer": "C",
        "explanation": "Worms can self-propagate across networks without user action.",
        "objective": "5.1 Malware types"
    },
    {
        "question": "One of your Windows services is failing to start when you boot up your laptop. You verified in the Services tool that it is set to Automatic. What should you attempt NEXT to get the service to startup?",
        "options": {
            "A": "Update the operating system",
            "B": "Run chkdsk on the system",
            "C": "Restore from backup",
            "D": "Reboot into Safe Mode and see if the service starts"
        },
        "answer": "D",
        "explanation": "Safe Mode loads minimal drivers/services and helps isolate conflicts preventing startup.",
        "objective": "3.5 Windows troubleshooting"
    },
    {
        "question": "A customer is deciding between integrated graphics and a dedicated graphics card for video editing and 3D rendering. What is the BEST reason to choose the dedicated option?",
        "options": {
            "A": "Optimized for general computing tasks",
            "B": "Consumes less power, longer on battery",
            "C": "Has its own memory, reducing strain on system RAM when rendering",
            "D": "Built into the processor, more efficient for creative apps"
        },
        "answer": "C",
        "explanation": "Dedicated GPUs use VRAM and provide significantly better performance for rendering workloads.",
        "objective": "1.2 PC hardware"
    },
    {
        "question": "Which of the following is the BEST way to regularly prevent different security threats from occurring within your network?",
        "options": {
            "A": "Disaster recovery planning",
            "B": "User training and awareness",
            "C": "Penetration testing",
            "D": "Business continuity training"
        },
        "answer": "B",
        "explanation": "User awareness reduces phishing, social engineering, and unsafe behavior—major threat vectors.",
        "objective": "5.3 Security awareness and training"
    },
    {
        "question": "A programmer is writing a script to display all the numbers from 1 to 100 to the screen. Which of the following should they use in their script?",
        "options": {
            "A": "Comment",
            "B": "Loop",
            "C": "Branch",
            "D": "Constant"
        },
        "answer": "B",
        "explanation": "A loop iterates through a numeric range to print values.",
        "objective": "1.8 Scripting basics"
    },
    {
        "question": "Which Linux command is used on a Linux system to delete a file from a directory?",
        "options": {
            "A": "cp",
            "B": "mv",
            "C": "rm",
            "D": "kill"
        },
        "answer": "C",
        "explanation": "The rm command removes files; rm -r removes directories recursively.",
        "objective": "1.9 Linux basics"
    },
    {
        "question": "Which tool should you utilize to ensure you don't damage a laptop's SSD while replacing it?",
        "options": {
            "A": "Air filter mask",
            "B": "ESD strap",
            "C": "Latex gloves",
            "D": "Antistatic bag"
        },
        "answer": "B",
        "explanation": "Use an ESD strap to prevent electrostatic discharge when servicing components.",
        "objective": "1.5 Safety procedures"
    },
    {
        "question": "You are troubleshooting a user's computer and want to create a new login with administrative privileges. Which Windows utility should you use?",
        "options": {
            "A": "Local Users and Groups",
            "B": "System Information",
            "C": "Group Policy",
            "D": "System Configuration"
        },
        "answer": "A",
        "explanation": "Local Users and Groups (lusrmgr.msc) is used to create users and assign group membership.",
        "objective": "3.2 Windows tools"
    },
    {
        "question": "The network administrator noticed the border router has high network capacity loading during non-working hours, causing outages for the company's web servers. What is the MOST likely cause?",
        "options": {
            "A": "Distributed DoS",
            "B": "Session hijacking",
            "C": "ARP spoofing",
            "D": "Evil twin"
        },
        "answer": "A",
        "explanation": "Sustained high load off-hours suggests a volumetric DDoS attack against public-facing services.",
        "objective": "2.7 Threats and attacks"
    },
    {
        "question": "Which Windows 10 option creates a small hibernation file before shutdown to reduce boot time when powered on?",
        "options": {
            "A": "USB selective suspend",
            "B": "Lock mode",
            "C": "Sleep mode",
            "D": "Fast startup"
        },
        "answer": "D",
        "explanation": "Fast startup uses a partial hibernation image to start faster.",
        "objective": "3.1 Windows features"
    },
    {
        "question": "During reconnaissance for a penetration test, employees use Android smartphones that connect back via a secure VPN. Which method would MOST likely be the best for exploiting them?",
        "options": {
            "A": "Use web-based exploits against the device's web interfaces",
            "B": "Use social engineering to trick a user into opening a malicious APK",
            "C": "Identify a jailbroken device for easy exploitation",
            "D": "Use a tool like ICS SPlOIT to target specific vulnerabilities"
        },
        "answer": "B",
        "explanation": "Convincing users to sideload a malicious APK is a common and effective social engineering path.",
        "objective": "5.2 Social engineering"
    },
    {
        "question": "Your company is expanding into the EU. Which regulation applies when processing personal data within the EU?",
        "options": {
            "A": "PCI",
            "B": "GDPR",
            "C": "PII",
            "D": "PHI"
        },
        "answer": "B",
        "explanation": "GDPR governs the protection and processing of personal data for EU residents.",
        "objective": "5.3 Compliance and policies"
    },
    {
        "question": "After upgrading a laptop from Windows 10 to Windows 11, several legacy apps crash. What is the BEST solution to keep the legacy programs working?",
        "options": {
            "A": "Run Disk Cleanup and clear temporary files",
            "B": "Reinstall Windows 10",
            "C": "Enable compatibility mode for the problematic applications",
            "D": "Increase the laptop’s RAM"
        },
        "answer": "C",
        "explanation": "Compatibility mode shims help older apps run on newer Windows versions.",
        "objective": "3.5 Windows troubleshooting"
    },
    {
        "question": "Jason has an old 2017 Dell laptop running Windows 7 with a cracked screen. What do you recommend?",
        "options": {
            "A": "Replace the display and contact the manufacturer for reimbursement",
            "B": "Replace the display and charge him for parts/installation",
            "C": "Purchase a new laptop",
            "D": "Sell him an external 15\" monitor/tablet to connect as a workaround"
        },
        "answer": "D",
        "explanation": "For an old Windows 7 machine, an external monitor is a low-cost workaround versus repairing an aged device.",
        "objective": "1.2 Hardware/OS support decisions"
    },
    {
        "question": "After installing a new workstation in a workgroup, the user needs to see other workstations. Which setting should you ensure is enabled?",
        "options": {
            "A": "Enable an RDP connection",
            "B": "Enable network discovery",
            "C": "Enable file and folder sharing",
            "D": "Enable BitLocker"
        },
        "answer": "B",
        "explanation": "Network discovery lets the system find and be found by other devices on the LAN.",
        "objective": "2.2 SOHO/workgroup configuration"
    },
    {
        "question": "Which Control Panel option should a technician use to change a user's role from standard to administrator?",
        "options": {
            "A": "Administrative Tools",
            "B": "Network and Sharing Center",
            "C": "System",
            "D": "User Accounts"
        },
        "answer": "D",
        "explanation": "User Accounts manages local account types and privileges.",
        "objective": "3.2 Windows tools"
    },
    {
        "question": "Which type of software CANNOT be updated via the Windows Update program?",
        "options": {
            "A": "Firmware updates",
            "B": "Critical fixes",
            "C": "Driver updates",
            "D": "Security patches"
        },
        "answer": "A",
        "explanation": "Windows Update delivers OS patches and drivers; firmware updates are vendor-specific (some OEMs integrate but generally separate).",
        "objective": "3.1 Windows servicing"
    },
    {
        "question": "A hospital file server’s files are encrypted, and an attacker demands payment for the decryption key. Which malware is this?",
        "options": {
            "A": "Keylogger",
            "B": "Spyware",
            "C": "Rootkit",
            "D": "Ransomware"
        },
        "answer": "D",
        "explanation": "Ransomware encrypts data and extorts payment for decryption.",
        "objective": "5.1 Malware types"
    },
    {
        "question": "Which device should you NEVER disassemble during troubleshooting due to risk of electrocution?",
        "options": {
            "A": "External hard drive enclosure",
            "B": "CRT display",
            "C": "Tablet",
            "D": "Printer"
        },
        "answer": "B",
        "explanation": "CRT displays hold dangerous voltages even when unplugged.",
        "objective": "1.5 Safety procedures"
    },
    {
        "question": "A company issues tablets used in public areas. Which biometric screen lock is most practical and secure for regular employee use?",
        "options": {
            "A": "Voice recognition",
            "B": "Facial recognition",
            "C": "Swipe pattern",
            "D": "Retina scanning"
        },
        "answer": "B",
        "explanation": "Facial recognition balances usability and security; retina scans are impractical for routine use.",
        "objective": "5.4 Mobile device security"
    },
    {
        "question": "An employee’s browser is slow and freezes after installing a plug-in from an unknown source. What should IT advise to promptly resolve the issue?",
        "options": {
            "A": "Enable built-in pop-up blocking",
            "B": "Disable or remove the recently installed plug-in",
            "C": "Clear the browser cache",
            "D": "Update the browser to the latest version"
        },
        "answer": "B",
        "explanation": "Removing the suspicious plug-in directly addresses the likely cause.",
        "objective": "3.5 Browser troubleshooting"
    },
    {
        "question": "Which command is used on Linux to copy a file from one directory to another?",
        "options": {
            "A": "cp",
            "B": "mv",
            "C": "rm",
            "D": "ls"
        },
        "answer": "A",
        "explanation": "cp copies files and directories.",
        "objective": "1.9 Linux basics"
    },
    {
        "question": "Which Windows command-line tool displays the files and directories within the current path?",
        "options": {
            "A": "sfc",
            "B": "ls",
            "C": "chkdsk",
            "D": "dir"
        },
        "answer": "D",
        "explanation": "dir lists contents in Windows shells; ls is used on Unix/Linux.",
        "objective": "3.2 Windows tools"
    },
    {
        "question": "A user wants to know how much RAM to install for a game (8 GB minimum, 16 GB recommended). They only run one game at a time. What's the BEST recommendation?",
        "options": {
            "A": "Install far beyond the recommended amount",
            "B": "Install the minimum required amount",
            "C": "Upgrade to the recommended amount",
            "D": "Reduce RAM below the minimum requirement"
        },
        "answer": "C",
        "explanation": "Recommended specs offer headroom and better experience; minimum may cause stutters.",
        "objective": "1.2 PC hardware"
    },
    {
        "question": "Which description correctly identifies a primary characteristic of a PIN-based screen lock?",
        "options": {
            "A": "Uses a fingerprint sensor",
            "B": "Uses a numeric code entered on a keypad",
            "C": "Requires drawing a shape or pattern",
            "D": "Relies on facial features captured by a camera"
        },
        "answer": "B",
        "explanation": "PINs are numeric codes used for access.",
        "objective": "5.4 Authentication methods"
    },
    {
        "question": "After a security patch via MECM, users report their screen fills with static when moving the mouse. What should you do to resolve the issue?",
        "options": {
            "A": "Rollback the video card driver and wait for a new driver",
            "B": "Reboot to Safe Mode and allow the user to continue work",
            "C": "Use SFC to repair system files",
            "D": "Disable the DirectX service in services.msc"
        },
        "answer": "A",
        "explanation": "Symptoms suggest a faulty graphics driver after the update—rollback the driver.",
        "objective": "3.5 Driver troubleshooting"
    },
    {
        "question": "How should an instructor accurately describe a valid security certificate?",
        "options": {
            "A": "A digital document confirming the website’s identity and secure connection",
            "B": "A software update for browser security",
            "C": "A privacy setting preventing websites from tracking",
            "D": "A plug-in ensuring faster website loading"
        },
        "answer": "A",
        "explanation": "Certificates bind identities to public keys and enable trusted TLS connections.",
        "objective": "2.6 PKI/TLS fundamentals"
    },
    {
        "question": "Which of the following is the MOST secure wireless security and encryption protocol?",
        "options": {
            "A": "WPA3",
            "B": "WEP",
            "C": "WPA2",
            "D": "WPA"
        },
        "answer": "A",
        "explanation": "WPA3 is the current strongest standard; WEP is obsolete.",
        "objective": "2.4 Wireless security"
    },
    {
        "question": "Which of the following is a connectionless protocol that utilizes UDP?",
        "options": {
            "A": "FTP",
            "B": "HTTPS",
            "C": "TFTP",
            "D": "HTTP"
        },
        "answer": "C",
        "explanation": "TFTP uses UDP port 69 and is connectionless.",
        "objective": "2.6 Network services and ports"
    },
    {
        "question": "You submitted an RFC to install a security patch during the weekly maintenance window. Which document describes WHY the change is being installed during this window?",
        "options": {
            "A": "Plan",
            "B": "Scope",
            "C": "Risk analysis",
            "D": "Purpose"
        },
        "answer": "D",
        "explanation": "The Purpose section explains the reason and business justification for a change.",
        "objective": "5.3 Change management"
    },
    {
        "question": "Which of the following is a common sign that a computer may be infected with malware?",
        "options": {
            "A": "Unexpected pop-ups appear even when no browsers are open",
            "B": "OS hides all desktop icons after a reboot",
            "C": "Manual restart required after every update",
            "D": "System prevents installing new apps"
        },
        "answer": "A",
        "explanation": "Unsolicited pop-ups often indicate adware or PUPs.",
        "objective": "5.1 Malware indicators"
    },
    {
        "question": "An organization plans to upgrade its company-wide VPN solution. This is not routine and not an emergency; it requires testing, approvals, and scheduling. How should this change be categorized?",
        "options": {
            "A": "Emergency change",
            "B": "Standard change",
            "C": "Normal change",
            "D": "Unauthorized change"
        },
        "answer": "C",
        "explanation": "Normal changes follow full change management (testing, CAB approval, scheduling).",
        "objective": "5.3 Change management"
    },
    {
        "question": "During a penetration test, which of the following recovered passwords is the WEAKEST and should be changed FIRST?",
        "options": {
            "A": "P@$$w0rd",
            "B": "Pa55w0rd",
            "C": "pa55word",
            "D": "P@$$W0RD"
        },
        "answer": "C",
        "explanation": "Lowercase only and predictable; others include case and/or special characters.",
        "objective": "5.4 Password hygiene"
    },
    {
        "question": "John is setting up 100 Windows 10 computers and wants to ensure no one can change the boot order and boot from an unauthorized OS. What feature should he ensure is enabled?",
        "options": {
            "A": "Secure Boot",
            "B": "BIOS password required",
            "C": "RAM integrity checking",
            "D": "Full disk encryption"
        },
        "answer": "A",
        "explanation": "Secure Boot prevents loading untrusted bootloaders and OSes.",
        "objective": "3.6 Windows security features"
    },
    {
        "question": "A system was infected and redirected browsers to malicious websites. After quarantine and remediation, a few valid sites still redirect. What should you do NEXT?",
        "options": {
            "A": "Verify the hosts file hasn’t been maliciously modified",
            "B": "Install a secondary anti-malware solution",
            "C": "Reformat and reinstall the OS",
            "D": "Perform a System Restore"
        },
        "answer": "A",
        "explanation": "Malware often adds entries to the hosts file to redirect domains.",
        "objective": "3.5 Windows troubleshooting"
    },
    {
        "question": "Which Control Panel section would you use to configure Narrator to read aloud the list of files on screen?",
        "options": {
            "A": "Ease of Access",
            "B": "Indexing Options",
            "C": "File Explorer Options",
            "D": "Sound"
        },
        "answer": "A",
        "explanation": "Narrator is an accessibility feature under Ease of Access.",
        "objective": "3.1 Windows settings"
    },
    {
        "question": "You removed old memory chips from a laptop. Where should you safely store them until reuse?",
        "options": {
            "A": "Ziploc bags",
            "B": "Manila envelopes",
            "C": "Cardboard box",
            "D": "Antistatic bag"
        },
        "answer": "D",
        "explanation": "Use antistatic packaging to prevent ESD damage.",
        "objective": "1.5 Safety procedures"
    },
    {
        "question": "Employees notice a significant slowdown after installing multiple browser extensions. What immediate advice should IT provide?",
        "options": {
            "A": "Adjust browser security to block external scripts",
            "B": "Run frequent antivirus scans",
            "C": "Temporarily disable unnecessary extensions",
            "D": "Regularly clear cookies and history"
        },
        "answer": "C",
        "explanation": "Extensions can heavily impact performance; disable unneeded ones.",
        "objective": "3.5 Browser troubleshooting"
    },
    {
        "question": "Which TWO of the following would provide the BEST security for both computers and smartphones?",
        "options": {
            "A": "Configuring organizational units",
            "B": "Using a cable lock",
            "C": "Utilizing access control lists",
            "D": "Enabling data loss prevention",
            "E": "Enforcing trusted software sources",
            "F": "Enabling multifactor authentication"
        },
        "answer": "EF",
        "explanation": "MFA strengthens authentication, and trusted sources (allowlists/stores) reduce malicious installs across platforms.",
        "objective": "5.4 Authentication & application control"
    },
    {
        "question": "When using an MBR, which type of partitions can only have up to four?",
        "options": {
            "A": "Logical",
            "B": "Primary",
            "C": "Extended",
            "D": "Swap"
        },
        "answer": "B",
        "explanation": "MBR supports up to 4 primary partitions (or 3 primary + 1 extended).",
        "objective": "1.4 Storage concepts"
    },
    {
        "question": "Your mother needs help with her Windows 10 laptop. Which technology would BEST allow you to remotely access and interact with her computer?",
        "options": {
            "A": "VPN",
            "B": "RDP",
            "C": "Telnet",
            "D": "SSH"
        },
        "answer": "B",
        "explanation": "Remote Desktop Protocol allows interactive remote control.",
        "objective": "2.6 Remote access"
    },
    {
        "question": "You're educating new staff about mobile security practices, focusing on encryption methods. Which statement accurately describes the primary purpose of device encryption?",
        "options": {
            "A": "Restricts network access through secure passwords",
            "B": "Protects stored data by making it unreadable without a key",
            "C": "Prevents installation of unauthorized applications",
            "D": "Verifies user identity with biometrics"
        },
        "answer": "B",
        "explanation": "Encryption protects data at rest if the device is lost or stolen.",
        "objective": "5.4 Mobile device security"
    },
    {
        "question": "Sam cannot log in to a web-based SaaS product from his computer, but Mary can on hers. Mary attempts to log in from Sam’s PC and gets an error; she noticed a pop-up about new software on Sam’s computer. Which TWO steps should Mary take?",
        "options": {
            "A": "Have Sam clear his browser cache and try again",
            "B": "Ask Sam for his username/password",
            "C": "Install a new web browser and reboot",
            "D": "Verify Sam’s browser configuration and settings",
            "E": "Ask Sam about the pop-up and what he installed",
            "F": "Have Sam attempt to log on to another website"
        },
        "answer": "DE",
        "explanation": "Confirm browser settings and investigate the recent software change likely causing the issue.",
        "objective": "3.5 Browser/app troubleshooting"
    },
    {
        "question": "Your company replaced all workstations and wants to donate the old computers to a community center. Which type of data destruction/sanitization should you use so the PCs remain usable?",
        "options": {
            "A": "Degaussing",
            "B": "Wiping",
            "C": "Shredding",
            "D": "Purging"
        },
        "answer": "B",
        "explanation": "Wiping (secure erase) removes data while leaving drives usable.",
        "objective": "4.1 Data disposal & sanitization"
    },
    {
        "question": "You installed a flat panel television in a conference room. The facilities manager is concerned about lightning strikes but not outages. What should be installed to BEST mitigate the concern?",
        "options": {
            "A": "UPS",
            "B": "Line conditioner",
            "C": "Surge suppressor",
            "D": "Power strip"
        },
        "answer": "C",
        "explanation": "A surge suppressor protects equipment from voltage spikes (e.g., lightning).",
        "objective": "1.5 Safety/power protection"
    },
    {
        "question": "An ethical hacker dresses like a plumber and follows an employee through the turnstile after they badge in. What attack is this?",
        "options": {
            "A": "Shoulder surfing",
            "B": "Social engineering",
            "C": "Spoofing",
            "D": "Tailgating"
        },
        "answer": "D",
        "explanation": "Tailgating is entering a secure area by closely following an authorized person.",
        "objective": "5.2 Physical/social engineering"
    },
    {
        "question": "When Jonathan opens his browser, the home page is a search engine he doesn't recognize and pop-ups appear. Which TWO actions should be performed FIRST?",
        "options": {
            "A": "Update the browser",
            "B": "Uncheck unapproved apps in Startup",
            "C": "Switch to a different browser",
            "D": "Reboot and install a second AV program",
            "E": "Delete cache, temporary files, and cookies",
            "F": "Reset the browser to default settings"
        },
        "answer": "EF",
        "explanation": "Resetting the browser and clearing data remove hijacker settings and cached redirects.",
        "objective": "3.5 Browser troubleshooting"
    },
    {
        "question": "An employee moved from HR to Sales. Which should you check to ensure they no longer have access to HR share drives?",
        "options": {
            "A": "Security Groups",
            "B": "Group Policy",
            "C": "Home Folder",
            "D": "Credential Manager"
        },
        "answer": "A",
        "explanation": "Access to shares is commonly controlled via AD security group membership.",
        "objective": "5.3 Access control"
    },
    {
        "question": "You’re concerned servers could be damaged during a power failure or under-voltage event. Which TWO devices would protect against these conditions?",
        "options": {
            "A": "Grounding the server rack",
            "B": "Surge suppressor",
            "C": "Battery backup",
            "D": "Line conditioner"
        },
        "answer": "CD",
        "explanation": "A UPS provides backup during outages; a line conditioner stabilizes brownouts/undervoltage.",
        "objective": "1.5 Power protection"
    },
    {
        "question": "Which remote access tool is a command-line terminal emulation program operating on port 23?",
        "options": {
            "A": "Telnet",
            "B": "SSH",
            "C": "VNC",
            "D": "RDP"
        },
        "answer": "A",
        "explanation": "Telnet uses TCP 23 and is plaintext (insecure).",
        "objective": "2.6 Network services and ports"
    },
    {
        "question": "You submitted an RFC to install a security patch during maintenance. Which change request document would describe HOW the installation will be performed?",
        "options": {
            "A": "Scope",
            "B": "Purpose",
            "C": "Risk analysis",
            "D": "Plan"
        },
        "answer": "D",
        "explanation": "The implementation plan details procedures, timing, and rollback.",
        "objective": "5.3 Change management"
    },
    {
        "question": "Which backup rotation uses a three-tiered approach to ensure at least one monthly full backup is conducted?",
        "options": {
            "A": "3-2-1 backup",
            "B": "Tower of Hanoi",
            "C": "Grandfather-father-son",
            "D": "FIFO Backup"
        },
        "answer": "C",
        "explanation": "Grandfather-father-son rotates daily/weekly/monthly full backups.",
        "objective": "4.1 Backup strategies"
    },
    {
        "question": "New employees must sign a document stating they understand proper rules for using company computers—what can and cannot be done. Which document BEST describes this?",
        "options": {
            "A": "MOU",
            "B": "SLA",
            "C": "SOW",
            "D": "AUP"
        },
        "answer": "D",
        "explanation": "An Acceptable Use Policy defines permitted and prohibited activities.",
        "objective": "5.3 Policies"
    },
    {
        "question": "Which Windows command-line tool would you use to end one or more hung processes?",
        "options": {
            "A": "net use",
            "B": "gpupdate",
            "C": "taskkill",
            "D": "sfc"
        },
        "answer": "C",
        "explanation": "taskkill terminates processes by PID or image name.",
        "objective": "3.2 Windows tools"
    },
    {
        "question": "Which description accurately explains the function of clearing the browser cache?",
        "options": {
            "A": "Disables tracking of browsing history",
            "B": "Blocks harmful websites from loading",
            "C": "Deletes stored copies of web pages to force fresh content loading",
            "D": "Prevents pop-up ads from displaying"
        },
        "answer": "C",
        "explanation": "Clearing cache removes stored files so the browser fetches new versions.",
        "objective": "3.5 Browser troubleshooting"
    },
    {
        "question": "You are troubleshooting a computer that is operating slowly. Which tool should you use to troubleshoot this workstation?",
        "options": {
            "A": "DxDiag",
            "B": "Device Manager",
            "C": "Task Scheduler",
            "D": "Performance Monitor"
        },
        "answer": "D",
        "explanation": "Performance Monitor helps baseline and analyze system resource bottlenecks.",
        "objective": "3.5 Windows troubleshooting"
    },
    {
        "question": "You received multiple calls reporting websites are inaccessible. Which tool tests end-to-end connectivity and reports each hop found in the connection to determine if the issue is on the intranet or with the ISP?",
        "options": {
            "A": "netstat",
            "B": "ping",
            "C": "nslookup",
            "D": "tracert"
        },
        "answer": "D",
        "explanation": "tracert (traceroute) maps the path and identifies where latency or failure occurs.",
        "objective": "2.5 Network troubleshooting"
    },
    {
        "question": "Which of the tools should a technician NOT use with a solid-state device on a workstation?",
        "options": {
            "A": "Performance Monitor",
            "B": "Disk Cleanup",
            "C": "Disk defragmenter",
            "D": "Device Manager"
        },
        "answer": "C",
        "explanation": "Defragmentation is unnecessary and can reduce SSD lifespan.",
        "objective": "1.4 Storage best practices"
    },
{
    "question": "A user requests a site's certificate, but an evil twin intercepts the request and presents a spoofed certificate, which the user's browser accepts. What has just happened? (Select three.)",
    "options": {
      "A": "The user thinks they have a secure connection.",
      "B": "An on-path attack",
      "C": "A rootkit attack",
      "D": "Malware is in the middle of the session."
    },
    "answer": ["A", "B", "D"],
    "explanation": "The user is tricked into thinking the site is secure, but the attacker is sitting in the middle of the connection (on-path attack) and inserting malicious activity. A rootkit is unrelated here.",
    "objective": "Certificate spoofing & on-path attacks"
  },
  {
    "question": "A security awareness trainer spends a good portion of the training class talking about phishing. Which of the following is an indicator of phishing? (Select three.)",
    "options": {
      "A": "Disguised links",
      "B": "No signature",
      "C": "Urgency",
      "D": "Inconsistent sender and reply to addresses"
    },
    "answer": ["A", "C", "D"],
    "explanation": "Phishing often uses disguised links, urgent language, and mismatched sender/reply-to addresses to trick victims.",
    "objective": "Phishing awareness"
  },
  {
    "question": "A user calls the help desk complaining that Windows freezes to a blue screen every time it tries to boot. Why does the technician want to enter Safe Mode first?",
    "options": {
      "A": "Antivirus scans can be run in Safe Mode.",
      "B": "Safe Mode loads only the minimum amount of drivers and services to start the system.",
      "C": "Safe Mode is necessary for troubleshooting.",
      "D": "CHKDSK can be run in Safe Mode."
    },
    "answer": "B",
    "explanation": "Safe Mode only loads the basics, which helps narrow down if the crash is caused by drivers or software.",
    "objective": "Windows troubleshooting"
  },
  {
    "question": "A user has owned the same personal computer for a while and thinks it might be time for an upgrade. Which of the following are upgrade considerations? (Select three.)",
    "options": {
      "A": "Hardware compatibility",
      "B": "Backup files",
      "C": "Application support",
      "D": "PXE support"
    },
    "answer": ["A", "B", "C"],
    "explanation": "Before upgrading, check that new hardware is compatible, back up important files, and make sure applications will run on the new system.",
    "objective": "System upgrade preparation"
  },
  {
    "question": "A server administrator migrates from physical servers to a virtualized environment. What is the best approach to deploy new virtual machine operating systems?",
    "options": {
      "A": "ISOs",
      "B": "Downloadable",
      "C": "Proxy",
      "D": "Physical media"
    },
    "answer": "A",
    "explanation": "ISO images are the standard method for installing operating systems in virtual machines.",
    "objective": "Virtualization deployment"
  },
  {
    "question": "A server administrator wants to set up basic domain services such as Active Directory, email, and DNS. Which client operating systems will be compatible with domain-joined networks? (Select three.)",
    "options": {
      "A": "Pro",
      "B": "Enterprise",
      "C": "Education",
      "D": "Home"
    },
    "answer": ["A", "B", "C"],
    "explanation": "Domain-joining is only supported in Pro, Enterprise, and Education editions. Home editions cannot join a domain.",
    "objective": "Active Directory compatibility"
  },
  {
    "question": "A malware infection can manifest in many ways. Which of the following issues could it cause? (Select all that apply.)",
    "options": {
      "A": "Windows update fails",
      "B": "Roaming profiles",
      "C": "Redirection",
      "D": "UAC is enabled"
    },
    "answer": ["A", "C"],
    "explanation": "Malware often blocks updates and redirects the user to malicious sites. UAC being enabled is normal, and roaming profiles are unrelated.",
    "objective": "Malware symptoms"
  },
  {
    "question": "An attacker imitates IT support and asks for a user's password to gain remote access. What is this called?",
    "options": {
      "A": "Shoulder surfing",
      "B": "Tailgating",
      "C": "Dumpster diving",
      "D": "Impersonation"
    },
    "answer": "D",
    "explanation": "The attacker pretends to be someone else to gain trust. This is impersonation.",
    "objective": "Social engineering tactics"
  },
  {
    "question": "The Snapchat app on an iOS phone will not close even after a reboot. What is the best fix?",
    "options": {
      "A": "Factory Reset",
      "B": "Wiping",
      "C": "Uninstall, then reinstall",
      "D": "System updates"
    },
    "answer": "C",
    "explanation": "Reinstalling the app often fixes crashes or unresponsiveness without wiping the device.",
    "objective": "iOS troubleshooting"
  },
  {
    "question": "A teenager downloads games from outside the Google Play store. What best describes this behavior?",
    "options": {
      "A": "APK sideloading",
      "B": "Rooting",
      "C": "Bootlegging",
      "D": "Jailbreaking"
    },
    "answer": "A",
    "explanation": "Installing Android apps from outside the official store is called sideloading APKs.",
    "objective": "Mobile device security"
  },
  {
    "question": "An administrator wants to use slipstream and image deployment for endpoints. Which boot method best supports this?",
    "options": {
      "A": "Optical",
      "B": "Internet",
      "C": "Network",
      "D": "Internal hard drive"
    },
    "answer": "C",
    "explanation": "Network booting (PXE) allows large-scale OS deployments and is the best option for imaging.",
    "objective": "System deployment methods"
  },
  {
    "question": "The electronic health records software crashes. It already has backups and the latest updates. What could fix it?",
    "options": {
      "A": "Update the application driver.",
      "B": "Uninstall and reinstall the application driver.",
      "C": "Try to recover data from temporary files.",
      "D": "Uninstall and reinstall the application."
    },
    "answer": "D",
    "explanation": "Since updates and backups are handled, the next step is to reinstall the program to repair corruption.",
    "objective": "Application troubleshooting"
  },
  {
    "question": "A new AI tool produces an output that is wrong and not based on its training data. What is this issue called?",
    "options": {
      "A": "Hallucinations",
      "B": "NLP",
      "C": "Bias",
      "D": "Accuracy"
    },
    "answer": "A",
    "explanation": "AI 'hallucination' means making up false or unsupported answers.",
    "objective": "AI reliability"
  },
  {
    "question": "A technician must remove all corporate accounts and files from an employee’s device but leave personal data untouched. What is this called?",
    "options": {
      "A": "Remote wipe",
      "B": "Locator application",
      "C": "Profile security requirements",
      "D": "Enterprise wipe"
    },
    "answer": "D",
    "explanation": "An enterprise wipe deletes company data while leaving personal files safe.",
    "objective": "Mobile device management"
  },
  {
    "question": "Before submitting an application for change, IT must include a document with risk analysis. What type of document is this?",
    "options": {
      "A": "Date and time change",
      "B": "Scope of the change",
      "C": "Affected systems",
      "D": "Purpose of the change"
    },
    "answer": "B",
    "explanation": "The scope of change explains risks, what systems are affected, and what happens if it’s not done.",
    "objective": "Change management documentation"
  },
  {
    "question": "Two friends try to share photos using AirDrop, but one gets a message saying no one is nearby. Why?",
    "options": {
      "A": "The first friend has Nearby Share disabled.",
      "B": "The second friend has Wi-Fi disabled.",
      "C": "The second friend has Bluetooth disabled.",
      "D": "The first friend has Bluetooth disabled."
    },
    "answer": "C",
    "explanation": "AirDrop requires both Wi-Fi and Bluetooth. If Bluetooth is off, AirDrop won’t detect nearby devices.",
    "objective": "iOS file sharing"
  },
  {
    "question": "What is the last step before removing a computer from quarantine during malware removal?",
    "options": {
      "A": "Antivirus scan",
      "B": "Re-enable System Restore.",
      "C": "Create a fresh restore point.",
      "D": "Verify DNS configuration."
    },
    "answer": "C",
    "explanation": "After cleaning the system, create a restore point so the system can be rolled back safely if needed.",
    "objective": "Malware removal process"
  },
  {
    "question": "An employee is working with a substance that can harm them. Which should they use? (Select two.)",
    "options": {
      "A": "Lifting techniques",
      "B": "Safety goggles",
      "C": "Fuse",
      "D": "Air filter mask"
    },
    "answer": ["B", "D"],
    "explanation": "Protective gear like goggles and masks prevents harm from hazardous substances.",
    "objective": "Workplace safety"
  },
  {
    "question": "An administrator is backup chaining a database with a moderate time and storage requirement. What backup type is this?",
    "options": {
      "A": "Frequency",
      "B": "Full with incremental",
      "C": "Retention",
      "D": "Full with differential"
    },
    "answer": "D",
    "explanation": "Differential backups save changes since the last full backup. They balance speed and storage.",
    "objective": "Backup strategies"
  },
  {
    "question": "A user plugs USB-C headphones into a USB 3 port but gets 'not enough USB controller resources.' What is the best fix?",
    "options": {
      "A": "Open Resource Monitor to check compatibility.",
      "B": "Close programs to free memory.",
      "C": "Connect the headphones to a USB 2 port.",
      "D": "Run SFC to update USB controller drivers."
    },
    "answer": "C",
    "explanation": "USB 2 uses fewer resources and is more compatible with some simple devices like headphones.",
    "objective": "USB troubleshooting"
  },
  {
    "question": "A user's phone is slow and shows pop-up ads. What other symptoms are common with malware on a phone? (Select two.)",
    "options": {
      "A": "Fake security warnings",
      "B": "Redirection",
      "C": "APK sideloading",
      "D": "Increased response times"
    },
    "answer": ["A", "B"],
    "explanation": "Malware often shows fake warnings and redirects you to malicious sites. APK sideloading is a cause, not a symptom.",
    "objective": "Mobile malware symptoms"
  },
  {
    "question": "A company has employees sign a document enforcing rules to prevent misuse of equipment. What is this document?",
    "options": {
      "A": "Procurement life cycle",
      "B": "Splash screen",
      "C": "Assigned users",
      "D": "Acceptable use policy"
    },
    "answer": "D",
    "explanation": "An acceptable use policy defines how company equipment and data should be used safely.",
    "objective": "Policy & compliance"
  },
  {
    "question": "A user notices their device has a leaking component and must dispose of it properly. Which disposal is this?",
    "options": {
      "A": "Fuse",
      "B": "Device",
      "C": "Toner",
      "D": "Battery"
    },
    "answer": "D",
    "explanation": "Batteries can leak harmful chemicals and must be disposed of at approved facilities.",
    "objective": "Hazardous materials handling"
  },
  {
    "question": "A user finds that their iPhone 11 runs slowly, and reboot doesn’t fix it. Which issues could cause this? (Select three.)",
    "options": {
      "A": "OS update",
      "B": "Too many apps open",
      "C": "Mesh network",
      "D": "Low battery charge"
    },
    "answer": ["A", "B", "D"],
    "explanation": "Updates, too many open apps, or low battery can all slow performance. Mesh networks are unrelated.",
    "objective": "Mobile performance troubleshooting"
  },
  {
    "question": "During an IT meeting, the topic of employee security behavior comes up. Why would IT focus on behavior? (Select two.)",
    "options": {
      "A": "Phishing",
      "B": "Jailbreaking",
      "C": "Hashing",
      "D": "Social engineering"
    },
    "answer": ["A", "D"],
    "explanation": "Employees are most vulnerable to phishing and social engineering, which rely on human mistakes.",
    "objective": "Security awareness"
  },
  {
    "question": "A user is on a website with HTTPS. The browser shows the certificate in the address bar. What does the certificate validate?",
    "options": {
      "A": "Pop-up blocker",
      "B": "Browser sign-in",
      "C": "Secure connection",
      "D": "Untrusted source"
    },
    "answer": "C",
    "explanation": "An HTTPS certificate validates that the connection is encrypted and secure between the browser and site.",
    "objective": "Web security"
  },
    {
        "question": "A technician helps a customer with a ticket request and needs to record that the customer has accepted that the ticket can be closed. Which of the following fields reflect this part of the ticket life cycle?",
        "options": {
            "A": "Progress notes",
            "B": "Problem description",
            "C": "Problem resolution",
            "D": "Escalation levels"
        },
        "answer": "C",
        "explanation": "Recording that the customer accepted closure is part of documenting the resolution of the issue.",
        "objective": "Ticket lifecycle & closure"
    },
    {
        "question": "A helpdesk operator looks at build numbers for Windows as they plan upgrade timelines. The operator investigates the significance of the build numbers. Which of the following are the build numbers based on? (Select two.)",
        "options": {
            "A": "Windows version",
            "B": "Time of year",
            "C": "32 bit vs. 64 bit",
            "D": "Year"
        },
        "answer": ["A", "D"],
        "explanation": "Windows build numbers reflect the Windows version and the year of release. They are not tied to system architecture or the exact time of year.",
        "objective": "Windows versioning"
    },
    {
        "question": "What type of data can be associated with a specific person or use an anonymized or de-identified data set for analysis and research?",
        "options": {
            "A": "PII",
            "B": "Open-source license",
            "C": "Personal government-issued information",
            "D": "Healthcare data"
        },
        "answer": "A",
        "explanation": "PII (Personally Identifiable Information) refers to any data that can directly or indirectly identify a person.",
        "objective": "Data privacy"
    },
    {
        "question": "A manager for a Windows server team recently purchased new software that will help to streamline operations, but they are worried that in IT, there is a high turnover of personnel. The manager wants to ensure they can obtain updates, monitor and fix security issues, and are provided technical assistance. What impact is the manager trying to mitigate?",
        "options": {
            "A": "Business",
            "B": "Network",
            "C": "Training",
            "D": "Licensing"
        },
        "answer": "A",
        "explanation": "The concern is about ensuring continued support and updates regardless of staff turnover, which is a business continuity risk.",
        "objective": "Risk management"
    },
    {
        "question": "Many mobile apps collect location data. Rogue apps could use location data for criminal purposes, such as burglary. However, many legitimate apps also track a mobile user's location. Why would a legitimate shopping app have an interest in a user's location?",
        "options": {
            "A": "Targeted advertising",
            "B": "Redirection",
            "C": "Geotagging",
            "D": "Clicks"
        },
        "answer": "A",
        "explanation": "Shopping apps use location to deliver targeted ads and promotions relevant to where the user is.",
        "objective": "Mobile app permissions"
    },
    {
        "question": "Which of the following are direct advantages of integrating AI into software applications? (Select two.)",
        "options": {
            "A": "Faster Installation",
            "B": "Enhanced Functionality",
            "C": "Increased capabilities",
            "D": "Reduced cost"
        },
        "answer": ["B", "C"],
        "explanation": "AI enhances applications by adding new functions and increasing what the software can do.",
        "objective": "AI in software"
    },
    {
        "question": "A technician creates full backups by having the chain start with an initial full backup as normal and afterward makes a series of incremental backups. Which of the following backups is this?",
        "options": {
            "A": "Synthetic",
            "B": "On-site backup storage",
            "C": "Retention",
            "D": "Frequency"
        },
        "answer": "A",
        "explanation": "A synthetic backup is created by combining a full backup with a series of incremental backups, making future restores easier.",
        "objective": "Backup methods"
    },
    {
        "question": "A vulnerability management lead wants to set up the company using a more secure authentication method than a simple password. What hardware aspect should the management lead consider?",
        "options": {
            "A": "Dedicated graphics card",
            "B": "Integrated graphics card",
            "C": "CPU requirements",
            "D": "Hardware token"
        },
        "answer": "D",
        "explanation": "Hardware tokens provide stronger authentication by requiring possession of a physical device in addition to a password.",
        "objective": "Authentication methods"
    },
    {
        "question": "A threat actor uses a technique that executes statements through an unfiltered user response. What is this technique?",
        "options": {
            "A": "Dictionary attack",
            "B": "XSS",
            "C": "SQL injection",
            "D": "Brute force attack"
        },
        "answer": "C",
        "explanation": "SQL injection allows attackers to run unauthorized commands on a database through insecure input fields.",
        "objective": "Web security"
    },
    {
        "question": "A technician uses a method where each server is configured with a public/private encryption key pair and identified by a host key fingerprint. What is this method?",
        "options": {
            "A": "RDP",
            "B": "VNC",
            "C": "SSH",
            "D": "VPN"
        },
        "answer": "C",
        "explanation": "SSH uses key pairs and fingerprints to securely authenticate servers and clients.",
        "objective": "Secure communication protocols"
    },
    {
        "question": "An employee enters the web address of their local newspaper to check for news on the company, and a site pops up with many click-bait celebrity stories. The employee re-enters the address, assuming a misspelling, but returns to the same page. When the help desk technician arrives, which of the following troubleshooting steps would be appropriate?",
        "options": {
            "A": "Check the System Configuration Utility.",
            "B": "Check to see if the newspaper website's certificate is expired.",
            "C": "Check to see if the DNS browser is configured correctly.",
            "D": "Check HOSTS files for malicious entries."
        },
        "answer": "D",
        "explanation": "Hackers can modify the HOSTS file so that when you type in a real website, your computer redirects you to a fake one. Checking the HOSTS file can reveal if this is the case.",
        "objective": "Malware troubleshooting & DNS redirection"
    },
    {
        "question": "A technician detected and reported a security incident, resulting in the appropriate unit being notified and tasked with acting as first responders. What is this unit called?",
        "options": {
            "A": "IRP",
            "B": "Chain of custody",
            "C": "Open-source",
            "D": "CSIRT"
        },
        "answer": "D",
        "explanation": "A CSIRT (Computer Security Incident Response Team) is the group responsible for handling and responding to security incidents within an organization.",
        "objective": "Incident response process"
    },
    {
        "question": "A company has backup storage located at a different location, which lowers the risk of losing both production and backup copies of data. Which of the following is this backup storage?",
        "options": {
            "A": "Frequency",
            "B": "Off-site backup storage",
            "C": "On-site backup storage",
            "D": "Synthetic"
        },
        "answer": "B",
        "explanation": "Keeping backups in a different location protects against disasters like fires or floods that could destroy both the original and the backup if they were together.",
        "objective": "Data backup & disaster recovery"
    },
    {
        "question": "Malware encyclopedias are a resource that antivirus vendors often make available to IT professionals. What is their value for IT practitioners? (Select two.)",
        "options": {
            "A": "They provide a pricing model for remediation based on the malware found.",
            "B": "They are documentation of known malware.",
            "C": "They troubleshoot unknown malware based on the behavior of known malware.",
            "D": "They provide information about the type, symptoms, purpose, and removal of malware."
        },
        "answer": "B and D",
        "explanation": "Malware encyclopedias help IT staff by listing known malware and providing details like symptoms, how it spreads, and how to remove it. They don’t set prices or directly troubleshoot unknown malware.",
        "objective": "Malware identification & remediation resources"
    },
    {
        "question": "While researching and writing a paper on their home computer, a student notices an alert in the notification area that Windows Defender has expired and needs to be updated. The student is annoyed by the interruption but clicks on the alert and follows the update instructions. Later, the student told their parents that Defender expired, and they installed the update. The student's parents are panic-stricken. Determine the best reason for the parents' reaction from the information provided.",
        "options": {
            "A": "A malicious browser push notification tricked the student into downloading malware.",
            "B": "The parents know the Windows Defender subscription was recently renewed.",
            "C": "The parents have scheduled all updates to occur during the automatic maintenance window at 2:00 am.",
            "D": "A malicious browser push notification tricked the student into a drive-by download."
        },
        "answer": "A",
        "explanation": "Windows Defender is free and doesn’t expire. The 'expiration' message was fake, likely a trick to get the student to install malware.",
        "objective": "Social engineering & malware delivery"
    },
    {
        "question": "A technician needs this skill to give full attention to the customer so there is no disagreement or misinterpretation of what was said. What is this skill?",
        "options": {
            "A": "Cultural sensitivity",
            "B": "Active listening",
            "C": "Proper language",
            "D": "Open-ended questions"
        },
        "answer": "B",
        "explanation": "Active listening means paying close attention and making sure you understand the customer correctly, reducing the chance of confusion.",
        "objective": "Customer service skills"
    },
    {
        "question": "A user is buying software for their PC. Which of the following would the user be purchasing for individual use?",
        "options": {
            "A": "DRM",
            "B": "Personal license",
            "C": "Corporate-use license",
            "D": "Data retention requirements"
        },
        "answer": "B",
        "explanation": "A personal license allows one person to use the software. Corporate licenses are for businesses with multiple users.",
        "objective": "Software licensing"
    },
    {
        "question": "An accountant has an unlimited data plan and has set data usage limit triggers for their mobile phone. What concern does the accountant have with high data usage with an unlimited data plan? (Select two.)",
        "options": {
            "A": "Crypto mining",
            "B": "Jailbreaking",
            "C": "Phishing",
            "D": "DDoS"
        },
        "answer": "A and D",
        "explanation": "High data use can mean the phone is secretly being used for crypto mining or as part of a DDoS attack. Jailbreaking and phishing don’t directly cause heavy data use.",
        "objective": "Mobile device security monitoring"
    },
    {
        "question": "Which of the following can prevent, detect, and remove software threats that consist of ransomware, Trojans, spyware, and rootkits?",
        "options": {
            "A": "Recovery mode",
            "B": "OS reinstallation",
            "C": "Security-awareness training",
            "D": "Anti-malware"
        },
        "answer": "D",
        "explanation": "Anti-malware software is specifically designed to find and stop different types of malicious software.",
        "objective": "Malware protection"
    },
    {
        "question": "A company needs to set up perimeter security to control and monitor who can approach the building. Which of the following should the company use? (Select three.)",
        "options": {
            "A": "Folder redirection",
            "B": "Access control vestibule",
            "C": "Fencing",
            "D": "Guard"
        },
        "answer": "B, C, and D",
        "explanation": "Physical security measures like guards, fencing, and secure entry points help control who enters the building. Folder redirection is a computer setting, not a physical security tool.",
        "objective": "Physical security controls"
    },
{
    "question": "You are employed by a company that is implementing a new CRM system. They need to automatically sync customer data with the company's billing and inventory management software. Which of the following would BEST address this requirement?",
    "options": {
      "A": "Software patch management",
      "B": "Application integration",
      "C": "Virtualization",
      "D": "Endpoint protection"
    },
    "answer": "B",
    "explanation": "Application integration connects different programs (CRM, billing, inventory) so they can share data automatically. This reduces errors and avoids manual data entry.",
    "objective": "System integration & workflow efficiency"
  },
  {
    "question": "Which command-line tool on a Windows system is used to display the resulting set of policy settings that were enforced on a computer for a specified user when they logged on?",
    "options": {
      "A": "gpupdate",
      "B": "dism",
      "C": "gpresult",
      "D": "sfc"
    },
    "answer": "C",
    "explanation": "The gpresult tool shows which group policies are applied to a user or computer at logon. This helps troubleshoot security or permission issues.",
    "objective": "Windows policy troubleshooting"
  },
  {
    "question": "Regardless of what website Michelle types into her browser, she is being redirected to 'malwarescammers.com.' What should Michelle do to fix this problem?",
    "options": {
      "A": "Update the anti-virus software and run a full system scan",
      "B": "Rollback the application to the previous version",
      "C": "Restart the network services",
      "D": "Reset the web browser's proxy setting"
    },
    "answer": "A",
    "explanation": "Malicious redirects are often caused by malware. Running a full antivirus scan ensures the system detects and removes the infection.",
    "objective": "Malware removal & prevention"
  },
  {
    "question": "Which of the following should you use when attempting to dislodge dirt in a keyboard with compressed air?",
    "options": {
      "A": "Safety goggles",
      "B": "Antistatic bag",
      "C": "ESD strap",
      "D": "Gloves"
    },
    "answer": "A",
    "explanation": "Compressed air can blow dust and debris into your eyes. Safety goggles protect you from particles while cleaning a keyboard.",
    "objective": "Workplace safety & equipment maintenance"
  },
  {
    "question": "Which of the following commands is used on a Linux system to change the ownership of a file or directory on a system?",
    "options": {
      "A": "chmod",
      "B": "chown",
      "C": "passwd",
      "D": "pwd"
    },
    "answer": "B",
    "explanation": "The chown command changes the owner of a file or folder. This is important for setting the right permissions in Linux.",
    "objective": "Linux file permissions management"
  },
  {
    "question": "A Windows 2019 server is crashing every evening at 2:35 am, but you are not sure why. Which of the following tools should you use to identify the cause of the system crash?",
    "options": {
      "A": "Performance monitor",
      "B": "Event viewer",
      "C": "Registry editor",
      "D": "System information"
    },
    "answer": "B",
    "explanation": "Event Viewer records system logs, including errors and crashes. Reviewing these logs helps identify the cause of recurring server crashes.",
    "objective": "Windows server troubleshooting"
  },
  {
    "question": "Which of the following commands is used to display the amount of disk space available on the file system in Linux?",
    "options": {
      "A": "pwd",
      "B": "cat",
      "C": "ls",
      "D": "df"
    },
    "answer": "D",
    "explanation": "The df command shows how much disk space is used and available on Linux file systems. It is useful for monitoring storage.",
    "objective": "Linux storage monitoring"
  },
  {
    "question": "Which of the following is the BEST encryption from the options below to maximize network security between AP4 and AP5?",
    "options": {
      "A": "Open",
      "B": "WPA2-CCMP",
      "C": "WEP",
      "D": "WPA",
      "E": "WPA2-TKIP"
    },
    "answer": "B",
    "explanation": "WPA2-CCMP (AES) is the most secure encryption method listed. WEP and WPA are outdated, and WPA2-TKIP is weaker than CCMP.",
    "objective": "Wireless security configuration"
  },
  {
    "question": "Which of the following MacOS features is the equivalent of File Explorer in Windows?",
    "options": {
      "A": "Dock",
      "B": "Mission Control",
      "C": "Spotlight",
      "D": "Finder"
    },
    "answer": "D",
    "explanation": "Finder in macOS is used to browse files and folders, just like File Explorer in Windows.",
    "objective": "Cross-platform file navigation"
  },
  {
    "question": "Dion Training uses DHCP to assign private Class B IP addresses to its Windows 10 workstations. Which of the following IP addresses is a Class B address?",
    "options": {
      "A": "169.254.125.154",
      "B": "10.5.34.15",
      "C": "192.168.2.14",
      "D": "172.16.13.12"
    },
    "answer": "D",
    "explanation": "Class B private addresses range from 172.16.0.0 to 172.31.255.255. 172.16.13.12 falls in this range.",
    "objective": "Networking & IP addressing"
  },
    {
        "question": "Tamera trying to install Windows 11 (64-bit) on an older laptop she found in her closet. The installation is continually failing and producing an error. The laptop has a dual-core 1.2 GHz processor, 2 GB of memory, a 250 GB hard drive, and a 1280 x 720 screen resolution. Which item in the laptop must be upgraded to meet the minimum requirements for installing Windows 11?",
        "options": {
            "A": "The screen resolution",
            "B": "Amount of memory",
            "C": "Number of CPU cores",
            "D": "Amount of hard drive space"
        },
        "answer": "B",
        "explanation": "Windows 11 requires at least 4 GB of RAM. Since this laptop only has 2 GB, it will fail the installation until the memory is upgraded.",
        "objective": "Windows 11 system requirements"
    },
    {
        "question": "What is the name of a program that monitors user activity and sends that information to someone else?",
        "options": {
            "A": "Rootkit",
            "B": "Virus",
            "C": "Keylogger",
            "D": "Spyware"
        },
        "answer": "D",
        "explanation": "Spyware secretly tracks a user's activity and sends the data to a third party without permission.",
        "objective": "Types of malware"
    },
    {
        "question": "You received an email saying 'You won a free iPhone!' with a link to claim the prize. How should you classify this email?",
        "options": {
            "A": "Phishing",
            "B": "Spoofing",
            "C": "Spear phishing",
            "D": "Zero-day"
        },
        "answer": "A",
        "explanation": "This is a phishing attempt. It tries to trick the user into clicking a malicious link to steal information.",
        "objective": "Email threats & phishing"
    },
    {
        "question": "Your smartphone's battery has been draining quickly. You checked the apps and noticed that a free game collects GPS data even when not in use. Which threat is this an example of?",
        "options": {
            "A": "Unintended Bluetooth pairing",
            "B": "Unauthorized microphone activation",
            "C": "Unauthorized location tracking",
            "D": "Unauthorized account access"
        },
        "answer": "C",
        "explanation": "The app is secretly collecting GPS location data, which is unauthorized location tracking.",
        "objective": "Mobile device security"
    },
    {
        "question": "Which tool should you use to ensure you don’t damage a laptop’s SSD while replacing it?",
        "options": {
            "A": "ESD strap",
            "B": "Air filter mask",
            "C": "Antistatic bag",
            "D": "Latex gloves"
        },
        "answer": "A",
        "explanation": "An ESD (Electrostatic Discharge) strap grounds you, preventing static electricity from damaging sensitive computer parts.",
        "objective": "Hardware protection"
    },
    {
        "question": "A user's personal settings are not showing up on their computer. You suspect the profile is corrupted. You cannot see the profile file. Which option should you configure to view it?",
        "options": {
            "A": "Display Settings",
            "B": "User Accounts",
            "C": "Folder Options",
            "D": "Internet Options"
        },
        "answer": "C",
        "explanation": "Folder Options lets you show hidden system files, which is where corrupted profiles may be stored.",
        "objective": "Windows troubleshooting"
    },
    {
        "question": "A workstation is running very slowly. The user recently downloaded a new app, and you notice many unknown background processes. What type of infection is MOST likely?",
        "options": {
            "A": "Rootkit",
            "B": "Keylogger",
            "C": "Trojan",
            "D": "Ransomware"
        },
        "answer": "C",
        "explanation": "A Trojan disguises itself as a normal program but installs malicious processes in the background.",
        "objective": "Malware identification"
    },
    {
        "question": "Which WPA3 feature is used for password-based authentication using the dragonfly handshake instead of the old WPA 4-way handshake?",
        "options": {
            "A": "Management protection frames",
            "B": "SAE",
            "C": "AES GCMP",
            "D": "Enhanced open"
        },
        "answer": "B",
        "explanation": "SAE (Simultaneous Authentication of Equals) replaces the old WPA handshake, making authentication more secure.",
        "objective": "Wi-Fi security protocols"
    },
    {
        "question": "Which setting must be enabled to allow a video game console or VoIP handset to automatically configure your firewall by opening required ports?",
        "options": {
            "A": "UPnP",
            "B": "NAT",
            "C": "MDM",
            "D": "DHCP"
        },
        "answer": "A",
        "explanation": "UPnP (Universal Plug and Play) allows devices to request the firewall open specific ports automatically.",
        "objective": "Network configuration"
    },
    {
        "question": "You want to check if a workstation is reporting any S.M.A.R.T. errors. Which tool should you use?",
        "options": {
            "A": "Task scheduler",
            "B": "Performance monitor",
            "C": "DxDiag",
            "D": "Disk management"
        },
        "answer": "D",
        "explanation": "Disk Management can show disk health status, including S.M.A.R.T. error reports.",
        "objective": "Disk health monitoring"
    },
    {
        "question": "Multiple users report screen static when moving their mouse. You suspect the video driver is the issue. Which log should you check to confirm if the driver was updated?",
        "options": {
            "A": "System log",
            "B": "Application log",
            "C": "Setup",
            "D": "Security log"
        },
        "answer": "C",
        "explanation": "The Setup log records driver and hardware installation changes, including video drivers.",
        "objective": "Windows event logs"
    },
{
    "question": "You are working as a service desk analyst. This morning, you have received multiple calls from users reporting that they cannot access websites from their work computers. You decide to troubleshoot the issue by running a program to see where the connection is failing. Which tool should you use?",
    "options": { "A": "netstat", "B": "tracert", "C": "nslookup", "D": "ping" },
    "answer": "B",
    "explanation": "Tracert shows the path that data takes from your computer to a website and identifies where the connection is breaking down.",
    "objective": "Network troubleshooting"
  },
  {
    "question": "An attacker has been collecting credit card details by calling victims and tricking them over the phone. What type of attack is this?",
    "options": { "A": "Vishing", "B": "Spear phishing", "C": "Whaling", "D": "Phishing" },
    "answer": "A",
    "explanation": "Vishing is phishing done through voice calls, where attackers pretend to be someone trustworthy to steal information.",
    "objective": "Social engineering attacks"
  },
  {
    "question": "A macOS user browsing the internet sees a pop-up that says: 'Windows Enterprise Defender: Your computer is infected, click here to remove it!' What type of threat is this?",
    "options": { "A": "Phishing", "B": "Pharming", "C": "Rogue anti-virus", "D": "Worm" },
    "answer": "C",
    "explanation": "A rogue anti-virus pretends to be real security software but is actually a scam to trick users into downloading malware.",
    "objective": "Threat identification"
  },
  {
    "question": "Which Linux command is used to print the full contents of a file to the screen at once?",
    "options": { "A": "grep", "B": "dig", "C": "ls", "D": "cat" },
    "answer": "D",
    "explanation": "The 'cat' command shows the entire contents of a file directly on the screen.",
    "objective": "Linux file commands"
  },
  {
    "question": "Which of the following file types are commonly used by management and administrative tasks in Windows with the Integrated Scripting Environment?",
    "options": { "A": ".py", "B": ".ps1", "C": ".sh", "D": ".js" },
    "answer": "B",
    "explanation": "Windows PowerShell uses '.ps1' script files for automation and administration.",
    "objective": "Windows scripting"
  },
  {
    "question": "Which process describes documenting everyone who has physical access or possession of evidence?",
    "options": { "A": "Financial responsibility", "B": "Legal hold", "C": "Chain of custody", "D": "Secure copy protocol" },
    "answer": "C",
    "explanation": "Chain of custody keeps track of who handled evidence to ensure it hasn’t been tampered with.",
    "objective": "Evidence handling"
  },
  {
    "question": "During a firmware upgrade, the power goes out and the upgrade fails. Which plan helps restore the system to the previous working version?",
    "options": { "A": "Contingency plan", "B": "Rollback plan", "C": "Backup plan", "D": "Alternative plan" },
    "answer": "B",
    "explanation": "A rollback plan lets you return to the previous working version if the update fails.",
    "objective": "Disaster recovery planning"
  },
  {
    "question": "A company had several virus infections caused by known software vulnerabilities. What should they do to prevent future outbreaks?",
    "options": { "A": "Incident response team", "B": "Host-based intrusion detection", "C": "Acceptable use policies", "D": "Patch management" },
    "answer": "D",
    "explanation": "Patch management fixes vulnerabilities by keeping software updated, preventing attackers from exploiting them.",
    "objective": "Preventing malware infections"
  },
  {
    "question": "You are troubleshooting a connectivity issue and need to identify the path data takes from your computer to a remote server. Which tool should you use?",
    "options": { "A": "nbtstat", "B": "netstat", "C": "ipconfig", "D": "tracert" },
    "answer": "D",
    "explanation": "Tracert shows the step-by-step path that data takes between computers.",
    "objective": "Network troubleshooting"
  },
  {
    "question": "An attacker tries WPS PINs one by one (00000000, 00000001, 00000002, etc.) until they find the correct one. What type of password attack is this?",
    "options": { "A": "Rainbow table", "B": "Brute-force", "C": "Hybrid", "D": "Dictionary" },
    "answer": "B",
    "explanation": "Brute-force tries every possible combination until the correct one is found.",
    "objective": "Password attacks"
  },
  {
    "question": "A government agency is retiring hard drives with classified data. Which method ensures data cannot be recovered?",
    "options": { "A": "Standard formatting", "B": "Secure deletion software", "C": "Magnetic degausser", "D": "Locked storage units" },
    "answer": "C",
    "explanation": "A degausser permanently erases data by disrupting the magnetic fields on the drive.",
    "objective": "Data destruction"
  },
  {
    "question": "A computer is infected with malware that hides in the Windows kernel. What type of malware is this?",
    "options": { "A": "Botnet", "B": "Rootkit", "C": "Trojan", "D": "Ransomware" },
    "answer": "B",
    "explanation": "A rootkit hides deep in the system (kernel level) to avoid detection and control the computer.",
    "objective": "Malware identification"
  },
  {
    "question": "A company is comparing cloud AI vs self-hosted AI. Which factor is most important to minimize risk?",
    "options": { "A": "AI processing speed", "B": "Data security", "C": "Scalability", "D": "Open-source compatibility" },
    "answer": "B",
    "explanation": "Keeping data secure is the top concern when choosing between external vs internal solutions.",
    "objective": "Security in cloud decisions"
  },
  {
    "question": "Which feature is unique to NTFS compared to FAT32?",
    "options": { "A": "OS compatibility", "B": "Support for files larger than 4GB", "C": "No file permission settings", "D": "Case-sensitive naming" },
    "answer": "B",
    "explanation": "NTFS supports larger files (over 4GB), while FAT32 cannot handle them.",
    "objective": "File system comparison"
  },
  {
    "question": "Which password policy prevents reusing old passwords?",
    "options": { "A": "Password history", "B": "Password complexity", "C": "Password length", "D": "Password expiration" },
    "answer": "A",
    "explanation": "Password history blocks users from reusing recently used passwords.",
    "objective": "Password security"
  },
  {
    "question": "Which Windows editions support installation on an Intel x86 workstation?",
    "options": { "A": "Windows 11 Home", "B": "Windows 10 Enterprise", "C": "Windows 11 Pro", "D": "Windows 10 Pro" },
    "answer": "A, C, D",
    "explanation": "Windows 11 Home, Pro, and Windows 10 Pro support x86. Windows 10 Enterprise generally needs x64.",
    "objective": "OS compatibility"
  },
  {
    "question": "How do cloud-based spreadsheets enhance team collaboration?",
    "options": { "A": "Editing is locked to one user", "B": "Changes appear in real-time", "C": "Only the owner can modify", "D": "Files must be re-uploaded" },
    "answer": "B",
    "explanation": "Cloud spreadsheets allow multiple users to see changes instantly as they happen.",
    "objective": "Collaboration tools"
  },
  {
    "question": "A laptop is sluggish after installing a second antivirus program. What should you do first?",
    "options": { "A": "Install Spybot Search & Destroy", "B": "Enable real-time protection", "C": "Run Windows Update", "D": "Uninstall the second antivirus" },
    "answer": "D",
    "explanation": "Running two antivirus programs causes conflicts, so remove the extra one first.",
    "objective": "System performance troubleshooting"
  },
  {
    "question": "Which description correctly identifies a primary characteristic of a PIN-based screen lock?",
    "options": { "A": "Uses fingerprint", "B": "Requires shape pattern", "C": "Uses facial features", "D": "Uses a numeric code" },
    "answer": "D",
    "explanation": "A PIN lock is based on entering a simple numeric code.",
    "objective": "Screen lock types"
  },
  {
    "question": "After a patch update, users complain of static when moving their mouse. Which step should you take?",
    "options": { "A": "Reboot in Safe Mode", "B": "Rollback video card driver", "C": "Run SFC", "D": "Disable DirectX service" },
    "answer": "B",
    "explanation": "If a new driver causes problems, rolling it back to the previous version usually fixes it.",
    "objective": "Driver troubleshooting"
  },
  {
    "question": "A smartphone is unresponsive after an iOS update. What should the technician do?",
    "options": { "A": "Update applications", "B": "Factory reset", "C": "Reimage", "D": "Rollback iOS update" },
    "answer": "D",
    "explanation": "Rolling back removes the problematic update and restores performance.",
    "objective": "Mobile troubleshooting"
  },
  {
    "question": "A company installs a UPS to protect servers from losing power for several minutes. What are they preventing?",
    "options": { "A": "Power failure", "B": "Power surge", "C": "Power spikes", "D": "Under-voltage event" },
    "answer": "A",
    "explanation": "A UPS provides backup power to keep systems running during a power outage.",
    "objective": "Power protection"
  },
  {
    "question": "After installing a second OS, you see 'Operating System Not Found'. Boot.ini is fine. What is likely the issue?",
    "options": { "A": "Partition marked active incorrectly", "B": "Startup services not running", "C": "Wrong MBR bootloader", "D": "Unsupported Linux version" },
    "answer": "A",
    "explanation": "If the wrong partition is marked active, the system won’t find the OS to boot from.",
    "objective": "Dual boot troubleshooting"
  },
  {
    "question": "Elizabeth replaced a security device protecting a subnet, and now external users can’t connect remotely. Which device is likely misconfigured?",
    "options": { "A": "DNS", "B": "Content filter", "C": "Firewall", "D": "DHCP" },
    "answer": "C",
    "explanation": "Firewalls control remote access. A misconfiguration could block outside users.",
    "objective": "Network troubleshooting"
  },
  {
    "question": "Which best describes the benefit of instant messaging for workplace collaboration?",
    "options": { "A": "Must be in same location", "B": "Messages appear at scheduled times", "C": "Conversations are permanent", "D": "Messages are instant" },
    "answer": "D",
    "explanation": "Instant messaging allows real-time communication across teams.",
    "objective": "Collaboration tools"
  },
  {
    "question": "Before replacing a desktop power supply, which action should you take first?",
    "options": { "A": "Remove jewelry", "B": "Check cable management", "C": "Use grounding probe", "D": "Dispose old power supply" },
    "answer": "A",
    "explanation": "Removing jewelry reduces the risk of electric shock and accidents.",
    "objective": "Hardware safety"
  },
  {
    "question": "You submit a request to install a Windows patch. Which document describes risks or negative effects that could occur?",
    "options": { "A": "Plan", "B": "Purpose", "C": "Risk analysis", "D": "Scope" },
    "answer": "C",
    "explanation": "A risk analysis outlines what might go wrong and how it can be managed.",
    "objective": "Change management"
  },
  {
    "question": "A customer reports intermittent PC problems. Which tool shows logs of past errors?",
    "options": { "A": "System Information", "B": "Event Viewer", "C": "Device Manager", "D": "Performance Monitor" },
    "answer": "B",
    "explanation": "Event Viewer logs system errors and warnings to help diagnose issues.",
    "objective": "Windows troubleshooting"
  },
  {
    "question": "Which command is used to create a new disk partition on Windows?",
    "options": { "A": "format", "B": "chkdsk", "C": "dd", "D": "diskpart" },
    "answer": "D",
    "explanation": "Diskpart is the tool used to create and manage partitions in Windows.",
    "objective": "Disk management"
  }
]

import random
import os
import json

STORE_PATH = "used_questions.json"
# ---- Helpers ----
def load_used_indices(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return [int(x) for x in data]
        return []
    except Exception:
        return []

def save_used_indices(path, used):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(used, f)
    except Exception:
        pass  # fail-safe: do not crash workflow if disk is read-only

def pick_unseen_index(pool_size, used):
    if len(used) >= pool_size:
        used.clear()
    # pick until unseen
    while True:
        idx = random.randint(0, pool_size - 1)
        if idx not in used:
            used.append(idx)
            return idx


def reset_if_too_many(path, limit=10):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = []

    if not isinstance(data, list):
        data = []

    if len(data) > limit:
        with open(path, "w", encoding="utf-8") as f:
            f.write("[]")

# ---- Main ----
used_indices = load_used_indices(STORE_PATH)
idx = pick_unseen_index(len(p), used_indices)
q = p[idx]
save_used_indices(STORE_PATH, used_indices)
reset_if_too_many(STORE_PATH, limit=80)


formatted = [{
    "question": q["question"],
    "options": q["options"],
    "answer": q["answer"],
    "explanation": q["explanation"],
    "objective": q["objective"],
    "content": f"**A+ Core 2 Practice Question**\nObjective: {q['objective']}\n\n{q['question']}\n\n```text\nA) {q['options']['A']}\nB) {q['options']['B']}\nC) {q['options']['C']}\nD) {q['options']['D']}\n```",
    "raw_text": json.dumps(q),
    "latest_record": False
}]



#return formatted



print ("total diff: ", 371 - len(p ))

print (len(p ))
print ('formatted: ',formatted)