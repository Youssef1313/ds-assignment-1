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
alg_name = ['Bubble Sort',
            'Insertion Sort',
            'Selection Sort',
            'Merge Sort',
            'Heap Sort',
            'Quick Sort Last Pivot',
            'Quick Sort Rnadom Pivot']


def show_alg(i, st):
    print(i, " : ", st)


def sort_alg(op, arr):
    if op == '1':
        bubble_sort(arr)
    elif op == '2':
        insertion_sort(arr)
    elif op == '3':
        selection_sort(arr)
    elif op == '4':
        merge_sort(arr)
    elif op == '5':
        heap_sort(arr)
    elif op == '6':
        quick_sort_last_pivot(arr)
    elif op == '7':
        quick_sort_random_pivot(arr)
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
        graph()
    elif option == SORTING_ARRAY:
        print("Select an option:")
        for i in range(len(alg_name)):
            show_alg(i, alg_name[i])
        opt = input()
        try:
            print('Enter your array numbers')
            arr_nums = list(map(int, input().split()))
            sort_alg(opt,arr_nums)
        except: 
            print('Enter Valid Number !')
        
    else:
        print("Unexpected input entered. Terminating the script.")
