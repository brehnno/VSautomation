import requests

def analyze_http_headers(target):
    vulnerabilities = []
    target = target.strip()  # Remover espaços em branco que possam estar na URL

    # Verifica se a URL já contém o prefixo "http://" antes de adicionar
    if not target.startswith(("http://", "https://")):
        target = f"http://{target}"

    try:
        response = requests.get(target, timeout=10)
        headers = response.headers

        # Verificação de cabeçalhos
        if 'Content-Security-Policy' not in headers:
            vulnerabilities.append("Content-Security-Policy missing")
        if 'X-Content-Type-Options' not in headers:
            vulnerabilities.append("X-Content-Type-Options missing")
        if 'X-Frame-Options' not in headers:
            vulnerabilities.append("X-Frame-Options missing")
        if 'Strict-Transport-Security' not in headers:
            vulnerabilities.append("Strict-Transport-Security missing")
    except requests.exceptions.RequestException as e:
        vulnerabilities.append(f"Error analyzing headers: {str(e)}")

    return vulnerabilities
