from matplotlib import pyplot as plt


def graph():
    x_axis = [10, 100, 1000, 10000, 100000]

    plt.yscale("log")
    plt.xscale("log")

    # Algorithms running times were obtained from running `benchmarks.py`
    # script which is expensive, so data from a sample run are hard-coded
    # to be graphed using Matplotlib.

    bubble_run_times = [3.4599999999995745e-05,
                        0.001337900000000003,
                        0.12916070000000002,
                        13.1553888,
                        1409.4415357999999]

    plt.plot(x_axis, bubble_run_times, label='Bubble sort')

    heap_run_times = [0.0001296000000000075,
                      0.0009455999999999909,
                      0.014609100000000041,
                      0.2000244000000002,
                      2.5589740000000347]
    plt.plot(x_axis, heap_run_times, label='Heap sort')

    insertion_run_times = [2.940000000001275e-05,
                           0.0007565999999999962,
                           0.0726116,
                           7.505490299999998,
                           839.1033212999998]
    plt.plot(x_axis, insertion_run_times, label='Insertion sort')

    merge_run_times = [9.660000000000224e-05,
                       0.0006404999999999883,
                       0.007498800000000028,
                       0.08596700000000013,
                       1.0144304999998894]
    plt.plot(x_axis, merge_run_times, label='Merge sort')

    quick_last_pivot_run_times = [0.0001516000000000295,
                                  0.0006526000000000032,
                                  0.008095799999999986,
                                  0.09926670000000115,
                                  1.1763576000003013]
    plt.plot(x_axis, quick_last_pivot_run_times, label='Quick sort (last pivot)')

    quick_random_pivot_run_times = [0.00020999999999998797,
                                    0.0010640000000000094,
                                    0.012826399999999905,
                                    0.13442350000000047,
                                    1.5613330999999562]
    plt.plot(x_axis, quick_random_pivot_run_times, label='Quick sort (random pivot)')

    selection_run_times = [2.980000000002425e-05,
                           0.0005186999999999831,
                           0.04861139999999997,
                           4.801655199999999,
                           668.9253484000001]
    plt.plot(x_axis, selection_run_times, label='Selection sort')

    plt.title("Logarithmic scale of sorting algorithms run times")
    plt.legend()
    plt.show()
