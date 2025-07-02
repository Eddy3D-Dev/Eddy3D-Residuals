from pathlib import Path

import pandas as pd

from openfoam_residuals import plot as orp


def find_residual_files(w_dir):
    """Return a list of all residuals*.dat files recursively found under w_dir."""
    return [str(p) for p in Path(w_dir).rglob("residuals*.dat")]


def find_min_and_max_iteration(residual_files):
    """Return (min_val, max_iter) across all files."""
    min_val = 1
    max_iter = 0
    for file in residual_files:
        data, _ = pre_parse(file)
        min_i = 10 ** orp.order_of_magnitude(data.min().min())
        if 0 < min_i < min_val:
            min_val = min_i
        max_iter_i = data.index.max()
        if max_iter_i > max_iter:
            max_iter = orp.roundup(max_iter_i)
    return min_val, max_iter


def pre_parse(file):
    raw_data = pd.read_csv(file, skiprows=1, delimiter='\s+')
    iterations = raw_data['#']
    data = raw_data.iloc[:, 1:].shift(+1, axis=1).drop(["Time"], axis=1)
    data = data.set_index(iterations)

    return data, iterations
