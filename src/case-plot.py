from typing import List

from modules.cpop.algorithms import closest_pair_distance
from modules.cpop.geometry import ColoredPoint
from modules.utils import parse_data, group_by_color, plot_points


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