import math
from pathlib import Path
import numpy as np

import matplotlib.pyplot as plt

import openfoam_residuals.filesystem as fs


def order_of_magnitude(number):
    if number is np.nan:
        return 0
    return math.floor(math.log(number, 10))


def roundup(x):
    return int(math.ceil(x / 100.0)) * 100


def export_files(residual_files, min_val, max_iter, output_dir=None):
    """Export PNG plots for all residual files."""
    if output_dir is not None:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    else:
        output_dir = Path.cwd()

    for idx, filepath in enumerate(residual_files):
        data, _ = fs.pre_parse(filepath)
        ax = data.plot(logy=True, figsize=(15, 5))
        ax.legend(loc='upper right')
        ax.set_xlabel("Iterations")
        ax.set_ylabel("Residuals")
        ax.set_ylim(min_val, 1)
        ax.set_xlim(0, max_iter)
        file_parts = Path(filepath).parts
        wind_dir = file_parts[-4] if len(file_parts) >= 4 else "Dir"
        iteration = file_parts[-2] if len(file_parts) >= 2 else "Iter"
        out_name = f"{idx}_{wind_dir}_{iteration}_residuals.png"
        out_path = output_dir / out_name
        print(f"Plotting {out_name}")
        plt.savefig(out_path, dpi=600)
        plt.close()
