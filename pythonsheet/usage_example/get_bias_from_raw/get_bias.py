import pythonsheet.pythonsheet.utility as utility
import pythonsheet.pythonsheet.major as pm
import pythonsheet.pythonsheet.file as pfile
import pythonsheet.pythonsheet.csv_ as csv


files_in = ["./pythonsheet/usage_example/get_bias_from_raw/raw.csv"]
files_out = ["./pythonsheet/usage_example/get_bias_from_raw/bias.csv"]
ground_truth = 75

for i in range(len(files_in)):
    series = csv.get_series(files_in[i], "measurement")

    measurement_bias = pm.add(series, -1 * ground_truth)

    measurement_bias.name = "measurement_bias"
    csv.write_series_to_csv(files_out[i], measurement_bias)
