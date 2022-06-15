import pandas
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from PIL import Image
import numpy as np

#Zadania 3
pd.options.mode.chained_assignment = None
data = pd.read_csv("nieruchomosci2.csv", sep=';', decimal=',', header=None)
data = data.transpose()
rp = data[data[0] == "rynek pierwotny"]

rw = data[data[0] == "rynek wtórny"]
rp.loc[:, 3] = rp[3].str.replace(" ", "")
print(rp)

#Zestaw 11 Procentowo hotele ilość gwiazdek zapis do jpg
xlsx = pd.ExcelFile("turystyka11.xlsx")
data = pd.read_excel(xlsx, header=None)

data = data.transpose()

r2014 = data[data[1] == '2014']
r2019 = data[data[1] == '2019']
print(r2014)
fig, axs = plt.subplots(1, 2, )
axs[0].pie(r2014[2].values, labels=['5*', '4*', '3*', '2*', '1*'], autopct='(%.f %%)', pctdistance=1.55)
axs[0].set_title("Rok 2014")
axs[1].pie(r2019[2].values, labels=['5*', '4*', '3*', '2*', '1*'], autopct='(%.f %%)', pctdistance=1.55)
axs[1].set_title("Rok 2019")
plt.tight_layout()
plt.savefig("Z3Z11.png")
im = Image.open("Z3Z11.png")
im = im.convert("RGB")
im.save("Z3Z11.jpg")
plt.show()

#zestaw4 Liczba sprzedanych owoców w poszczególnych latach zapis jpg
data = pd.read_csv("sprzedaz4.csv", sep='@', header=None)
data = data.transpose()
print(data)
jablka = data[data[0] == "Jabłka"]
gruszki = data[data[0] == "Gruszki"]
sliwki = data[data[0] == "Śliwki"]

plt.plot(data[1].unique(), jablka[2], label="Jabłka",marker='.')
plt.plot(data[1].unique(), gruszki[2], label="Gruszki",marker='.')
plt.plot(data[1].unique(), sliwki[2],  label="Śliwki",marker='.')
plt.legend()
plt.grid()
plt.xlabel("Rok")
plt.ylabel("Liczba sprzedanych sztuk")
plt.title("Liczba wybranych sprzedanych owoców (2011-2014)")
plt.savefig("Z3Z4.png")
im = Image.open("Z3Z4.png")
im = im.convert('RGB')
im.save("Z3Z4.jpg")
plt.show()

#Zestaw 44 wykres horyzontalny dużo wartości zapis do png
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
plt.savefig("Z3Z44.png")
plt.show()

#Zestaw21 - ZERÓWKA Wykres kołoowy udział jednostek żywieniowych procentowo w poszczególnych latach
data = pd.read_csv('gastro21.csv', sep=',', header=None).transpose()

data = data[(data[1] == '2016') | (data[1] == '2017')]

restauracje = data[data[0] == 'restauracje']
bary = data[data[0] == 'bary']
stolowki = data[data[0] == 'stołówki']
gastro = data[data[0] == 'punkty gastronomiczne']


x = ['Restauracje', 'Bary', 'Stołówki', 'Pkt. Gastronomiczne']
y1 = [restauracje.iloc[0, 2], bary.iloc[0, 2], stolowki.iloc[0, 2], gastro.iloc[0, 2]]
y2 = [restauracje.iloc[1, 2], bary.iloc[1, 2], stolowki.iloc[1, 2], gastro.iloc[1, 2]]

fig, axs = plt.subplots(1, 2)

axs[0].pie(y1, autopct='%.1f %%')
axs[0].set_title('Rok 2016')

axs[1].pie(y2, autopct='%.1f %%')
axs[1].set_title('Rok 2017')

plt.legend(x, bbox_to_anchor=(0.45, -0.1))

plt.savefig('Z3Z21-0.png')
im = Image.open('Z3Z21-0.png')
im = im.convert('RGB')
im.save('Z3Z21-0.jpg')

plt.show()