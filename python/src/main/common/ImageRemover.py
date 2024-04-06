import os


class ImageRemover:
    @staticmethod
    def remove_image(image_path):
        if os.path.exists(image_path):
            print('File to delete:' + image_path)
            os.remove(image_path)
        else:
            print('File does not exist')
