from flask import Flask, request, redirect, session, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from PIL import Image
import io
import os

load_dotenv()

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'heic'}

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})  # to be changed to the actual domain

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/trans", methods=['POST'])
def trans():
    if 'image' not in request.files:
        return jsonify({'error': 'no image provided'}), 400
    
    image = request.files['image']

    extension = image.filename.split('.')[-1]

    if extension not in ALLOWED_EXTENSIONS:
        return jsonify({'error': 'invalid file type'}), 400
    
    image = Image.open(image)

    # process image here
    # (pooja this is where you come in)
    processed_image = image

    response = processed_image.convert('RGB')
    response_io = io.BytesIO()
    response.save(response_io, format='PNG')
    response_io.seek(0)
    return jsonify({'processed_image': response_io.read().hex()}), 200


if __name__ == '__main__':
    app.run(debug=True)