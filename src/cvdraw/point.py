import cv2
import numpy as np
from pydantic import Field

from .graphic import Graphic, Position, GraphicType


class Point(Graphic):
    """Point graphic in the cvdraw library."""

    type: str = Field(GraphicType.POINT.value, init=False)
    position: Position = Field(..., description="Position of the point in 2D space.")
    radius: float = Field(
        default=1.0, ge=0.0, description="Radius of the point, representing its size."
    )

    @property
    def centroid(self) -> Position:
        """Calculate the centroid of the point, which is its position."""
        return self.position


def render_point(canvas: np.ndarray, point: Point) -> np.ndarray:
    """Render a point on the canvas."""
    center = point.position.to_absolute(canvas.shape[:2]).to_tuple(to_int=True)
    color = point.color.to_tuple()
    radius = int(point.radius)
    return cv2.circle(canvas, center, radius, color, -1)
