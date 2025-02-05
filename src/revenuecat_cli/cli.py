from pathlib import Path

import typer
from typing_extensions import Annotated, Optional

from .common import Environment
from .v1 import customers, entitlements, extensions

app = typer.Typer(help="RevenueCat CLI")

v1_app = typer.Typer(help="API v1")
app.add_typer(v1_app, name="v1")

customers_app = typer.Typer(help="Manage customers")
v1_app.add_typer(customers_app, name="customers")

entitlements_app = typer.Typer(help="Manage entitlements")
v1_app.add_typer(entitlements_app, name="entitlements")


OptApiKey = Annotated[
    str, typer.Option(envvar="REVENUECAT_API_KEY", help="Your RevenueCat API key")
]
OptUserId = Annotated[
    str,
    typer.Option(
        envvar="REVENUECAT_USER_ID",
        help="The App User ID of the Customer. Wrap in single quotes to ensure all characters such as $ are not dropped.",
    ),
]
OptEnvironment = Annotated[
    Environment,
    typer.Option(
        envvar="REVENUECAT_ENVIRONMENT",
        help="The environment to use.",
    ),
]

# TODO(giorgio): I think there are a few issues with the current approach:
#   * The default is None, so forgetting the parameter means granting the entitlement indefinitely
#   * Passing ms is annoying, typer offers DateTime: https://typer.tiangolo.com/tutorial/parameter-types/datetime/
#   * `duration` is anyway deprecated in the API... so maybe we shouldn't even allow it?
#     https://www.revenuecat.com/docs/api-v1#tag/entitlements
#   My proposal is to force the user to provide EITHER `end_duration_ms` or `duration` (and optionally `start_time_ms`)
#   In alternative to `end_duration_ms`, we can provide a nicer `end_duration` to pass as a DateTime object.
OptEndTimeMs = Annotated[
    Optional[int],
    typer.Option(
        help="The end time of the entitlement in milliseconds since epoch. If not provided, the entitlement will be granted for lifetime."
    ),
]


@customers_app.command("get")
def get_customer(
    api_key: OptApiKey,
    user_id: OptUserId,
    environment: OptEnvironment = Environment.production,
):
    """
    Gets the latest Customer Info for the customer with the given App User ID, or creates a new customer if it doesn't exist.
    """
    typer.echo("Starting customer retrieval process...")

    response = customers.get(
        api_key,
        user_id,
        environment,
    )

    typer.echo(response)


@customers_app.command("delete")
def delete_customer(
    api_key: OptApiKey,
    user_id: OptUserId,
    environment: OptEnvironment = Environment.production,
):
    """
    Deletes a Customer.
    """
    typer.echo("Starting customer deletion process...")

    response = customers.delete(
        api_key,
        user_id,
        environment,
    )
    typer.echo(response)


@entitlements_app.command("grant")
def grant_entitlement(
    api_key: OptApiKey,
    user_id: OptUserId,
    entitlement_id: Annotated[
        str,
        typer.Option(
            help="The identifier for the entitlement you want to grant to the Customer",
        ),
    ],
    end_time_ms: OptEndTimeMs = None,
    environment: OptEnvironment = Environment.production,
):
    """
    Grants a Customer an entitlement. Does not override or defer a store transaction, applied simultaneously.
    """
    typer.echo("Starting entitlement granting process...")

    response = entitlements.grant(
        api_key,
        user_id,
        entitlement_id,
        end_time_ms,
        environment,
    )
    typer.echo(response)


@entitlements_app.command("revoke")
def revoke_entitlement(
    api_key: OptApiKey,
    user_id: OptUserId,
    entitlement_id: Annotated[
        str,
        typer.Option(
            help="The identifier for the entitlement you want to revoke from the Customer",
        ),
    ],
    environment: OptEnvironment = Environment.production,
):
    """
    Revokes a Customer's entitlement.
    """
    typer.echo("Starting entitlement revoking process...")

    response = entitlements.revoke(
        api_key,
        user_id,
        entitlement_id,
        environment,
    )
    typer.echo(response)


@entitlements_app.command("grant-from-export")
def grant_entitlement_from_export(
    api_key: OptApiKey,
    file_path: Annotated[
        Path, typer.Option(help="The path to the CSV file containing the customer data")
    ],
    entitlement_id: Annotated[
        str,
        typer.Option(
            help="The identifier for the entitlement you want to grant to the Customer",
        ),
    ],
    end_time_ms: OptEndTimeMs = None,
    user_id_field: Annotated[
        str, typer.Option(help="The field in the CSV file that contains the user ID")
    ] = "app_user_id",
    environment: OptEnvironment = Environment.production,
    seconds_per_request: Annotated[
        int, typer.Option(help="The number of seconds to wait between requests.")
    ] = 1,
):
    """
    Grants entitlements to customers from a CSV file.
    """
    typer.echo("Starting entitlement granting process...")

    response = extensions.grant_entitlement_from_export(
        api_key,
        file_path,
        entitlement_id,
        end_time_ms,
        user_id_field,
        environment,
        seconds_per_request,
    )
    typer.echo(response)


if __name__ == "__main__":
    app()
