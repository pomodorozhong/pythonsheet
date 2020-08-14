import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math
from . import major as pm
from . import utility as pu


def _fit_poly_through_origin(x, y, n=1):
    a = x[:, np.newaxis] ** np.arange(1, n+1)
    coeff = np.linalg.lstsq(a, y)[0]
    return np.concatenate(([0], coeff))


def fit(x: 'series', y: 'series', deg: int,
        plot_file="",
        y_upper_bound=None,
        y_lower_bound=None,
        pass_zero=False):

    df = pu.combine_series_to_dataframe([x, y])

    # remove rows that contains non-numeric
    df = df[pd.to_numeric(df[x.name], errors='coerce').notnull()]
    df = df[pd.to_numeric(df[y.name], errors='coerce').notnull()]
    df[x.name] = pd.to_numeric(df[x.name])
    df[y.name] = pd.to_numeric(df[y.name])

    # remove outliers
    if y_upper_bound:
        df = df[df[y.name] < y_upper_bound]
    if y_lower_bound:
        df = df[df[y.name] > y_lower_bound]
    df = df[(np.abs(stats.zscore(df)) < 4).all(axis=1)]

    x = getattr(df, x.name)
    y = getattr(df, y.name)
    if pass_zero:
        model = _fit_poly_through_origin(x, y, deg)
    else:
        model = np.polynomial.polynomial.polyfit(x, y, deg)
    predict = np.polynomial.Polynomial(model)

    if plot_file != "":
        # clear plot
        plt.clf()

        # plotting
        x_min = pm.min(x)
        x_max = pm.max(x)
        x_diff = x_max - x_min
        plot_x_min = math.floor(x_min - x_diff * 0.1)
        plot_x_max = math.ceil(x_max + x_diff * 0.1)

        x_lin_reg = range(plot_x_min, plot_x_max)
        y_lin_reg = predict(x_lin_reg)
        plt.plot(x, y, 'kx')
        plt.plot(x_lin_reg, y_lin_reg, c='r')
        plt.title(predict)

        # save plot
        plt.savefig(plot_file)

    return predict
