import os
import face_recognition


class FaceImageProcessor:
    @staticmethod
    def process_image(filename):
        try:
            image = face_recognition.load_image_file(filename)
            face_locations = face_recognition.face_locations(image)

            if not face_locations:
                os.remove(filename)
                return f"Deleted '{filename}' as no faces were detected."
            else:
                return f"Kept '{filename}', faces detected."

        except Exception as e:
            try:
                os.remove(filename)
                return f"Deleted '{filename}' due to error opening file: {e}"
            except Exception as del_error:
                return f"Error processing '{filename}': {e}, and error deleting: {del_error}"
