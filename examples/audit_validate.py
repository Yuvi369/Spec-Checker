from spec_checker import validator

errors = validator.validate(
    'rules/laptops.csv',
    product_type='laptop',
    rules_path=r'D:\examples\rules\laptop.json'  # raw string to avoid escape issues
)

if errors:
    print("Validation errors found:")
    for err in errors:
        print(err)
else:
    print("All laptop specs are valid!")
