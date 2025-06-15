import cv2
import numpy as np

from .graphic import Graphic
from .registry import get_renderer


def render_one(canvas: np.ndarray, graphic: Graphic) -> np.ndarray:
    """Render a graphic on the canvas with optional transparency (alpha)."""
    if not graphic.visible:
        return canvas

    renderer = get_renderer(graphic.type)
    if renderer is None:
        raise ValueError(f"No renderer registered for type: {graphic.type}")

    if graphic.alpha >= 1.0:
        return renderer(canvas, graphic)

    overlay = canvas.copy()
    overlay = renderer(overlay, graphic)

    blended = cv2.addWeighted(overlay, graphic.alpha, canvas, 1 - graphic.alpha, 0)
    return blended


def render_many(canvas: np.ndarray, graphics: list[Graphic]) -> np.ndarray:
    """Render multiple graphics on the canvas."""
    for graphic in sorted(graphics, key=lambda g: g.index):
        canvas = render_one(canvas, graphic)
    return canvas
