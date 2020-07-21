import numpy as np


def min(series):
    min = series.min()

    return min


def max(series):
    max = series.max()

    return max


def median(series):
    med = series.median()

    return med


def std(series):
    std = np.std(series)

    return std
