from matplotlib import pyplot as plt


def graph(algorithms_runtimes):
    x_axis = algorithms_runtimes.x_axis
    # plt.yscale("log")
    # plt.xscale("log")
    for display_name, run_times in algorithms_runtimes.algorithms.items():
        plt.plot(x_axis, run_times, label=display_name)

    plt.title("Sorting algorithms run times")
    plt.legend()
    plt.show()
