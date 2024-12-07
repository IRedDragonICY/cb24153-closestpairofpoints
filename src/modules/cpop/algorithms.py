"""
algorithms.py

This modules implements the closest pair of points algorithm using a
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
    n = len(points)
    min_dist = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            d = dist(points[i], points[j])
            if d < min_dist:
                min_dist = d
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
    # Sort strip by y-coordinate
    strip.sort(key=lambda p: p.y)
    min_dist = d
    n = len(strip)

    # According to the closest pair theorem, we need to check at most 7 points ahead.
    for i in range(n):
        for j in range(i+1, min(i+7, n)):
            if (strip[j].y - strip[i].y) >= min_dist:
                break
            d_ij = dist(strip[i], strip[j])
            if d_ij < min_dist:
                min_dist = d_ij
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
    n = len(points)
    # If the dataset is small, use brute force directly.
    if n <= 3:
        return brute_force(points)

    # Divide step
    mid = n // 2
    mid_point = points[mid]

    # Recursively find the smallest distances in left and right subsets
    d_left = closest_pair_util(points[:mid])
    d_right = closest_pair_util(points[mid:])
    d = min(d_left, d_right)

    # Create the strip subset of points
    strip = [p for p in points if abs(p.x - mid_point.x) < d]

    # Find the closest points in strip
    d_strip = strip_closest(strip, d)

    return min(d, d_strip)


def closest_pair_distance(points: List[Point]) -> float:
    """
    The main function to find the closest pair of points distance from a given set of points.
    Uses a divide-and-conquer approach with O(n log n) complexity.

    Parameters:
    - points (List[Point]): The list of points.

    Returns:
    - (float): The smallest distance between any pair of points.
    """
    if not points or len(points) < 2:
        return float('inf')

    # Sort points by x-coordinate
    points_sorted = sorted(points, key=lambda p: p.x)

    return closest_pair_util(points_sorted)
