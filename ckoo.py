from commandRegistry import REGISTRY
from commandRegistry import SUMMARY
from commandRunner import run_command
from riskScorer import analyze_output
import reportGenerator as report
print("----------------------------")

# --- Function: Print Header ---
def print_header():
    header = r"""
   ____ _               
  / ___| | _____   ___  
 | |   | |/ / _ \ / _ \ 
 | |___|   < (_) | (_) |
  \____|_|\_\___/ \___/ 

        C K O O
   OS-Level Security Auditor

    """
    print(header)
    report.beginReport(header)

# --- MAIN ---
print_header()
for check in REGISTRY:
    # --- Label the Currently Checked Area ---
    #report.Append(f"Check: {check['name']}")
    #report.Append(f"Description: {check['description']}")

    # --- Capture Data for Security Analysis ---
    output = run_command(check["command"])
    
    # --- Perform Security Checks on Captured Data ---
    for risk in check["risk_patterns"]:
        analyze_output(output, risk)
        is_risky = False
        if risk['occurances'] > 0:
            is_risky = True

        if is_risky:
            #report.Append(f"Risk detected ({risk['severity']})")
            #report.Append(f"Occurances: {risk['occurances']}")
            #----UNCOMMENT to see logs of 'risky' output
            # for log in risk['logged_occurances']:
            #     print(f"{log}")
            4
        else:
            4
            #report.Append("No obvious risk detected")
        #report.Append("-" * 40)

        # --- Update the Summary ---
        SUMMARY['total_checks_run'] = SUMMARY['total_checks_run'] + 1
        SUMMARY['issues_found'] = SUMMARY['issues_found'] + risk['occurances']
    
report.generateReport()