# Python Log Analysis Report

## Objective
Analyze authentication logs for suspicious failed login activity.

---

## Detection Logic
The Python script scans authentication logs and identifies repeated failed login attempts from source IP addresses.

---

## Findings

| IP Address | Failed Attempts |
|---|---|
| 185.220.101.1 | 2 |
| 45.33.32.156 | 3 |
| 103.24.77.91 | 1 |

---

## Security Observations
- Repeated failed logins may indicate brute-force attempts
- Multiple failures from the same IP should trigger monitoring
- Authentication logs are critical for threat detection

---

## Analyst Perspective
A SOC analyst would investigate:
- geolocation of suspicious IPs
- frequency of login attempts
- whether successful logins followed failures

---

## Defensive Recommendations
- Enable MFA
- Rate-limit login attempts
- Monitor authentication logs continuously
- Block repeated malicious IPs

---

## What I Learned
- How to parse logs using Python
- How failed login detection works
- How analysts identify suspicious authentication behavior