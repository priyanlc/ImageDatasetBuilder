from multiprocessing import get_context
import os

class ImageBatchProcessor:
    def __init__(self, processor, batch_size=60, num_processes=4):
        self.processor = processor
        self.batch_size = batch_size
        self.num_processes = num_processes

    def process_batch(self, batch):
        with get_context("spawn").Pool(self.num_processes) as pool:
            results = pool.map(self.processor.process_image, batch)
        for result in results:
            print(result)

    def process_folder(self, folder_path):
        image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".jpg")]

        for i in range(0, len(image_files), self.batch_size):
            batch = image_files[i:i + self.batch_size]
            self.process_batch(batch)
