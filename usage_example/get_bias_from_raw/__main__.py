from pythonsheet import major as pm
from pythonsheet import csv_ as csv


files_in = ["./usage_example/get_bias_from_raw/raw.csv"]
files_out = ["./usage_example/get_bias_from_raw/bias.csv"]
ground_truth = 75

for i in range(len(files_in)):
    series = csv.get_series(files_in[i], "measurement")

    measurement_bias = pm.add(series, -1 * ground_truth)

    measurement_bias.name = "measurement_bias"
    csv.write_series_to_csv(files_out[i], measurement_bias)
