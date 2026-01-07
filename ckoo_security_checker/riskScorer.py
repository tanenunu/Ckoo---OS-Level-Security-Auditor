def analyze_output(output, risk_pattern):
    lines = output.splitlines()


    # Case 1: existence-based risk (each line is a risk occurrence)
    if risk_pattern.get("match_any") == True:
         risk_pattern["occurrences"] += len(lines)
         risk_pattern["logged_occurrences"].extend(lines)
         risk_pattern["checked"] = True
         return
    
    # Case 2: pattern-based risk (lines that match the pattern are a risk occurrence)
    pattern = risk_pattern.get("pattern")
    if not pattern:
         return
    
    for line in lines:
         if pattern in line:
              risk_pattern["occurrences"] += 1
              risk_pattern["logged_occurrences"].append(line)
    risk_pattern['checked'] = True


def calculate_risk_breakdown(REGISTRY):
     # --- Returns a high level breakdown of data risk ---
     # Used by reportGenerator.py to render a bar chart in the report overview
     SEVERITY_WEIGHTS = {
          "LOW" : 1,
          "MEDIUM" : 3,
          "HIGH" : 5
     }
     BREAKDOWN = {
          "LOW" : 0,
          "MEDIUM" : 0,
          "HIGH" : 0
     }
     OCCURRENCE_CAP = 10

     for check in REGISTRY:
          for risk in check['risk_patterns']:
               severity = risk['severity'].upper()
               weight = SEVERITY_WEIGHTS.get(severity, 0)
               occurrences = min(risk['occurrences'], OCCURRENCE_CAP)
               BREAKDOWN[severity] += weight * occurrences
     return BREAKDOWN


          
     

def calculate_total_risk(REGISTRY):
    # --- Calculate Total Checks Performed by the Program ---
    SEVERITY_WEIGHTS = {
        "LOW" : 1,
        "MEDIUM" : 3,
        "HIGH" : 5
    }
    OCCURRENCE_CAP = 10
    actual_risk = 0
    maximum_risk = 0
    for check in REGISTRY:
        for risk in check['risk_patterns']:
            severity = risk["severity"].upper()
            weight = SEVERITY_WEIGHTS.get(severity, 0)
            
            # Maximum possible contribution from this risk pattern
            maximum_risk += weight * OCCURRENCE_CAP

            # Actual contribution
            occurrences = min(risk["occurrences"], OCCURRENCE_CAP) # will return the cap if occurences is higher
            actual_risk += weight * occurrences
    if maximum_risk == 0:
            return "LOW"
    
    risk_ratio = actual_risk / maximum_risk

    if risk_ratio <= 0.25:
        return "LOW"
    elif risk_ratio <= 0.60:
            return "MEDIUM"
    else:
            return "HIGH"
    

    


