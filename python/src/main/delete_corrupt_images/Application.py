from main.common.ConfigLoader import ConfigLoader
from main.delete_corrupt_images.DeleteCorruptImages import DeleteCorruptImages


class Application:
    def __init__(self, config_path):
        self.config_loader = ConfigLoader(config_path)
        config = self.config_loader.load_config()
        self.cleaner = DeleteCorruptImages(config['download_dir'])

    def run(self):
        self.cleaner.clean_directory()


def main():
    app = Application('../common/config.json')
    app.run()


if __name__ == "__main__":
    main()
