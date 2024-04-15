from pathlib import Path

import torch

from main.common.ConfigLoader import ConfigLoader
from main.delete_character.EasyOCRProcessor import EasyOCRProcessor
from main.delete_character.ImageBatchProcessor import ImageBatchProcessor


class Application:
    def __init__(self, config_path):
        if not torch.cuda.is_available():
            raise EnvironmentError("GPU is not available. Please check your CUDA setup.")

        self.config_loader = ConfigLoader(config_path)
        self.processor = EasyOCRProcessor()
        self.batch_processor = ImageBatchProcessor(self.processor)

    def run(self):
        config = self.config_loader.load_config()
        self.batch_processor.process_folder(config['download_dir'])


def get_config_path():
    # Get the directory of the current script file
    current_script_directory = Path(__file__).parent
    # Build the path to config.json relative to the current script
    local_config_path = current_script_directory / Path('../common/config.json')
    return local_config_path


if __name__ == "__main__":
    app = Application(str(get_config_path()))
    app.run()
