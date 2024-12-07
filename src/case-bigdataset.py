"""
case_bigdataset.py

This script evaluates the performance of the brute force and divide & conquer 
methods on larger datasets. It generates random points, measures execution time,
and plots the results. It demonstrates how the O(n^2) brute force approach 
compares to the O(n log n) divide-and-conquer approach.
"""

import time
import random
import pandas as pd
import matplotlib.pyplot as plt
from modules.cpop.geometry import Point
from modules.cpop.algorithms import brute_force, closest_pair_distance

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)


def generate_points(n, x_range=(0, 10**6), y_range=(0, 10**6)):
    """
    Generate a list of random points within given ranges.

    Parameters:
    - n (int): Number of points to generate.
    - x_range (tuple): Range of possible x-values.
    - y_range (tuple): Range of possible y-values.

    Returns:
    - (List[Point]): List of generated points.
    """
    return [Point(random.randint(*x_range), random.randint(*y_range)) for _ in range(n)]


def evaluate_performance(sizes):
    """
    Evaluate performance (execution time and found distances) for different dataset sizes.

    Parameters:
    - sizes (List[int]): List of sizes for which to run the tests.

    Returns:
    - (pd.DataFrame): DataFrame with performance results.
    """
    results = []
    for n in sizes:
        points = generate_points(n)

        start = time.time()
        bf_dist = brute_force(points)
        bf_time = time.time() - start

        start = time.time()
        dc_dist = closest_pair_distance(points)
        dc_time = time.time() - start

        results.append({
            "Number of Points": n,
            "Brute Force Distance": round(bf_dist, 6),
            "Brute Force Time (s)": round(bf_time, 6),
            "Divide & Conquer Distance": round(dc_dist, 6),
            "Divide & Conquer Time (s)": round(dc_time, 6)
        })

    results_df = pd.DataFrame(results)
    print(results_df)
    return results_df


def plot_performance(results_df):
    """
    Plot the performance of brute force and divide-and-conquer methods 
    in terms of execution time as a function of dataset size.

    Parameters:
    - results_df (pd.DataFrame): DataFrame with performance results.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(results_df["Number of Points"], results_df["Brute Force Time (s)"], 
            label="Brute Force Time (s)", marker='o')
    ax.plot(results_df["Number of Points"], results_df["Divide & Conquer Time (s)"], 
            label="Divide & Conquer Time (s)", marker='o')

    ax.set_xlabel("Number of Points")
    ax.set_ylabel("Time (s)")
    ax.set_title("Performance Comparison of Closest Pair Algorithms")
    ax.legend()
    ax.grid(True)
    ax.set_xscale('log')
    ax.set_yscale('log')

    plt.show()


if __name__ == "__main__":
    dataset_sizes = [1000, 10000, 100000]
    performance_results = evaluate_performance(dataset_sizes)
    plot_performance(performance_results)

