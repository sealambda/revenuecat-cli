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
    fields: list[str] = None,
    show_output: bool = False
) -> dict:
    response_json = response.json()
    
    if show_output:
        print(response_json)

    if response.status_code not in success_status_codes:
        print(f"Error: {response_json}")

    if not fields:
        return response_json
    
    if len(fields) == 1:
        return response_json[fields[0]]
    
    return {field: response_json[field] for field in fields}