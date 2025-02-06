from datetime import datetime

import requests
from requests.compat import quote

from ..common import (
    API_ENDPOINTS,
    Duration,
    Environment,
    datetime_to_ms,
    get_headers,
    handle_response,
)


def grant(
    api_key: str,
    user_id: str,
    entitlement_id: str,
    end_time: datetime | None,
    duration: Duration | None,
    start_time: datetime | None,
    environment: Environment,
) -> dict:
    """
    Grant a RevenueCat entitlement to a user.
    """
    base_url = API_ENDPOINTS["v1"][environment]
    url = (
        f"{base_url}/subscribers"
        f"/{quote(user_id)}/entitlements"
        f"/{quote(entitlement_id)}/promotional"
    )
    data = {}

    if end_time is None:
        data["duration"] = duration
    else:
        data["end_time_ms"] = datetime_to_ms(end_time)

    if start_time is not None:
        data["start_time_ms"] = datetime_to_ms(start_time)

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
    url = (
        f"{base_url}/subscribers"
        f"/{quote(user_id)}/entitlements"
        f"/{quote(entitlement_id)}/revoke_promotionals"
    )
    response = requests.post(url, headers=get_headers(api_key))

    return handle_response(response, [200], ["subscriber"])
