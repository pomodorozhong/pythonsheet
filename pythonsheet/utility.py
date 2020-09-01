import pandas as pd
import numpy as np


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


def append_serieses(series1, series2):
    series1_is_empty = False
    series2_is_empty = False
    if series1 is None:
        series1_is_empty = True
    elif len(series1) == 0:
        series1_is_empty = True
    if series2 is None:
        series2_is_empty = True
    elif len(series2) == 0:
        series2_is_empty = True

    if series1_is_empty and series2_is_empty:
        return None
    elif series1_is_empty:
        return series2
    elif series2_is_empty:
        return series1

    out = series1.append(series2, ignore_index=True)
    return out
