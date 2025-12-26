from fastapi import Header, HTTPException
from app.core.config import settings
from app.core.security import verify_access_token

# Dependency to validate API key from request header
def get_api_key(api_key: str = Header(...)):
    """
    Dependency to validate the API key provided in the request header.
    Raises HTTPException if the API key is invalid.
    """
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

# Dependency to validate and extract user information from JWT token
def get_current_user(token: str = Header(...)):
    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid JWT Token")
    return payload