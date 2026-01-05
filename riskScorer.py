def analyze_output(output, risk_pattern):
    matching_lines = []
    for line in output.splitlines():
        if risk_pattern['pattern'] in line:
            matching_lines.append(line.strip())
    risk_pattern['logged_occurances'] = matching_lines
    risk_pattern['occurances'] = len(matching_lines)
    risk_pattern['checked'] = True