REGISTRY = [
    {
        "name" : "Open Network Ports",
        "command" : "netstat -an",
        "description" : "Lists all active network connections and listening ports",
        "risk_patterns" : [
            {
                "pattern" : "LISTEN",
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
         "command" : "ps aux",
         "description" : "Lists all running processes",
        "risk_patterns" : [
            {
                "pattern" : "root",
                "reason" : "Process running with elevated privileges",
                "severity" : "Medium",
                "checked" : False,
                "occurrences" : 0,
                "logged_occurrences" : []
            },
            {
                "pattern" : " ? ",
                "reason" : "Background process without controlling terminal",
                "severity" : "Medium",
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
