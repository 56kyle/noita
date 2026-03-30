"""Command-line interface."""
from pathlib import Path
from typing import Annotated
from typing import Optional

import typer

from noita.constants import NOITA_CURRENT_SAVE_PATH
from noita.constants import NOITA_DEFAULT_SAVE_NAME
from noita.constants import USER_NOITA_SAVES_FOLDER
from noita.game_state import clear
from noita.game_state import find_most_recent_save
from noita.game_state import get_new_quick_save_path
from noita.game_state import load
from noita.game_state import quick_save
from noita.game_state import save
from noita.game_state import show_saves


app: typer.Typer = typer.Typer()


@app.command(name="noita")
def main() -> None:
    """Noita."""


@app.command(name="save")
def noita_save(
    save_name: Annotated[Optional[str], typer.Argument(
        show_default=True,
        help="The name of the save to load, or nothing to load the latest quicksave."
    )] = None,
    force: Annotated[bool, typer.Option("--force", "-f", is_flag=True)] = False
) -> None:
    """Create a new Noita save state."""
    if save_name is None:
        path: Path = get_new_quick_save_path()
    else:
        path: Path = USER_NOITA_SAVES_FOLDER / save_name

    if path.exists() and force:
        clear(path=path)

    save(path=path)


@app.command(name="load")
def noita_load(
    save_name: Annotated[Optional[str], typer.Argument(show_default=True)] = None,
    force: Annotated[bool, typer.Option(is_flag=True)] = False
) -> None:
    """Load an existing Noita save state."""
    if save_name is None:
        path: Path = find_most_recent_save()
    else:
        path: Path = USER_NOITA_SAVES_FOLDER / save_name

    if NOITA_CURRENT_SAVE_PATH and force:
        clear(path=NOITA_CURRENT_SAVE_PATH)

    load(path=path)


@app.command(name="show")
def noita_show() -> None:
    """Show available Noita save states."""
    show_saves()


if __name__ == "__main__":
    app()  # pragma: no cover
