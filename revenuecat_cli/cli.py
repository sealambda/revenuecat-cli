import typer
from .v1 import entitlements

app = typer.Typer(help="RevenueCat CLI")

v1_app = typer.Typer(help="API v1")
app.add_typer(v1_app, name="v1")

entitlements_app = typer.Typer(help="Manage entitlements")
v1_app.add_typer(entitlements_app, name="entitlements")

@entitlements_app.command("grant")
def grant_entitlement(
    api_key: str = typer.Option(..., "--api-key", help="Your RevenueCat API key"),
    app_user_id: str = typer.Option(..., "--app-user-id", help="The App User ID of the Customer. Use single quotes to pass in it due to special characters like $."),
    entitlement_id: str = typer.Option(..., "--entitlement-id", help="The identifier for the entitlement you want to grant to the Customer"),
    end_time_ms: int | None = typer.Option(None, "--end-time-ms", help="The end time of the entitlement in milliseconds since epoch. If not provided, the entitlement will be granted for lifetime."),
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
    )

    if response:
        typer.echo(response)
    else:
        typer.echo("Entitlement granted successfully")

@entitlements_app.command("revoke")
def revoke_entitlement(
    api_key: str = typer.Option(..., "--api-key", help="Your RevenueCat API key"),
    app_user_id: str = typer.Option(..., "--app-user-id", help="The App User ID of the Customer. Use single quotes to pass in it due to special characters like $."),
    entitlement_id: str = typer.Option(..., "--entitlement-id", help="The identifier for the entitlement you want to revoke from the Customer"),    
):
    """
    Revokes a Customer's entitlement.
    """
    typer.echo("Starting entitlement revoking process...")

    response = entitlements.revoke(
        api_key,
        app_user_id,
        entitlement_id,
    )

    if response:
        typer.echo(response)
    else:
        typer.echo("Entitlement revoked successfully")

if __name__ == "__main__":
    app()