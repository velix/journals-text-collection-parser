import numpy as np
import matplotlib.pyplot as plt 


def IO(file):
    with open(file) as in_fyle:
        data = np.fromfile(in_fyle, sep = ' ')

        return data


data = IO('word_collection.txt')

