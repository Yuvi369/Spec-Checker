import pandas as pd
import json
import argparse
import ast
import os

def parse_rule(value, rule):
    if rule.startswith(">="):
        return float(value) >= float(rule[2:])
    elif rule.startswith("<="):
        return float(value) <= float(rule[2:])
    elif rule.startswith("=="):
        return str(value).strip() == rule[2:].strip()
    elif rule.startswith("in:"):
        options = ast.literal_eval(rule[3:])  # caution: replace with safe eval later
        return str(value) in options
    return False

def validate(data_path, rules_path):
    df = pd.read_csv(data_path)
    with open(rules_path) as f:
        rules = json.load(f)

    # Load data file based on extension
    ext = os.path.splitext(data_path)[1].lower()
    if ext == '.csv':
        df = pd.read_csv(data_path)
    elif ext == '.json':
        df = pd.read_json(data_path)
    else:
        raise ValueError("Unsupported file format. Use .csv or .json")

    results = []
    for index, row in df.iterrows():
        device_result = {"Device": row.to_dict(), "Status": "Pass", "Failed": []}
        for field, rule in rules.items():
            if not parse_rule(row[field], rule):
                device_result["Status"] = "Fail"
                device_result["Failed"].append(field)
        results.append(device_result)

    for result in results:
        print(f"\n{result['Device']}")
        print(f"✔ Status: {result['Status']}")
        if result['Failed']:
            print(f"❌ Failed Fields: {', '.join(result['Failed'])}")

def main():
    parser = argparse.ArgumentParser(description="Laptop Spec Validator")
    parser.add_argument('data_path', help='Path to the CSV file')
    parser.add_argument('--config', dest='rules_path', required=True, help='Path to the rules JSON file')
    args = parser.parse_args()

    validate(args.data_path, args.rules_path)

