from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

@app.route('/draw', methods=['POST'])
def draw_image():
    
    data = request.json
    text = data.get("text", "Hello, World!")

    img = Image.new('RGB', (400, 200), color = (255, 255, 255))
    d = ImageDraw.Draw(img)

    font = ImageFont.load_default()
    d.text((10, 90), text, fill=(0, 0, 0), font=font)

    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
