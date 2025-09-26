# Insurance Premium Prediction Web App

A web application that predicts insurance premiums based on user inputs using a pre-trained Gradient Boosting model. Built with **Flask**, **pandas**, and **scikit-learn**, this app demonstrates a full-stack deployment for machine learning projects.

---

## 🔹 Features

- Predict insurance premiums based on user inputs:
  - Age
  - Sex
  - BMI
  - Number of children
  - Smoking status
  - Region
- Simple, user-friendly web interface
- Display prediction results instantly

---

## 🛠️ Tech Stack

- **Frontend**: HTML, Bootstrap (via Flask templates)
- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, pandas, joblib
- **Web Server**: Gunicorn
- **Deployment**: Render, Vercel (via serverless or container)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/Abhishekraj276/Insurance.git
cd Insurance
Create and activate a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Ensure the model files are present:

gradient_boosting_model.pkl

feature_names.pkl

🚀 Usage
Run the Flask application locally:

bash
Copy code
python app.py
Open your browser and go to:

cpp
Copy code
http://127.0.0.1:5000
Fill in the form and submit to get the predicted insurance premium.

⚙️ Deployment
On Render
Add a .python-version file in the root with:

Copy code
3.11.7
Render will install dependencies from requirements.txt.

Use Gunicorn as the web server (app:app).

On Vercel
Vercel serverless functions have a 250 MB limit. For large ML models, consider using a container deployment.

📁 File Structure
pgsql
Copy code
Insurance/
├── app.py                  # Flask application
├── gradient_boosting_model.pkl
├── feature_names.pkl
├── templates/
│   ├── index.html
│   └── result.html
├── requirements.txt
└── .python-version
📌 Dependencies
Flask==3.1.2

pandas==2.3.2

numpy==1.27.2

scikit-learn==1.5.1

joblib==1.5.2

gunicorn==23.0.0

⚠️ Notes
Make sure your Python version matches the dependencies to avoid installation issues.

For large ML models, consider container-based deployment instead of serverless functions.

📄 License
This project is licensed under the MIT License.

yaml
Copy code

---

If you want, I can also **add badges** for Python version, license, and GitHub repo stats to make it look professional on GitHub. Do you want me to do that?







Ask ChatGPT
