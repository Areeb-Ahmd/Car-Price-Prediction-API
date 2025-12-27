# Car Price Prediction API

This project is a **Machine Learning-powered API** built using **FastAPI** to predict the selling price of a used car based on its characteristics.

---

## 📦 Project Features

- 🔐 **Authentication**: JWT-based token authentication with API key validation
- 🧠 **ML Model Prediction**: Trained model predicts used car prices using Scikit-learn
- ⚡ **Redis Caching**: Avoid redundant model computation with intelligent caching
- 📈 **Monitoring Ready**: Prometheus metrics integration for production monitoring
- 🐳 **Dockerized Setup**: Simplified deployment with Docker Compose
- ☁️ **Cloud Deployment**: Easily deploy to [Render](https://render.com)
- 📝 **Logging Middleware**: Request/response logging for debugging and monitoring

---

## 🧠 Model Input Variables

The prediction model expects the following input features:

| Feature           | Type    | Description                          | Example         |
|-------------------|---------|--------------------------------------|-----------------|
| `company`         | string  | Brand of the car                     | `"Maruti"`      |
| `year`            | integer | Year of manufacturing                | `2015`          |
| `owner`           | string  | Number of previous owners            | `"Second"`      |
| `fuel`            | string  | Fuel type                            | `"Petrol"`      |
| `seller_type`     | string  | Individual or Dealer                 | `"Individual"`  |
| `transmission`    | string  | Transmission type                    | `"Manual"`      |
| `km_driven`       | integer | Kilometers driven                    | `200000`        |
| `mileage_mpg`     | float   | Mileage in miles per gallon          | `55.0`          |
| `engine_cc`       | float   | Engine capacity in cc                | `1250.0`        |
| `max_power_bhp`   | float   | Maximum power in BHP                 | `80.0`          |
| `torque_nm`       | float   | Torque in Newton meters              | `200.0`         |
| `seats`           | float   | Number of seats                      | `5.0`           |

---

## 🚀 Getting Started (Local)

### 1. Clone the Repository
```bash
git clone https://github.com/Areeb-Ahmd/Car-Price-Prediction-API.git
cd Car-Price-Prediction-API
```

### 2. Set Environment Variables
Create a `.env` file in the project root:
```bash
API_KEY=demo-key
JWT_SECRET_KEY=secret
REDIS_URL=redis://localhost:6379
```

### 3. Install Dependencies (Without Docker)
```bash
pip install -r requirements.txt
```

### 4. Run the Application

**Option A: Using Docker Compose (Recommended)**
```bash
docker-compose up --build
```

**Option B: Run Locally**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Access the API
- **API Documentation (Swagger UI)**: http://localhost:8000/docs
- **Alternative API Docs (ReDoc)**: http://localhost:8000/redoc
- **Prometheus Metrics**: http://localhost:8000/metrics
- **Prometheus UI**: http://localhost:9090 (if using Docker Compose)

---

## 📡 API Endpoints

### Authentication
| Method | Endpoint  | Description                    | Auth Required |
|--------|-----------|--------------------------------|---------------|
| POST   | `/login`  | Get JWT access token           | ❌            |

**Login Credentials:**
- Username: `admin`
- Password: `admin`

### Prediction
| Method | Endpoint    | Description              | Auth Required |
|--------|-------------|--------------------------|---------------|
| POST   | `/predict`  | Predict car price        | ✅ (JWT + API Key) |

### Monitoring
| Method | Endpoint   | Description                    | Auth Required |
|--------|------------|--------------------------------|---------------|
| GET    | `/metrics` | Prometheus metrics endpoint    | ❌            |

---

## 🧪 Example API Usage

### 1. Login to Get Access Token
```bash
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "admin"
  }'
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### 2. Predict Car Price
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Authorization: Bearer <your_access_token>" \
  -H "X-API-Key: demo-key" \
  -H "Content-Type: application/json" \
  -d '{
    "company": "Maruti",
    "year": 2015,
    "owner": "Second",
    "fuel": "Petrol",
    "seller_type": "Individual",
    "transmission": "Manual",
    "km_driven": 50000,
    "mileage_mpg": 55.0,
    "engine_cc": 1250.0,
    "max_power_bhp": 80.0,
    "torque_nm": 200.0,
    "seats": 5.0
  }'
```

**Response:**
```json
{
  "The Predicted Car Price is:": "₹4,50,000"
}
```

---

## 🚀 Deployment on Render

### Prerequisites
- GitHub account with your repository
- Render account ([Sign up here](https://render.com))

### Deployment Steps

1. **Push your code to GitHub**
```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
```

2. **Connect to Render**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure the Web Service**
   - **Name**: `car-price-prediction-api`
   - **Environment**: `Docker`
   - **Region**: Choose closest to your users
   - **Branch**: `main`

4. **Add Environment Variables**
```
   API_KEY=your-secure-api-key
   JWT_SECRET_KEY=your-secure-jwt-secret
   REDIS_URL=your-redis-url
```

5. **Deploy**
   - Click "Create Web Service"
   - Wait for the build to complete
   - Your API will be live at `https://your-app-name.onrender.com`

---

## 🛠️ Tech Stack

- **Backend Framework**: FastAPI
- **ML Framework**: Scikit-learn (Joblib for model serialization)
- **Caching**: Redis
- **Monitoring**: Prometheus + Grafana (optional)
- **Authentication**: JWT (JSON Web Tokens)
- **Containerization**: Docker & Docker Compose
- **Deployment**: Render
- **Data Validation**: Pydantic

---

## 📂 Project Structure
```
Car-Price-Prediction-API/
├── app/
│   ├── __init__.py
│   ├── main.py                      # FastAPI application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes_auth.py           # Authentication endpoints
│   │   └── routes_predict.py        # Prediction endpoints
│   ├── cache/
│   │   └── redis_cache.py           # Redis caching logic
│   ├── core/
│   │   ├── config.py                # Configuration management
│   │   ├── dependencies.py          # Dependency injection
│   │   ├── exceptions.py            # Custom exceptions
│   │   └── security.py              # JWT token handling
│   ├── middleware/
│   │   └── logging_middleware.py    # Request/response logging
│   ├── models/
│   │   └── prediction_model.joblib  # Trained ML model
│   └── services/
│       └── model_service.py         # Model prediction logic
├── data/
│   └── car-details.csv              # Training dataset
├── notebooks/
│   ├── car-details.csv              # Dataset for exploration
│   └── sample.ipynb                 # Jupyter notebook for analysis
├── training/
│   ├── __init__.py
│   ├── train_model.py               # Model training script
│   └── train_utils.py               # Training utilities
├── .env                             # Environment variables
├── .gitignore                       # Git ignore file
├── docker-compose.yml               # Docker orchestration
├── Dockerfile                       # Container configuration
├── prometheus.yml                   # Prometheus configuration
├── render.yaml                      # Render deployment config
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

---

## 🔧 Configuration

### Environment Variables

| Variable          | Description                    | Default              |
|-------------------|--------------------------------|----------------------|
| `API_KEY`         | API key for authentication     | `demo-key`           |
| `JWT_SECRET_KEY`  | Secret key for JWT tokens      | `secret`             |
| `REDIS_URL`       | Redis connection URL           | `redis://localhost:6379` |

---

## 🧪 Model Training

To retrain the model with new data:

1. **Prepare your dataset** in `data/car-details.csv`

2. **Run the training script**:
```bash
   python -m training.train_model
```

3. **The trained model** will be saved to `app/models/prediction_model.joblib`

---

## 📊 Monitoring

### Prometheus Metrics
The API exposes Prometheus metrics at `/metrics` endpoint:
- Request count
- Request duration
- Response status codes
- Active requests

### Access Prometheus UI (Docker only)
```
http://localhost:9090
```

### Grafana Setup (Optional)
1. Access Grafana at `http://localhost:3000`
2. Default credentials: `admin` / `admin`
3. Add Prometheus as data source: `http://prometheus:9090`
4. Import dashboards for FastAPI metrics

---

## 🧹 Redis Cache Management

The API uses Redis to cache prediction results:
- **Cache Key Format**: `predict:{hash_of_input_features}`
- **TTL**: Configurable (default: 1 hour)
- **Benefits**: Reduces model inference time for repeated requests

---

## 🤝 Contributing

Contributions are always welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Made with ❤️ by **Syed Areeb Ahmad**

---

## 😇 Connect With Me

I'd love to connect with you! Feel free to reach out:

- 📧 **Email**: [ahmad.syedareeb7@gmail.com](mailto:ahmad.syedareeb7@gmail.com)
- 💼 **LinkedIn**: [linkedin.com/in/areeb-ahmad7](https://www.linkedin.com/in/areeb-ahmad7)
- 🐙 **GitHub**: [@Areeb-Ahmd](https://github.com/Areeb-Ahmd)

---

⭐ **If you found this project helpful, please give it a star!** ⭐

---
