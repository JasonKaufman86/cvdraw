import cv2
from src.cvdraw.color import BGR
from src.cvdraw.point import Point, Position
from src.cvdraw.line import Line
from src.cvdraw.polygon import Polygon
from src.cvdraw.square import Square
from src.cvdraw.rectangle import Rectangle
from src.cvdraw.circle import Circle
from src.cvdraw.marker import Marker
from src.cvdraw.text import Text, Font
from src.cvdraw.render import render_one, render_many


def main():

    image = cv2.imread(
        r"C:\Users\Annelene Derbyshire\Desktop\Projects\cvdraw\sticker.png"
    )
    cv2.imshow("Original Image", image)
    point = Point(
        color=BGR(r=255, g=0, b=0),
        alpha=0.5,
        position=Position.relative(x=0.5, y=0.5),
        radius=50,
        visible=False,
    )
    line = Line(
        points=[
            Position.relative(x=0.1, y=0.1),
            Position.relative(x=0.9, y=0.9),
            Position.relative(x=0.9, y=0.1),
        ],
        thickness=5,
        visible=False,
        alpha=0.5,
    )
    polygon = Polygon(
        points=[
            Position.relative(x=0.1, y=0.1),
            Position.relative(x=0.9, y=0.1),
            Position.relative(x=0.9, y=0.9),
            Position.relative(x=0.1, y=0.9),
        ],
        thickness=2,
        color=BGR(r=0, g=255, b=0),
        visible=False,
        alpha=0.7,
    )
    marker = Marker(
        position=Position.relative(x=0.5, y=0.5),
        size=50,
        color=BGR(r=0, g=0, b=200),
        visible=False,
        thickness=3,
        alpha=0.9,
    )
    square = Square(
        center=Position.relative(x=0.5, y=0.5),
        side=50,
        color=BGR(r=0, g=0, b=255),
        visible=False,
        alpha=0.5,
        fill=BGR(r=255, g=0, b=0),
    )
    circle = Circle(
        center=Position.relative(x=0.5, y=0.5),
        radius=20,
        color=BGR(r=255, g=0, b=255),
        visible=False,
        alpha=0.6,
        thickness=2,
        fill=BGR(r=0, g=255, b=255),
    )
    rectangle = Rectangle(
        top_left=Position.relative(x=0.1, y=0.1),
        btm_right=Position.relative(x=0.3, y=0.9),
        color=BGR(r=255, g=255, b=0),
        visible=True,
        alpha=0.8,
        thickness=3,
    )
    text = Text(
        position=Position.relative(x=0.3, y=0.5),
        text="Hello\ncvdraw!",
        font=Font(thickness=2),
        color=BGR(r=255, g=255, b=255),
        visible=True,
        alpha=1.0,
    )

    import json

    with open("compound.json", "w") as f:
        json.dump(text.model_dump(), f, indent=4)

    # new = render_one(image, point)
    # new = render_one(new, line)
    # new = render_one(new, polygon)
    # new = render_one(new, marker)
    # new = render_one(new, square)
    # new = render_one(new, circle)
    # new = render_one(new, rectangle)

    # new = render_one(image, compound)

    # cv2.imshow("Rendered Point", new)
    # cv2.waitKey(0)


if __name__ == "__main__":
    main()
