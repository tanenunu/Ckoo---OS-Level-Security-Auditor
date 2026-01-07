# TODO: Support allowlists / negative patterns to reduce false positives


REGISTRY = [
    {
        "name" : "Open Network Ports",
        "commands" : {
            "Darwin" : "netstat -an",
            "Windows" : "netstat -an"
        },
        "description" : "Lists all active network connections and listening ports",
        "risk_patterns" : [
            {
                "pattern" : "LISTEN",
                "match_any": False,
                "reason" : "Open ports with LISTEN enabled",
                "severity" : "Medium",
                "checked" : False,
                "occurrences" : 0,
                "logged_occurrences" : []
            }
        ]
     },
     {
         "name" : "Running Processes",
         "commands" : {
             "Darwin" : "ps aux",
             "Windows" : "tasklist"
         },
         "description" : "Lists all running processes",
        "risk_patterns" : [
            {
                "pattern" : "root",
                "match_any": False,
                "reason" : "Process running with elevated privileges",
                "severity" : "Medium",
                "checked" : False,
                "occurrences" : 0,
                "logged_occurrences" : []
            },
            {
                "pattern": "SYSTEM",
                "match_any": False,
                "reason": "Process running as SYSTEM account",
                "severity": "Medium",
                "checked": False,
                "occurrences": 0,
                "logged_occurrences": []
            }
            
        ]
    },
    {
        "name": "Startup Persistence",
        "commands": {
            "Darwin": "ls /Library/LaunchAgents /Library/LaunchDaemons ~/Library/LaunchAgents 2>/dev/null",
            "Windows": "schtasks"
        },
        "description": "Detects programs configured to run at startup",
        "risk_patterns": [
            {
                "pattern": ".plist",
                "match_any": False,
                "reason": "Startup launch agent or daemon detected",
                "severity": "Medium",
                "checked": False,
                "occurrences": 0,
                "logged_occurrences": []
            },
            {
                "pattern": "Ready",
                "match_any": False,
                "reason": "Scheduled task configured to run automatically",
                "severity": "Medium",
                "checked": False,
                "occurrences": 0,
                "logged_occurrences": []
            }
        ]
    },
    {
        "name": "World-Writable Files",
        "commands": {
            "Darwin": "find /Applications /Library /usr/local -type f -perm -002",
            "Windows": "icacls C:\\ /T /C"
        },
        "description": "Finds files writable by any user",
        "risk_patterns": [
            {
                "pattern" : None,
                "match_any" : True,
                "reason" : "File writable by all users",
                "severity" : "High",
                "checked" : False,
                "occurrences" : 0,
                "logged_occurrences" : []
            }
        ]
}


]
SUMMARY = {
            "total_checks_run" : 0,
            "issues_found" : 0,
            "overall_risk" : "LOW"
}
