from enum import Enum

import typer
from typing_extensions import Annotated

from .v1 import customers, entitlements, extensions

app = typer.Typer(help="RevenueCat CLI")

v1_app = typer.Typer(help="API v1")
app.add_typer(v1_app, name="v1")

customers_app = typer.Typer(help="Manage customers")
v1_app.add_typer(customers_app, name="customers")

entitlements_app = typer.Typer(help="Manage entitlements")
v1_app.add_typer(entitlements_app, name="entitlements")


class Environment(str, Enum):
    production = "production"
    sandbox = "sandbox"


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
    environment: OptEnvironment = Environment.production,
    entitlement_id: str = typer.Option(
        ...,
        "--entitlement-id",
        help="The identifier for the entitlement you want to grant to the Customer",
    ),
    end_time_ms: int | None = typer.Option(
        None,
        "--end-time-ms",
        help="The end time of the entitlement in milliseconds since epoch. If not provided, the entitlement will be granted for lifetime.",
    ),
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
    environment: OptEnvironment = Environment.production,
    entitlement_id: str = typer.Option(
        ...,
        "--entitlement-id",
        help="The identifier for the entitlement you want to revoke from the Customer",
    ),
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


@entitlements_app.command("grant_from_export")
def grant_entitlement_from_export(
    api_key: OptApiKey,
    environment: OptEnvironment = Environment.production,
    file_path: str = typer.Option(
        ..., "--file-path", help="The path to the CSV file containing the customer data"
    ),
    entitlement_id: str = typer.Option(
        ...,
        "--entitlement-id",
        help="The identifier for the entitlement you want to grant to the Customer",
    ),
    end_time_ms: int | None = typer.Option(
        None,
        "--end-time-ms",
        help="The end time of the entitlement in milliseconds since epoch. If not provided, the entitlement will be granted for lifetime.",
    ),
    user_id_field: str = typer.Option(
        "app_user_id",
        "--user-id-field",
        help="The field in the CSV file that contains the user ID",
    ),
    seconds_per_request: int = typer.Option(
        1,
        "--seconds-per-request",
        help="The number of seconds to wait between requests. Defaults to 1.",
    ),
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
