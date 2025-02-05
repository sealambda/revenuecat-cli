import csv
from . import customers, entitlements
from datetime import datetime
import time

def grant_entitlement_from_export(
    api_key: str,
    file_path: str,
    entitlement_id: str,
    end_time_ms: int | None = None,
    user_id_field: str = "app_user_id",
    environment: str = "production",
    seconds_per_request: int = 1,
) -> bool:
    """
    Grant an entitlement to a customer from a RevenueCat export file.
    """
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            user_id = row[user_id_field]
            customer = customers.get(api_key, user_id, environment)
            if not customer:
                print(f"Customer {user_id} not found")
                time.sleep(seconds_per_request)
                continue

            entitlement = customer.get("entitlements", {}).get(entitlement_id)
            if entitlement and entitlement.get("expires_date"):
                expires_date = datetime.strptime(entitlement.get("expires_date"), "%Y-%m-%dT%H:%M:%SZ")
                if expires_date > datetime.now():
                    print(f"Customer {user_id} already has the entitlement {entitlement_id}")
                    time.sleep(seconds_per_request)
                    continue

            entitlements.grant(api_key, user_id, entitlement_id, end_time_ms, environment)
            print(f"Granted entitlement {entitlement_id} to customer {user_id}")
            time.sleep(seconds_per_request)
    return True