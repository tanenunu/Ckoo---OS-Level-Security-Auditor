from commandRegistry import REGISTRY
from commandRegistry import SUMMARY
from datetime import datetime
import getpass
import platform
import socket
from riskScorer import calculate_total_risk

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

    with open("report.txt", "a") as file:
        file.write(f"\nCKOO SECURITY REPORT\n===================\n")
        file.write(f"Generated: {current_datetime}\nUser: {user}\nHost: {hostname}\nSystem: {system + " " + os_version + " " + architecture}\n\n")
        file.write(f"SUMMARY\n-------\n")
        file.write(f"Total checks run: {total_checks_run}\nIssues found: {total_issues_found}\nOverall risk: {overall_risk}")
    
    # --- CHECK RESULTS ---



    


    