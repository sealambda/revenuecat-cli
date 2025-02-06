import requests

from ..common import API_ENDPOINTS, get_headers, handle_response


def get(
    api_key: str,
    user_id: str,
    environment: str = "production",
) -> dict:
    """
    Get a RevenueCat customer.
    """
    base_url = API_ENDPOINTS["v1"][environment]
    url = f"{base_url}/subscribers/{requests.utils.quote(user_id)}"

    response = requests.get(url, headers=get_headers(api_key))

    return handle_response(response, [200, 201], ["subscriber"])


def delete(
    api_key: str,
    user_id: str,
    environment: str = "production",
) -> dict:
    """
    Delete a RevenueCat customer.
    """
    base_url = API_ENDPOINTS["v1"][environment]
    url = f"{base_url}/subscribers/{requests.utils.quote(user_id)}"
    response = requests.delete(url, headers=get_headers(api_key))

    return handle_response(response, [200], ["subscriber"])
