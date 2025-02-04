# Vulnerability Scanner

This is a Python-based vulnerability scanner. It detects common security vulnerabilities, such as HTTP header analysis, open port scanning, and CMS (Content Management System) detection.

## Features

- **Port Scanning**: Scans the target for open ports.
- **HTTP Header Analysis**: Checks if the web server has the recommended security headers.
- **CMS Detection**: Identifies if the site is using a popular CMS like WordPress or Joomla.
- **Report Generation**: Creates reports in HTML or JSON format with scan results.

## Prerequisites

Before running the project, ensure you have Python 3.x installed on your system. If not, download and install Python from [here](https://www.python.org/downloads/).

Additionally, install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vulnerability-scanner.git
   cd vulnerability-scanner
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

The scanner can be executed via the command line. The basic format is:

```bash
python main.py <target> [--scan-ports] [--analyze-http] [--detect-cms] [--report-type html|json]
```

### Parameters:

- `<target>`: The IP address or domain you want to scan.
- `--scan-ports`: Scans for open ports.
- `--analyze-http`: Analyzes HTTP security headers.
- `--detect-cms`: Detects if the website is using a CMS.
- `--report-type html|json`: Specifies the report format (HTML or JSON).

### Example:

To perform a full scan on a domain and generate an HTML report:

```bash
python main.py http://example.com --scan-ports --analyze-http --detect-cms --report-type html
```

## Reports

Reports are automatically generated in the specified format (`html` or `json`) and saved in the `reports` folder. These reports contain details such as open ports, missing security headers, and detected CMS.

### HTML Report Structure:
- **Target**: The scanned IP or domain.
- **Open Ports**: A list of detected open ports.
- **HTTP Vulnerabilities**: Missing security headers that may pose risks.
- **Detected CMS**: The CMS used by the website (if identified).

## Contribution

If you wish to contribute to this project, feel free to fork the repository and submit a pull request with your improvements. If you find any bugs or have suggestions, create an issue in the repository.

### Steps to Contribute:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/new-feature`).
3. Make your changes and commit (`git commit -am 'Adding new feature'`).
4. Push to the remote repository (`git push origin feature/new-feature`).
5. Create a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Your Name** - brehnno (https://github.com/brehnno)
