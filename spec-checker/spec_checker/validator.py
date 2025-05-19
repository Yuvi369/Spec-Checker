import pandas as pd
import json
import os
from .parser import parse_rule
from spec_checker.html_report import generate_html_report


def validate_and_return(data_path, product_type, rules_path=None):
    ext = os.path.splitext(data_path)[1].lower()
    if ext == '.csv':
        df = pd.read_csv(data_path)
    elif ext == '.json':
        df = pd.read_json(data_path)
    else:
        raise ValueError("Unsupported file format")

    if not rules_path:
        rules_path = os.path.join(os.path.dirname(__file__), '..', 'rules', f"{product_type.lower()}.json")

    with open(rules_path) as f:
        rules = json.load(f)

    results = []
    for _, row in df.iterrows():
        device_result = {"Device": row.to_dict(), "Status": "Pass", "Failed": []}
        for field, rule in rules.items():
            if not parse_rule(row[field], rule):
                device_result["Status"] = "Fail"
                device_result["Failed"].append(field)
        results.append(device_result)
    
    return results

def validate(data_path, product_type, rules_path=None, report_path=None):
    results = validate_and_return(data_path, product_type, rules_path)

    for result in results:
        print(f"\n{result['Device']}")
        print(f"✔ Status: {result['Status']}")
        if result['Failed']:
            print(f"❌ Failed Fields: {', '.join(result['Failed'])}")

    if report_path:
        generate_html_report(results, report_path)

