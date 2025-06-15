import cv2
import numpy as np
from pydantic import Field

from .graphic import Graphic, Position, GraphicType


class Line(Graphic):
    """Line graphic consisting of multiple connected points."""

    type: str = Field(GraphicType.LINE.value, init=False)
    points: list[Position] = Field(
        ..., min_length=2, max_length=10, description="List of points forming the line."
    )
    thickness: int = Field(default=1, ge=1, description="Line thickness in pixels.")

    @property
    def centroid(self) -> Position:
        """Compute the centroid as the average of all points."""
        x = sum(p.x for p in self.points) / len(self.points)
        y = sum(p.y for p in self.points) / len(self.points)
        return Position(x=x, y=y)


def render_line(canvas: np.ndarray, line: Line) -> np.ndarray:
    """Render a polyline (multi-point line) on the canvas."""
    height, width = canvas.shape[:2]
    points = np.array(
        [p.to_absolute((height, width)).to_tuple(to_int=True) for p in line.points],
        dtype=np.int32,
    )
    return cv2.polylines(
        canvas,
        [points],
        isClosed=False,
        color=line.color.to_tuple(),
        thickness=line.thickness,
    )
