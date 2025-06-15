from typing import Optional

import cv2
import numpy as np
from pydantic import Field

from .graphic import Graphic, Position, GraphicType
from .color import BGR


class Polygon(Graphic):
    """Polygon graphic in the cvdraw library."""

    type: str = Field(GraphicType.POLYGON.value, init=False)
    points: list[Position] = Field(
        ...,
        min_length=3,
        max_length=20,
        description="List of polygon vertices (at least 3, max 20).",
    )
    thickness: int = Field(
        default=1, ge=1, description="Thickness of the polygon edges."
    )

    fill: Optional[BGR] = Field(
        default=None,
        description="Fill color for the polygon. If None, the polygon is not filled.",
    )

    @property
    def centroid(self) -> Position:
        """Calculate the centroid of the polygon (average of all points)."""
        x = sum(p.x for p in self.points) / len(self.points)
        y = sum(p.y for p in self.points) / len(self.points)
        return Position(x=x, y=y)


def render_polygon(canvas: np.ndarray, polygon: Polygon) -> np.ndarray:
    """Render a polygon on the canvas."""
    height, width = canvas.shape[:2]
    points = np.array(
        [p.to_absolute((height, width)).to_tuple(to_int=True) for p in polygon.points],
        dtype=np.int32,
    )

    if polygon.fill:
        cv2.fillPoly(
            canvas,
            [points],
            color=polygon.fill.to_tuple(),
        )

    return cv2.polylines(
        canvas,
        [points],
        isClosed=True,
        color=polygon.color.to_tuple(),
        thickness=polygon.thickness,
    )
