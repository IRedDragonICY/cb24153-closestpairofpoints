from typing import List
from .geometry import Point, dist


def brute_force(points: List[Point]) -> float:
    """
    Brute force method to find the closest pair distance among a small set of points.
    This is used when n <= 3 or as a fallback method.

    Parameters:
    - points (List[Point]): The list of points to consider.

    Returns:
    - (float): The smallest distance between any pair of points.
    """
    print("===================================================================================")
    print("[brute_force] Brute forcing the closest pair in a small subset of points.")
    print("[brute_force] Points considered:")
    for p in points:
        print(f"             {p}")
    n = len(points)
    min_dist = float("inf")
    print("[brute_force] Initial min_dist = inf")

    # Compare every pair of points
    for i in range(n):
        for j in range(i+1, n):
            print("---------------------------------------------------------------------------------------------------")
            print(f"[brute_force] Checking pair: {points[i]} and {points[j]}")
            d = dist(points[i], points[j])
            print(f"[brute_force] Distance between {points[i]} and {points[j]} = {d}")

            if d < min_dist:
                print(f"[brute_force] Found a smaller distance: {d} < {min_dist}")
                min_dist = d
                print(f"[brute_force] Updating min_dist = {min_dist}")
            else:
                print(f"[brute_force] Current distance {d} is not less than min_dist {min_dist}")

    print("[brute_force] Brute force complete. Minimum distance found:", min_dist)
    return min_dist


def strip_closest(strip: List[Point], d: float) -> float:
    """
    Given a strip (a subset of points close to the dividing vertical line)
    and a current minimum distance d, this function finds the closest distance
    in the strip. Points in the strip are sorted by their y-coordinate.

    Parameters:
    - strip (List[Point]): The list of points in the strip.
    - d (float): The current known minimum distance.

    Returns:
    - (float): The updated minimum distance found in the strip.
    """
    print("===================================================================================")
    print("[strip_closest] Checking the 'strip' area for possibly closer pairs.")
    print("[strip_closest] Current minimum distance:", d)
    print("[strip_closest] Points in strip before sorting by y:")
    for p in strip:
        print("                ", p)

    # Sort strip by y-coordinate
    strip.sort(key=lambda p: p.y)
    print("[strip_closest] Points in strip after sorting by y-coordinate:")
    for p in strip:
        print("                ", p)

    min_dist = d
    n = len(strip)

    # According to the closest pair theorem, we need to check at most 7 points ahead.
    for i in range(n):
        for j in range(i+1, min(i+7, n)):
            vertical_distance = strip[j].y - strip[i].y
            if vertical_distance >= min_dist:
                print("---------------------------------------------------------------------------------------------------")
                print(f"[strip_closest] For {strip[i]} and {strip[j]}, vertical distance {vertical_distance} >= {min_dist}.")
                print("[strip_closest] No need to check further in this inner loop.")
                break
            else:
                print("---------------------------------------------------------------------------------------------------")
                print(f"[strip_closest] Checking {strip[i]} vs {strip[j]}:")
                print(f"[strip_closest] Vertical distance {vertical_distance} < {min_dist}, proceeding to distance calculation.")
                d_ij = dist(strip[i], strip[j])
                print(f"[strip_closest] Computed distance = {d_ij}")
                if d_ij < min_dist:
                    print(f"[strip_closest] Found smaller distance: {d_ij} < {min_dist}")
                    min_dist = d_ij
                else:
                    print(f"[strip_closest] Distance {d_ij} >= {min_dist}, no update.")

    print("[strip_closest] Strip check complete. Minimum distance in strip:", min_dist)
    return min_dist


def closest_pair_util(points: List[Point]) -> float:
    """
    A recursive utility function that computes the closest pair distance
    for a list of points sorted by x-coordinate.

    Parameters:
    - points (List[Point]): Points sorted by x-coordinate.

    Returns:
    - (float): The smallest distance between any pair of points in the subset.
    """
    print("===================================================================================")
    print("[closest_pair_util] Divide and Conquer step")
    print("[closest_pair_util] Number of points:", len(points))
    print("[closest_pair_util] Points sorted by x (as given):")
    for p in points:
        print("                 ", p)

    n = len(points)
    # If the dataset is small, use brute force directly.
    if n <= 3:
        print("[closest_pair_util] n <= 3, using brute force on these points.")
        return brute_force(points)

    # Divide step
    mid = n // 2
    mid_point = points[mid]
    print("[closest_pair_util] Dividing the points into two halves.")
    print("[closest_pair_util] Mid index:", mid, "Mid point:", mid_point)
    left_points = points[:mid]
    right_points = points[mid:]
    print("[closest_pair_util] Left subset:")
    for p in left_points:
        print("                  ", p)
    print("[closest_pair_util] Right subset:")
    for p in right_points:
        print("                  ", p)

    # Recursively find the smallest distances in left and right subsets
    print("[closest_pair_util] Recursively solving left half:")
    d_left = closest_pair_util(left_points)
    print("[closest_pair_util] Closest pair distance in left half:", d_left)
    print("[closest_pair_util] Recursively solving right half:")
    d_right = closest_pair_util(right_points)
    print("[closest_pair_util] Closest pair distance in right half:", d_right)

    # Find the minimum of the two distances
    d = min(d_left, d_right)
    print("[closest_pair_util] Minimum distance between left and right:", d)

    # Create the strip subset of points
    print("[closest_pair_util] Building strip of points close to the dividing line.")
    strip = [p for p in points if abs(p.x - mid_point.x) < d]
    print("[closest_pair_util] Points within the strip (|x - mid_point.x| < d):")
    for p in strip:
        print("                  ", p)

    # Find the closest points in strip
    d_strip = strip_closest(strip, d)
    print("[closest_pair_util] Minimum distance found in strip:", d_strip)

    final_min = min(d, d_strip)
    print("[closest_pair_util] Returning minimum distance from this subproblem:", final_min)
    return final_min


def closest_pair_distance(points: List[Point]) -> float:
    """
    The main function to find the closest pair of points distance from a given set of points.
    Uses a divide-and-conquer approach with O(n log n) complexity.

    Parameters:
    - points (List[Point]): The list of points.

    Returns:
    - (float): The smallest distance between any pair of points.
    """
    print("===================================================================================")
    print("[closest_pair_distance] Initiating closest pair computation.")
    if not points or len(points) < 2:
        print("[closest_pair_distance] Not enough points provided. Returning inf.")
        return float('inf')

    # Sort points by x-coordinate
    print("[closest_pair_distance] Sorting points by x-coordinate.")
    points_sorted = sorted(points, key=lambda p: p.x)
    print("[closest_pair_distance] Points after sorting by x:")
    for p in points_sorted:
        print("                       ", p)

    # Use recursive divide and conquer method
    result = closest_pair_util(points_sorted)
    print("[closest_pair_distance] Closest pair distance result:", result)
    return result
