from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "secret"

def create_access_token(username):
    expire = datetime.utcnow() + timedelta(hours=1)

    payload = {
        "sub": username,
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )