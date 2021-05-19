import random
import timeit

from algorithms_runtimes import AlgorithmsRuntimes
from graph import graph


def _get_times(list_length, algorithms, is_sorted):
    # For numbers from 0 to list_length - 1, select list_length random numbers.
    # Mumber range == the number of samples for high chance of duplicates.
    unsorted_list = [random.randrange(list_length) for _ in range(list_length)]
    if is_sorted:
        unsorted_list.sort()
    unsorted = str(unsorted_list)
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

    print("Enter 1 to run against random list or 2 to run against sorted list")
    user_option = input()
    if user_option == "1":
        is_sorted = False
    elif user_option == "2":
        is_sorted = True
    else:
        print("Unexpected value. Terminating the program.")
        return

    # x_axis = [10, 100, 1000, 10000, 100000]
    x_axis = [*range(0, 1500, 10)]
    runtimes = AlgorithmsRuntimes(x_axis)
    for input_size in x_axis:
        _get_times(input_size, algorithms, is_sorted)

    for algorithm in algorithms:
        print(algorithm[1], algorithm[2])
        # pylint: disable=W0511
        # TODO: Nicer display name.
        runtimes.add(algorithm[1], algorithm[2])
    graph(runtimes)
