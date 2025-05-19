import io
import sys
from spec_checker import validator, html_report

# Capture printed output of validator.validate
old_stdout = sys.stdout
sys.stdout = mystdout = io.StringIO()

errors = validator.validate(
    'rules/laptops.csv',
    product_type='laptop',
    rules_path=r'D:\examples\rules\laptop.json'
)

sys.stdout = old_stdout  # reset stdout

output = mystdout.getvalue()
print("Captured validation output:")
print(output)

# Now parse the output string into a results list for report generation
# Example parsing logic for your output format:
results = []
current_device = {}
for line in output.splitlines():
    if line.startswith("{'Brand'"):
        # Convert string dict to python dict safely
        current_device = eval(line)  # use with caution; better to use ast.literal_eval if possible
    elif line.startswith("✔ Status:"):
        status = line.split(":")[1].strip()
        current_device['Status'] = status
    elif line.startswith("❌ Failed Fields:"):
        failed = line.split(":")[1].strip().split(", ")
        current_device['Failed'] = failed
        results.append(current_device)

# If some devices passed without failed fields, handle them
if current_device and 'Status' in current_device and current_device['Status'] == 'Pass':
    current_device['Failed'] = []
    results.append(current_device)

# Generate the report using parsed results
html_report.generate_html_report(results, "validation_report.html")
print("HTML report generated!")
