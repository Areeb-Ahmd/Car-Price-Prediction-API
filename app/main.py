from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth, routes_predict
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers

# Define FastAPI app
app = FastAPI(title="Car Price Prediction API")

# Link Middleware
app.add_middleware(LoggingMiddleware)

# Link Routes/Endpoints
app.include_router(routes_auth.router, tags=['Auth'])
app.include_router(routes_predict.router, tags=['Prediction'])

# Monitoring with Prometheus
Instrumentator().instrument(app).expose(app)

# Register custom exception handlers
register_exception_handlers(app)