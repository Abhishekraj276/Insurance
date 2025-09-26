from flask import Flask, render_template, request
import joblib
import pandas as pd

model = joblib.load("gradient_boosting_model.pkl")
feature_names = joblib.load("feature_names.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:

        age = int(request.form["age"])
        sex = request.form["sex"]
        bmi = float(request.form["bmi"])
        children = int(request.form["children"])
        smoker = request.form["smoker"]
        region = request.form["region"]


        input_dict = {
            "age": [age],
            "bmi": [bmi],
            "children": [children],
            "sex": [sex],
            "smoker": [smoker],
            "region": [region]
        }
        df_input = pd.DataFrame(input_dict)

        df_input = pd.get_dummies(df_input, columns=["sex", "smoker", "region"], drop_first=True)

        for col in feature_names:
            if col not in df_input.columns:
                df_input[col] = 0
        df_input = df_input[feature_names]

        prediction = model.predict(df_input)[0] 

       
        return render_template("result.html", prediction=prediction)

    except Exception as e:
        return render_template("result.html", prediction=None, error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
