from commandRegistry import REGISTRY
from commandRegistry import SUMMARY
from commandRunner import run_command
from riskScorer import analyze_output
import platform
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
    # --- Capture Data for Security Analysis ---
    output = run_command(check)
    
    # --- Perform Security Checks on Captured Data ---
    for risk in check["risk_patterns"]:
        analyze_output(output, risk)
        
        # --- Update the Summary ---
        SUMMARY['total_checks_run'] = SUMMARY['total_checks_run'] + 1
        SUMMARY['issues_found'] = SUMMARY['issues_found'] + risk['occurrences']
    
report.generateReport()