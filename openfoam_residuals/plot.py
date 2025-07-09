"""Plotting utilities for OpenFOAM residuals analysis."""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

import openfoam_residuals.filesystem as fs


def order_of_magnitude(number: float) -> int:
    """Return the order of magnitude of a number."""
    if np.isnan(number):
        return 0
    return math.floor(math.log10(number))


def roundup(x: float) -> int:
    """Round up to the next hundred."""
    return math.ceil(x / 100.0) * 100


def export_files(
    residual_files: list[Path],
    min_val: float,
    max_iter: int,
    output_dir: Path | None = None,
) -> None:
    """Export PNG plots for all residual files."""
    if output_dir is not None:
        output_dir_path = output_dir
        output_dir_path.mkdir(parents=True, exist_ok=True)
    else:
        output_dir_path = Path.cwd()

    for idx, filepath in enumerate(residual_files):
        data, _ = fs.pre_parse(filepath)
        ax = data.plot(logy=True, figsize=(15, 5))
        ax.legend(loc="upper right")
        ax.set_xlabel("Iterations")
        ax.set_ylabel("Residuals")
        ax.set_ylim(min_val, 1)
        ax.set_xlim(0, max_iter)
        file_parts = filepath.parts
        wind_dir = file_parts[-4] if len(file_parts) >= 4 else "Dir"
        iteration = file_parts[-2] if len(file_parts) >= 2 else "Iter"
        out_name = f"{idx}_{wind_dir}_{iteration}_residuals.png"
        out_path = output_dir_path / out_name
        plt.savefig(out_path, dpi=600)
        plt.close()
