from enum import Enum

import cv2
import numpy as np
from pydantic import Field

from .graphic import Graphic, Position, GraphicType


class MarkerType(Enum):
    """Enumeration for OpenCV marker types."""

    CROSS = cv2.MARKER_CROSS
    TILTED_CROSS = cv2.MARKER_TILTED_CROSS
    STAR = cv2.MARKER_STAR
    DIAMOND = cv2.MARKER_DIAMOND
    SQUARE = cv2.MARKER_SQUARE
    TRIANGLE_UP = cv2.MARKER_TRIANGLE_UP
    TRIANGLE_DOWN = cv2.MARKER_TRIANGLE_DOWN


class Marker(Graphic):
    """Marker graphic using OpenCV's drawMarker."""

    type: str = Field(GraphicType.MARKER.value, init=False)
    marker: int = Field(
        default=MarkerType.CROSS.value,
        description="Marker type (OpenCV constant, e.g., cv2.MARKER_CROSS).",
    )
    position: Position = Field(..., description="Center position of the marker.")
    size: int = Field(default=10, ge=1, description="Size of the marker.")
    thickness: int = Field(default=1, ge=1, description="Line thickness of the marker.")

    @property
    def centroid(self) -> Position:
        """The center of the marker is its centroid."""
        return self.position


def render_marker(canvas: np.ndarray, marker: Marker) -> np.ndarray:
    """Render a marker using OpenCV's drawMarker()."""
    center = marker.position.to_absolute(canvas.shape[:2]).to_tuple(to_int=True)
    color = marker.color.to_tuple()
    return cv2.drawMarker(
        canvas,
        center,
        color,
        marker.marker,
        marker.size,
        marker.thickness,
    )
