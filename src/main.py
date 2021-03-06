from algorithms_runtimes import AlgorithmsRuntimes
from benchmarks import run_benchmarks
from graph import graph
from sorting.bubble_sort import bubble_sort
from sorting.insertion_sort import insertion_sort
from sorting.selection_sort import selection_sort
from sorting.merge_sort import merge_sort
from sorting.heap_sort import heap_sort
from sorting.quick_sort import quick_sort_last_pivot
from sorting.quick_sort import quick_sort_random_pivot


RUN_BENCHMARKS = "1"
PLOT_GRAPH = "2"
SORTING_ARRAY = "3"
algorithms = {
    '1': ("Bubble sort", bubble_sort),
    '2': ("Insertion sort", insertion_sort),
    '3': ("Selection sort", selection_sort),
    '4': ("Merge sort", merge_sort),
    '5': ("Heap sort", heap_sort),
    '6': ("Quick sort (last pivot)", quick_sort_last_pivot),
    '7': ("Quick sort (random  pivot)", quick_sort_random_pivot),
}


def show_algorithm(key):
    print(key, ": ", algorithms[key][0])


def sort_alg(alg_num, arr):
    alg = algorithms[alg_num][1]
    alg(arr)
    print(arr)


if __name__ == '__main__':
    print("Select an option:")
    print(f"{RUN_BENCHMARKS}: Run the benchmarks. This will take a while.")
    print(f"{PLOT_GRAPH}: Plot the graph on hard-coded data sample.")
    print(f"{SORTING_ARRAY}: Sorting input array")

    option = input()
    if option == RUN_BENCHMARKS:
        run_benchmarks()
    elif option == PLOT_GRAPH:
        graph(AlgorithmsRuntimes.get_static_data())
    elif option == SORTING_ARRAY:
        print("Select an option:")
        for algorithm in algorithms:
            show_algorithm(algorithm)
        opt = input()
        try:
            print('Enter numbers separated by spaces')
            arr_nums = [*map(int, input().split())]
            sort_alg(opt, arr_nums)
        except ValueError:
            print('Enter Valid Number !')
    else:
        print("Unexpected input entered. Terminating the script.")
