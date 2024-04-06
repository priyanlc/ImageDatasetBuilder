import os

from main.image_filter.ImageValidator import ImageValidator


class DeleteCorruptImages:
    def __init__(self, image_folder_path):
        self.image_folder_path = image_folder_path

    def clean_directory(self):
        image_files = [os.path.join(self.image_folder_path, f) for f in os.listdir(self.image_folder_path) if
                       f.endswith(('.jpg', '.jpeg', '.png'))]

        for image_file in image_files:
            ImageValidator.validate_image(image_file)

        print("Corrupt image files deletion process completed.")
