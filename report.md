## Project: Network Reconnaissance Lab

### Objective
Perform network reconnaissance on a publicly available test host to identify open ports, running services, and potential security risks.

### Target
scanme.nmap.org

### Tools Used
- Nmap
- macOS Terminal
- VS Code

### Commands Executed
```bash
nmap -A scanme.nmap.org
```

### Findings
- Port 22 (SSH) open
- Port 80 (HTTP) open
- Linux-based system detected
- Service versions exposed

### Security Risks
SSH:
- Brute force login attempts possible
- Remote access exposure

HTTP:
- Unencrypted traffic
- Vulnerable to interception (MITM attacks)

### Attacker Perspective
An attacker could scan open ports, identify service versions, and search for known exploits.

### Defensive Recommendations
- Restrict SSH access
- Use key-based authentication
- Disable unused services
- Upgrade outdated software

### What I Learned
- How to run Nmap scans
- How to identify open ports
- How attackers view exposed systems
- How to document security findings

### Analyst Summary
- This scan demonstrates basic external reconnaissance techniques used in cybersecurity assessments. The target system exposes multiple services that increase its attack surface, requiring proper hardening and monitoring.