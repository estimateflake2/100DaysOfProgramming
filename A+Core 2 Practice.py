p =  [
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
    }
]

import random
import json
q = p[random.randint(0, len(p)-1)]
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