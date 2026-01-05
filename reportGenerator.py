def analyze_output(output, risk_pattern):
    if risk_pattern in output:
        return True
    return False