import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from PIL import Image

xlsx = pd.ExcelFile("ceny41.xlsx")
data = pd.read_excel(xlsx, header=0)

# print(data)


produkt_grupa_srednia = data.groupby("Rodzaje towarów i usług").agg({"Wartosc" : ["mean"]})
print(produkt_grupa_srednia)

marchew = data[data["Rodzaje towarów i usług"] == "marchew - za 1 kg"]
cebula = data[data["Rodzaje towarów i usług"] == "cebula - za 1 kg"]
ziemniaki = data[data["Rodzaje towarów i usług"] == "ziemniaki - za 1 kg"]
# x = data["Miesiące"].unique()
x = ['STY', 'LUT', 'MAR', 'KWI', 'MAJ', 'CZE', 'LIP', 'SIE', 'WRZ', 'PAŹ', 'LIS', 'GRU']
plt.plot(x, marchew["Wartosc"], label="marchew", marker='.')
plt.plot(x, cebula["Wartosc"], label="cebula", marker='.')
plt.plot(x, ziemniaki["Wartosc"], label="ziemniaki", marker='.')
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f zł'))
plt.grid()
plt.ylabel("Cena 1 kg w danym miesiącu")
plt.xticks(rotation=30)
plt.legend()
plt.figtext(0.01, 0.02, '166309', size=10, color='k') # text
#plt.tight_layout()
plt.title("Ceny cebuli, marchwi i ziemniaków w 2017 r.")
plt.savefig("wykres2.png")
im = Image.open("wykres2.png")
im = im.convert("RGB")
im.save("wykres2.jpg")
plt.show()
