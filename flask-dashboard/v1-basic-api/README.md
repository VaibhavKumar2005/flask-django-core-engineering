# 🩺 V1: Basic Health API

A lightweight Flask service designed to test container orchestration and health checks.

## ⚙️ Tech Stack
* **Python 3.11 Slim**
* **Flask** (No heavy ML libraries)

## 🔌 API Endpoints
### 1. Home
* **URL:** `/`
* **Response:** HTML Welcome Page.

### 2. Health Check
* **URL:** `/health`
* **Response:**
```json
{
  "status": "active",
  "scale": "basic"
}