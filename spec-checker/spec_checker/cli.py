import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Universal Spec Validator for Electronics")

    parser.add_argument("data_path", nargs="?", help="Path to CSV or JSON file")
    parser.add_argument("--type", dest="product_type", help="Product type (e.g. laptop, mobile, monitor)")
    parser.add_argument("--config", dest="rules_path", help="Optional path to custom rules JSON")
    parser.add_argument("--report", dest="report_path", help="Optional path to save HTML report")

    args = parser.parse_args()

    from .validator import validate
    validate(args.data_path, args.product_type, args.rules_path, args.report_path)
