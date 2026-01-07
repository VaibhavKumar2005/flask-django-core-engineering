from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Project Initialized</h1><p>The Flask server is running on local IP.</p>"

@app.route('/api/v1/health')
def health():
    return jsonify({
        "status": "active",
        "environment": "development",
        "developer": "Vaibhav"
    })

if __name__ == '__main__':
    app.run(debug=True)