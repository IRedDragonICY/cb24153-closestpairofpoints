"""
case_withoutcolor.py

Finds the closest pair distance for a mixed set of points, ignoring their colors.
Demonstrates that we can treat ColoredPoints as Points if we only care about their
coordinates. Also plots the points, colored by their assigned color but not used in calculations.
"""

import matplotlib.pyplot as plt
from collections import defaultdict
from ..module.cpopstep.geometry import ColoredPoint
from ..module.cpopstep.algorithms import closest_pair_distance

if __name__ == "__main__":
    # Sample data
    data = [
        ("green", 2, 3), ("green", 5, 1), ("green", 6, 2), ("green", 7, 7), ("green", 20, 24),
        ("black", 3, 5), ("black", 13, 14), ("black", 27, 25),
        ("purple", 9, 6), ("purple", 12, 10), ("purple", 17, 21), ("purple", 18, 15),
        ("blue", 8, 15), ("blue", 19, 20), ("blue", 31, 33), ("blue", 40, 50),
        ("red", 12, 30), ("red", 22, 29), ("red", 25, 18), ("red", 35, 40)
    ]

    colored_points = [ColoredPoint(c, x, y) for c, x, y in data]

    # Compute the closest pair distance ignoring color
    d = closest_pair_distance(colored_points)
    print(f"Closest pair distance (ignoring color) is {d}")

    fig, ax = plt.subplots(figsize=(8,8))
    color_groups = defaultdict(list)
    for p in colored_points:
        color_groups[p.color].append(p)

    for c, pts in color_groups.items():
        xs = [p.x for p in pts]
        ys = [p.y for p in pts]
        ax.scatter(xs, ys, c=c, s=30, edgecolors='black', linewidths=0.5, zorder=3)

    ax.set_xlim(0, 64)
    ax.set_ylim(0, 64)

    major_ticks = range(0, 61, 10)
    minor_ticks = range(-4, 65, 2)

    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(minor_ticks, minor=True)

    ax.grid(which='major', color='black', linestyle='-', linewidth=1)
    ax.grid(which='minor', color='grey', linestyle=':', linewidth=0.5)

    plt.show()
