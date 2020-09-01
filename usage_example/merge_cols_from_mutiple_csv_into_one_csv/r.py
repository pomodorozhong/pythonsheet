from random import random
import numpy as np
import pandas as pd
from pythonsheet.pythonsheet import csv_ as csv


array = []
for i in range(20):
    r = 2.9 + random() * 0.33
    array.append(r)

data = np.array(array)

ser = pd.Series(data)
ser.name = 'torsion'

csv.write_series_to_csv("./waat.csv", ser)
