import matplotlib.pyplot as plt
from collections import defaultdict
from typing import List, Tuple
from ..module.cpop.geometry import ColoredPoint
from ..module.cpop.algorithms import closest_pair_distance

def parse_data(data: List[Tuple[str, int, int]]) -> List[ColoredPoint]:
    """Converts raw data into a list of ColoredPoint objects."""
    return [ColoredPoint(color, x, y) for color, x, y in data]

def group_by_color(points: List[ColoredPoint]) -> defaultdict:
    """Groups points by their color."""
    groups = defaultdict(list)
    for point in points:
        groups[point.color].append(point)
    return groups

def compute_closest_distances(points: List[ColoredPoint], by_color: bool = True) -> None:
    """
    Computes and prints the closest pair distances.
    - If by_color is True, computes per color.
    - If by_color is False, computes for all points together.
    """
    if by_color:
        groups = group_by_color(points)
        for color, pts in groups.items():
            dist = closest_pair_distance(pts)
            print(f"Closest pair distance for color {color}: {dist}")
    else:
        dist = closest_pair_distance(points)
        print(f"Closest pair distance (ignoring color): {dist}")

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

if __name__ == "__main__":
    raw_data = [
        ("green", 2, 3), ("green", 5, 1), ("green", 6, 2), ("green", 7, 7), ("green", 20, 24),
        ("black", 3, 5), ("black", 13, 14), ("black", 27, 25),
        ("purple", 9, 6), ("purple", 12, 10), ("purple", 17, 21), ("purple", 18, 15),
        ("blue", 8, 15), ("blue", 19, 20), ("blue", 31, 33), ("blue", 40, 50),
        ("red", 12, 30), ("red", 22, 29), ("red", 25, 18), ("red", 35, 40)
    ]

    parsed_points = parse_data(raw_data)
    print("Computing distances by color:")
    compute_closest_distances(parsed_points, by_color=True)

    print("\nComputing distances ignoring color:")
    compute_closest_distances(parsed_points, by_color=False)

    print("\nVisualizing points:")
    plot_points(parsed_points)

