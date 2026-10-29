"""
This module will create the rules for triple triad,
meaning the comparison for the base rule,
and the bunus rules, such as plus, combo, and same.
"""


def compare_values(attacking_value, defending_value):
    if attacking_value > defending_value:
        return True
    else:
        return False


test_cases = {
    "TC001_True_Case": {
        "inputs": {"v1": 4, "v2": 3},
        "expected": True
    },
    "TC002_False_Case: Less_Than": {
        "inputs": {"v1": 3, "v2": 4},
        "expected": False
    },
    "TC003_False_Case: Same": {
        "inputs": {"v1": 4, "v2": 4},
        "expected": False
    }
}

for test_case, data in test_cases.items():
    v1 = data["inputs"]["v1"]
    v2 = data["inputs"]["v2"]

    result = compare_values(v1, v2)
    assert result == data["expected"]
    print(f"{test_case}'s result is {result}")