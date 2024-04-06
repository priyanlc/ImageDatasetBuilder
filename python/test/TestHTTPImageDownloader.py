import unittest
from unittest.mock import patch, mock_open
from pathlib import Path
import requests

from main.image_downloader.ImageDownloader import HTTPImageDownloader

class TestHTTPImageDownloader(unittest.TestCase):
    def setUp(self):
        self.downloader = HTTPImageDownloader()
        self.url = ("https://images.unsplash.com/photo-1711574786543-0078cf358b50?q=80&w=2574&auto=format&fit=crop"
                    "&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
        self.download_dir = Path("python/resources/downloads")
        self.filename = "image.jpg"

    @patch("builtins.open", new_callable=mock_open)
    @patch("requests.get")
    def test_download_success(self, mock_get, mock_file):
        # Mocking the requests response for success scenario
        mock_get.return_value.status_code = 200
        mock_get.return_value.iter_content = lambda chunk_size: [b'data']

        self.downloader.download(self.url, self.download_dir)

        # Check if the file write happens as expected
        mock_file.assert_called_once_with(self.download_dir / self.filename, 'wb')
        mock_file().write.assert_called_with(b'data')
        mock_get.assert_called_once_with(self.url, stream=True)

    @patch("requests.get")
    def test_download_failure(self, mock_get):
        # Mocking the requests response for failure scenario
        mock_get.return_value.status_code = 404

        with self.assertLogs(level='ERROR') as log:
            self.downloader.download(self.url, self.download_dir)

        # Check if an error log is generated
        self.assertIn("Error downloading", log.output[0])


if __name__ == '__main__':
    unittest.main()
