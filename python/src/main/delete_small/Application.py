from pathlib import Path

from main.common.ConfigLoader import ConfigLoader
from main.delete_small.DeleteSmall import DeleteSmallImages


class Application:
    def __init__(self, config_path):
        self.config_loader = ConfigLoader(config_path)
        self.image_filter = DeleteSmallImages(self.config_loader.load_config()['min_size_kb'],
                                              self.config_loader.load_config()['max_size_mb'])

    def run(self):
        config = self.config_loader.load_config()
        self.image_filter.delete_images_by_size(config['download_dir'])


def get_config_path():
    # Get the directory of the current script file
    current_script_directory = Path(__file__).parent
    # Build the path to config.json relative to the current script
    local_config_path = current_script_directory / Path('../common/config.json')
    return local_config_path


if __name__ == "__main__":
    app = Application(str(get_config_path()))
    app.run()
