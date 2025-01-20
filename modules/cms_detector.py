import requests
from bs4 import BeautifulSoup

def detect_cms(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        if "wp-content" in response.text:
            return "WordPress"
        if "Joomla" in soup.find_all('meta', content=True):
            return "Joomla"
        return "Unknown CMS"
    except requests.exceptions.RequestException as e:
        return f"Error detecting CMS: {str(e)}"
