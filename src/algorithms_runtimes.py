class AlgorithmsRuntimes:
    """
    This class holds the value of x_axis (list lengths), and
    the corresponding running time for each length for each algorithm.
    """

    def __init__(self, x_axis):
        self.x_axis = x_axis
        # This will hold algorithm display name as key,
        # and running times list as value.
        # The running times list should be the same length as
        # x_axis
        self.algorithms = {}

    def add(self, display_name, running_times):
        if len(running_times) != len(self.x_axis):
            raise ValueError()
        self.algorithms[display_name] = running_times

    def get(self, display_name):
        return self.algorithms[display_name]

    @staticmethod
    def get_static_data():
        x_axis = [10, 100, 1000, 10000, 100000]
        runtimes = AlgorithmsRuntimes(x_axis)
        bubble_run_times = [3.4599999999995745e-05,
                            0.001337900000000003,
                            0.12916070000000002,
                            13.1553888,
                            1409.4415357999999]
        runtimes.add("Bubble sort", bubble_run_times)
        heap_run_times = [0.0001296000000000075,
                          0.0009455999999999909,
                          0.014609100000000041,
                          0.2000244000000002,
                          2.5589740000000347]
        runtimes.add("Heap sort", heap_run_times)
        insertion_run_times = [2.940000000001275e-05,
                               0.0007565999999999962,
                               0.0726116,
                               7.505490299999998,
                               839.1033212999998]
        runtimes.add("Insertion sort", insertion_run_times)
        merge_run_times = [9.660000000000224e-05,
                           0.0006404999999999883,
                           0.007498800000000028,
                           0.08596700000000013,
                           1.0144304999998894]
        runtimes.add("Merge sort", merge_run_times)
        quick_last_pivot_run_times = [0.0001516000000000295,
                                      0.0006526000000000032,
                                      0.008095799999999986,
                                      0.09926670000000115,
                                      1.1763576000003013]
        runtimes.add("Quick sort (last pivot)", quick_last_pivot_run_times)
        quick_random_pivot_run_times = [0.00020999999999998797,
                                        0.0010640000000000094,
                                        0.012826399999999905,
                                        0.13442350000000047,
                                        1.5613330999999562]
        runtimes.add("Quick sort (random pivot)", quick_random_pivot_run_times)
        selection_run_times = [2.980000000002425e-05,
                               0.0005186999999999831,
                               0.04861139999999997,
                               4.801655199999999,
                               668.9253484000001]
        runtimes.add("Selection sort", selection_run_times)
        return runtimes
