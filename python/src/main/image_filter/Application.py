from main.common.ConfigLoader import ConfigLoader
from main.image_filter.DeleteSmall import DeleteSmallImages


class Application:
    def __init__(self, config_path):
        self.config_loader = ConfigLoader(config_path)
        self.image_filter = DeleteSmallImages(self.config_loader.load_config()['min_size_kb'],
                                              self.config_loader.load_config()['max_size_mb'])

    def run(self):
        config = self.config_loader.load_config()
        self.image_filter.delete_images_by_size(config['download_dir'])


def main():
    app = Application('../common/config.json')
    app.run()
