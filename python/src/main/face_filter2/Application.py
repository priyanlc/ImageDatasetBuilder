from main.common.ConfigLoader import ConfigLoader
from main.face_filter2.ImageProcessor import ImageProcessor


class Application:
    def __init__(self, config_path):
        self.config = ConfigLoader.load_config(config_path)
        self.processor = ImageProcessor(self.config['download_dir'], num_processes=1)

    def run(self):
        self.processor.process_images()

def main():
    app = Application('../../resources/config/config.json')
    app.run()


if __name__ == "__main__":
    main()
