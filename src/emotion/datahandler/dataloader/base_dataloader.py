from abc import ABC
from pathlib import Path


class BaseDataLoader(ABC):
    """
    This is the abstract base class for loading data from a file.
    """

    def __init__(self, file_path: Path, frequency: int):
        self.file_path = file_path
        if not self.file_path.exists():
            raise FileNotFoundError(f"File {self.file_path} does not exist")
        if frequency not in (0, None):
            self.frequency = frequency
        else:
            raise ValueError("Frequency cannot be 0 or None")

    def __iter__(self):
        """Return the iterator object itself"""

    def __next__(self):
        """Returns the next value from iterator"""
