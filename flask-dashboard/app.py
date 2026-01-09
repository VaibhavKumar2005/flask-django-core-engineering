from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    user_name = "Vaibhav"
    project_status = "44 Contributions & Counting"
    
    # We are returning a f-string (formatted string) to see the change
    return f"""
    <h1>Welcome, {user_name}!</h1>
    <p>Current Progress: <strong>{project_status}</strong></p>
    <hr>
    <a href="/api/v1/health">Check API Health</a>
    """

@app.route('/api/v1/health')
def health():
    return jsonify({
        "status": "active",
        "environment": "development",
        "developer": "Vaibhav"
    })

if __name__ == '__main__':
    app.run(debug=True)
