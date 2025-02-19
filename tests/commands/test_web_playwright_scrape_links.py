# Date: 2023-5-12
# Author: Generated by GoCodeo.


import unittest
from unittest.mock import patch, MagicMock
from typing import Union, List
from bs4 import BeautifulSoup
from autogpt.commands.web_playwright import sync_playwright
from autogpt.commands.web_playwright import scrape_links
patch_func1 = "autogpt.commands.web_playwright.sync_playwright"
class TestScrapeLinks(unittest.TestCase):

    @patch(patch_func1)
    def test_positive_scrape_links(self, mock_sync_playwright):
        mock_page = MagicMock()
        mock_page.content.return_value = '<html><body><a href="https://example.com">Example</a></body></html>'
        mock_sync_playwright.return_value.__enter__.return_value.chromium.launch.return_value.new_page.return_value = mock_page

        url = "https://example.com"
        expected_result = ['Example (https://example.com)']
        result = scrape_links(url)
        self.assertEqual(result, expected_result)

    @patch(patch_func1)
    def test_negative_scrape_links_no_links(self, mock_sync_playwright):
        mock_page = MagicMock()
        mock_page.content.return_value = '<html><body><p>No links here</p></body></html>'
        mock_sync_playwright.return_value.__enter__.return_value.chromium.launch.return_value.new_page.return_value = mock_page

        url = "https://example.com"
        expected_result = []
        result = scrape_links(url)
        self.assertEqual(result, expected_result)

    @patch(patch_func1)
    def test_error_scrape_links_invalid_url(self, mock_sync_playwright):
        mock_page = MagicMock()
        mock_page.goto.side_effect = Exception("Invalid URL")
        mock_sync_playwright.return_value.__enter__.return_value.chromium.launch.return_value.new_page.return_value = mock_page

        url = "invalid_url"
        expected_result = "Error: Invalid URL"
        result = scrape_links(url)
        self.assertEqual(result, expected_result)

    @patch(patch_func1)
    def test_edge_scrape_links_multiple_links(self, mock_sync_playwright):
        mock_page = MagicMock()
        mock_page.content.return_value = '<html><body><a href="https://example.com">Example</a><a href="https://example2.com">Example2</a></body></html>'
        mock_sync_playwright.return_value.__enter__.return_value.chromium.launch.return_value.new_page.return_value = mock_page

        url = "https://example.com"
        expected_result = ['Example (https://example.com)', 'Example2 (https://example2.com)']
        result = scrape_links(url)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
