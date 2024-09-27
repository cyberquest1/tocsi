import unittest
from tocsi.crawler import crawl_for_forms

class TestCrawler(unittest.TestCase):
    def test_crawl_for_forms(self):
        url = "http://localhost/test"
        forms = crawl_for_forms(url)
        self.assertGreaterEqual(len(forms), 1)

if __name__ == '__main__':
    unittest.main()
