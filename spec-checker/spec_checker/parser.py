import ast

def parse_rule(value, rule):
    if rule.startswith(">="):
        return float(value) >= float(rule[2:])
    elif rule.startswith("<="):
        return float(value) <= float(rule[2:])
    elif rule.startswith("=="):
        return str(value).strip() == rule[2:].strip()
    elif rule.startswith("in:"):
        options = ast.literal_eval(rule[3:])
        return str(value) in options
    return False
