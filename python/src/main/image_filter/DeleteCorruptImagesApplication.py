from pathlib import Path

from main.common.ConfigLoader import ConfigLoader
from main.image_filter.DeleteCorruptImages import DeleteCorruptImages


class DeleteCorruptImagesApplication:
    def __init__(self, config_path):
        self.config_loader = ConfigLoader(config_path)
        config = self.config_loader.load_config()
        self.cleaner = DeleteCorruptImages(config['download_dir'])

    def run(self):
        self.cleaner.clean_directory()


def main():
    app = DeleteCorruptImagesApplication('../../resources/config/config.json')
    app.run()


if __name__ == "__main__":
    main()
