import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def match(search_keys: 'series', search_range: 'series'):
    result = []

    for key in search_keys:
        if (search_range == key).any():
            index = int((search_range == key).argmax())
        else:
            index = "!NO_MATCH!"

        result.append(index)

    return result


def index(references: 'series', rows_to_extract: 'series'):
    result = []

    for row in rows_to_extract:
        if row == "!NO_MATCH!":
            result.append("NO_MATCH")
        else:
            result.append(references[row])

    return result


def combine_series_to_dataframe(series_array):
    dataframe = pd.concat(series_array, axis=1)
    return dataframe


def fit(x: 'series', y: 'series', deg: int,
        plot_file="",
        upper_bound=None,
        lower_bound=None,
        pass_zero=False):

    def fit_poly_through_origin(x, y, n=1):
        a = x[:, np.newaxis] ** np.arange(1, n+1)
        coeff = np.linalg.lstsq(a, y)[0]
        return np.concatenate(([0], coeff))

    df = combine_series_to_dataframe([x, y])

    # remove rows that contains non-numeric
    df = df[pd.to_numeric(df[x.name], errors='coerce').notnull()]
    df = df[pd.to_numeric(df[y.name], errors='coerce').notnull()]
    df[x.name] = pd.to_numeric(df[x.name])
    df[y.name] = pd.to_numeric(df[y.name])

    # remove outliers
    if upper_bound:
        df = df[df[y.name] < upper_bound]
    if lower_bound:
        df = df[df[y.name] > lower_bound]
    df = df[(np.abs(stats.zscore(df)) < 4).all(axis=1)]

    x = getattr(df, x.name)
    y = getattr(df, y.name)
    if pass_zero:
        model = fit_poly_through_origin(x, y, deg)
    else:
        model = np.polynomial.polynomial.polyfit(x, y, deg)
    predict = np.polynomial.Polynomial(model)

    if plot_file != "":
        # clear plot
        plt.clf()

        # plotting
        x_lin_reg = range(0, 2000)
        y_lin_reg = predict(x_lin_reg)
        plt.plot(x, y, 'kx')
        plt.plot(x_lin_reg, y_lin_reg, c='r')
        plt.title(predict)

        # save plot
        plt.savefig(plot_file)

    return predict
