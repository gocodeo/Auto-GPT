# Date: 2023-5-13
# Author: Generated by GoCodeo.


import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from autogpt.commands.web_requests import scrape_text, get_response
patch_func1 = "autogpt.commands.web_requests.get_response"

class TestScrapeText(unittest.TestCase):

    @patch(patch_func1)
    def test_positive_scrape_text(self, mock_get_response):
        # Positive Test
        magic_response = MagicMock()
        magic_response.text = '<html><body><p>Hello, World!</p></body></html>'
        mock_get_response.return_value = (magic_response, None)
        url = "https://example.com"
        expected_text = "Hello, World!"
        result = scrape_text(url)
        self.assertEqual(result, expected_text)

    @patch(patch_func1)
    def test_negative_scrape_text(self, mock_get_response):
        # Negative Test
        mock_get_response.return_value = (None, "Error: Invalid URL")
        url = "https://invalid-url"
        expected_text = "Error: Invalid URL"
        result = scrape_text(url)
        self.assertEqual(result, expected_text)

    @patch(patch_func1)
    def test_error_scrape_text(self, mock_get_response):
        # Error Test
        mock_get_response.return_value = (None, None)
        url = "https://no-response.com"
        expected_text = "Error: Could not get response"
        result = scrape_text(url)
        self.assertEqual(result, expected_text)

    @patch(patch_func1)
    def test_edge_scrape_text(self, mock_get_response):
        # Edge Test
        magic_response = MagicMock()
        magic_response.text = '<html><body><p></p></body></html>'
        mock_get_response.return_value = (magic_response, None)
        url = "https://empty-element.com"
        expected_text = ""
        result = scrape_text(url)
        self.assertEqual(result, expected_text)

if __name__ == '__main__':
    unittest.main()