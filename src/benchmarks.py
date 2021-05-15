import random
import timeit


def get_times(list_length):
    # For numbers from 0 to list_length - 1, select list_length random numbers.
    # Mumber range == the number of samples for high chance of duplicates.
    unsorted = str([random.randrange(list_length) for i in range(list_length)])

    for algorithm in algorithms:
        time_in_seconds = timeit.timeit(
            setup=f"from sorting.{algorithm[0]} import {algorithm[1]}",
            stmt=f"{algorithm[1]}({unsorted})",
            number=1)
        algorithm[2].append(time_in_seconds)


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

get_times(10)
get_times(100)
get_times(1000)
get_times(10000)
get_times(100000)

for algorithm in algorithms:
    print(algorithm[0], algorithm[2])
