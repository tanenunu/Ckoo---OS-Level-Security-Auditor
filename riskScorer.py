def analyze_output(output, risk_pattern):
    matching_lines = []
    for line in output.splitlines():
        if risk_pattern['pattern'] in line:
            matching_lines.append(line.strip())
    risk_pattern['logged_occurances'] = matching_lines
    risk_pattern['occurances'] = len(matching_lines)
    risk_pattern['checked'] = True

def calculate_total_risk(REGISTRY):
    # --- Calculate Total Checks Performed by the Program ---
    total_checks = 0
    actual_risk = 0
    for check in REGISTRY:
        for risk in check['risk_patterns']:
            total_checks = total_checks + 1
            if risk['occurances'] > 0:
                if risk['severity'] == "LOW":
                    actual_risk = actual_risk + 1
                elif risk['severity'] == "MEDIUM":
                    actual_risk = actual_risk + 2
                elif risk['severity'] == "HIGH":
                    actual_risk = actual_risk + 3
    maximum_risk = total_checks * 3
    overall_risk = "NOTYETMADE"
    if actual_risk <= maximum_risk / 3:
        overall_risk = "LOW"
    elif actual_risk <= maximum_risk / 2:
        overall_risk = "MEDIUM"
    else:
        overall_risk = "HIGH"
    return overall_risk
    

    


