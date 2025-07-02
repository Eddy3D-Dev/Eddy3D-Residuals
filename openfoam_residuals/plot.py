import math
import os
import pathlib
import sys

import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm

def order_of_magnitude(number):
    return math.floor(math.log(number, 10))

def roundup(x):
    return int(math.ceil(x / 100.0)) * 100

def pre_parse(file):
    raw_data = pd.read_csv(file, skiprows=1, delimiter='\s+')
    iterations = raw_data['#']
    data = raw_data.iloc[:, 1:].shift(+1, axis=1).drop(["Time"], axis=1)
    data = data.set_index(iterations)
    
    return data, iterations

def find_min_and_max_iteration(residual_files):
    min_val = 1
    max_iter = 0

    for file in residual_files:
        data, iterations = pre_parse(file)
        min_i = math.pow(10, order_of_magnitude(data.min().min()))
        if min_i < min_val and min_i > 0:
            min_val = min_i
        max_iter_i = data.index.max()
        if max_iter_i > max_iter and max_iter_i > 0:
            max_iter = roundup(max_iter_i)
    
    return min_val, max_iter
