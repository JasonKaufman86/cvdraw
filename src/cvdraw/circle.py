from typing import Optional

import cv2
import numpy as np
from pydantic import Field

from .color import BGR
from .graphic import Graphic, Position, GraphicType


class Circle(Graphic):
    """Circle graphic in the cvdraw library."""

    type: str = Field(GraphicType.CIRCLE.value, init=False)
    center: Position = Field(
        ..., description="Center position of the circle in 2D space."
    )
    radius: int = Field(default=5, ge=0, description="Radius of the circle.")
    thickness: int = Field(
        default=1, description="Line thickness of the circle. Use -1 for filled circle."
    )
    fill: Optional[BGR] = Field(
        default=None, description="Optional fill color for the circle."
    )

    @property
    def centroid(self) -> Position:
        """The center of the circle is its centroid."""
        return self.center


def render_circle(canvas: np.ndarray, circle: Circle) -> np.ndarray:
    """Render a circle on the canvas."""
    center = circle.center.to_absolute(canvas.shape[:2]).to_tuple(to_int=True)
    color = circle.color.to_tuple()

    if circle.fill:
        cv2.circle(canvas, center, circle.radius, circle.fill.to_tuple(), -1)

    return cv2.circle(canvas, center, circle.radius, color, circle.thickness)
