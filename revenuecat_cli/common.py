import requests
from typing import Dict

# 🔗 API Endpoints
API_ENDPOINTS = {
    "v1": {
        "production": "https://api.revenuecat.com/v1",
        "sandbox": "https://api-staging.revenuecat.com/v1"
    },
    "v2": {
        "production": "https://api.revenuecat.com/v2",
        "sandbox": "https://api-staging.revenuecat.com/v2"
    }
}

def get_headers(
    api_key: str
) -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

def handle_response(
    response: requests.Response, 
    success_status_codes: list[int],
    show_output: bool = False
) -> str | None:
    response_json = response.json()
    
    if show_output:
        print(response_json)

    if response.status_code not in success_status_codes:
        return f"Error: {response_json}"
    
    return None
