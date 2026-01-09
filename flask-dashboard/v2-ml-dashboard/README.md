# 🧠 V2: ML Marks Predictor Dashboard

A full-stack AI microservice that predicts student exam scores based on study hours using **Linear Regression**.

## 🏗️ Architecture
* **Backend:** Flask (Python)
* **ML Engine:** Scikit-Learn + Numpy
* **Frontend:** HTML5 + JavaScript (Fetch API)
* **Container:** Docker (Optimized to ~200MB)

## 🤖 The Model
The model is trained on student study data. It uses a simple linear equation:
> $y = mx + c$
* **Input (x):** Hours Studied
* **Output (y):** Predicted Percentage

## 🚀 How to Run
Pull the pre-built image from Docker Hub to skip the build time:

```bash
docker run -p 5000:5000 vaibhavkumar0412/flask-ml-dashboard:v3-app2