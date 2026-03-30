"""Module containing constants used throughout the noita package."""

import datetime
from pathlib import Path

from platformdirs import user_cache_path
from platformdirs import user_data_path
from platformdirs import user_log_path
from pydantic import ConfigDict


FILE_SAFE_DATETIME_FORMAT: str = "%Y-%m-%d_%H-%M-%S"


APP_NAME: str = "noita"
APP_AUTHOR: str = "56kyle"
APP_START_TIME: datetime.datetime = datetime.datetime.now(tz=datetime.timezone.utc)

USER_CACHE_FOLDER: Path = user_cache_path(appname=APP_NAME, appauthor=APP_AUTHOR, ensure_exists=True)
USER_DATA_FOLDER: Path = user_data_path(appname=APP_NAME, appauthor=APP_AUTHOR, ensure_exists=True)
USER_LOG_FOLDER: Path = user_log_path(appname=APP_NAME, appauthor=APP_AUTHOR, ensure_exists=True)

USER_NOITA_QUICK_SAVES_FOLDER: Path = USER_DATA_FOLDER / "quick_saves"
USER_NOITA_QUICK_SAVES_FOLDER.mkdir(parents=True, exist_ok=True)
USER_NOITA_SAVES_FOLDER: Path = USER_DATA_FOLDER / "saves"
USER_NOITA_SAVES_FOLDER.mkdir(parents=True, exist_ok=True)

NOITA_DATA_FOLDER: Path = USER_CACHE_FOLDER.parent.parent.parent.parent / "LocalLow" / "Nolla_Games_Noita"
NOITA_DEFAULT_SAVE_NAME: str = "save00"
NOITA_CURRENT_SAVE_PATH: Path = NOITA_DATA_FOLDER / NOITA_DEFAULT_SAVE_NAME

DEFAULT_PYDANTIC_CONFIG: ConfigDict = ConfigDict(arbitrary_types_allowed=True)


REPO_ROOT: Path = Path(__file__).parent.parent.parent
