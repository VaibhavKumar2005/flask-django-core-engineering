from flask import Flask, render_template, request, jsonify
from predictor import get_marks_prediction 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    hours = data.get('hours', 0)
    result = get_marks_prediction(hours)
    return jsonify({'prediction': result})

if __name__ == '__main__':
    # FIXED: host='0.0.0.0' allows external access from Windows
    app.run(debug=True, host='0.0.0.0', port=5000)
