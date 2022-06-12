import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("cechy41.csv", sep=';', decimal=',', header=0)

data = data.fillna(0)
cecha1 = data["Cecha1"].values
cecha2 = data["Cecha2"].values
bins = [0, 50, 100, 150, 200]

catC1 = pd.cut(cecha1, bins)
catC2 = pd.cut(cecha2, bins)
fig, axs = plt.subplots(1, 2)
axs[0].barh(np.arange(1, 545, 1), cecha1)
axs[0].set_title("Cecha 1")
axs[0].set_ylabel("Indeks cechy")
axs[0].set_xlabel("Wartość cechy")
axs[1].barh(np.arange(1, 545, 1), cecha2)
axs[1].set_title("Cecha 2")
axs[1].set_ylabel("Indeks cechy")
axs[1].set_xlabel("Wartość cechy")
plt.tight_layout()
plt.savefig("wykres3.png")
plt.show()


