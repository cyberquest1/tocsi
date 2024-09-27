import unittest
from tocsi.scanner import scan_website

class TestScanner(unittest.TestCase):
    def test_scan_website(self):
        # Assuming we have a local test site to test on
        url = "http://localhost/test"
        scan_website(url)
        # You can add assertions here to validate expected behavior

if __name__ == '__main__':
    unittest.main()
