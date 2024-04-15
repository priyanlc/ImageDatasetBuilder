from multiprocessing import Pool, cpu_count
import time
import os

from main.face_filter2.DeepFaceAnalyzer import DeepFaceAnalyzer


class ImageProcessor:
    def __init__(self, folder_path, num_processes=1):
        self.folder_path = folder_path
        self.num_processes = num_processes

    def process_images(self):
        start_time = time.time()
        image_files = [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path) if f.endswith(".jpg")]

        with Pool(self.num_processes) as pool:
            results = pool.map(DeepFaceAnalyzer.process_image, image_files)

        for result in results:
            print(result)

        end_time = time.time()
        print(f"Time taken to execute: {end_time - start_time} seconds.")
