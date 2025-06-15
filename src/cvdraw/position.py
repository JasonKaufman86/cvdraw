from enum import Enum
from typing import Union
from pydantic import BaseModel, Field


class PositionType(str, Enum):
    """Enumeration for position types."""

    ABSOLUTE = "absolute"
    RELATIVE = "relative"


class Position(BaseModel, frozen=True):
    """Position in 2D space with x and y coordinates."""

    type: PositionType = Field(
        ..., description="Type of position, either 'absolute' or 'relative'."
    )
    x: float = Field(..., description="X coordinate of the position.")
    y: float = Field(..., description="Y coordinate of the position.")

    @staticmethod
    def absolute(x: float, y: float) -> "Position":
        """Create an absolute position."""
        return Position(type=PositionType.ABSOLUTE, x=x, y=y)

    @staticmethod
    def relative(x: float, y: float) -> "Position":
        """Create a relative position."""
        return Position(type=PositionType.RELATIVE, x=x, y=y)

    def to_absolute(self, dimensions: tuple[int, int]) -> "Position":
        """Convert relative position to absolute based on canvas dimensions."""
        if self.type == PositionType.RELATIVE:
            return Position(
                type=PositionType.ABSOLUTE,
                x=self.x * dimensions[0],
                y=self.y * dimensions[1],
            )
        return self

    def to_relative(self, dimensions: tuple[int, int]) -> "Position":
        """Convert absolute position to relative based on canvas dimensions."""
        if self.type == PositionType.ABSOLUTE:
            return Position(
                type=PositionType.RELATIVE,
                x=self.x / dimensions[0],
                y=self.y / dimensions[1],
            )
        return self

    def to_tuple(
        self, to_int: bool = False
    ) -> tuple[Union[float, int], Union[float, int]]:
        """Convert position to a tuple of floats."""
        return (self.x, self.y) if not to_int else (int(self.x), int(self.y))
