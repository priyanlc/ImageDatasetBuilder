from concurrent.futures import ThreadPoolExecutor
import time
from pathlib import Path

from main.common.ConfigLoader import ConfigLoader
from main.image_downloader.ImageDownloader import HTTPImageDownloader
from main.image_downloader.URLManager import URLManager


class ImageDownloaderApplication:
    def __init__(self, config_path):
        self.config_loader = ConfigLoader(config_path)
        self.downloader = HTTPImageDownloader()

    def run(self):
        config = self.config_loader.load_config()
        urls_file = config['urls_file']
        download_dir = Path(config['download_dir'])
        num_threads = config['num_threads']

        url_manager = URLManager(urls_file)
        urls = url_manager.get_urls()

        download_dir.mkdir(parents=True, exist_ok=True)

        start_time = time.time()
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(self.downloader.download, url, download_dir) for url in urls]
            for future in futures:
                future.result()
        end_time = time.time()

        print("All downloads completed.")
        print(f"Time taken to execute: {end_time - start_time} seconds.")


if __name__ == "__main__":
    app = ImageDownloaderApplication('../../resources/config/config.json')
    app.run()
