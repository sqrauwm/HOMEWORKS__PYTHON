import pandas as pd
from matplotlib import pyplot as plt
pd.options.mode.chained_assignment = None
data = pd.read_csv("nieruchomosci2.csv", sep=';', decimal=',', header=None)
data = data.transpose()
rp = data[data[0] == "rynek pierwotny"]

rw = data[data[0] == "rynek wtórny"]
rp.loc[:, 3] = rp[3].str.replace(" ", "")
print(rp)
