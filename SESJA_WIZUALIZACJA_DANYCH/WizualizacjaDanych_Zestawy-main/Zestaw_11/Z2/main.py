import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

xlsx = pd.ExcelFile("mieszkania11.xlsx")
data = pd.read_excel(xlsx, header=0)

indywidualne = data[data["Formy budownictwa"] == "indywidualne"]
spoldzielcze = data[data["Formy budownictwa"] == "spółdzielcze"]
komunalne = data[data["Formy budownictwa"] == "komunalne"]

plt.figure(figsize=(6, 5))
plt.figtext(0.02, 0.95, '166309', size=12, color='k')
plt.grid(zorder=0)
plt.bar(data["Rok"].unique()-0.3, komunalne["Wartość"].values, 0.3, label="komunalne", zorder=3)
plt.bar(data["Rok"].unique(), spoldzielcze["Wartość"].values, 0.3, label="spoldzielcze", zorder=3)
plt.bar(data["Rok"].unique()+0.3, indywidualne["Wartość"].values, 0.3, label="indywidualne", zorder=3)
plt.xlabel("Rok")
plt.ylabel("Wartość")
plt.yticks(np.arange(0, 70000, 5000))
plt.xticks(data["Rok"].unique())
plt.title("Wartość mieszkań 2015-2018")
plt.legend(loc=7)
plt.savefig("wykres2.pdf", format='pdf')
plt.show()

print(data)