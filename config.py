import os

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("Lack of environment variable: API_KEY")