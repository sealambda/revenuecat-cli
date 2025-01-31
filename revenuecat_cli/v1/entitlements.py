import requests
from ..common import BASE_URL_V1, get_headers, handle_response

def grant(
    api_key: str,
    app_user_id: str,
    entitlement_id: str,
    end_time_ms: int | None = None,
) -> str | None:
    """
    Grant a RevenueCat entitlement to a user.
    """
    url = f"{BASE_URL_V1}/subscribers/{requests.utils.quote(app_user_id)}/entitlements/{requests.utils.quote(entitlement_id)}/promotional"
    data = {}
    if end_time_ms is None:
        data["duration"] = "lifetime"
    else:
        data["end_time_ms"] = end_time_ms

    response = requests.post(url, json=data, headers=get_headers(api_key))

    return handle_response(response, 201)

def revoke(
    api_key: str,
    app_user_id: str,
    entitlement_id: str,
) -> str | None:
    """
    Revoke a RevenueCat entitlement from a user.
    """
    url = f"{BASE_URL_V1}/subscribers/{requests.utils.quote(app_user_id)}/entitlements/{requests.utils.quote(entitlement_id)}/revoke_promotionals"
    response = requests.post(url, headers=get_headers(api_key))

    return handle_response(response, 200)
