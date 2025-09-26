Insurance Premium Prediction Web App
https://img.shields.io/badge/python-3.11.7-blue
https://img.shields.io/badge/Flask-3.1.2-green
https://img.shields.io/badge/License-MIT-green
https://img.shields.io/github/stars/Abhishekraj276/Insurance?style=social

A machine learning web application that predicts insurance premiums based on user demographics using a Gradient Boosting model. Built with Flask and scikit-learn.

https://via.placeholder.com/800x400/4A90E2/FFFFFF?text=Insurance+Premium+Prediction+App

🚀 Features
Accurate Predictions: Uses Gradient Boosting algorithm for reliable premium estimates

User-Friendly Interface: Clean, responsive web form built with Bootstrap

Real-time Results: Instant predictions without page reload

Input Validation: Comprehensive client and server-side validation

RESTful API: JSON API endpoint for programmatic access

Deployment Ready: Configured for Render, Vercel, and other platforms

📊 Input Parameters
Parameter	Description	Range/Options
Age	Policyholder's age	18 - 100 years
Sex	Biological sex	Male / Female
BMI	Body Mass Index	10.0 - 50.0
Children	Number of dependents	0 - 10
Smoker	Tobacco usage	Yes / No
Region	Geographic region	Northeast, Northwest, Southeast, Southwest
🛠️ Tech Stack
Backend: Python 3.11.7, Flask 3.1.2

Machine Learning: scikit-learn, pandas, numpy

Frontend: HTML5, Bootstrap 5, JavaScript

Model Serialization: joblib

Deployment: Gunicorn, Render, Vercel

📦 Installation
Prerequisites
Python 3.11.7 or higher

pip (Python package manager)

Step-by-Step Setup
Clone the repository

bash
git clone https://github.com/Abhishekraj276/Insurance.git
cd Insurance
Create virtual environment

bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Run the application

bash
python app.py
Open your browser and navigate to:

text
http://localhost:5000
🎯 Usage
Web Interface
Fill in the form with your details

Click "Predict Premium"

View the estimated insurance premium

API Usage
bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 35,
    "sex": "male", 
    "bmi": 28.5,
    "children": 2,
    "smoker": "no",
    "region": "northwest"
  }'
Response:

json
{
  "success": true,
  "prediction": 8450.75,
  "parameters": {
    "age": 35,
    "sex": "male",
    "bmi": 28.5,
    "children": 2,
    "smoker": "no",
    "region": "northwest"
  }
}
🌐 Deployment
Deploy on Render (Recommended)
Fork this repository

Create a new Web Service on Render

Connect your GitHub repository

Use these settings:

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

Deploy!

Deploy on Vercel
bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
📁 Project Structure
text
Insurance/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .python-version       # Python version specification
├── gradient_boosting_model.pkl    # Trained ML model
├── feature_names.pkl     # Model feature names
└── README.md             # Project documentation
🔧 API Endpoints
Endpoint	Method	Description
/	GET	Main web interface
/predict	POST	Premium prediction API
/health	GET	Health check endpoint
🧪 Testing
The application includes automatic sample model creation for testing:

python
# If model files are missing, a sample model is created automatically
python app.py
📈 Model Information
Algorithm: Gradient Boosting Regressor

Features: 8 engineered features including one-hot encoding

Training: Pre-trained model included

Accuracy: High predictive performance on insurance data

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🐛 Troubleshooting
Common Issues
ModuleNotFoundError: No module named 'flask'

bash
# Ensure virtual environment is activated and dependencies installed
source venv/bin/activate
pip install -r requirements.txt
Model file not found

The application will automatically create a sample model for testing

Port already in use

bash
# Use a different port
python app.py --port 5001
📞 Support
If you encounter any problems or have questions:

Check the Issues page

Create a new issue with detailed description

Provide your Python version and error logs

🙏 Acknowledgments
scikit-learn team for the machine learning library

Flask team for the web framework

Bootstrap team for the UI components

<div align="center">
⭐ Don't forget to star this repository if you find it helpful!

https://img.shields.io/github/stars/Abhishekraj276/Insurance?style=social

</div>
