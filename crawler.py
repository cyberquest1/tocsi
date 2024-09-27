import requests
from bs4 import BeautifulSoup

def crawl_for_forms(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = []

        for form in soup.find_all('form'):
            inputs = [input_tag.get('name') for input_tag in form.find_all('input') if input_tag.get('name')]
            action = form.get('action')
            forms.append({'action': action, 'inputs': inputs})

        return forms
    except Exception as e:
        print(f"Error crawling {url}: {e}")
        return []
