from flask import Flask, request, redirect, session, jsonify, send_file
from dotenv import load_dotenv
from flask_cors import CORS
from PIL import Image
from io import BytesIO
import os
import numpy as np

load_dotenv()

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'heic'}

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})  # to be changed to the actual domain

def generate_image():
    image = Image.new('RGB', (200, 200), color="blue")
    img_io = BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io

@app.route("/test-image", methods=["GET"])
def get_image():
    img_io = generate_image()
    return send_file(img_io, mimetype="image/png")

@app.route("/mirror", methods=["GET", "POST"])
def mirror():
    uploaded_image = request.files['image']
    img = Image.open(uploaded_image)
    img_array = np.array(img)
    mirrored_img_array = np.fliplr(img_array)
    mirrored_img = Image.fromarray(mirrored_img_array)
    mirrored_img_io = BytesIO()
    mirrored_img.save(mirrored_img_io, format="PNG")
    mirrored_img_io.seek(0)
    return send_file(mirrored_img_io, mimetype="image/png")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello", methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from Crochet Web App!'})

# @app.route("/trans", methods=['POST'])
# def trans():
#     if 'image' not in request.files:
#         return jsonify({'error': 'no image provided'}), 400
#     
#     image = request.files['image']
# 
#     extension = image.filename.split('.')[-1]
# 
#     if extension not in ALLOWED_EXTENSIONS:
#         return jsonify({'error': 'invalid file type'}), 400
#     
#     image = Image.open(image)
# 
#     # process image here
#     # (pooja this is where you come in)
#     processed_image = image
# 
#     response = processed_image.convert('RGB')
#     response_io = io.BytesIO()
#     response.save(response_io, format='PNG')
#     response_io.seek(0)
#     return jsonify({'processed_image': response_io.read().hex()}), 200


if __name__ == '__main__':
    app.run(debug=True, port=3000)
