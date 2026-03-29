"""Module containing constants used throughout the noita package."""
import datetime
from pathlib import Path

from platformdirs import user_cache_path
from platformdirs import user_log_path


_FILE_SAFE_DATETIME_FORMAT: str = "%Y-%m-%d_%H-%M-%S"


APP_NAME: str = "noita"
APP_AUTHOR: str = "56kyle"
APP_START_TIME: datetime.datetime = datetime.datetime.now(tz=datetime.timezone.utc)

USER_CACHE_FOLDER: Path = user_cache_path(appname=APP_NAME, appauthor=APP_AUTHOR, ensure_exists=True)
USER_LOG_FOLDER: Path = user_log_path(appname=APP_NAME, appauthor=APP_AUTHOR, ensure_exists=True)

NOITA_DATA_FOLDER: Path = USER_CACHE_FOLDER.parent.parent.parent / "LocalLow" / "Nolla_Games_Noita"


REPO_ROOT: Path = Path(__file__).parent.parent.parent
