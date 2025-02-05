import typer
from .v1 import customers, entitlements, extensions
from typing import Tuple
# Constants
API_KEY_HELP = "Your RevenueCat API key"
USER_ID_HELP = "The App User ID of the Customer. Use single quotes to pass in it due to special characters like $."
ENVIRONMENT_HELP = "The environment to use. Possible values are 'production' and 'sandbox'. Defaults to production."

app = typer.Typer(help="RevenueCat CLI")

v1_app = typer.Typer(help="API v1")
app.add_typer(v1_app, name="v1")

customers_app = typer.Typer(help="Manage customers")
v1_app.add_typer(customers_app, name="customers")

entitlements_app = typer.Typer(help="Manage entitlements")
v1_app.add_typer(entitlements_app, name="entitlements")

@customers_app.command("get")
def get_customer(
    api_key: str = typer.Option(..., "--api-key", help=API_KEY_HELP),
    user_id: str = typer.Option(..., "--user-id", help=USER_ID_HELP),
    environment: str = typer.Option("production", "--environment", help=ENVIRONMENT_HELP),
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
    api_key: str = typer.Option(..., "--api-key", help=API_KEY_HELP),
    user_id: str = typer.Option(..., "--user-id", help=USER_ID_HELP),
    environment: str = typer.Option("production", "--environment", help=ENVIRONMENT_HELP),
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
    api_key: str = typer.Option(..., "--api-key", help=API_KEY_HELP),
    user_id: str = typer.Option(..., "--user-id", help=USER_ID_HELP),
    entitlement_id: str = typer.Option(..., "--entitlement-id", help="The identifier for the entitlement you want to grant to the Customer"),
    end_time_ms: int | None = typer.Option(None, "--end-time-ms", help="The end time of the entitlement in milliseconds since epoch. If not provided, the entitlement will be granted for lifetime."),
    environment: str = typer.Option("production", "--environment", help=ENVIRONMENT_HELP),
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
    api_key: str = typer.Option(..., "--api-key", help=API_KEY_HELP),
    user_id: str = typer.Option(..., "--user-id", help=USER_ID_HELP),
    entitlement_id: str = typer.Option(..., "--entitlement-id", help="The identifier for the entitlement you want to revoke from the Customer"),    
    environment: str = typer.Option("production", "--environment", help=ENVIRONMENT_HELP),
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
    api_key: str = typer.Option(..., "--api-key", help=API_KEY_HELP),
    file_path: str = typer.Option(..., "--file-path", help="The path to the CSV file containing the customer data"),
    entitlement_id: str = typer.Option(..., "--entitlement-id", help="The identifier for the entitlement you want to grant to the Customer"),
    end_time_ms: int | None = typer.Option(None, "--end-time-ms", help="The end time of the entitlement in milliseconds since epoch. If not provided, the entitlement will be granted for lifetime."),
    user_id_field: str = typer.Option("app_user_id", "--user-id-field", help="The field in the CSV file that contains the user ID"),
    environment: str = typer.Option("production", "--environment", help=ENVIRONMENT_HELP),
    seconds_per_request: int = typer.Option(1, "--seconds-per-request", help="The number of seconds to wait between requests. Defaults to 1."),
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