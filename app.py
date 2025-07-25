import sys
import os
from flask import Flask, render_template, request
import torch
from torchvision import transforms
from PIL import Image

# Add the model directory to the Python path
sys.path.append(os.path.join(os.getcwd(), 'models'))

# Import the CNN model from the model directory
from models.model import CNNModel  # Assuming CNNModel is in model.py in the models directory

# Initialize Flask app
app = Flask(__name__)

# Load the trained model (make sure to have the model.pth file in the correct path)
model = CNNModel(num_classes=3)  # Make sure the model architecture is correct here
model.load_state_dict(torch.load('models/models/model.pth'))  # Update path if necessary
model.eval()  # Set the model to evaluation mode

# Image transformation (same as used during training)
transform = transforms.Compose([
    transforms.Resize((128, 128)),  # Adjust the size if necessary
    transforms.ToTensor(),
])

# Class names (adjust based on your dataset)
class_names = ['Bacterial Leaf Blight', 'Brown Spot', 'Leaf Smut']

# Fertilizer recommendations for each class
fertilizer_recommendations = {
    'Bacterial Leaf Blight': 'Use Nitrogen-rich fertilizer. Apply 50kg/acre.',
    'Brown Spot': 'Apply Phosphorus-based fertilizer. Use 45kg/acre.',
    'Leaf Smut': 'Use Potassium-based fertilizer. Apply 40kg/acre.'
}


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400

    # Save file temporarily
    image_path = os.path.join('static', file.filename)
    file.save(image_path)

    # Open and transform the image
    image = Image.open(image_path)
    image = transform(image).unsqueeze(0)  # Add batch dimension

    # Prediction
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)

    predicted_class = class_names[predicted.item()]
    fertilizer = fertilizer_recommendations[predicted_class]

    result = {
        'disease': predicted_class,
        'fertilizer': fertilizer
    }

    # Return the result to the HTML page
    return render_template('home.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
