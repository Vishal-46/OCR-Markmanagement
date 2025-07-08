from PIL import Image
import pytesseract
import tempfile

def process_uploaded_images(files):
    data = []
    for file in files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name

        img = Image.open(tmp_path)
        text = pytesseract.image_to_string(img)

        # Dummy extraction logic (replace with actual regex/parser)
        lines = text.splitlines()
        if len(lines) >= 3:
            data.append({
                "Register Number": lines[0].strip(),
                "Name": lines[1].strip(),
                "Subject Code": lines[2].strip(),
                "Mark": int(lines[3].strip()) if lines[3].strip().isdigit() else 0
            })
    return data