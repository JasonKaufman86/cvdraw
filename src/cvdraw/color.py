from pydantic import BaseModel, Field


class BGR(BaseModel):
    """BGR color model."""

    b: int = Field(..., ge=0, le=255, description="Blue channel value (0-255).")
    g: int = Field(..., ge=0, le=255, description="Green channel value (0-255).")
    r: int = Field(..., ge=0, le=255, description="Red channel value (0-255).")

    @classmethod
    def red(cls) -> "BGR":
        """Return a BGR instance representing red color."""
        return cls(b=0, g=0, r=255)

    @classmethod
    def green(cls) -> "BGR":
        """Return a BGR instance representing green color."""
        return cls(b=0, g=255, r=0)

    @classmethod
    def blue(cls) -> "BGR":
        """Return a BGR instance representing blue color."""
        return cls(b=255, g=0, r=0)

    def to_tuple(self) -> tuple[int, int, int]:
        """Convert BGR to a tuple."""
        return (self.b, self.g, self.r)
