# Security Tools

A collection of Python-based cybersecurity tools built during a structured security learning programme as part of a BSc Cyber Security degree at Birmingham City University.

## Tools

### Port Scanner
Multithreaded network port scanner built using Python sockets. Scans a target IP across a list of ports and identifies which ones are open. Includes timeout handling and clean output formatting.

### Password Auditor
Analyses password strength against four criteria — minimum length, uppercase letters, digits and special characters. Returns a strength rating from Weak to Very Strong.

### IP Threat Tracker
Hash map based threat tracker that stores suspicious IP addresses and their associated threat types. Supports O(1) lookup, addition, deletion and display of tracked threats.

### SOC Alert Triage System
Simulates a Security Operations Centre alert management system. Logs security alerts with auto-generated IDs, severity levels and status. Supports adding, viewing, closing and filtering critical alerts — the same workflow a junior SOC analyst would follow.

### IP Blocklist with Binary Search
Maintains a sorted list of blocked IP addresses and uses binary search (O(log n)) for fast lookups. Includes automatic numerical sorting of IP addresses.

## Legal notice
All tools are for educational purposes and authorised testing only.

## Tech stack
Python 3 · Git
