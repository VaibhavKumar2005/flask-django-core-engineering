from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome, Vaibhav!</h1><p>Status: Active</p>'

@app.route('/health')
def health():
    return jsonify({"status": "active", "scale": "basic"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
