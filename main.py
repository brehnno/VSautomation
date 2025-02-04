import argparse
import logging
from modules.port_scanner import scan_ports
from modules.header_analyzer import analyze_http_headers
from modules.cms_detector import detect_cms
from utils.report_generator import generate_html_report, save_report_as_json

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class VulnerabilityScanner:
    def __init__(self, target):
        self.target = target
        self.open_ports = []
        self.http_vulnerabilities = []
        self.cms = None

    def scan_ports(self):
        logging.info("Scanning ports...")
        self.open_ports = scan_ports(self.target)

    def analyze_http(self):
        logging.info("Analyzing HTTP headers...")
        try:
            self.http_vulnerabilities = analyze_http_headers(self.target)
        except Exception as e:
            logging.error(f"Error analyzing HTTP headers: {e}")
            self.http_vulnerabilities.append(f"Error analyzing headers: {e}")

    def detect_cms(self):
        logging.info("Detecting CMS...")
        try:
            self.cms = detect_cms(self.target)
        except Exception as e:
            logging.error(f"Error detecting CMS: {e}")
            self.cms = f"Error detecting CMS: {e}"

def format_target_url(target):
    """
    Add 'http://' to target if it does not contain a schema.
    """
    if not target.startswith(("http://", "https://")):
        return f"http://{target}"
    return target

def main():
    parser = argparse.ArgumentParser(description="Vulnerability Scanner")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("--scan-ports", action="store_true", help="Scan for open ports")
    parser.add_argument("--analyze-http", action="store_true", help="Analyze HTTP headers")
    parser.add_argument("--detect-cms", action="store_true", help="Detect CMS")
    parser.add_argument("--report-type", choices=["html", "json"], help="Report format")
    
    args = parser.parse_args()
    
    # Format the target URL
    target = format_target_url(args.target)
    
    scanner = VulnerabilityScanner(target)

    if args.scan_ports:
        scanner.scan_ports()
    if args.analyze_http:
        scanner.analyze_http()
    if args.detect_cms:
        scanner.detect_cms()
    
    # Report generator
    if args.report_type == "html":
        generate_html_report(
            target=target,
            open_ports=scanner.open_ports,
            http_vulnerabilities=scanner.http_vulnerabilities,
            cms=scanner.cms
        )
        logging.info("Report saved as HTML at reports/report.html")
    elif args.report_type == "json":
        save_report_as_json(
            {
                "target": target,
                "open_ports": scanner.open_ports,
                "http_vulnerabilities": scanner.http_vulnerabilities,
                "cms": scanner.cms,
            },
            "reports/report.json"
        )
        logging.info("Report saved as JSON at reports/report.json")

if __name__ == "__main__":
    main()
