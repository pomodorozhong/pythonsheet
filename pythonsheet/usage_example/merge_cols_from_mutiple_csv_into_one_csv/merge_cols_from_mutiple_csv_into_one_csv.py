import pythonsheet.pythonsheet.major as pm
import pythonsheet.pythonsheet.csv_ as csv
import pythonsheet.pythonsheet.utility as pu

file_a = ""
file_b = ""
new_csv = ""

col_a = ""
col_b = ""

series_a = csv.get_series(file_a, col_a)
series_b = csv.get_series(file_b, col_b)

dataframe = pu.combine_series_to_dataframe([
    series_a,
    series_b,
])
csv.write_dataframe_to_csv(new_csv, dataframe)
