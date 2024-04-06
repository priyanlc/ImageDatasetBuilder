import os
import easyocr


class EasyOCRProcessor:
    def __init__(self, languages=None):  # Default to Japanese
        if languages is None:
            languages = ['ja']
        self.reader = easyocr.Reader(languages)

    def process_image(self, filename):
        try:
            results = self.reader.readtext(filename, detail=0, paragraph=True)
            japanese_text_detected = len(results) > 0

            if japanese_text_detected:
                os.remove(filename)
                return f"Deleted '{filename}' as Japanese text was detected."
            else:
                return f"Kept '{filename}', no Japanese text detected."
        except Exception as e:
            return f"Error processing '{filename}': {e}, kept the file."
