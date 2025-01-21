import json
import os

def generate_html_report(target, open_ports, http_vulnerabilities, cms, output_path="reports/report.html"):
    """
    Generates an HTML report for the vulnerability scan.
    """
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vulnerability Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 0;
        }}
        header {{
            background-color: #0078d7;
            color: white;
            padding: 1rem 0;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        }}
        header h1 {{
            margin: 0;
            font-size: 2rem;
        }}
        main {{
            padding: 2rem;
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }}
        h2, h3 {{
            color: #0078d7;
        }}
        ul {{
            list-style-type: none;
            padding: 0;
        }}
        ul li {{
            background: #e7f3ff;
            margin: 0.5rem 0;
            padding: 0.5rem;
            border-left: 4px solid #0078d7;
            border-radius: 4px;
        }}
        footer {{
            text-align: center;
            padding: 1rem 0;
            margin-top: 2rem;
            background: #0078d7;
            color: white;
        }}
    </style>
</head>
<body>
    <header>
        <h1>Vulnerability Report</h1>
    </header>
    <main>
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
    </main>
    <footer>
        &copy; 2025 - Vulnerability Scanner
    </footer>
</body>
</html>
"""

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
