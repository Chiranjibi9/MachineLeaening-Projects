from flask import Flask, request, jsonify, render_template
import json
import pickle
import numpy as np

app = Flask(__name__)

# Load model and data
with open("columns.json", "r") as f:
    columns = json.load(f)["data_columns"]

model = pickle.load(open("Bengaluru_House-Model.pkl", "rb"))

# Extract locations (ignore first 3 columns: sqft, bath, bhk)
locations = columns[3:]

@app.route("/")
def home():
    return render_template("predict.html", locations=locations)

@app.route("/predict", methods=["POST"])
def predict():
    total_sqft = float(request.form["total_sqft"])
    bhk = int(request.form["bhk"])
    bath = int(request.form["bath"])
    location = request.form["location"]

    # Create input array
    input_data = np.zeros(len(columns))
    input_data[0] = total_sqft
    input_data[1] = bath
    input_data[2] = bhk

    if location in columns:
        loc_index = columns.index(location)
        input_data[loc_index] = 1

    # Predict price
    predicted_price = model.predict([input_data])[0]

    return f"Predicted House Price: ₹{predicted_price:.2f} Lakhs"

if __name__ == "__main__":
    app.run(debug=True)
