# Home Network Mapping Report

## Objective
Identify devices connected to a local home network and analyze potential security exposure from visible internal assets.

---

## Tools Used
- Nmap
- macOS Terminal
- VS Code

---

## Command Executed

```bash
nmap -sn 192.168.1.0/24
```

---

## Devices Identified

| Device | IP Address | Notes |
|---|---|---|
| Verizon FiOS Router | 192.168.1.1 | Primary gateway/router |
| E3200 Extender | 192.168.1.102 | Wi-Fi network extender |
| Sensi Devices | 192.168.1.151 / .152 / .231 | Smart thermostat / IoT devices |
| HP Devices | 192.168.1.179 / .191 | End-user systems |
| Denon AVR Receiver | 192.168.1.193 | Smart entertainment device |
| Mac | 192.168.1.243 | Analyst workstation |

---

## Security Observations

- Multiple IoT devices are present on the network
- Smart devices may introduce additional attack surface
- Internal devices are discoverable through network enumeration
- Home networks often lack segmentation between IoT and primary systems

---

## Attacker Perspective

An attacker with local network access could:
- Enumerate connected devices
- Identify potential weak IoT targets
- Pivot laterally between devices
- Attempt credential attacks against exposed systems

---

## Defensive Recommendations

- Enable WPA2/WPA3 encryption
- Change default router credentials
- Regularly update IoT firmware
- Segment IoT devices onto separate networks if possible
- Monitor unknown devices connected to the network

---

## What I Learned

- How to identify devices on a local network
- How attackers perform internal reconnaissance
- How IoT devices increase attack surface
- How to document network visibility findings professionally

---

## Analyst Summary

This lab demonstrates foundational internal reconnaissance techniques used in cybersecurity operations and network visibility assessments. Mapping connected devices helps identify unmanaged assets and evaluate potential internal security risks.