import pandas
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from PIL import Image

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


plt.savefig("wykres2.png")
im = Image.open("wykres2.png")
im = im.convert("RGB")
im.save("wykres2.jpg")
plt.show()
