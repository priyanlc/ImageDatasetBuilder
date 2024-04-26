import dlib

from main.common.ConfigLoader import ConfigLoader
from main.face_recognition.FaceImageProcessor import FaceImageProcessor
from main.face_recognition.ImageBatchManager import ImageBatchManager

from pathlib import Path


class Application:
    def __init__(self, config_path):
        self.config_loader = ConfigLoader(config_path)
        self.processor = FaceImageProcessor()
        self.batch_manager = ImageBatchManager(self.processor)

    def run(self):
        config = self.config_loader.load_config()
        self._check_cuda()
        self.batch_manager.process_folder(config['download_dir'])

    @staticmethod
    def _check_cuda():
        if dlib.DLIB_USE_CUDA:
            print("CUDA is enabled in dlib, GPU will be used for processing.")
        else:
            print("CUDA is not enabled in dlib, processing will use the CPU.")


def get_config_path():
    # Get the directory of the current script file
    current_script_directory = Path(__file__).parent
    # Build the path to config.json relative to the current script
    local_config_path = current_script_directory / Path('../common/config.json')
    return local_config_path


if __name__ == "__main__":
    app = Application(str(get_config_path()))
    app.run()
