import math
import os
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm
from openfoam_residuals import plot as orp

def find_residual_files(w_dir):
    residual_files = []
    for root, dirs, files in os.walk(w_dir):
        for file in files:
            if file.startswith("residuals") and file.endswith(".dat"):
                p = os.path.join(root, file)
                residual_files.append(p)
                print(p)
    return residual_files

def find_min_and_max_iteration(residual_files):
    min_val = 1
    max_iter = 0

    for file in residual_files:
        data, iterations = orp.pre_parse(file)
        min_i = math.pow(10, orp.order_of_magnitude(data.min().min()))
        if min_i < min_val and min_i > 0:
            min_val = min_i
        max_iter_i = data.index.max()
        if max_iter_i > max_iter and max_iter_i > 0:
            max_iter = orp.roundup(max_iter_i)
    
    return min_val, max_iter


def export_files(residual_files, min_val, max_iter):
    for filepath in tqdm(residual_files):
        data, iterations = orp.pre_parse(filepath)
        plot = data.plot(logy=True, figsize=(15, 5))
        fig = plot.get_figure()
        ax = plt.gca()
        ax.legend(loc='upper right')
        ax.set_xlabel("Iterations")
        ax.set_ylabel("Residuals")
        ax.set_ylim(min_val, 1)
        ax.set_xlim(0, max_iter)

        try:
            wind_dir = Path(filepath).parts[-4]
            iteration = Path(filepath).parts[-2]
        except:
            print(" This was probably not written by Eddy3D. Assuming default names...")
            wind_dir = "Dir"
            iteration = "Iter"

        plt.savefig(wind_dir + "_" + iteration + "_residuals.png", dpi=600)
        plt.close()

