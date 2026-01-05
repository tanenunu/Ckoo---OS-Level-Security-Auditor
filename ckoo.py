from commandRegistry import REGISTRY
from commandRunner import run_command
from reportGenerator import analyze_output

for check in REGISTRY:
    output = run_command(check["command"])
    is_risky = analyze_output(output, check["risk_pattern"])

    print(f"Check: {check['name']}")
    print(f"Description: {check['description']}")

    if is_risky:
        print(f"Risk detected ({check['severity']})")
    else:
        print("No obvious risk detected")
    print("-" * 40)