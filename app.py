from flask import Flask, request, redirect, session, jsonify, send_file
from dotenv import load_dotenv
from flask_cors import CORS
from PIL import Image
import io
import os
from ImageToColors import ImageToColors
import base64

load_dotenv()

CONVERTER = ImageToColors()

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'heic'}

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})  # to be changed to the actual domain

# @app.route("/")
# def hello_world():
    # return "<p>Hello, World!</p>"

def downscale(image):
    r = 100 / image.width
    return image.resize((int(image.width * r), int(image.height * r)))

@app.route("/trans", methods=['POST'])
def trans():
    image = request.files.get('input-image', None)
    if image is None:
        print('no image provided')
        return jsonify({'error': 'no image provided'}), 400
    extension = image.filename.split('.')[-1]

    if extension not in ALLOWED_EXTENSIONS:
        print('invalid file type')
        return jsonify({'error': 'invalid file type'}), 400
    
    image = Image.open(image)

    # process image here
    # (pooja this is where you come in)
    processed_image = downscale(image)

    response = processed_image.convert('RGB')
    response_io = io.BytesIO()
    response.save(response_io, format='PNG')
    response_io.seek(0)
    processed_image_data = base64.b64encode(response_io.getvalue()).decode('utf-8')

    print('returning processed image')
    return send_file(response_io, mimetype='image/png')
    # return jsonify({'processedImage': processed_image_data}), 200


if __name__ == '__main__':
    app.run(debug=True, port=8888)