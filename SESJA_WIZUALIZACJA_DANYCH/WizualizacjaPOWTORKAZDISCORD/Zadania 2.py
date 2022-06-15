import pandas
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from PIL import Image
import numpy as np

#Zadania 2
#Zestaw 1 Wykres ceny i mąki w poszczególnych latach zapis w jpg
xlsx = pandas.ExcelFile("ceny2.xlsx")
data = pandas.read_excel(xlsx, header=0)
ryz = data[data["Rodzaje towarów"] == "ryż - za 1kg"]
maka = data[data["Rodzaje towarów"] == "mąka pszenna - za 1kg"]

plt.plot(ryz["Rok"], ryz["Wartość"], label="Ryż", marker='o')
plt.plot(maka["Rok"], maka["Wartość"], label="Mąka pszenna",marker='o')
plt.title("Ceny ryżu i mąki pszennej w latach 2010-2019")
plt.xlabel("Rok")
plt.ylabel("Cena za 1kg")
plt.grid()
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f zł'))
plt.legend(loc=4)


plt.savefig("Z2Z1.png")
im = Image.open("Z2Z1.png")
im = im.convert("RGB")
im.save("Z2Z1.jpg")
plt.show()

#Zestaw 11 Wykres mieszkań na przestrzeni lat zapis do pdf

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
plt.savefig("Z2Z11.pdf", format='pdf')
plt.show()

print(data)

#Zestaw 4 Dwa wykresy na jednym sale kinowe i miejsca w nich zapis do png
xlsx = pd.ExcelFile("kina4.xlsx")
data = pd.read_excel(xlsx, header=0)

miejskie = data[data["Gestor"] == "miejskie"]
powiatowe = data[data["Gestor"] == "powiatowe"]
wojewodzkie = data[data["Gestor"] == "wojewódzkie"]

miejskie_sale = miejskie[miejskie["Wykaz"] == "sale"]
powiatowe_sale = powiatowe[powiatowe["Wykaz"] == "sale"]
wojewodzkie_sale = wojewodzkie[wojewodzkie["Wykaz"] == "sale"]

miejskie_miejsca = miejskie[miejskie["Wykaz"] == "miejsca na widowni"]
powiatowe_miejsca = powiatowe[powiatowe["Wykaz"] == "miejsca na widowni"]
wojewodzkie_miejsca = wojewodzkie[wojewodzkie["Wykaz"] == "miejsca na widowni"]

fig, axs = plt.subplots(1, 2, )
print(miejskie_sale)
axs[0].grid(zorder=0)
axs[0].bar(data["Rok"].unique()-0.3, miejskie_sale["Wartosc"].values,width=0.3, color="tab:green", label="miejskie", zorder=3)
axs[0].bar(data["Rok"].unique(), powiatowe_sale["Wartosc"].values,width=0.3, color="tab:blue", label="powiatowe", zorder=3)
axs[0].bar(data["Rok"].unique()+0.3, wojewodzkie_sale["Wartosc"].values,width=0.3, color="tab:orange", label="wojewódzkie", zorder=3)
axs[0].set_xticks([2015, 2016, 2017])
axs[0].set_yticks(np.arange(0,700,50))
axs[0].set_title("Liczba sal kinowych")
axs[1].grid()
axs[1].bar(data["Rok"].unique()-0.3, miejskie_miejsca["Wartosc"].values,width=0.3, color="tab:green", label="miejskie", zorder=3)
axs[1].bar(data["Rok"].unique(), powiatowe_miejsca["Wartosc"].values,width=0.3, color="tab:blue", label="powiatowe", zorder=3)
axs[1].bar(data["Rok"].unique()+0.30, wojewodzkie_miejsca["Wartosc"].values,width=0.3, color="tab:orange", label="wojewódzkie", zorder=3)
axs[1].set_xticks([2015, 2016, 2017])
axs[1].set_yticks(np.arange(0,150000,10000))
axs[1].set_title("Liczba miejsc w salach kinowych")
axs[0].legend(loc=5)
axs[1].legend(loc=5)
axs[0].set_xlabel("Rok")
axs[1].set_xlabel("Rok")
plt.tight_layout()
plt.savefig("Z2Z4.png")
plt.show()

#Zestaw 44 Wykres cen narchwi cebuli i ziemniaków w poszczególnych latach zapis w jpg

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
plt.savefig("Z2Z44.png")
im = Image.open("Z2Z44.png")
im = im.convert("RGB")
im.save("Z2Z44.jpg")
plt.show()

#Zestaw21 - Zerówka Sprzedaż produktów w poszczególnych latach wykres słupkowy
xlsl = pd.ExcelFile('sprzedaz21.xlsx')
data = pd.read_excel(xlsl, header=0)

marchew = data[data['Produkt'] == 'Marchew']
pomidor = data[data['Produkt'] == 'Pomidor']
ogorek = data[data['Produkt'] == 'Ogórek']

plt.figtext(0.82, 0.02, '2020-06-12', size=12, color='k')
plt.grid(zorder=0)
plt.bar(data['Rok'].unique() - 0.3, marchew['Sprzedaż'], 0.3, label='Marchew', zorder=3)
plt.bar(data['Rok'].unique(), pomidor['Sprzedaż'], 0.3, label='Pomidor', zorder=3)
plt.bar(data['Rok'].unique() + 0.3, ogorek['Sprzedaż'], 0.3, label='Ogórek', zorder=3)
plt.xlabel('Rok')
plt.ylabel('Sprzedaż')
plt.xticks(data['Rok'].unique())
plt.title('Sprzedaż warzyw w latach 2015-2018')
plt.legend(loc='upper right')
plt.show()
