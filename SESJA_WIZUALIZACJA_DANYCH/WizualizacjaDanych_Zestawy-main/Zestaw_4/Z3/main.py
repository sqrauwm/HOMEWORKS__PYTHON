import pandas as pd
from matplotlib import pyplot as plt
from PIL import Image

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
plt.savefig("wykres3.png")
im = Image.open("wykres3.png")
im = im.convert('RGB')
im.save("wykres3.jpg")
plt.show()