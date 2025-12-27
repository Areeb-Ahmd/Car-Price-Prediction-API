# Car Price Prediction API

This project is a **Machine Learning-powered API** built using **FastAPI** to predict the selling price of a used car based on its characteristics.

---

## 📦 Project Features

- 🔐 **Authentication**: JWT-based token auth and API key validation
- 🧠 **ML Model Prediction**: Trained model predicts used car prices
- ⚡ **Redis Caching**: Avoid redundant model computation
- 📈 **Monitoring Ready**: Prometheus metrics + Grafana dashboards
- 🐳 **Dockerized Setup**: Simplified deployment with Docker Compose
- ☁️ **Cloud Deployment**: Easily deploy to [Render](https://render.com)

---

## 🧠 Model Input Variables

The prediction model expects the following input features:

| Feature           | Description                          | Example         |
|-------------------|--------------------------------------|-----------------|
| `company`         | Brand of the car                     | `"Maruti"`      |
| `year`            | Year of manufacturing                | `2015`          |
| `owner`           | Number of previous owners            | `"Second"`      |
| `fuel`            | Fuel type                            | `"Petrol"`      |
| `seller_type`     | Individual or Dealer                 | `"Individual"`  |
| `transmission`    | Transmission type                    | `"Automatic"`   |
| `km_driven`       | Kilometers driven                    | `200000`        |
| `mileage_mpg`     | Mileage in miles per gallon          | `55`            |
| `engine_cc`       | Engine capacity in cc                | `1250`          |
| `max_power_bhp`   | Maximum power in BHP                 | `80`            |
| `torque_nm`       | Torque in Newton meters              | `200`           |
| `seats`           | Number of seats                      | `5`             |

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
JWT_SECRET_KEY=your-secret
REDIS_URL=redis://localhost:6379
```

### 3. Build and Run via Docker
```bash
docker-compose up --build
```

### 4. Access Interfaces
- **FastAPI Docs**: http://localhost:8000/docs
- **FastAPI Metrics**: http://localhost:8000/metrics
- **Prometheus UI**: http://localhost:9090
- **Grafana UI**: http://localhost:3000

---

## 📡 API Endpoints

### Authentication
- `POST /token` - Get JWT access token
- `POST /register` - Register new user

### Prediction
- `POST /predict` - Predict car price (requires authentication)

### Health Check
- `GET /health` - Check API status

---

## 🧪 Example API Request
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Authorization: Bearer <your_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "company": "Maruti",
    "year": 2015,
    "owner": "Second",
    "fuel": "Petrol",
    "seller_type": "Individual",
    "transmission": "Automatic",
    "km_driven": 200000,
    "mileage_mpg": 55,
    "engine_cc": 1250,
    "max_power_bhp": 80,
    "torque_nm": 200,
    "seats": 5
  }'
```

---

## 🚀 Deployment on Render (API only)

1. Push code to GitHub
2. Add `render.yaml` to the project root
3. Create a new Web Service on Render
4. Include environment variables:
   - `API_KEY`
   - `JWT_SECRET_KEY`
   - `REDIS_URL`

---

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **ML Framework**: Scikit-learn
- **Caching**: Redis
- **Monitoring**: Prometheus + Grafana
- **Containerization**: Docker & Docker Compose
- **Authentication**: JWT tokens

---

## 📂 Project Structure
```
Car-Price-Prediction-API/
├── app/
│   ├── main.py              # FastAPI application
│   ├── models/              # ML models
│   ├── routers/             # API routes
│   └── utils/               # Helper functions
├── docker-compose.yml       # Docker orchestration
├── Dockerfile               # Container configuration
├── requirements.txt         # Python dependencies
└── README.md               # Project documentation
```

---

## 🤝 Contributing

Feel free to fork this repo, open issues, and submit pull requests. Contributions are always welcome!

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Made with ❤️ by **Syed Areeb Ahmad**

---

## 😇 Connect

Feel free to connect:
- 📧 [Email](mailto:ahmad.syedareeb7@gmail.com)
- 💼 [LinkedIn](https://www.linkedin.com/in/areeb-ahmad7)
- 🐙 [GitHub](https://github.com/Areeb-Ahmd)

---

⭐ **If you found this project helpful, please give it a star!**