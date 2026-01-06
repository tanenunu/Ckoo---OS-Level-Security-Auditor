from commandRegistry import REGISTRY
from commandRunner import run_command
from riskScorer import analyze_output
import reportGenerator as report
print("----------------------------")
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

print_header()
for check in REGISTRY:
    report.Append(f"Check: {check['name']}")

    report.Append(f"Description: {check['description']}")

    output = run_command(check["command"])
    for risk in check["risk_patterns"]:

        analyze_output(output, risk)
        is_risky = False
        if risk['occurances'] > 0:
            is_risky = True

        if is_risky:
            report.Append(f"Risk detected ({risk['severity']})")
            report.Append(f"Occurances: {risk['occurances']}")
            #----UNCOMMENT to see logs of 'risky' output
            # for log in risk['logged_occurances']:
            #     print(f"{log}")
        else:
            report.Append("No obvious risk detected")
        report.Append("-" * 40)