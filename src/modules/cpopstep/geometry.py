# geometry.py
"""
Defines Point and ColoredPoint classes and the dist function.
All logging is through log_message from logger.py.
"""

import math
from .logger import log_message

class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        log_message(f"[Point] Created {self}")

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

class ColoredPoint(Point):
    __slots__ = ('color',)

    def __init__(self, color: str, x: float, y: float):
        self.color = color
        super().__init__(x, y)
        log_message(f"[ColoredPoint] Created {self}")

    def __repr__(self):
        return f"ColoredPoint(color={self.color}, x={self.x}, y={self.y})"

def dist(a: Point, b: Point) -> float:
    log_message("---------------------------------------------------------------------------------------------------")
    log_message(f"[dist] Calculating Euclidean distance between {a} and {b}:")
    dx = a.x - b.x
    dy = a.y - b.y
    log_message(f"[dist] δx = {a.x} - {b.x} = {dx}")
    log_message(f"[dist] δy = {a.y} - {b.y} = {dy}")
    d_squared = dx**2 + dy**2
    log_message(f"[dist] δ² = ({dx})² + ({dy})² = {d_squared}")
    d = math.sqrt(d_squared)
    log_message(f"[dist] δ = sqrt({d_squared}) = {d}")
    return d
