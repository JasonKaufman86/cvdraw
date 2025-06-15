# cvdraw

> A declarative, Pydantic-first wrapper around OpenCV drawing functions

## Why

I really love working with [Pydantic](https://docs.pydantic.dev) and [OpenCV](https://opencv.org/), and I often find myself needing to annotate or visualize data on images — whether it's keypoints, bounding boxes, or debug overlays. I wanted something structured and strongly typed that still feels lightweight and flexible.

This library is the result of that: **a simple but extensible graphics system for image annotation**, built on top of OpenCV and powered by Pydantic models.

---

## What is `cvdraw`?

`cvdraw` is a small framework for defining graphics like points, lines, rectangles, and text as structured Python objects — and rendering them on images using OpenCV.

Each graphic is a `pydantic.BaseModel`, so you get:
- 🔒 Type safety
- 🧼 Validation
- 📋 Clear structure
- 🔁 Easy serialization if you ever need it

---

## Features

- ✅ Declarative graphics (e.g. `Point`, `Rectangle`, `Circle`, etc.)
- ✅ Strong typing with Pydantic
- ✅ Support for grouping graphics (`Group`)
- ✅ Layered rendering via `index`
- ✅ Transparency via `alpha`
- ✅ Extendable with custom graphic types (`set_renderer()`)

---

## Example

```python
import numpy as np
from cvdraw import Point, render_many, BGR, Position

# Create a blank canvas
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

# Define some graphics
graphics = [
    Point(position=Position(x=100, y=150), color=BGR(r=255, g=0, b=0), radius=5),
    Point(position=Position(x=300, y=200), color=BGR(r=0, g=255, b=0), radius=10, alpha=0.6),
]

# Draw them
canvas = render_many(canvas, graphics)
```

---

## Extending with Custom Graphics

You can register your own graphic types easily:

```python
from cvdraw import Graphic, set_renderer

class MyArrow(Graphic):
    type: str = "arrow"
    # your fields...

def render_arrow(canvas: np.ndarray, arrow: MyArrow) -> np.ndarray:
    # your OpenCV drawing logic
    return canvas

set_renderer("arrow", render_arrow)
```

---
