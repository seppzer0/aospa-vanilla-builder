from pathlib import Path
from dataclasses import dataclass

@dataclass
class Config:
    """A variable storage to use across the application."""
    DIR_ROOT: Path = Path(__file__).absolute().parents[2]
    DIR_ARTIFACTS: str = Path(DIR_ROOT, "artifacts").absolute()
    NAME_IMAGE: str = "aospa-vanilla-builder"
    NAME_CONTAINER: str = NAME_IMAGE + "-container"
