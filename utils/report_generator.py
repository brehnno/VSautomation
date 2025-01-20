import json
import os

def generate_html_report(target, open_ports, http_vulnerabilities, cms, output_path="reports/report.html"):
    """
    Generates an HTML report for the vulnerability scan.
    """
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Vulnerability Report</title>
</head>
<body>
    <h1>Vulnerability Report</h1>
    <h2>Target: {target}</h2>
    <h3>Open Ports:</h3>
    <ul>
        {''.join(f'<li>{port}</li>' for port in open_ports)}
    </ul>
    <h3>HTTP Vulnerabilities:</h3>
    <ul>
        {''.join(f'<li>{vuln}</li>' for vuln in http_vulnerabilities)}
    </ul>
    <h3>Detected CMS:</h3>
    <p>{cms}</p>
</body>
</html>"""

    # Ensure the reports directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write the HTML content to the file
    with open(output_path, "w") as file:
        file.write(html_content)

def save_report_as_json(target, open_ports, http_vulnerabilities, cms, output_path="reports/report.json"):
    """
    Saves the vulnerability scan report as a JSON file.
    """
    report_data = {
        "target": target,
        "open_ports": open_ports,
        "http_vulnerabilities": http_vulnerabilities,
        "cms": cms
    }

    # Ensure the reports directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write the JSON content to the file
    with open(output_path, "w") as file:
        json.dump(report_data, file, indent=4)
