import requests
from ..common import API_ENDPOINTS, get_headers, handle_response

def grant(
    api_key: str,
    user_id: str,
    entitlement_id: str,
    end_time_ms: int | None = None,
    environment: str = "production",
) -> dict:
    """
    Grant a RevenueCat entitlement to a user.
    """
    base_url = API_ENDPOINTS["v1"][environment]
    url = f"{base_url}/subscribers/{requests.utils.quote(user_id)}/entitlements/{requests.utils.quote(entitlement_id)}/promotional"
    data = {}
    if end_time_ms is None:
        data["duration"] = "lifetime"
    else:
        data["end_time_ms"] = end_time_ms

    response = requests.post(url, json=data, headers=get_headers(api_key))

    return handle_response(response, [201], ["subscriber"])

def revoke(
    api_key: str,
    user_id: str,
    entitlement_id: str,
    environment: str = "production",
) -> dict:
    """
    Revoke a RevenueCat entitlement from a user.
    """
    base_url = API_ENDPOINTS["v1"][environment]
    url = f"{base_url}/subscribers/{requests.utils.quote(user_id)}/entitlements/{requests.utils.quote(entitlement_id)}/revoke_promotionals"
    response = requests.post(url, headers=get_headers(api_key))

    return handle_response(response, [200], ["subscriber"])
