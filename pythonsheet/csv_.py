# Using this file name "csv_.py", to avoid file name collision with pandas.
# related discussion: https://stackoverflow.com/a/62272471/13044647

import pandas as pd


def get_series(file_name, col):
    df = pd.read_csv(file_name)
    series = getattr(df, col)
    return series


def write_table_to_csv(file_name, table):
    f = open(file_name, "w")
    for row in table:
        for element in row:
            f.write(str(element)+",")
        f.write("\n")
    f.close()


def write_1d_array_to_csv(file_name, array):
    f = open(file_name, "w")
    for element in array:
        f.write(str(element)+",")
        f.write("\n")
    f.close()


def write_dataframe_to_csv(file_name, dataframe):
    dataframe.to_csv(file_name)


def write_series_to_csv(file_name, series):
    series.to_csv(file_name)
