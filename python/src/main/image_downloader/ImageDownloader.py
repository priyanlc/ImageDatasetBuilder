from abc import ABC, abstractmethod
from pathlib import Path

import requests


class ImageDownloader(ABC):
    @abstractmethod
    def download(self, url, download_loc_dir):
        pass


class HTTPImageDownloader(ImageDownloader):
    def download(self, url, download_loc_dir):
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                filename = Path(url).name
                filepath = download_loc_dir / filename
                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                print(f"Downloaded {filename}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")
