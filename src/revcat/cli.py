from datetime import datetime
from pathlib import Path
from typing import Annotated, Optional

from typer import BadParameter, Option, Typer

from .common import Duration, Environment
from .v1 import customers, entitlements, extensions

app = Typer(help="RevenueCat CLI", no_args_is_help=True)

v1_app = Typer(help="API v1", no_args_is_help=True)
app.add_typer(v1_app, name="v1", no_args_is_help=True)

customers_app = Typer(help="Manage customers", no_args_is_help=True)
v1_app.add_typer(customers_app, name="customers")

entitlements_app = Typer(help="Manage entitlements", no_args_is_help=True)
v1_app.add_typer(entitlements_app, name="entitlements")


OptApiKey = Annotated[
    str, Option(envvar="REVENUECAT_API_KEY", help="Your RevenueCat API key")
]
OptUserId = Annotated[
    str,
    Option(
        envvar="REVENUECAT_USER_ID",
        help="The App User ID of the Customer. "
        "Wrap in single quotes to ensure all characters such as $ are not dropped.",
    ),
]
OptEnvironment = Annotated[
    Environment,
    Option(
        envvar="REVENUECAT_ENVIRONMENT",
        help="The environment to use.",
    ),
]

OptEndTime = Annotated[
    Optional[datetime],
    Option(help="When the entitlement should expire (e.g. '2024-12-31T23:59:59')."),
]
OptDuration = Annotated[
    Optional[Duration],
    Option(
        help="The duration of the entitlement.",
    ),
]
OptStartTime = Annotated[
    Optional[datetime],
    Option(help="When the entitlement should start (defaults to now)."),
]

OptEntitlementId = Annotated[
    str,
    Option(help="The identifier for the entitlement you want to grant to the Customer"),
]


@customers_app.command("get")
def get_customer(
    api_key: OptApiKey,
    user_id: OptUserId,
    environment: OptEnvironment = Environment.production,
):
    """
    Gets the latest Customer Info for the customer with the given App User ID,
    or creates a new customer if it doesn't exist.
    """
    print("Starting customer retrieval process...")

    response = customers.get(
        api_key,
        user_id,
        environment,
    )

    print(response)


@customers_app.command("delete")
def delete_customer(
    api_key: OptApiKey,
    user_id: OptUserId,
    environment: OptEnvironment = Environment.production,
):
    """
    Deletes a Customer.
    """
    print("Starting customer deletion process...")

    response = customers.delete(
        api_key,
        user_id,
        environment,
    )
    print(response)


@entitlements_app.command("grant")
def grant_entitlement(
    api_key: OptApiKey,
    user_id: OptUserId,
    entitlement_id: OptEntitlementId,
    end_time: OptEndTime = None,
    duration: OptDuration = None,
    start_time: OptStartTime = None,
    environment: OptEnvironment = Environment.production,
):
    """
    Grants a Customer an entitlement.
    Does not override or defer a store transaction, applied simultaneously.
    """
    if not end_time and not duration:
        raise BadParameter("Either end_time or duration must be provided")

    print("Starting entitlement granting process...")

    response = entitlements.grant(
        api_key,
        user_id,
        entitlement_id,
        end_time,
        duration,
        start_time,
        environment,
    )
    print(response)


@entitlements_app.command("revoke")
def revoke_entitlement(
    api_key: OptApiKey,
    user_id: OptUserId,
    entitlement_id: Annotated[
        str,
        Option(
            help="The identifier for the entitlement to revoke from the Customer",
        ),
    ],
    environment: OptEnvironment = Environment.production,
):
    """
    Revokes a Customer's entitlement.
    """
    print("Starting entitlement revoking process...")

    response = entitlements.revoke(
        api_key,
        user_id,
        entitlement_id,
        environment,
    )
    print(response)


@entitlements_app.command("grant-from-export")
def grant_entitlement_from_export(
    api_key: OptApiKey,
    file_path: Annotated[
        Path, Option(help="The path to the CSV file containing the customer data")
    ],
    entitlement_id: OptEntitlementId,
    end_time: OptEndTime = None,
    duration: OptDuration = None,
    start_time: OptStartTime = None,
    user_id_field: Annotated[
        str, Option(help="The field in the CSV file that contains the user ID")
    ] = "app_user_id",
    environment: OptEnvironment = Environment.production,
    seconds_per_request: Annotated[
        int, Option(help="The number of seconds to wait between requests.")
    ] = 1,
):
    """
    Grants entitlements to customers from a CSV file.
    """
    if not end_time and not duration:
        raise BadParameter("Either end_time or duration must be provided")

    print("Starting entitlement granting process...")

    response = extensions.grant_entitlement_from_export(
        api_key,
        file_path,
        entitlement_id,
        end_time,
        duration,
        start_time,
        user_id_field,
        environment,
        seconds_per_request,
    )
    print(response)


if __name__ == "__main__":
    app()
