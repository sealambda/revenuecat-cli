import typer
from .v1 import customers, entitlements

# Constants
API_KEY_HELP = "Your RevenueCat API key"
APP_USER_ID_HELP = "The App User ID of the Customer. Use single quotes to pass in it due to special characters like $."
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
    app_user_id: str = typer.Option(..., "--app-user-id", help=APP_USER_ID_HELP),
    environment: str = typer.Option("production", "--environment", help=ENVIRONMENT_HELP),
):
    """
    Gets the latest Customer Info for the customer with the given App User ID, or creates a new customer if it doesn't exist.
    """
    typer.echo("Starting customer retrieval process...")

    response = customers.get(
        api_key,
        app_user_id,
        environment,
    )

    if response:
        typer.echo(response)
    else:
        typer.echo("Customer retrieved or created successfully")
        
@entitlements_app.command("grant")
def grant_entitlement(
    api_key: str = typer.Option(..., "--api-key", help=API_KEY_HELP),
    app_user_id: str = typer.Option(..., "--app-user-id", help=APP_USER_ID_HELP),
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
        app_user_id,
        entitlement_id,
        end_time_ms,
        environment,
    )

    if response:
        typer.echo(response)
    else:
        typer.echo("Entitlement granted successfully")

@entitlements_app.command("revoke")
def revoke_entitlement(
    api_key: str = typer.Option(..., "--api-key", help=API_KEY_HELP),
    app_user_id: str = typer.Option(..., "--app-user-id", help=APP_USER_ID_HELP),
    entitlement_id: str = typer.Option(..., "--entitlement-id", help="The identifier for the entitlement you want to revoke from the Customer"),    
    environment: str = typer.Option("production", "--environment", help=ENVIRONMENT_HELP),
):
    """
    Revokes a Customer's entitlement.
    """
    typer.echo("Starting entitlement revoking process...")

    response = entitlements.revoke(
        api_key,
        app_user_id,
        entitlement_id,
        environment,
    )

    if response:
        typer.echo(response)
    else:
        typer.echo("Entitlement revoked successfully")

if __name__ == "__main__":
    app()