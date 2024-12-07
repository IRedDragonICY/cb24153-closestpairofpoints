"""
algorithms.py

These modules implement the closest pair of points algorithm using a
divide-and-conquer approach, as well as a brute-force approach for small subsets.

Key functions:
- brute_force(points): O(n^2) approach, used for small subsets.
- closest_pair_distance(points): O(n log n) divide and conquer solution.

The divide-and-conquer solution:
1. Sort points by x-coordinate.
2. Recursively find the closest pairs in the left and right subsets.
3. Combine results and check the "strip" (points close to the dividing line)
   to find if there's a closer pair that straddles the two subsets.
"""

from collections import defaultdict
from typing import List, Tuple

from matplotlib import pyplot as plt

from .cpop.geometry import ColoredPoint

def parse_data(data: List[Tuple[str, int, int]]) -> List[ColoredPoint]:
    """Converts raw data into a list of ColoredPoint objects."""
    return [ColoredPoint(color, x, y) for color, x, y in data]

def group_by_color(points: List[ColoredPoint]) -> defaultdict:
    """Groups points by their color."""
    groups = defaultdict(list)
    for point in points:
        groups[point.color].append(point)
    return groups

def plot_points(points: List[ColoredPoint]) -> None:
    """Visualizes the points on a 2D grid, colored by their assigned color."""
    groups = group_by_color(points)
    fig, ax = plt.subplots(figsize=(8, 8))
    for color, pts in groups.items():
        xs = [p.x for p in pts]
        ys = [p.y for p in pts]
        ax.scatter(xs, ys, c=color, s=30, edgecolors='black', linewidths=0.5, zorder=3)

    ax.set_xlim(0, 64)
    ax.set_ylim(0, 64)
    ax.set_xticks(range(0, 61, 10), minor=False)
    ax.set_yticks(range(0, 61, 10), minor=False)
    ax.set_xticks(range(-4, 65, 2), minor=True)
    ax.set_yticks(range(-4, 65, 2), minor=True)
    ax.grid(which='major', color='black', linestyle='-', linewidth=1)
    ax.grid(which='minor', color='grey', linestyle=':', linewidth=0.5)
    plt.show()