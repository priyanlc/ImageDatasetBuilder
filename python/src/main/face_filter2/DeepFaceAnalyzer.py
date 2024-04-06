from deepface import DeepFace

class DeepFaceAnalyzer:
    @staticmethod
    def process_image(filename):
        try:
            analysis = DeepFace.analyze(img_path=filename, actions=['emotion'], enforce_detection=False)
            return f"Kept '{filename}', faces detected."
        except Exception as e:
            if 'OOM' in str(e):
                return f"Skipped '{filename}' due to memory constraints."
            try:
                os.remove(filename)
                return f"Deleted '{filename}' as no faces were detected or error occurred: {e}"
            except Exception as del_error:
                return f"Error processing '{filename}': {e}, and error deleting: {del_error}"
