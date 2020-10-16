from typing import (
    Any,
    Optional,
)


class Cell:
    """Represents a single cell within the world."""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.entity: Optional[Any] = None
