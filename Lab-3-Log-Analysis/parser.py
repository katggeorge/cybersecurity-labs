from collections import Counter

log_file = "logs/auth.log"

failed_ips = []

with open(log_file, "r") as file:
    for line in file:
        if "Failed login" in line:
            ip = line.strip().split()[-1]
            failed_ips.append(ip)

ip_counts = Counter(failed_ips)

print("\nSuspicious Failed Login Attempts:\n")

for ip, count in ip_counts.items():
    print(f"{ip} -> {count} failed attempts")

print("\nAnalysis Complete.")