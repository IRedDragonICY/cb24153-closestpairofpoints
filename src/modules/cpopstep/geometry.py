"""
geometry.py

These modules define the geometric data structures (Point and ColoredPoint)
used in the closest pair of points problem. It keeps the focus on data
representations and basic operations (like distance computation).
"""

import math

class Point:
    """
    A basic 2D point with x and y coordinates.
    """
    __slots__ = ('x', 'y')

    def __init__(self, x: float, y: float):
        """
        Initialize a Point instance.

        Parameters:
        - x (float): The x-coordinate of the point.
        - y (float): The y-coordinate of the point.
        """
        self.x = x
        self.y = y
        print(f"[Point] Created {self}")

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


class ColoredPoint(Point):
    """
    A Point subclass that includes a color attribute.
    Useful for differentiating points by categories or classes.
    """
    __slots__ = ('color',)

    def __init__(self, color: str, x: float, y: float):
        """
        Initialize a ColoredPoint instance.

        Parameters:
        - color (str): The color associated with this point.
        - x (float): The x-coordinate of the point.
        - y (float): The y-coordinate of the point.
        """
        self.color = color
        super().__init__(x, y)
        print(f"[ColoredPoint] Created {self}")

    def __repr__(self):
        return f"ColoredPoint(color={self.color}, x={self.x}, y={self.y})"


def dist(a: Point, b: Point) -> float:
    """
    Compute the Euclidean distance between two points a and b.

    Parameters:
    - a (Point): The first point.
    - b (Point): The second point.

    Returns:
    - (float) The Euclidean distance between a and b.
    """
    print("---------------------------------------------------------------------------------------------------")
    print(f"[dist] Calculating distance between points {a} and {b}:")
    dx = a.x - b.x
    dy = a.y - b.y
    print(f"[dist] δx = {a.x} - {b.x} = {dx}")
    print(f"[dist] δy = {a.y} - {b.y} = {dy}")
    d_squared = dx**2 + dy**2
    print(f"[dist] δ_squared = ({dx})^2 + ({dy})^2 = {d_squared}")
    d = math.sqrt(d_squared)
    print(f"[dist] δ = sqrt({d_squared}) = {d}")
    return d
