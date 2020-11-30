import pandas as pd
import matplotlib.pyplot as plt
import pathlib
import os

w_dir = pathlib.Path.cwd()

residual_files = []
for root, dirs, files in os.walk(w_dir):
	for file in files:
		if file.startswith("residuals") and file.endswith(".dat"):
			p = os.path.join(root, file)
			residual_files.append(p)
			print(p)

for file in residual_files:
    iterations = pd.read_csv(file, skiprows = 1, delimiter='\s+')['#']
    data = pd.read_csv(file, skiprows=1, delimiter='\s+').iloc[:, 1:].shift(+1, axis=1).drop(["Time"], axis=1)
    data = data.set_index(iterations)
    plot = data.plot( logy=True, figsize=(15, 5))
    fig = plot.get_figure()
    ax = plt.gca()
    ax.legend(loc='upper right')
    ax.set_xlabel("Iterations")
    ax.set_ylabel("Residuals")
    ax.set_ylim(1e-7, 1)
    wind_dir = str(file).split('\\')[-5]
    iteration = str(file).split('\\')[-2]
    plt.savefig( wind_dir+ "_" + iteration + "_residuals.png", dpi=600)
