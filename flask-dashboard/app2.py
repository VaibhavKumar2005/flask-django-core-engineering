# app.py
from flask import Flask, render_template, request, jsonify
# --- THIS IS THE KEY LINE ---
from predictor import get_marks_prediction 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # 1. Get data from the frontend (the JavaScript Fetch call)
    data = request.get_json()
    user_hours = data.get('hours', 0)
    
    # 2. RUN THE PREDICTION using the imported function
    result = get_marks_prediction(user_hours)
    
    # 3. Send the result back as JSON
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True, port=5000)