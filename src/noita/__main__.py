"""Command-line interface."""

import typer


app: typer.Typer = typer.Typer()


@app.command(name="noita")
def main() -> None:
    """Noita."""


if __name__ == "__main__":
    app()  # pragma: no cover
