import random
import timeit


def _get_times(list_length, algorithms):
    # For numbers from 0 to list_length - 1, select list_length random numbers.
    # Mumber range == the number of samples for high chance of duplicates.
    unsorted = str([random.randrange(list_length) for i in range(list_length)])
    print(f"Started executing on list of length {list_length}")
    for algorithm in algorithms:
        print(f"Started {algorithm[1]}.")
        time_in_seconds = timeit.timeit(
            setup=f"from sorting.{algorithm[0]} import {algorithm[1]}",
            stmt=f"{algorithm[1]}({unsorted})",
            number=1)
        algorithm[2].append(time_in_seconds)
        print(f"Finished {algorithm[1]} in {time_in_seconds} seconds.")
        print()
    print()


def run_benchmarks():
    # List of tuple, each tuple contains module name, function name, and
    # execution times.
    algorithms = [
        ("bubble_sort", "bubble_sort", []),
        ("heap_sort", "heap_sort", []),
        ("insertion_sort", "insertion_sort", []),
        ("merge_sort", "merge_sort", []),
        ("quick_sort", "quick_sort_last_pivot", []),
        ("quick_sort", "quick_sort_random_pivot", []),
        ("selection_sort", "selection_sort", []),
    ]

    _get_times(10, algorithms)
    _get_times(100, algorithms)
    _get_times(1000, algorithms)
    _get_times(10000, algorithms)
    _get_times(100000, algorithms)

    for algorithm in algorithms:
        print(algorithm[1], algorithm[2])
