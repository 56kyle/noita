"""Module containing logic for interacting with copies of a given Noita game state."""

import datetime
import shutil
from pathlib import Path

from loguru import logger
from pydantic import DirectoryPath
from pydantic import NewPath
from pydantic import validate_call

from noita.constants import DEFAULT_PYDANTIC_CONFIG
from noita.constants import FILE_SAFE_DATETIME_FORMAT
from noita.constants import MAX_QUICK_SAVE_COUNT
from noita.constants import NOITA_CURRENT_SAVE_PATH
from noita.constants import USER_NOITA_QUICK_SAVES_FOLDER
from noita.constants import USER_NOITA_SAVES_FOLDER


def quick_save() -> None:
    """Create a new disposable Noita game save state."""
    logger.info(f"Creating a new Noita quicksave...")
    path: Path = get_new_quick_save_path()
    quick_saves: list[Path] = get_quick_save_paths()
    if len(quick_saves) >= MAX_QUICK_SAVE_COUNT:
        remove_oldest_quick_save()
    save(path=path)


def get_new_quick_save_path() -> Path:
    """Returns a new Noita quicksave folder."""
    quick_save_slug: str = datetime.datetime.now().strftime(FILE_SAFE_DATETIME_FORMAT)
    file_name: str = f"quicksave_{quick_save_slug}"
    path: Path = USER_NOITA_QUICK_SAVES_FOLDER / file_name
    return path


def remove_oldest_quick_save() -> None:
    """Remove the oldest Noita quicksave folder."""
    path: Path = find_oldest_quick_save()
    logger.info(f"Removing oldest quick save at `{path}`.")
    clear(path=path)


def find_oldest_quick_save() -> Path:
    """Returns the most oldlest Noita game save state's name."""
    quick_save_paths: list[Path] = get_quick_save_paths()
    if len(quick_save_paths) < 1:
        raise FileNotFoundError("Failed to find any existing Noita quick saves.")
    return min(quick_save_paths, key=lambda path: path.stat().st_mtime)


@validate_call(config=DEFAULT_PYDANTIC_CONFIG)
def save(path: NewPath) -> None:
    """Create a new Noita game save state."""
    logger.info(f"Saving current Noita game state to `{path}`")
    shutil.copytree(src=NOITA_CURRENT_SAVE_PATH, dst=path, dirs_exist_ok=True)


def quick_load() -> None:
    """Load the latest disposable Noita game save state."""
    logger.info(f"Loading the latest Noita quicksave...")
    path: Path = find_most_recent_save()
    load(path=path)


def find_most_recent_save() -> Path:
    """Returns the most recent Noita game save state's name."""
    all_save_paths: list[Path] = get_all_save_paths()
    if len(all_save_paths) < 1:
        raise FileNotFoundError("Failed to find any existing Noita saves.")
    return max(all_save_paths, key=lambda path: path.stat().st_mtime)


@validate_call(config=DEFAULT_PYDANTIC_CONFIG)
def load(path: DirectoryPath) -> None:
    """Load an existing Noita game save state."""
    logger.info(f"Loading new Noita game state from `{path}`")
    if NOITA_CURRENT_SAVE_PATH.exists():
        raise FileExistsError(f"{NOITA_CURRENT_SAVE_PATH} already exists.")
    shutil.copytree(src=path, dst=NOITA_CURRENT_SAVE_PATH, dirs_exist_ok=False)


def get_all_save_paths() -> list[Path]:
    """Returns a list of all existing Noita saves and quicksaves."""
    return [*get_save_paths(), *get_quick_save_paths()]


def get_save_paths() -> list[Path]:
    """Returns a list of all existing Noita save state paths."""
    return list(USER_NOITA_SAVES_FOLDER.iterdir())


def get_quick_save_paths() -> list[Path]:
    """Returns a list of all existing Noita quick save state paths."""
    return list(USER_NOITA_QUICK_SAVES_FOLDER.iterdir())


@validate_call(config=DEFAULT_PYDANTIC_CONFIG)
def clear(path: DirectoryPath) -> None:
    """Remove the current Noita game save state."""
    logger.warning(f"Clearing Noita game save state at `{path}`.")
    shutil.rmtree(path=path)
