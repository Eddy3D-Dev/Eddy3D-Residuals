import math
import os
import pathlib
import sys

import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm
from openfoam_residuals import filesystem as fs

w_dir = pathlib.Path.cwd().parent / "tests" / "files"

print("Looking for files...")
residual_files = fs.find_residual_files(w_dir)

if len(residual_files) == 0:
    print("No files found.")
    sys.exit()

min_val, max_iter = fs.find_min_and_max_iteration(residual_files)

print("Exporting files...")
fs.export_files(residual_files, min_val, max_iter)
print("Done.")
