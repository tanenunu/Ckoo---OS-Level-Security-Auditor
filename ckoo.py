from commandRegistry import REGISTRY
from commandRunner import run_command
from riskScorer import analyze_output
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

print_header()
for check in REGISTRY:
    print(f"Check: {check['name']}")
    print(f"Description: {check['description']}")
    output = run_command(check["command"])
    for risk in check["risk_patterns"]:
        print(f"Checking for: {risk["reason"]}")

        analyze_output(output, risk)
        is_risky = False
        if risk['occurances'] > 0:
            is_risky = True

        if is_risky:
            print(f"Risk detected ({risk['severity']})")
            print(f"Occurances: {risk['occurances']}")
            # for log in risk['logged_occurances']:
            #     print(f"{log}")
        else:
            print("No obvious risk detected")
        print("-" * 40)