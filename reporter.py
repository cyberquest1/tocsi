def log_vulnerability(url, form_action, payload):
    with open('report/report.txt', 'a') as f:
        f.write(f"Vulnerability found at {url}\n")
        f.write(f"Form action: {form_action}\n")
        f.write(f"Payload: {payload}\n\n")

    print(f"Logged vulnerability to report.txt")
