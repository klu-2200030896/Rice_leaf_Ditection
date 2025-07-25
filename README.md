# 🌾 RiceLeafDoctor – Rice Leaf Disease Detection using AI

**RiceLeafDoctor** is an AI-based web application that detects diseases in rice leaves using deep learning. The goal is to assist farmers and agricultural professionals in identifying common rice diseases such as **Bacterial Blight**, **Brown Spot**, and **Leaf Smut** by uploading leaf images through a simple web interface.

## 🚀 Features
- ✅ Detects multiple rice leaf diseases using CNN
- 📷 Upload and analyze leaf images via a user-friendly web UI
- 🧠 Built using Python, TensorFlow/Keras for AI, and Flask for deployment
- 🌱 Supports early disease diagnosis for crop health management

## 🗂️ Project Structure

Rice_leaf_Ditection/
├── models/ # Contains trained CNN model (.h5)
├── static/ # Static files (CSS, JS, Images)
├── templates/ # HTML templates for Flask
├── app.py # Flask web server
├── main.py # Model training and evaluation script
├── req.txt # Python package dependencies

bash
Copy
Edit

## 🧑‍💻 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Rice_leaf_Ditection.git
cd Rice_leaf_Ditection
2. Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r req.txt
4. Run the Flask Application
bash
Copy
Edit
python app.py
Open your browser and go to:
http://127.0.0.1:5000/

📂 Dataset (Not Included)
The dataset used to train the model is not included in this repository due to file size limits.

You can download a similar dataset from Kaggle:
🔗 Rice Leaf Disease Dataset - Kaggle

Expected Dataset Folder Structure:
Copy
Edit
dataset/
├── Bacterial_Blight/
├── Brown_Spot/
└── Leaf_Smut/
Make sure the paths in main.py match this structure when training the model.

🧪 Model Training
Use main.py to:

Load and preprocess image data

Train a Convolutional Neural Network

Save the trained model to the models/ directory

📝 To-Do
 Add real-time webcam image prediction

 Include remedy suggestions for each disease

 Deploy the app using Render, Heroku, or similar platforms

👨‍💻 Developed By
Kadarla Srikanth
B.Tech CSE (AI), Koneru Lakshmaiah University
📧 2200030896cseh@gmail.com
🔗 LinkedIn
🔗 GitHub

📄 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute it with proper attribution.

yaml
Copy
Edit

---

✅ You can now paste this directly into a file named `README.md` in your GitHub repo. Let me know if you'd like help creating a deployment section, demo video, or GIF badge integration too!








You said:
like  para so i can co[py paste



ChatGPT said:
Got it, Srikanth! Here's your full README.md content written as a single Markdown block (in paragraph-style text, not split into command/code blocks), so you can copy-paste directly into your GitHub README file with proper formatting:

🌾 RiceLeafDoctor – Rice Leaf Disease Detection using AI
RiceLeafDoctor is an AI-based web application that detects diseases in rice leaves using deep learning. The goal is to assist farmers and agricultural professionals in identifying common rice diseases such as Bacterial Blight, Brown Spot, and Leaf Smut by uploading leaf images through a simple web interface.

🚀 Features
Detects multiple rice leaf diseases using CNN

Upload and analyze leaf images via a user-friendly web UI

Built using Python, TensorFlow/Keras for AI, and Flask for deployment

Supports early disease diagnosis for crop health management

🗂️ Project Structure
graphql
Copy
Edit
Rice_leaf_Ditection/
├── models/           # Contains trained CNN model (.h5)
├── static/           # Static files (CSS, JS, Images)
├── templates/        # HTML templates for Flask
├── app.py            # Flask web server
├── main.py           # Model training and evaluation script
├── req.txt           # Python package dependencies
🧑‍💻 How to Run Locally
Clone the repository:

git clone https://github.com/yourusername/Rice_leaf_Ditection.git

cd Rice_leaf_Ditection

Set up a virtual environment:

python -m venv venv

source venv/bin/activate (or venv\Scripts\activate on Windows)

Install dependencies:

pip install -r req.txt

Run the application:

python app.py

Then, open your browser and visit: http://127.0.0.1:5000/

📂 Dataset (Not Included)
The dataset used to train the model is not included in this repository due to file size limitations. You can download a similar dataset from Kaggle:
Rice Leaf Disease Dataset – Kaggle

After downloading, structure the dataset as follows:

Copy
Edit
dataset/
├── Bacterial_Blight/
├── Brown_Spot/
└── Leaf_Smut/
Ensure that the paths in main.py match this structure for training to work correctly.

🧪 Model Training
Use main.py to preprocess the dataset, train a CNN model, and save the trained model to the models/ directory for use in the Flask application.

📝 To-Do
 Add webcam support for real-time detection

 Improve UI/UX with responsive design and disease remedies

 Deploy the app on Render or Heroku for public access


