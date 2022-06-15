import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

#Zestaw2, zadanie1, wykres

# x = ["A", "B", "C", "D", "E"]
# y1 = [35, 44, 14, 42, 41]
# y2 = [-30, -32, -36, -33, -31]
#
# fig, axs = plt.subplots(1, 2, )
# axs[0].barh(x, y1, color=["lightblue","pink","tab:orange","tab:gray","tab:purple"])
# axs[0].set_title("Wykres lewy")
# axs[1].barh(x, y2, color=["tab:pink","tab:cyan","tab:cyan","tab:brown","tab:olive"])
# axs[1].set_title("Wykres prawy")
# plt.savefig("wykres1.png")
# plt.show()

#Zestaw2, zadanie2, chuj

# xlsx = pd.ExcelFile("ceny2.xlsx")
# df = pd.read_excel(xlsx, header=0)
# ryz = df[df["Rodzaje towarów"] == "ryż - za 1kg"]
# maka= df[df["Rodzaje towarów"] == "mąka pszenna - za 1kg"]
#
# sredniaryz = ryz['Wartość'].mean()
# print(sredniaryz)
# sredniamaka = maka['Wartość'].mean()
# print(sredniamaka)
#
# plt.plot(ryz["Rok"], ryz["Wartość"], label="ryż")
# plt.plot(maka["Rok"], maka["Wartość"], label="mąka")
# # plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])
# plt.xlim([2010,2019])
# plt.xlabel("Rok")
# plt.ylabel("Wartość")
# plt.legend(loc=7)
# plt.grid(color='m')
# plt.figtext(0.02, 0.02, "Nr indeksu 166320", size=12, color="tab:brown", rotation=0)
# plt.savefig("wykres2.png")
# im = Image.open("wykres2.png")
# im = im.convert("RGB")
# im.save("wykres2.jpg")
# plt.show()

# Zestaw2 zadanie3, niedokonczone

# data = pd.read_csv("nieruchomosci2.csv", sep=';', decimal=',', header=None).transpose()
# pierwotny = data[data[0]=="rynek pierwotny"]
# wtorny = data[data[0]=="rynek wtórny"]
#
# fig, axs = plt.subplots(1,2)
# axs[0].pie(pierwotny[3].astype(float), labels=pierwotny[1])
# axs[0].title("Rynek pierwotny")
# axs[1].pie(wtorny[3].astype(float), labels=wtorny[1])
# axs[1].title("Rynek wtórny")
# plt.show()

# Zestaw 41, zadanie1

x = np.arange(0.5, 10+0.5, 0.5)
y1 = (np.log(2*x))
y2 = (-4*x) + 2
y3 = 2* np.cos(x)

plt.plot(x, y1, 'b:', label="y = log(2x)")
plt.plot(x, y2, 'g--' , label="y = -4x + 2")
plt.plot(x, y3, 'm^' ,label='2cos(x)')
plt.legend()
plt.xlabel("x", color='r')
plt.ylabel("f (x)", color='r')
plt.title("Wykresy funkcji: y = log(2x), y = −4x + 2, y = 2 cos(x)", color='r')
plt.grid(color='tab:cyan')
plt.xlim(0.5, 10)
plt.figtext(0.02, 0.02, "Nr indeksu", size=12, color="tab:brown", rotation=0)
plt.show()
