from flask import Flask, request, jsonify, render_template
import face_recognition
import cv2
import numpy as np

app = Flask(__name__)

# Home route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle image upload and face recognition
@app.route('/recognize', methods=['POST'])
def recognize_face():
    # Get the image file from the form
    file = request.files['image']
    
    # Convert the image to an array using face_recognition
    image = face_recognition.load_image_file(file)
    
    # Find all faces in the image
    face_locations = face_recognition.face_locations(image)
    
    # Return the number of faces found
    return jsonify({'face_count': len(face_locations)})

if __name__ == '__main__':
    app.run(debug=True)
