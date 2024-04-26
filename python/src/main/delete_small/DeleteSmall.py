import os

from main.common.ImageRemover import ImageRemover


class DeleteSmallImages:
    def __init__(self, min_size_kb, max_size_mb):
        self.min_size_bytes = min_size_kb * 1024
        self.max_size_bytes = max_size_mb * 1024 * 1024

    def delete_images_by_size(self, directory):
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(('.jpg', '.jpeg')):
                    file_path = os.path.join(root, file)
                    file_size_bytes = os.path.getsize(file_path)

                    if file_size_bytes < self.min_size_bytes or file_size_bytes > self.max_size_bytes:
                        ImageRemover.remove_image(file_path)
                        print(f"Deleted '{file_path}' as its size was outside the allowed range.")
