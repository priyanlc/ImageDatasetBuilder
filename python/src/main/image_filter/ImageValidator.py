from PIL import Image
import os


class ImageValidator:
    @staticmethod
    def validate_image(image_path):
        try:
            with Image.open(image_path) as img:
                img.verify()  # Verify if it's an image
            print(f"Image {image_path} is valid.")
        except (IOError, SyntaxError) as e:
            print(f"Deleting corrupt image: {image_path} - {e}")
            os.remove(image_path)
