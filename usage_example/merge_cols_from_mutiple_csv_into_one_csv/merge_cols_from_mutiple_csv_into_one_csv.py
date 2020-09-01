from pythonsheet.pythonsheet import major as pm
from pythonsheet.pythonsheet import csv_ as csv
from pythonsheet.pythonsheet import utility as pu

source_a = 'pythonsheet/usage_example/merge_cols_from_mutiple_csv_into_one_csv/probe.csv'
source_b = 'pythonsheet/usage_example/merge_cols_from_mutiple_csv_into_one_csv/gauge.csv'
whole_experiment = 'pythonsheet/usage_example/merge_cols_from_mutiple_csv_into_one_csv/curated.csv'

measure_a = 'temperature'
measure_b = 'torsion'

series_a = csv.get_series(source_a, measure_a)
series_b = csv.get_series(source_b, measure_b)

dataframe = pu.combine_series_to_dataframe([
    series_a,
    series_b,
])
csv.write_dataframe_to_csv(whole_experiment, dataframe)
