from commandRegistry import REGISTRY
from commandRegistry import SUMMARY
from datetime import datetime
import getpass
import platform
import socket
from riskScorer import calculate_total_risk
from riskScorer import calculate_risk_breakdown

def beginReport(header):
    with open("report.txt", "w") as file:
        file.write(header)

def Append(text):
    with open("report.txt", "a") as file:
        file.write(f"\n")
        file.write(text)
        print(text)
        
def get_system_metadata():
    return {
        "generated": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "user": getpass.getuser(),
        "hostname": socket.gethostname(),
        "system": platform.system(),
        "os_version": get_os_version(),
        "architecture": platform.machine(),
    }
def get_os_version():
    os_name = platform.system()
    if os_name == "Darwin":
        return platform.mac_ver()[0]
    elif os_name == "Linux":
        return platform.release()
    elif os_name == "Windows":
        return platform.version()
    else:
        return f"Unknown ({os_name})"

def render_risk_chart(breakdown):
    lines = []
    lines.append("\nRISK BREAKDOWN")
    lines.append("--------------")

    max_value = max(breakdown.values()) if breakdown else 1
    bar_width = 20

    for severity in ["HIGH", "MEDIUM", "LOW"]:
        value = breakdown.get(severity, 0)
        bar_length = int((value / max_value) * bar_width)
        bar = "█" * bar_length

        lines.append(
            f"{severity:<6} | {bar:<20} ({value})"
        )
    return "\n".join(lines)

def render_check_section(check):
    # check: dict from REGISTRY
    # results: dict containing analysed output for this check
    # --- Header ---
    lines = []
    lines.append(f"\nCHECK: {check['name']}")
    lines.append("Description:")
    lines.append(f"     {check['description']}\n")

    total_issues = sum(risk["occurrences"] for risk in check["risk_patterns"])

    status = "OK"
    if total_issues > 0:
        status = "WARNING"
    
    lines.append("Results:")
    lines.append(f"     Status: {status}")
    lines.append(f"     Total issues: {total_issues}\n")

    # --- Findings ---
    if total_issues == 0:
        lines.append("Findings:")
        lines.append("     No issues detected")
        return "\n".join(lines)
    
    lines.append("Findings:")
    for risk in check["risk_patterns"]:
        if risk["occurrences"] == 0:
            continue

        lines.append(f"     -[{risk['severity']}] {risk['reason']}")
        lines.append(f"     Occurrences: {risk['occurrences']}")

        if risk["logged_occurrences"]:
            lines.append("     Example:")
            for log in risk["logged_occurrences"][:5]:
                lines.append(f"     {log.strip()}")
        lines.append("") #spacing
    return "\n".join(lines)




def generateReport():
    # --- HEADER DATA ---
    metadata = get_system_metadata()
    current_datetime = metadata['generated']
    user = metadata['user']
    hostname = metadata['hostname']
    system = metadata['system']
    if system == "Darwin":
        system = "macOS"
    os_version = metadata['os_version']
    architecture = metadata['architecture']
   
    # --- SUMMARY DATA ---
    total_checks_run = SUMMARY['total_checks_run']
    total_issues_found = SUMMARY['issues_found']
    overall_risk = calculate_total_risk(REGISTRY)
    breakdown = calculate_risk_breakdown(REGISTRY)
    chart = render_risk_chart(breakdown)
    

    with open("report.txt", "a") as file:
        file.write(f"\nCKOO SECURITY REPORT\n===================\n")
        file.write(f"Generated: {current_datetime}\nUser: {user}\nHost: {hostname}\nSystem: {system + " " + os_version + " " + architecture}\n\n")
        file.write(f"SUMMARY\n-------\n")
        file.write(f"Total checks run: {total_checks_run}\nIssues found: {total_issues_found}\nOverall risk: {overall_risk}")
        file.write(f"\n{chart}")
        file.write(f"\n\nRESULTS\n-------")
    
    
    # --- CHECK RESULTS ---
    for check in REGISTRY:
        section = render_check_section(check)
        Append(section)




    


    