def format_url(url):
    if not url.startswith('http'):
        url = 'http://' + url
    return url

def is_valid_url(url):
    return url.startswith('http://') or url.startswith('https://')
