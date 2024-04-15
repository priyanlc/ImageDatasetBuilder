from pathlib import Path

from main.common.ConfigLoader import ConfigLoader
from main.delete_corrupt_images.DeleteCorruptImages import DeleteCorruptImages


class Application:
    def __init__(self, config_path):
        self.config_loader = ConfigLoader(config_path)
        config = self.config_loader.load_config()
        self.cleaner = DeleteCorruptImages(config['download_dir'])

    def run(self):
        self.cleaner.clean_directory()


def get_config_path():
    # Get the directory of the current script file
    current_script_directory = Path(__file__).parent
    # Build the path to config.json relative to the current script
    local_config_path = current_script_directory / Path('../common/config.json')
    return local_config_path


if __name__ == "__main__":
    app = Application(str(get_config_path()))
    app.run()
