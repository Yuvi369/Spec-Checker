def generate_html_report(results, report_path):
    """
    Generate an HTML report for device specification validation results.
    
    Args:
        results (list): List of dictionaries containing validation results with keys:
                        'Status', 'Device', and 'Failed'
        report_path (str): Path where the HTML report will be saved
    """
    # Count statistics
    total_count = len(results)
    passed_count = sum(1 for res in results if res['Status'] == 'PASS' or res['Status'] == 'Pass')
    failed_count = total_count - passed_count
    
    # Create HTML content as a single string with no format placeholders in CSS
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spec Checker Report</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        
        header {
            background-color: #2c3e50;
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            margin: 0;
            font-size: 28px;
        }
        
        .dashboard {
            display: flex;
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .stat-box {
            flex: 1;
            background-color: white;
            border-radius: 8px;
            padding: 15px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        .stat-number {
            font-size: 32px;
            font-weight: bold;
            margin: 10px 0;
        }
        
        .success { color: #27ae60; }
        .error { color: #e74c3c; }
        
        .result-card {
            background-color: white;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 15px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        .status-badge {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 4px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        
        .status-pass {
            background-color: #d5f5e3;
            color: #27ae60;
        }
        
        .status-fail {
            background-color: #fadbd8;
            color: #e74c3c;
        }
        
        .device-name {
            font-size: 18px;
            margin: 10px 0;
        }
        
        .failed-list {
            background-color: #fff9f9;
            padding: 10px 15px;
            border-left: 3px solid #e74c3c;
            margin-top: 10px;
            border-radius: 0 4px 4px 0;
        }
        
        .timestamp {
            color: #7f8c8d;
            font-size: 14px;
            text-align: right;
            margin-top: 20px;
        }
        
        @media (max-width: 768px) {
            .dashboard {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Device Specification Validation Report</h1>
    </header>"""
    
    # Add stats dashboard section
    html += f"""
    <div class="dashboard">
        <div class="stat-box">
            <div>Total Devices</div>
            <div class="stat-number">{total_count}</div>
        </div>
        <div class="stat-box">
            <div>Passed</div>
            <div class="stat-number success">{passed_count}</div>
        </div>
        <div class="stat-box">
            <div>Failed</div>
            <div class="stat-number error">{failed_count}</div>
        </div>
    </div>
    
    <div id="results-container">"""
    
    # Add each result card
    for res in results:
        status = res.get('Status', '')
        device = res.get('Device', '')
        failed = res.get('Failed', [])
        
        # Handle both 'PASS'/'FAIL' and 'Pass'/'Fail' formats
        is_pass = status.upper() == 'PASS' or status == 'Pass'
        status_class = "status-pass" if is_pass else "status-fail"
        
        html += f"""
        <div class="result-card">
            <div class="status-badge {status_class}">{status}</div>"""
            
        # If we have a 'Brand' key, this is likely the device specs in a dict format
        if isinstance(device, dict) and 'Brand' in device:
            html += f"""
            <div class="device-name">{device}</div>"""
        else:
            html += f"""
            <div class="device-name">{device}</div>"""
        
        if failed:
            html += f"""
            <div class="failed-list">
                <strong>Failed Fields:</strong> {', '.join(failed)}
            </div>"""
        
        html += """
        </div>"""
    
    # Add timestamp and close HTML tags
    from datetime import datetime
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html += f"""
    </div>
    
    <div class="timestamp">
        Report generated: {current_time}
    </div>
</body>
</html>"""
    
    # Write HTML to file
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Report successfully generated at {report_path}")