import torch

from main.common.ConfigLoader import ConfigLoader
from main.delete_character.EasyOCRProcessor import EasyOCRProcessor
from main.delete_character.ImageBatchProcessor import ImageBatchProcessor


class Application:
    def __init__(self, config_path):
        if not torch.cuda.is_available():
            raise EnvironmentError("GPU is not available. Please check your CUDA setup.")

        self.config = ConfigLoader.load_config(config_path)
        self.processor = EasyOCRProcessor()
        self.batch_processor = ImageBatchProcessor(self.processor)

    def run(self):
        self.batch_processor.process_folder(self.config['download_dir'])


def main():
    try:
        app = Application('../../resources/config/config.json')
        app.run()
    except Exception as e:
        print(f"Application error: {e}")


if __name__ == "__main__":
    main()
