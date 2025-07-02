import pathlib
import sys

from openfoam_residuals import filesystem as fs
from openfoam_residuals import plot as pl

w_dir = pathlib.Path.cwd().parent / "tests" / "files"

print("Looking for files...")
residual_files = fs.find_residual_files(w_dir)

if len(residual_files) == 0:
    print("No files found.")
    sys.exit()

min_val, max_iter = fs.find_min_and_max_iteration(residual_files)

print("Exporting files...")
pl.export_files(residual_files, min_val, max_iter)
print("Done.")
