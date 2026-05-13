import pandas as pd
import re

def parse_logs(log_text):

    logs = log_text.split("\n")

    parsed_data = []

    for log in logs:

        if log.strip() == "":
            continue

        # Extract IP Address
        ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', log)

        ip_address = ip_match.group(1) if ip_match else "Unknown"

        # Detect Threat Type
        if "Failed login" in log:
            threat_type = "Failed Login"

        elif "SQL Injection" in log:
            threat_type = "SQL Injection"

        elif "Malware" in log:
            threat_type = "Malware"

        elif "Brute force" in log:
            threat_type = "Brute Force"

        else:
            threat_type = "Normal Activity"

        parsed_data.append({
            "Log": log,
            "IP Address": ip_address,
            "Threat Type": threat_type
        })

    return pd.DataFrame(parsed_data)