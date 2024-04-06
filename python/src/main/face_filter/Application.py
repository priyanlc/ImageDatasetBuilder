import dlib

from main.common.ConfigLoader import ConfigLoader
from main.face_filter.FaceImageProcessor import FaceImageProcessor
from main.face_filter.ImageBatchManager import ImageBatchManager


class Application:
    def __init__(self, config_path):
        self.config = ConfigLoader.load_config(config_path)
        self.processor = FaceImageProcessor()
        self.batch_manager = ImageBatchManager(self.processor)

    def run(self):
        self._check_cuda()
        self.batch_manager.process_folder(self.config['download_dir'])

    @staticmethod
    def _check_cuda():
        if dlib.DLIB_USE_CUDA:
            print("CUDA is enabled in dlib, GPU will be used for processing.")
        else:
            print("CUDA is not enabled in dlib, processing will use the CPU.")


def main():
    app = Application('../../resources/config/config.json')
    app.run()


if __name__ == "__main__":
    main()
