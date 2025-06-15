from enum import Enum
from typing import Callable

import numpy as np
from pydantic import BaseModel, Field

from .color import BGR
from .position import Position


class GraphicType(Enum):
    """Enumeration of graphic types."""

    POINT = "point"
    LINE = "line"
    SQUARE = "square"
    RECTANGLE = "rectangle"
    POLYGON = "polygon"
    CIRCLE = "circle"
    TEXT = "text"
    MARKER = "marker"


class Graphic(BaseModel):
    """Base class for all graphics in the cvdraw library."""

    type: str = Field(
        ..., description="Type of the graphic, e.g., 'line', 'rectangle', 'circle'."
    )
    visible: bool = Field(default=True, description="Visibility of the graphic.")
    color: BGR = Field(
        default_factory=lambda: BGR(r=255, g=255, b=255),
        description="Color of the graphic in BGR format.",
    )
    alpha: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="Alpha transparency of the graphic (0.0 to 1.0).",
    )
    index: int = Field(
        default=0,
        ge=0,
        description="Index of the graphic in a list, used for rendering order.",
    )

    @property
    def centroid(self) -> Position:
        """Calculate the centroid of the graphic."""
        raise NotImplementedError(
            "Centroid calculation is not implemented for this graphic type."
        )


Renderer = Callable[[np.ndarray, Graphic], np.ndarray]
