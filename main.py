import argparse
from tocsi.scanner import scan_website

def main():
    parser = argparse.ArgumentParser(description="Tocsi XSS Vulnerability Scanner")
    parser.add_argument('--url', required=True, help="Target URL to scan")
    args = parser.parse_args()

    # Start scanning the website
    scan_website(args.url)

if __name__ == '__main__':
    main()
