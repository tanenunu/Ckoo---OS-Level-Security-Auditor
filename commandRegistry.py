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
                "occurances" : 0,
                "logged_occurances" : []
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
                "occurances" : 0,
                "logged_occurances" : []
            },
            {
                "pattern" : " ? ",
                "reason" : "Background process without controlling terminal",
                "severity" : "Medium",
                "checked" : False,
                "occurances" : 0,
                "logged_occurances" : []
            }
        ]
    }
]
