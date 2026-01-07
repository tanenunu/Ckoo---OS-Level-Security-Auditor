from ckoo_security_checker.riskScorer import analyze_output
from ckoo_security_checker.riskScorer import calculate_total_risk
from ckoo_security_checker.commandRunner import run_command

#Tests if registry correctly updates when data is analysed
#Pattern-based:
def test_pattern_based_risk_counts_correctly():
    # Sample Output
    output = """root process
user process
root daemon
"""
# Sample Registry Entry
    risk = {
        "pattern": "root",
        "occurrences": 0,
        "logged_occurrences": [],
        "checked": False
    }

    analyze_output(output, risk)

    assert risk["occurrences"] == 2
    assert len(risk["logged_occurrences"]) == 2
    assert risk["checked"] is True

# Tests if registry correctly updates when data is analysed
# Existence-based:
def test_match_any_counts_lines():
    # Sample Output
    output = """/file1
/file2
/file3
"""
# Sample Registry Entry
    risk = {
        "match_any": True,
        "occurrences": 0,
        "logged_occurrences": [],
        "checked": False
    }

    analyze_output(output, risk)

    assert risk["occurrences"] == 3
    assert len(risk["logged_occurrences"]) == 3
    assert risk["checked"] is True

# Test handle case when there are 0 risks to report
def test_total_risk_safe_when_no_issues():
    registry = [
        {
            "risk_patterns": [
                {"severity": "LOW", "occurrences": 0}
            ]
        }
    ]

    result = calculate_total_risk(registry)

    assert result == "LOW"


# Test that program handles an unknown operating system without breaking
def test_check_skipped_if_os_not_supported(monkeypatch):
    check = {
        "commands": {
            "Darwin": "ps aux"
        }
    }

    # Fake OS as Windows
    monkeypatch.setattr("platform.system", lambda: "Windows")

    output = run_command(check)

    assert output is None

