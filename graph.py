from matplotlib import pyplot as plt
import numpy as np

"""
Recommended to use Anaconda Environment (Spyder or Jupyter)
when running this script.
"""

x = [10, 100, 1000, 10000, 100000]

plt.yscale("log")
plt.xscale("log")

"""
Algorithms running times were obtained from running `benchmarks.py` script which is expensive,
so data from a sample run are hard-coded to be graphed using Matplotlib.
"""

plt.plot(x, np.array([3.4599999999995745e-05,
                      0.001337900000000003,
                      0.12916070000000002,
                      13.1553888,
                      1409.4415357999999]),
         label='Bubble sort')

plt.plot(x, np.array([0.0001296000000000075,
                      0.0009455999999999909,
                      0.014609100000000041,
                      0.2000244000000002,
                      2.5589740000000347]),
         label='Heap sort')

plt.plot(x, np.array([2.940000000001275e-05,
                      0.0007565999999999962,
                      0.0726116,
                      7.505490299999998,
                      839.1033212999998]),
         label='Insertion sort')

plt.plot(x, np.array([9.660000000000224e-05,
                      0.0006404999999999883,
                      0.007498800000000028,
                      0.08596700000000013,
                      1.0144304999998894]),
         label='Merge sort')

plt.plot(x, np.array([0.0001516000000000295,
                      0.0006526000000000032,
                      0.008095799999999986,
                      0.09926670000000115,
                      1.1763576000003013]),
         label='Quick sort (last pivot)')

plt.plot(x, np.array([0.00020999999999998797,
                      0.0010640000000000094,
                      0.012826399999999905,
                      0.13442350000000047,
                      1.5613330999999562]),
         label='quick_sort_random_pivot')

plt.plot(x, np.array([2.980000000002425e-05,
                      0.0005186999999999831,
                      0.04861139999999997,
                      4.801655199999999,
                      668.9253484000001]),
         label='selection_sort')

fig = plt.gcf()
fig.set_size_inches(10, 10)
plt.legend(bbox_to_anchor=(1, 1))
