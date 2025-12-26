import joblib
import pandas as pd
from app.core.config import settings
from app.cache.redis_cache import set_cached_prediction, get_cached_prediction

# Load the model
model = joblib.load(settings.MODEL_PATH)

# Prediction 
def predict_car_price(data: dict):
    cache_key = " ".join([str(val) for val in data.values()])
    # Check if cache_key is already available
    cached = get_cached_prediction(cache_key)
    if cached:
        return cached
    
    # Make new prediction
    input_data = pd.DataFrame([data])
    prediction = model.predict(input_data)[0]
    # Store prediction in cache
    set_cached_prediction(cache_key, prediction)
    return prediction