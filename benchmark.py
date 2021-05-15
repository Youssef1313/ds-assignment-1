import numpy as np


def get_random_normal_distributions(dists):
    dists_list = np.array([np.empty(num) for num in dists], dtype=object)
    for i, num in enumerate(dists):
        dists_list[i] = np.random.standard_normal(size=(1, num))
    return dists_list
