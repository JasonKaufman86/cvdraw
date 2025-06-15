from typing import Optional

import cv2
import numpy as np
from pydantic import Field

from .graphic import Graphic, Position, GraphicType
from .color import BGR


class Rectangle(Graphic):
    """Rectangle graphic in the cvdraw library."""

    type: str = Field(GraphicType.RECTANGLE.value, init=False)

    top_left: Position = Field(..., description="Top-left corner of the rectangle.")
    btm_right: Position = Field(
        ..., description="Bottom-right corner of the rectangle."
    )
    thickness: int = Field(default=1, ge=1, description="Border thickness.")
    fill: Optional[BGR] = Field(
        default=None, description="Optional fill color for the rectangle."
    )

    @property
    def centroid(self) -> Position:
        """Calculate the rectangle's centroid."""
        return Position(
            x=(self.top_left.x + self.btm_right.x) / 2,
            y=(self.top_left.y + self.btm_right.y) / 2,
        )


def render_rectangle(canvas: np.ndarray, rectangle: Rectangle) -> np.ndarray:
    """Render a rectangle on the canvas."""
    h, w = canvas.shape[:2]
    pt1 = rectangle.top_left.to_absolute((h, w)).to_tuple(to_int=True)
    pt2 = rectangle.btm_right.to_absolute((h, w)).to_tuple(to_int=True)

    if rectangle.fill:
        cv2.rectangle(canvas, pt1, pt2, rectangle.fill.to_tuple(), thickness=-1)

    return cv2.rectangle(
        canvas, pt1, pt2, rectangle.color.to_tuple(), rectangle.thickness
    )
