# Data structures II - Assignment 1

**Goal:** understand different running times for each algorithm, best and worst-case running times.

## Implementation

1. You're required to implement:

    - Three O(n<sup>2</sup>) algorithms (selection sort, bubble sort, and insertion sort).
    - Three O(nlogn) algorithms (merge sort, quick sort, and heap sort).

2. You're required to compare the running time performance of your algorithms against each other.

    To test your implementation and analyze the running time performance, generate a dataset of random numbers, and plot the relationship between the execution time of the sorting algorithm versus the input size.

## Report

A graph is required between time vs array length for the different algorithms and calculate the time required to sort it using the algorithms you implemented above and plot the results to a graph as what is shown in the image, you can use Excel sheet to achieve the job.

## Deliverables

- All the 6 sorting algorithms.
- Generate random arrays of sizes 10, 100, 1000, 10000, and 100000.

  - Do not include random arrays generation time when measuring each algorithm running time.
  - Make sure each algorithm runs on the randomly generated arrays. When you call other sorting technique, make sure that you call it with original array not the sorted one.

- Report containing the following:

    - Description of the program.
    - Pseudo code for each algorithm.
    - Sample runs.
    - Graph described earlier.

## Begin local development

To start developing/running locally:

1. Make sure you have Python 3.9 and VSCode installed.
2. Run the following commands in the root of the repository:

    ```
    python -m pip install --upgrade pip
    pip install -r dependencies/dev_requirements.txt
    pip install -r dependencies/requirements.txt
    ```

    This will install the [required dependencies](dependencies/requirements.txt) needed by `graph.py` as well as the [required development dependencies](dependencies/dev_requirements.txt) (linters and `pytest`).

    If you intend to only run `graph.py`, you can skip installing the `dev_requirements.txt` and only install `requirements.txt`.

3. Run `pytest` in the root of the repository, you should see all unit tests passing.
4. Open the directory in VSCode and enjoy!

## How to use

1. The script you need to run is `main.py`.
2. It gives you three options:

    ```
    Select an option:
    1: Run the benchmarks. This will take a while.
    2: Plot the graph on hard-coded data sample.
    3: Sorting input array
    ```

    1. Run benchmarks - this will then give you the option to either run *all the algorithms* (which can take LOTS of time) against random list (average case scenario), or a sorted list (best case scenario). The algorithms will be run against list lengths of 10, 100, 1000, 10000, 100000. You can change that in `benchmarks.py` by modifying `x_axis` variable. After that, it will show the plot.
    2. Plot the graph on hard-coded data sample - this will show a sample plot without having to wait for benchmarks.
    3. Sorting input array - this allows you to give an input of your choice to a specific algorithm.

### Important notes

- Running benchmarks against a sorted input is much faster, however, the quick sort algorithm will fail causing the program to crash with a stack overflow on large lists.
