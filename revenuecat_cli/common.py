import requests
from typing import Dict

# 🔗 API Endpoints
BASE_URL_V1 = "https://api.revenuecat.com/v1"
BASE_URL_V2 = "https://api.revenuecat.com/v2"

def get_headers(
    api_key: str
) -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

def handle_response(response: requests.Response, success_status_code: int) -> str | None:
    if response.status_code != success_status_code:
        return f"Error: {response.json()}"
    
    return None
