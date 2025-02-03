import requests
from ..common import API_ENDPOINTS, get_headers, handle_response

def get(
    api_key: str,
    app_user_id: str,
    environment: str = "production",
) -> str | None:
    """
    Get a RevenueCat customer.
    """
    base_url = API_ENDPOINTS["v1"][environment]
    url = f"{base_url}/subscribers/{requests.utils.quote(app_user_id)}"

    response = requests.get(url, headers=get_headers(api_key))

    return handle_response(response, [200, 201], True)

def delete(
    api_key: str,
    app_user_id: str,
    environment: str = "production",
) -> str | None:
    """
    Delete a RevenueCat customer.
    """
    base_url = API_ENDPOINTS["v1"][environment]
    url = f"{base_url}/subscribers/{requests.utils.quote(app_user_id)}"
    response = requests.delete(url, headers=get_headers(api_key))

    return handle_response(response, 200)
