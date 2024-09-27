import requests
from tocsi.crawler import crawl_for_forms
from tocsi.payloads import get_payloads
from tocsi.reporter import log_vulnerability

def scan_website(url):
    # Crawl for forms
    forms = crawl_for_forms(url)
    payloads = get_payloads()

    if not forms:
        print(f"No forms found on {url}")
        return

    print(f"Found {len(forms)} form(s) on {url}. Starting XSS scan...")

    for form in forms:
        for payload in payloads:
            data = {input_name: payload for input_name in form['inputs']}
            response = requests.post(form['action'], data=data)

            if payload in response.text:
                print(f"Vulnerability found with payload: {payload}")
                log_vulnerability(url, form['action'], payload)
            else:
                print(f"No vulnerability found with payload: {payload}")
