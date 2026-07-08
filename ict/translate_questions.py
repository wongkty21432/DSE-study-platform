#!/usr/bin/env python3
"""
Add English translations to all DSE ICT questions.
Creates bilingual questions-ict.json with _en fields.
"""
import json, os

SRC = "questions-ict.json"
DST = "questions-ict.json"
BAK = "questions-ict-zh-only-backup.json"

with open(SRC, 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Backup
with open(BAK, 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
print(f"Backed up to {BAK}")

# English translations keyed by QID
en = {}

def t(qid, q_en, opts_en, exp_en, mark_en):
    en[qid] = {
        "question_en": q_en,
        "options_en": opts_en,
        "explanation_en": exp_en,
        "markingNotes_en": mark_en
    }

# ==================== TOPIC 1: Information Processing I ====================
t("ICT-001",
  "Which of the following is the correct relationship between data and information?",
  ["A. Data and information are the same concept",
   "B. Information is processed and organized data",
   "C. Data is processed and organized information",
   "D. There is no relationship between them"],
  "Information is processed, organized, and analyzed data that carries meaning and purpose. Raw data lacks context on its own; only after processing does it become useful information.",
  "1 mark: B. Information is processed and organized data.")

t("ICT-002",
  "Which of the following is a characteristic of analog data?",
  ["A. Represented by discrete values",
   "B. Can only take values of 0 and 1",
   "C. Continuously varying values",
   "D. Must be stored in binary"],
  "Analog data consists of continuously varying physical quantities that can take any value within a range. Unlike digital data, analog data is not represented by discrete binary values.",
  "1 mark: C. Analog data is continuously varying values.")

t("ICT-003",
  "Convert the decimal number 45 to binary. The result is:",
  ["A. 101101", "B. 110101", "C. 101111", "D. 111101"],
  "45₁₀ = 32+8+4+1 = 2⁵+2³+2²+2⁰ = 101101₂. Verify: 1×32+0×16+1×8+1×4+0×2+1×1 = 45. Using repeated division: 45÷2=22r1, 22÷2=11r0, 11÷2=5r1, 5÷2=2r1, 2÷2=1r0, 1÷2=0r1. Read remainders bottom-up: 101101₂.",
  "1 mark: A (101101₂). Must show correct decimal to binary conversion steps.")

t("ICT-004",
  "An uncompressed 1024×768 pixel 24-bit full-color bitmap image has a file size of approximately:",
  ["A. 2.25 MB", "B. 2.36 MB", "C. 18.87 MB", "D. 24.00 MB"],
  "File size = 1024×768×24 bits = 1024×768×3 bytes = 2,359,296 bytes ≈ 2.25 MB. Note: 24-bit = 3 bytes per pixel (8 bits = 1 byte), 1 MB = 1,048,576 bytes. Common mistake: forgetting to convert bits to bytes (divide by 8).",
  "1 mark: A. 1024×768×24/8/1024/1024 ≈ 2.25 MB. Must handle unit conversions correctly.")

t("ICT-005",
  "Which of the following is the main advantage of Unicode encoding?",
  ["A. Uses the least storage space",
   "B. Can represent characters from multiple languages",
   "C. Can only represent English letters and numbers",
   "D. Completely incompatible with ASCII"],
  "Unicode is an international character encoding standard capable of representing characters from virtually all languages (Chinese, Japanese, Korean, Arabic, etc.), solving ASCII's limitation of only 128 characters and Big-5's restriction to Traditional Chinese. UTF-8 is backward-compatible with ASCII (first 128 characters identical).",
  "1 mark: B. Unicode can represent characters from multiple languages for international encoding.")

# ==================== TOPIC 2: Information Processing II ====================
t("ICT-006",
  "Which file format is most suitable for storing images with transparent backgrounds?",
  ["A. JPEG", "B. BMP", "C. PNG", "D. GIF or PNG"],
  "Both PNG (Portable Network Graphics) and GIF (Graphics Interchange Format) support transparent backgrounds. JPEG does not support transparency. BMP typically does not support transparency. PNG supports full alpha channel transparency (256 levels), while GIF only supports 1-bit transparency (fully transparent or fully opaque).",
  "1 mark: D (GIF or PNG). Both formats support transparent backgrounds. JPEG does not support transparency.")

t("ICT-007",
  "A 3-minute stereo (dual-channel) audio file with a sampling rate of 44.1 kHz and 16-bit quantization per sample. The uncompressed file size is approximately:",
  ["A. 15.1 MB", "B. 30.3 MB", "C. 60.6 MB", "D. 121.2 MB"],
  "File size = sample rate × bits per sample × channels × time. 44,100 Hz × 16 bits × 2 channels × (3×60) seconds = 254,016,000 bits = 31,752,000 bytes ≈ 30.3 MB. Key points: convert minutes to seconds (×60), dual channel requires ×2.",
  "1 mark: B. 44,100×16×2×180/8/1024/1024 ≈ 30.3 MB. Must account for stereo (dual channel).")

t("ICT-008",
  "In a spreadsheet, cell A1=5, A2=3. The result of the formula =IF(A1>A2, A1*A2, A1+A2) is:",
  ["A. 8", "B. 15", "C. 2", "D. 5"],
  "IF function syntax: IF(condition, value_if_true, value_if_false). A1=5, A2=3. Condition A1>A2 (5>3) is TRUE, so result = A1*A2 = 5×3 = 15. If the condition were FALSE, result would be A1+A2 = 8.",
  "1 mark: B (15). IF condition is true, so multiplication is executed.")

t("ICT-009",
  "Convert the hexadecimal number 2F to decimal. The result is:",
  ["A. 37", "B. 42", "C. 47", "D. 52"],
  "2F₁₆ = 2×16¹ + F×16⁰ = 2×16 + 15×1 = 32 + 15 = 47₁₀. Note: F = 15 in hexadecimal. Conversion method: multiply each hex digit by the corresponding power of 16 (right to left, powers 0,1,2...), then sum.",
  "1 mark: C. 2F₁₆ = 2×16 + 15 = 47₁₀.")

t("ICT-010",
  "Which of the following comparisons between vector graphics and bitmap images is correct?",
  ["A. Vector graphics do not lose quality when enlarged; bitmaps appear pixelated when enlarged",
   "B. Vector graphics are suitable for storing photos; bitmaps are suitable for storing charts",
   "C. Vector graphics are always larger in file size than bitmaps",
   "D. Bitmaps are described using mathematical formulas"],
  "Vector graphics use mathematical formulas (points, lines, curves, polygons) to describe images, so they can be scaled infinitely without quality loss. Bitmaps are composed of pixels; enlarging them reveals pixelation/jagged edges. Vectors suit charts, logos, and fonts; bitmaps suit photos and complex images.",
  "1 mark: A. Vector graphics = mathematical description, infinitely scalable. Bitmaps = pixel-based, quality loss on enlargement.")

# ==================== TOPIC 3: Computer System Fundamentals ====================
t("ICT-011",
  "Which component of the CPU is responsible for performing arithmetic and logical operations?",
  ["A. Control Unit (CU)", "B. Arithmetic Logic Unit (ALU)",
   "C. Register", "D. Cache Memory"],
  "The ALU (Arithmetic Logic Unit) executes all arithmetic operations (addition, subtraction, multiplication, division) and logical operations (AND, OR, NOT, comparison) in the CPU. The CU (Control Unit) controls instruction fetch and decode, coordinating all components. Registers are high-speed temporary storage inside the CPU. Cache is a high-speed buffer between CPU and main memory.",
  "1 mark: B. ALU performs arithmetic and logical operations. CU handles control.")

t("ICT-012",
  "Which of the following correctly describes the difference between RAM and ROM?",
  ["A. Both RAM and ROM are volatile memory",
   "B. RAM is volatile memory, ROM is non-volatile memory",
   "C. RAM is non-volatile memory, ROM is volatile memory",
   "D. Both RAM and ROM are non-volatile memory"],
  "RAM (Random Access Memory) is volatile — data is lost when power is off. It temporarily stores running programs and data. ROM (Read-Only Memory) is non-volatile — data is retained when power is off. It stores firmware such as BIOS/UEFI needed at boot time. Cache memory is also volatile but faster and smaller than RAM.",
  "1 mark: B. RAM = volatile (data lost on power off), ROM = non-volatile (data retained).")

t("ICT-013",
  "Which of the following is a primary function of an Operating System?",
  ["A. Editing documents and creating presentations",
   "B. Managing computer hardware and software resources",
   "C. Designing websites and applications",
   "D. Storing user data and files"],
  "An operating system is system software that manages computer hardware and software resources. It provides a user interface, memory management, processor scheduling (multitasking), file system management, I/O management, and device driver management. Document editing is application software (e.g., Word).",
  "1 mark: B. The OS manages computer hardware and software resources.")

t("ICT-014",
  "Which of the following correctly describes Virtual Memory?",
  ["A. It is memory inside the CPU",
   "B. It uses hard disk space to simulate additional RAM",
   "C. Its access speed is faster than RAM",
   "D. It can only be used by the operating system, not applications"],
  "Virtual memory is an OS technique that uses hard disk space as an extension of RAM when physical RAM is insufficient. Temporarily unused data is moved from RAM to disk (paging/swapping), freeing RAM for other programs. Virtual memory is much slower than RAM (disk speed << RAM speed). All applications benefit from virtual memory.",
  "1 mark: B. Virtual memory uses hard disk space as an extension of RAM when RAM is insufficient.")

t("ICT-015",
  "Which of the following storage devices has the fastest access speed?",
  ["A. Hard Disk Drive (HDD)", "B. Solid State Drive (SSD)", "C. RAM", "D. Optical Disc (DVD)"],
  "Speed comparison: RAM (~10-100 ns) > SSD (~0.1 ms) > HDD (~5-10 ms) > Optical disc (~100 ms+). RAM is main memory communicating directly with the CPU, making it the fastest. SSDs use flash memory with no moving parts. HDDs require mechanical head movement and disk rotation. Optical discs are slowest.",
  "1 mark: C. RAM has the fastest access speed (nanosecond level). Order: RAM > SSD > HDD > Optical disc.")

# ==================== TOPIC 4: Internet and Applications I ====================
t("ICT-016",
  "What is the primary function of TCP in the TCP/IP protocol suite?",
  ["A. Delivering data packets from source to destination",
   "B. Ensuring reliable data delivery and error detection",
   "C. Converting domain names to IP addresses",
   "D. Encrypting network communication data"],
  "TCP (Transmission Control Protocol) is responsible for reliable data delivery: segmenting data, flow control, error detection and retransmission, and ensuring data arrives in order. IP (Internet Protocol) handles addressing and routing. DNS handles domain name resolution. SSL/TLS handles encryption.",
  "1 mark: B. TCP ensures reliable data delivery and error detection. IP handles addressing and routing.")

t("ICT-017",
  "Which of the following about IPv4 and IPv6 is correct?",
  ["A. IPv4 addresses are 64-bit; IPv6 addresses are 32-bit",
   "B. IPv4 uses hexadecimal notation; IPv6 uses decimal notation",
   "C. IPv6 can provide significantly more IP addresses than IPv4",
   "D. IPv6 transmission speed is always faster than IPv4"],
  "IPv4 uses 32-bit addresses (~4.3 billion), displayed in dotted decimal (e.g., 192.168.1.1). IPv6 uses 128-bit addresses (~3.4×10³⁸), displayed in colon-separated hexadecimal. IPv6 thus provides vastly more addresses, solving IPv4 exhaustion. IPv6 does not inherently guarantee faster speed — speed depends on network infrastructure.",
  "1 mark: C. IPv6 (128-bit) provides far more addresses than IPv4 (32-bit).")

t("ICT-018",
  "The primary function of DNS (Domain Name System) is:",
  ["A. Encrypting network communication",
   "B. Converting domain names to IP addresses",
   "C. Assigning IP addresses to devices",
   "D. Filtering spam emails"],
  "DNS acts like the internet's phone book, converting human-readable domain names (e.g., www.google.com) into machine-readable IP addresses (e.g., 142.250.80.4). When a user enters a domain name, the computer queries DNS servers for the corresponding IP address. DHCP assigns IP addresses. SSL/TLS handles encryption.",
  "1 mark: B. DNS converts domain names to IP addresses. DHCP assigns IP addresses.")

t("ICT-019",
  "What is the primary function of a Firewall?",
  ["A. Preventing all types of virus infections on the computer",
   "B. Controlling network traffic based on predefined rules",
   "C. Increasing internet connection speed",
   "D. Automatically backing up all data on the computer"],
  "A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. It can block unauthorized access but cannot prevent all viruses (requires antivirus software). Firewalls do not improve connection speed and do not handle data backup.",
  "1 mark: B. A firewall controls network traffic based on predefined rules. Cannot prevent all viruses.")

t("ICT-020",
  "What is the primary difference between LAN (Local Area Network) and WAN (Wide Area Network)?",
  ["A. LAN uses wireless connections; WAN uses wired connections",
   "B. LAN covers a small area; WAN covers a large area",
   "C. LAN transmission speed is always slower than WAN",
   "D. LAN is only for home use; WAN is only for enterprise use"],
  "LAN covers a small geographic area (a room, building, or campus), typically managed by a single organization. WAN covers a large area (city, country, or globally — the Internet is the largest WAN). LAN can use wired (Ethernet) or wireless (Wi-Fi). LAN speeds are typically faster than WAN.",
  "1 mark: B. LAN = small coverage (within building), WAN = large coverage (across cities/countries).")

t("ICT-021",
  "In a URL, 'https' indicates:",
  ["A. The website uses HTTP protocol to transmit hypertext",
   "B. The website uses HTTP encrypted by SSL/TLS",
   "C. The website has particularly fast transmission speed",
   "D. The website only supports text content"],
  "HTTPS (HTTP Secure) is the secure version of HTTP, encrypting data using SSL/TLS (Secure Sockets Layer/Transport Layer Security) protocols. HTTPS provides data encryption (prevents eavesdropping), authentication (verifies website identity via digital certificates), and data integrity (prevents tampering). A padlock icon appears in the browser address bar.",
  "1 mark: B. HTTPS = HTTP + SSL/TLS encryption. Provides confidentiality, integrity, and authentication.")

# ==================== TOPIC 5: Internet and Applications II ====================
t("ICT-022",
  "Which of the following correctly describes Cloud Computing?",
  ["A. All data must be stored on the user's local computer",
   "B. On-demand computing resources and services delivered over the internet",
   "C. Can only be used on a specific operating system",
   "D. Requires installation of specialized software to use"],
  "Cloud computing delivers on-demand computing resources and services over the internet (servers, storage, databases, networking, software, analytics, etc.), with users paying only for what they use. Service models: IaaS, PaaS, SaaS. Users can access via browser without installing dedicated software. Cross-platform support is a key feature.",
  "1 mark: B. Cloud computing provides on-demand computing resources and services via the internet.")

t("ICT-023",
  "Which of the following is an example of IoT (Internet of Things) application?",
  ["A. Using a spreadsheet for data analysis",
   "B. Smart home devices communicating and automating via the network",
   "C. Editing documents with word processing software",
   "D. Playing offline games on a local computer"],
  "IoT refers to physical devices embedded with sensors, software, and other technologies that connect and exchange data over the internet. Smart homes (smart thermostats, lights, locks, voice assistants) are typical IoT applications. Other examples: smartwatches, smart cities (traffic management), industrial IoT (predictive maintenance).",
  "1 mark: B. IoT = interconnected smart devices communicating and automating over networks.")

t("ICT-024",
  "The full name of HTML is:",
  ["A. HyperText Markup Language",
   "B. High Technology Modern Language",
   "C. HyperText Modern Language",
   "D. High Tech Markup Language"],
  "HTML (HyperText Markup Language) is the standard markup language for creating web pages. It uses tags to define web page structure and content (headings, paragraphs, images, links, etc.). HTML is not a programming language — it is a markup language that marks up the structure and meaning of content.",
  "1 mark: A. HTML = HyperText Markup Language.")

t("ICT-025",
  "Which of the following is a characteristic of Public Key Encryption?",
  ["A. Encryption and decryption use the same key",
   "B. Uses a key pair: public key for encryption, private key for decryption",
   "C. Anyone can decrypt any message with the private key",
   "D. The encryption process requires no keys"],
  "Public key encryption (asymmetric encryption) uses a mathematically related key pair: a public key (can be openly shared) for encryption, and a private key (must be kept secret) for decryption. Anyone can encrypt with the recipient's public key, but only the holder of the corresponding private key can decrypt. SSL/TLS uses public-key encryption for initial key exchange.",
  "1 mark: B. Public key encryption uses a key pair: public key encrypts, private key decrypts.")

t("ICT-066",
  "Which of the following correctly describes Two-Factor Authentication (2FA)?",
  ["A. Using two identical passwords to log in",
   "B. Combining a password (something you know) with a phone verification code (something you have) for authentication",
   "C. Two people logging into the same account simultaneously",
   "D. Entering the password twice for confirmation"],
  "2FA requires two different types of authentication factors: (1) Something you know (password, PIN), (2) Something you have (phone, security token, smart card), (3) Something you are (fingerprint, facial recognition). Combining two factors greatly improves security — even if a password is stolen, attackers cannot pass the second factor.",
  "1 mark: B. 2FA = two different types of authentication factors. Common: password + phone verification code.")

# ==================== TOPIC 6: Computational Thinking and Programming I ====================
t("ICT-026",
  "Which of the following is a core element of Computational Thinking?",
  ["A. Rote memorization and repetitive practice",
   "B. Abstraction, algorithm design, and automation",
   "C. Using computers only for calculations",
   "D. Learning multiple programming languages"],
  "Computational thinking is a problem-solving approach with these core elements: Abstraction — extracting key information while ignoring irrelevant details; Algorithm Design — designing step-by-step solutions; Automation — using computers to automatically execute repetitive tasks. It is a universal problem-solving method not limited to programming.",
  "1 mark: B. Core elements of computational thinking: abstraction, algorithm design, and automation.")

t("ICT-027",
  "Which flowchart symbol represents a decision/condition?",
  ["A. Rectangle", "B. Diamond", "C. Oval", "D. Parallelogram"],
  "Standard flowchart symbols: Oval/Rounded rectangle = Start/End; Rectangle = Process/Operation; Diamond = Decision/Condition (typically Yes/No branches); Parallelogram = Input/Output; Arrows = Flow direction. The diamond is the only symbol with two exits (TRUE/FALSE).",
  "1 mark: B. Diamond = decision/condition. Rectangle = process, Oval = start/end, Parallelogram = I/O.")

t("ICT-028",
  "In programming, a 'variable' is used for:",
  ["A. Permanently storing data on the hard disk",
   "B. Temporarily storing data in memory, with values that can change",
   "C. Storing only numeric data",
   "D. Ensuring programs never have errors"],
  "A variable is a fundamental programming concept used to temporarily store data in memory, with values that can change during program execution. Variables can store different data types: integers, floats, strings, booleans, etc. Variables are stored in RAM, not hard disk. Using variables does not prevent all errors.",
  "1 mark: B. Variables store data temporarily in memory; their values can change. Supports multiple data types.")

t("ICT-029",
  "After executing the following pseudocode, what is the value of sum?\nsum = 0\nfor i = 1 to 5\n  if i mod 2 = 0 then\n    sum = sum + i\n  endif\nnext i",
  ["A. 6", "B. 9", "C. 15", "D. 10"],
  "Pseudocode trace: i=1: 1 mod 2 = 1 ≠ 0, skip, sum=0; i=2: 2 mod 2 = 0, sum=0+2=2; i=3: skip, sum=2; i=4: 4 mod 2 = 0, sum=2+4=6; i=5: skip, sum=6. Final sum = 6, which is the sum of all even numbers from 1 to 5 (2+4). 'mod' is the modulo (remainder) operator.",
  "1 mark: A (6). The program sums all even numbers from 1 to 5: 2+4=6.")

t("ICT-030",
  "Which control structure is used to repeatedly execute a group of instructions?",
  ["A. Sequence", "B. Selection (If-else)", "C. Iteration (Loop)", "D. Jump (Goto)"],
  "The three fundamental control structures in programming: (1) Sequence — instructions execute in order line by line; (2) Selection — different branches execute based on conditions (if-else, switch-case); (3) Iteration — a group of instructions executes repeatedly until a condition is met (for loop, while loop, do-while). Iteration handles repetitive tasks.",
  "1 mark: C. Iteration (for/while loops) is used to repeatedly execute instructions.")

t("ICT-056",
  "In the flowchart: Start → Input x → x>10? → (Yes) Output 'High' / (No) x>5? → (Yes) Output 'Medium' / (No) Output 'Low' → End\nIf x=8, the output is:",
  ["A. High", "B. Medium", "C. Low", "D. No output"],
  "Trace: x=8 → Check x>10? → 8>10 is No → Check x>5? → 8>5 is Yes → Output 'Medium'. This is a typical nested decision structure for categorizing values by ranges.",
  "1 mark: B (Medium). x=8 does not satisfy >10, does satisfy >5, outputs Medium.")

t("ICT-057",
  "After executing the following pseudocode, what is the value of count?\ncount = 0\nfor i = 1 to 10\n  if i mod 2 = 0 OR i mod 3 = 0 then\n    count = count + 1\n  endif\nnext i",
  ["A. 5", "B. 6", "C. 7", "D. 8"],
  "Numbers 1-10 satisfying i mod 2=0 (even) OR i mod 3=0 (multiple of 3): 2✓(even), 3✓(multiple of 3), 4✓(even), 6✓(both, OR counts once), 8✓(even), 9✓(multiple of 3), 10✓(even). Total: 7 numbers. Note: 6 satisfies both conditions but is counted only once (OR logic).",
  "1 mark: C (7). Numbers that are even OR multiples of 3: 2,3,4,6,8,9,10.")

t("ICT-058",
  "What is the primary purpose of Pseudocode?",
  ["A. Direct execution on a computer",
   "B. Describing algorithm logic in a human-readable way, independent of specific programming languages",
   "C. Replacing all programming languages",
   "D. Encrypting source code to protect intellectual property"],
  "Pseudocode uses natural language and basic program structures (if-then, for, while) to describe algorithm logic, unrestricted by specific programming language syntax. It is used for planning and communicating algorithm design before writing actual code. Pseudocode cannot be directly executed on a computer.",
  "1 mark: B. Pseudocode describes algorithm logic in natural language for planning and communication.")

# ==================== TOPIC 7: Computational Thinking and Programming II ====================
t("ICT-031",
  "In programming, the main benefit of decomposing a program into multiple functions/procedures is:",
  ["A. Increasing program execution speed",
   "B. Improving program readability and maintainability",
   "C. Reducing memory usage",
   "D. Making the program run only on specific platforms"],
  "Modular programming (decomposing into functions/procedures) improves readability (each function has a clear purpose), maintainability (changing one function doesn't affect others), reusability (functions can be called from multiple places), easier debugging (test each function independently), and team collaboration (different people handle different modules).",
  "1 mark: B. Modularization improves readability, maintainability, and reusability.")

t("ICT-032",
  "Which of the following correctly describes an Array?",
  ["A. A variable that can only store a single value",
   "B. A collection that can store multiple elements of the same data type",
   "C. A technique for file input/output",
   "D. Another name for a programming language"],
  "An array is a data structure that stores multiple elements of the same type in contiguous memory locations, accessed by index (starting from 0). Example: score[0]=85, score[1]=92, score[2]=78. Advantages: manage related data with one variable name, convenient processing via loops, random access (O(1) time complexity).",
  "1 mark: B. An array stores multiple elements of the same type, accessed by index.")

t("ICT-033",
  "What is the purpose of Boundary Value Testing in program testing?",
  ["A. Testing program behavior under all possible inputs",
   "B. Testing program behavior at the boundaries of valid input ranges",
   "C. Testing program behavior with random inputs",
   "D. Testing only with normal, expected inputs"],
  "Boundary value testing is a black-box testing technique focusing on boundary values of input ranges (minimum, maximum, just below minimum, just above maximum), because errors often occur at boundaries. Example: if a program accepts input 1-100, test 0 (below), 1 (lower bound), 100 (upper bound), 101 (above).",
  "1 mark: B. Boundary value testing focuses on testing program behavior at the edges of input ranges.")

t("ICT-034",
  "What is the primary purpose of program documentation?",
  ["A. Increasing program execution speed",
   "B. Helping other programmers understand and maintain the program",
   "C. Reducing program file size",
   "D. Converting the program to another programming language"],
  "Program documentation describes the program's function, structure, and usage. Purposes include: helping other programmers understand logic, facilitating maintenance and updates, recording design decisions, and serving as a user manual. Good documentation includes code comments, API docs, user manuals, and design documents.",
  "1 mark: B. Documentation helps understand and maintain programs.")

t("ICT-059",
  "In programming, what is the main difference between a Function and a Procedure?",
  ["A. A function returns a value; a procedure does not return a value",
   "B. A function can have multiple parameters; a procedure can only have one",
   "C. Functions execute faster than procedures",
   "D. Procedures can only be called from the main program; functions can be called from anywhere"],
  "A function performs calculations and returns a value (e.g., sqrt, sum). A procedure/subroutine performs a series of operations without returning a value (e.g., display message, print file). In many modern languages, 'function' is used generically. Both can accept parameters and be called from anywhere.",
  "1 mark: A. A function returns a value; a procedure does not. This is the fundamental difference.")

t("ICT-060",
  "After executing the following code, what is the array arr?\narr = [3,1,4,1,5]\nfor i = 0 to 3\n  for j = 0 to 3-i\n    if arr[j] > arr[j+1] then swap\n[Standard bubble sort implementation]",
  ["A. [5,4,3,1,1]", "B. [1,1,3,4,5]", "C. [3,1,4,1,5]", "D. [1,3,1,4,5]"],
  "This is a bubble sort algorithm that sorts the array in ascending order. Original [3,1,4,1,5] becomes [1,1,3,4,5] after a complete bubble sort. Bubble sort repeatedly compares adjacent elements and swaps them, with the largest unsorted element 'bubbling' to the end in each pass.",
  "1 mark: B [1,1,3,4,5]. Bubble sort produces ascending order. Understanding sorting algorithm processes is important.")

t("ICT-061",
  "Which of the following is a good programming practice?",
  ["A. Using meaningless variable names (e.g., a, b, x1, x2)",
   "B. Writing clear comments to explain complex logic",
   "C. Putting all code into one large function",
   "D. Not performing any testing"],
  "Good programming practices: using meaningful variable names (e.g., studentScore not x), writing clear comments, modular design (decomposing into small functions), thorough testing (including boundary testing), consistent coding style, and version control. These improve readability, maintainability, and reliability.",
  "1 mark: B. Clear comments are good practice. Meaningful names, modularization, and testing are also important.")

# ==================== TOPIC 8: Social Implications ====================
t("ICT-035",
  "Which of the following is a positive impact of ICT on education?",
  ["A. Completely replacing the role of traditional teachers",
   "B. Providing online learning platforms, increasing accessibility of learning resources",
   "C. Ensuring all students achieve excellent results",
   "D. Reducing student social interaction to zero"],
  "Positive ICT impacts on education: online learning platforms (Moodle, Google Classroom) enabling anytime/anywhere access; multimedia teaching (videos, animations, simulations) improving engagement; instant communication tools facilitating teacher-student interaction; AI-assisted personalized learning. ICT cannot fully replace teachers who provide guidance, motivation, and emotional support.",
  "1 mark: B. ICT provides online learning platforms, increasing accessibility and flexibility of learning resources.")

t("ICT-036",
  "Which of the following is the correct definition of the Digital Divide?",
  ["A. Differences between programming languages",
   "B. The gap in ICT resource access and usage between different regions or communities",
   "C. Incompatibility issues between hardware and software",
   "D. Technical limitations of internet speed"],
  "The digital divide refers to the gap between different regions, socioeconomic classes, age groups, and education levels in accessing and using ICT. This gap manifests in: hardware access (computers, smartphones), internet access (broadband/mobile), digital skills, and digital literacy. The digital divide may exacerbate social inequality.",
  "1 mark: B. The digital divide is the gap in ICT resource access and usage between different communities.")

t("ICT-037",
  "What is the primary subject protected by Intellectual Property rights?",
  ["A. Physical items such as computer hardware",
   "B. Creative and intellectual works such as software, music, and literary works",
   "C. Natural resources such as water and air",
   "D. Free resources in the public domain"],
  "Intellectual property protects creators' intellectual and creative works including: Copyright (literary, musical, artistic works, software source code), Patents (inventions and technical innovations), Trademarks (brand names and logos), Trade Secrets. In ICT, software is protected by copyright, unique algorithms can be patented, and brand names can be trademarked.",
  "1 mark: B. Intellectual property protects intellectual creations including software, music, and literary works.")

t("ICT-038",
  "Which of the following is a characteristic of Open Source Software?",
  ["A. Must pay a fee to use it",
   "B. Source code is publicly available; users can freely modify and distribute",
   "C. Cannot be used together with other software",
   "D. Only the original author can use it"],
  "Open source software characteristics: source code is publicly available (anyone can view), free modification (users can modify code for their needs), free distribution (can share with others), usually free of charge. Common licenses: GPL (modifications must also be open source), MIT (very permissive, can be used in commercial software), Apache (includes patent grant).",
  "1 mark: B. Open source software has publicly available source code; users can freely modify and distribute.")

t("ICT-039",
  "Which of the following is NOT a health issue caused by prolonged computer use?",
  ["A. Repetitive Strain Injury (RSI)",
   "B. Eye strain and vision problems",
   "C. Improved body flexibility",
   "D. Neck and back pain"],
  "Health issues from prolonged computer use: Repetitive Strain Injury (RSI — wrist/hand damage from repetitive motions like carpal tunnel syndrome), eye strain (blurred vision, dry eyes from staring at screens), neck and back pain (poor posture and prolonged sitting). Improved body flexibility is a positive effect from proper exercise, not a health issue from computer use.",
  "1 mark: C. Improved body flexibility is NOT a health issue from computer use. RSI, eye strain, and neck/back pain are.")

t("ICT-040",
  "Which of the following is an effective method to protect online privacy?",
  ["A. Using the same password on all websites",
   "B. Regularly clearing browser history and cookies",
   "C. Publicly sharing all personal information on social media",
   "D. Disabling all security software for faster browsing"],
  "Effective methods for online privacy: regularly clearing browser history and cookies (reducing tracking), using strong unique passwords for each site, limiting personal information shared on social media, using VPNs to encrypt traffic, enabling two-factor authentication (2FA), and keeping software updated. Using the same password everywhere is a major security risk.",
  "1 mark: B. Regularly clearing browser history and cookies helps protect online privacy.")

t("ICT-062",
  "Which of the following is a characteristic of the GPL open source license?",
  ["A. Allows users to modify source code but prohibits distribution",
   "B. Modified derivative works must also be released under the GPL license",
   "C. Can only be used for non-commercial purposes",
   "D. Does not allow anyone to view the source code"],
  "The GPL (GNU General Public License)'s core feature is 'Copyleft' — when you modify GPL-licensed software, your derivative work must also be released under the GPL license. This ensures the software and its derivatives remain perpetually open source. MIT license is more permissive. GPL allows commercial use and source code viewing.",
  "1 mark: B. GPL's core is Copyleft: derivative works must also use GPL licensing.")

t("ICT-063",
  "The '20-20-20 rule' is used to prevent which of the following caused by prolonged computer use?",
  ["A. Repetitive Strain Injury (RSI)",
   "B. Computer viruses",
   "C. Eye strain",
   "D. Network attacks"],
  "The '20-20-20 rule' recommends: Every 20 minutes of computer use, look at something 20 feet (~6 meters) away for at least 20 seconds. This reduces eye strain and digital eye fatigue from prolonged screen focus. RSI prevention requires regular breaks and proper wrist posture. Virus prevention requires antivirus software.",
  "1 mark: C. The 20-20-20 rule (every 20 min, look 20 ft away for 20 sec) prevents eye strain.")

t("ICT-064",
  "Which of the following is an effective method to reduce the Digital Divide?",
  ["A. Increasing internet service prices",
   "B. Providing free computers and internet access in public libraries and community centers",
   "C. Only providing high-speed internet in urban areas",
   "D. Reducing ICT courses in schools"],
  "Strategies to reduce the digital divide: providing free computers and internet access in public spaces, building network infrastructure in remote areas, offering digital skills training programs, providing computer/internet subsidies for low-income families, and developing simplified interfaces for the elderly. Higher prices and reduced coverage only worsen the divide.",
  "1 mark: B. Free public access to computers and internet is an effective method to reduce the digital divide.")

# ==================== Remaining questions ====================
t("ICT-041",
  "In an information system, which of the following belongs to the 'hardware' category?",
  ["A. Operating system", "B. Database management system", "C. Central Processing Unit (CPU)", "D. User manual"],
  "The CPU is a physical electronic component and belongs to hardware. Operating systems (A) and DBMS (B) are software. User manuals (D) are procedures/documentation. The five components of an information system: hardware, software, data, people, and procedures.",
  "1 mark: C. CPU is hardware. Distinguish hardware (physical devices) from software (programs and instructions).")

t("ICT-042",
  "Which of the following correctly compares Direct Access and Sequential Access?",
  ["A. Hard disks use sequential access; magnetic tapes use direct access",
   "B. Direct access can immediately read data at any location; sequential access must start from the beginning",
   "C. Sequential access is always faster than direct access",
   "D. RAM uses sequential access"],
  "Direct access (random access) allows jumping directly to any data location without traversing preceding data (e.g., HDD, SSD, RAM). Sequential access must read data from the beginning until the target is found (e.g., magnetic tape). HDDs use direct access (A wrong), sequential is usually slower (C wrong), RAM uses direct access (D wrong).",
  "1 mark: B. Direct access = instant data location; sequential = must start from beginning. Tape=sequential, HDD/SSD/RAM=direct.")

t("ICT-043",
  "Range Check in data validation is used for:",
  ["A. Checking if data is within an allowed range",
   "B. Checking if the data type is correct",
   "C. Checking if data is duplicated",
   "D. Checking if data is encrypted"],
  "Range check verifies that input data falls within a predefined reasonable range. Example: age should be 0-150, exam scores should be 0-100. Range checking is one of the most common data validation methods, preventing obvious input errors. Type check (B) verifies data type (e.g., number vs text).",
  "1 mark: A. Range check ensures data is within a reasonable range. Example: 0 ≤ age ≤ 150.")

t("ICT-044",
  "Which of the following correctly compares JPEG and PNG file formats?",
  ["A. JPEG uses lossless compression; PNG uses lossy compression",
   "B. JPEG supports transparent backgrounds; PNG does not support transparency",
   "C. JPEG is suitable for photos; PNG supports transparency and uses lossless compression",
   "D. JPEG and PNG use the same compression algorithm"],
  "JPEG uses lossy compression (discards some image data to reduce file size), ideal for photos and images with rich gradients. PNG uses lossless compression (preserves all image data), supports alpha channel transparency, ideal for logos, charts, and images needing sharp edges and transparency. JPEG does not support transparency.",
  "1 mark: C. JPEG = lossy, good for photos; PNG = lossless, supports transparency.")

t("ICT-045",
  "A 5-minute mono audio file, sampled at 22.05 kHz with 8-bit quantization. The uncompressed file size is approximately:",
  ["A. 1.26 MB", "B. 6.62 MB", "C. 13.23 MB", "D. 52.92 MB"],
  "File size = sample rate × bit depth × channels × time. 22,050 Hz × 8 bits × 1 channel × (5×60) seconds = 22,050 × 8 × 300 = 52,920,000 bits ≈ 6.62 MB. Note: single channel (×1, not ×2). Unit conversions are critical.",
  "1 mark: B. 22,050×8×1×300/8/1024/1024 ≈ 6.3 MB. Note this is mono (single channel).")

t("ICT-046",
  "In a spreadsheet, to calculate the sum of values in cells A1 to A10, which function should be used?",
  ["A. =AVERAGE(A1:A10)", "B. =COUNT(A1:A10)", "C. =SUM(A1:A10)", "D. =MAX(A1:A10)"],
  "SUM calculates the total of all numeric values in a range. AVERAGE calculates the mean. COUNT counts the number of cells containing numbers. MAX returns the largest value. These are the most basic spreadsheet functions.",
  "1 mark: C. SUM() adds values. AVERAGE=mean, COUNT=count cells, MAX=largest value.")

t("ICT-047",
  "What is a key characteristic of a GPU (Graphics Processing Unit)?",
  ["A. Can only process text data",
   "B. Has many cores, optimized for parallel processing of graphics and image data",
   "C. Much slower than a CPU",
   "D. Specifically designed for managing network connections"],
  "A GPU has hundreds to thousands of small processing cores designed for parallel processing, particularly suited for graphics rendering, image processing, machine learning, and other tasks requiring massive parallel computation. GPUs complement CPUs (fewer high-performance cores, optimized for sequential processing). Modern GPUs are also used for cryptocurrency mining and AI training.",
  "1 mark: B. GPU has many cores optimized for parallel processing. CPU=few strong cores, GPU=many small cores.")

t("ICT-048",
  "Which of the following correctly describes the Bus System?",
  ["A. A type of operating system",
   "B. Communication channels between the CPU and other components for transmitting data",
   "C. A network communication protocol",
   "D. A database management system"],
  "The bus system consists of communication channels connecting the CPU to other computer components: Data bus (transmits data), Address bus (transmits memory addresses), Control bus (transmits control signals). Bus width (in bits) affects system performance — wider buses can transfer more data per cycle.",
  "1 mark: B. The bus system is the communication channel between CPU and components. Three types: data, address, control.")

t("ICT-049",
  "Which of the following correctly describes Distributed Processing?",
  ["A. All processing must be completed on a single computer",
   "B. Multiple computers collaborate over a network to complete a shared task",
   "C. Only identical computer models can be used",
   "D. Does not require operating system support"],
  "Distributed processing breaks large tasks into subtasks, distributes them to multiple computers on a network for parallel processing, then combines the results. Advantages: improved speed, higher reliability (single point of failure doesn't affect everything), resource sharing, scalability. Examples: SETI@home, blockchain networks, cloud computing.",
  "1 mark: B. Distributed processing = multiple computers collaborating via network. Distinct from parallel processing (multiple CPUs in one machine).")

t("ICT-050",
  "Which network device primarily forwards data based on MAC addresses?",
  ["A. Router", "B. Switch", "C. Modem", "D. Firewall"],
  "A Switch operates at the Data Link layer (Layer 2) of the OSI model, forwarding data frames based on MAC addresses to specific ports. A Router operates at the Network layer (Layer 3), forwarding data packets based on IP addresses. A Modem handles analog-digital signal conversion. A Firewall filters traffic based on security rules.",
  "1 mark: B. Switch uses MAC addresses (Layer 2); Router uses IP addresses (Layer 3).")

t("ICT-051",
  "Which of the following correctly describes the difference between Circuit Switching and Packet Switching?",
  ["A. Circuit switching establishes a dedicated channel; packet switching divides data into small packets sent independently",
   "B. The internet uses circuit switching technology",
   "C. Packet switching requires establishing a dedicated connection before communication",
   "D. Circuit switching is more suitable for bursty data transmission than packet switching"],
  "Circuit switching establishes a dedicated physical channel before communication (e.g., traditional telephone networks); the channel is exclusively occupied during communication, suitable for continuous communication (voice calls). Packet switching divides data into small packets, each independently routed (e.g., internet using TCP/IP), suitable for bursty data. Internet uses packet switching (B wrong).",
  "1 mark: A. Circuit switching = dedicated channel (telephone); Packet switching = packet-based transmission (internet TCP/IP).")

t("ICT-052",
  "How many bits are used to represent an IPv4 address?",
  ["A. 16 bits", "B. 32 bits", "C. 64 bits", "D. 128 bits"],
  "IPv4 addresses use 32 bits (4 bytes), displayed in dotted decimal notation (e.g., 192.168.1.1). This provides approximately 4.3 billion unique addresses. As internet devices far exceed 4.3 billion, IPv4 addresses are largely exhausted. IPv6 uses 128 bits (16 bytes), providing 2¹²⁸ addresses.",
  "1 mark: B. IPv4 = 32 bits (~4.3 billion addresses); IPv6 = 128 bits.")

t("ICT-053",
  "Which of the following is a typical example of SaaS (Software as a Service)?",
  ["A. Installing Microsoft Word locally",
   "B. Using Google Docs to edit documents through a browser",
   "C. Purchasing and installing the Windows operating system",
   "D. Setting up your own email server"],
  "SaaS (Software as a Service) lets users use software via the internet without installation or maintenance. Google Docs is typical SaaS — users only need a browser to edit documents; all processing and storage happen in the cloud. Installing Word locally (A) is traditional software. Buying Windows (C) is licensing, not service. Self-hosting email (D) is IaaS or self-managed.",
  "1 mark: B. SaaS = using cloud software through a browser. Google Docs, Office 365, Gmail are SaaS examples.")

t("ICT-054",
  "Which of the following about SSL/TLS and HTTPS is correct?",
  ["A. HTTPS uses symmetric encryption for the initial connection",
   "B. SSL/TLS first uses public-key encryption to exchange a symmetric key, then uses symmetric encryption for data transmission",
   "C. HTTPS cannot verify a website's identity",
   "D. SSL/TLS only protects text data, not images and videos"],
  "SSL/TLS operation: (1) Client and server use public-key (asymmetric) encryption to securely exchange a symmetric key; (2) Subsequent data transmission uses this symmetric key (faster). HTTPS = HTTP + SSL/TLS. Digital certificates verify website identity (C wrong). SSL/TLS encrypts all data types (D wrong).",
  "1 mark: B. SSL/TLS uses asymmetric encryption to exchange the symmetric key, then symmetric encryption for data. Hybrid cryptosystem.")

t("ICT-055",
  "Which HTML tag is used to create a hyperlink?",
  ["A. <img>", "B. <a>", "C. <p>", "D. <div>"],
  "The <a> (anchor) tag creates hyperlinks, using the href attribute to specify the target URL. Example: <a href='https://example.com'>Click here</a>. <img> inserts images, <p> defines paragraphs, <div> defines block-level divisions.",
  "1 mark: B. <a href='...'> is the HTML hyperlink tag.")

t("ICT-065",
  "Which of the following is a characteristic of the Client-Server network architecture?",
  ["A. All computers have exactly equal status",
   "B. Servers provide resources and services; clients send requests and receive services",
   "C. Does not require a network connection",
   "D. Can only be used on the internet, not on a LAN"],
  "In client-server architecture, servers centrally manage resources and provide services (file servers, web servers, database servers). Clients send requests to servers and receive responses. Unlike peer-to-peer (P2P) where all computers are equal (A wrong). This architecture requires network connection (C wrong) and can be used on both LAN and internet (D wrong).",
  "1 mark: B. Servers provide services; clients request services. Distinct from P2P architecture.")

# ==================== Apply translations ====================
count = 0
for q in questions:
    qid = q.get('qid')
    if qid in en:
        q['question_en'] = en[qid]['question_en']
        q['options_en'] = en[qid]['options_en']
        q['explanation_en'] = en[qid]['explanation_en']
        q['markingNotes_en'] = en[qid]['markingNotes_en']
        count += 1

# Save
with open(DST, 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Translated {count}/{len(questions)} questions to English")
print(f"Saved to {DST}")
