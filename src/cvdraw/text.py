import cv2
import numpy as np
from pydantic import BaseModel, Field

from .graphic import Graphic, Position, GraphicType


class Font(BaseModel):
    """Font settings for text rendering."""

    face: int = Field(
        default=cv2.FONT_HERSHEY_SIMPLEX, description="Font face constant from OpenCV."
    )
    scale: float = Field(default=1.0, gt=0.0, description="Font scale (relative size).")
    thickness: int = Field(default=1, ge=1, description="Thickness of the text stroke.")


class Text(Graphic):
    """Text graphic in the cvdraw library."""

    type: str = Field(GraphicType.TEXT.value, init=False)
    text: str = Field(..., description="Text string to display.")
    font: Font = Field(default_factory=Font, description="Font configuration.")
    position: Position = Field(..., description="Top-left position of the text.")

    @property
    def centroid(self) -> Position:
        """Approximate the centroid as the anchor position."""
        return self.position


def render_text(canvas: np.ndarray, text: Text) -> np.ndarray:
    """Render text on the canvas."""
    position = text.position.to_absolute(canvas.shape[:2]).to_tuple(to_int=True)
    color = text.color.to_tuple()
    return cv2.putText(
        canvas,
        text.text,
        position,
        text.font.face,
        text.font.scale,
        color,
        text.font.thickness,
    )
