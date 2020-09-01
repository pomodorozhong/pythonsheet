from pythonsheet import utility as pu
from pythonsheet import fitting
from pythonsheet import csv_ as csv

root_path = "./usage_example/fitting_a_curve/"
coeff_file = root_path + "coefficients.txt"
data_files = [
    root_path + "data.csv",
]

xs = [
    "time(s)",
]
ys = [
    "length",
]

coefficients = []
for file_index in range(len(data_files)):
    for x in xs:
        for y in ys:
            x_series = csv.get_series(data_files[file_index], x)
            y_series = csv.get_series(data_files[file_index], y)
            deg = 2
            fitting_plot = f"{root_path}plot_{x}_{y}"

            out = fitting.fit(x_series, y_series, deg, fitting_plot)

            coefficient = f"{out}: {x}_{y}"
            coefficients.append(coefficient)
        coefficients.append("")
    coefficients.append("")

csv.write_1d_array_to_csv(coeff_file, coefficients)
