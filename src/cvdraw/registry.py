from .graphic import Renderer, GraphicType

from .line import render_line
from .point import render_point
from .square import render_square
from .rectangle import render_rectangle
from .polygon import render_polygon
from .circle import render_circle
from .text import render_text
from .marker import render_marker


REGISTRY: dict[str, Renderer] = {}


def set_renderer(type: str, renderer: Renderer) -> None:
    """Register a graphic with its renderer function."""
    if type in REGISTRY:
        raise ValueError(f"Graphic type '{type}' is already registered.")
    REGISTRY[type] = renderer


def get_renderer(type: str) -> Renderer:
    """Get the renderer function for a given graphic type."""
    if type not in REGISTRY:
        raise ValueError(f"No renderer registered for graphic type '{type}'.")
    return REGISTRY[type]


set_renderer(GraphicType.POINT.value, render_point)
set_renderer(GraphicType.LINE.value, render_line)
set_renderer(GraphicType.SQUARE.value, render_square)
set_renderer(GraphicType.RECTANGLE.value, render_rectangle)
set_renderer(GraphicType.POLYGON.value, render_polygon)
set_renderer(GraphicType.CIRCLE.value, render_circle)
set_renderer(GraphicType.TEXT.value, render_text)
set_renderer(GraphicType.MARKER.value, render_marker)
