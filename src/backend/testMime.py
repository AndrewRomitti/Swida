from PIL import Image
import io

def get_mime_type_from_bytes(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    return f'image/{image.format.lower()}'