import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def getSeries(file_name, col):
    df = pd.read_csv(file_name)
    series = getattr(df, col)
    return series


def min(file_name, col):
    # prepare data series
    series = getSeries(file_name, col)

    # calculation
    min = series.min()

    return min


def max(file_name, col):
    # prepare data series
    series = getSeries(file_name, col)

    # calculation
    max = series.max()

    return max


def median(file_name, col):
    # prepare data series
    series = getSeries(file_name, col)

    # calculation
    med = series.median()

    return med


def std(file_name, col):
    # prepare data series
    series = getSeries(file_name, col)

    # calculation
    std = np.std(series)

    return std


def writeTableToCSV(file_name, table):
    f = open(file_name, "w")
    for row in table:
        for element in row:
            f.write(str(element)+",")
        f.write("\n")
    f.close()
