from typing import Optional

import cv2
import numpy as np
from pydantic import Field

from .graphic import Graphic, Position, GraphicType
from .color import BGR


class Square(Graphic):
    """Square graphic in the cvdraw library."""

    type: str = Field(GraphicType.SQUARE.value, init=False)
    center: Position = Field(..., description="Center of the square.")
    side: float = Field(..., gt=0, description="Side length in pixels (absolute).")
    thickness: int = Field(default=1, ge=1, description="Border thickness.")
    fill: Optional[BGR] = Field(
        default=None, description="Optional fill color for the square."
    )

    @property
    def centroid(self) -> Position:
        """Calculate the square's centroid, which is its center."""
        return self.center


def render_square(canvas: np.ndarray, square: Square) -> np.ndarray:
    """Render a square on the canvas."""
    h, w = canvas.shape[:2]
    cx, cy = square.center.to_absolute((h, w)).to_tuple(to_int=True)
    half = int(square.side / 2)

    pt1 = (cx - half, cy - half)
    pt2 = (cx + half, cy + half)

    if square.fill:
        cv2.rectangle(canvas, pt1, pt2, square.fill.to_tuple(), thickness=-1)

    return cv2.rectangle(canvas, pt1, pt2, square.color.to_tuple(), square.thickness)
