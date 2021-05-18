from benchmarks import run_benchmarks
from graph import graph


RUN_BENCHMARKS = "1"
PLOT_GRAPH = "2"

if __name__ == '__main__':
    print("Select an option:")
    print(f"{RUN_BENCHMARKS}: Run the benchmarks. This will take a while.")
    print(f"{PLOT_GRAPH}: Plot the graph on hard-coded data sample.")
    option = input()
    if option == RUN_BENCHMARKS:
        run_benchmarks()
    elif option == PLOT_GRAPH:
        graph()
    else:
        print("Unexpected input entered. Terminating the script.")
