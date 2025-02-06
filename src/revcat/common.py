from datetime import datetime
from enum import Enum

import requests


class Duration(str, Enum):
    DAILY = "daily"
    THREE_DAY = "three_day"
    WEEKLY = "weekly"
    TWO_WEEK = "two_week"
    MONTHLY = "monthly"
    TWO_MONTH = "two_month"
    THREE_MONTH = "three_month"
    SIX_MONTH = "six_month"
    YEARLY = "yearly"
    LIFETIME = "lifetime"


class Environment(str, Enum):
    production = "production"
    sandbox = "sandbox"


# 🔗 API Endpoints
API_ENDPOINTS = {
    "v1": {
        Environment.production: "https://api.revenuecat.com/v1",
        Environment.sandbox: "https://api-staging.revenuecat.com/v1",
    },
    "v2": {
        Environment.production: "https://api.revenuecat.com/v2",
        Environment.sandbox: "https://api-staging.revenuecat.com/v2",
    },
}


def get_headers(api_key: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}


def handle_response(
    response: requests.Response,
    success_status_codes: list[int],
    fields: list[str] = None,
    show_output: bool = False,
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


def datetime_to_ms(dt: datetime) -> int:
    return int(dt.timestamp() * 1000)
