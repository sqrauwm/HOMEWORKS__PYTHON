import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# wykres liniowy funkcji 1/x --------------------------------------------
# x = np.arange(1, 21, 1)
# plt.plot(x, 1/x, label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([0, 20, 0, 1])
# plt.legend()
# plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
# plt.show()

# to co wyzej ale inny wygląd --------------------------------------------
# x = np.arange(1, 21, 1)
# plt.plot(x, 1/x, 'g>:', label='f(x) = 1/x' )
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([0, 20, 0, 1])
# plt.legend()
# plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
# plt.show()

# sin(x) i cos(x) na jednym wykresie --------------------------------------------
# x = np.arange(0, 30, .1)
# plt.plot(x, np.sin(x), 'b', label='sin(x)')
# plt.plot(x, np.cos(x), 'r', label='cos(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x) cos(x)')
# plt.legend(loc='upper right')
# plt.title('Wykres sin(x), cos(x)')
# plt.show()

# wykres punktowy z iris.data, wektor x == 'sepal length', wektor y == 'sepal width', losowe kolorki --------------------------------------------
# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
# print(df)
# # przygotowanie wektora kolorów
# colors = np.random.randint(0, 50, len(df.index))
# # przygotowanie wektora z rozmiarami 'kropek'
# scale = np.abs(df['sepal length'] - df['sepal width'])
#
#
# plt.scatter(df['sepal length'], df['sepal width'], c=colors, s=scale)
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.show()

# 3 wykresy na jednym płótnie (jeden wiersz, 3 kolumny) --------------------------------------------
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)

# # wykres słupkowy, ilosc narodzonych K i M w całym okresie
# plt.subplot(1, 3, 1)
# grouped = df.groupby('Plec')
# etykiety = list(grouped.groups.keys())
# wartosci = list(grouped.agg('Liczba').sum())
# plt.bar(x=etykiety, height=wartosci, color=['green', 'red'])
# plt.xlabel('Płeć')
# plt.ylabel('Liczba narodzonych dzieci')

# # wykres liniowy-podwójny, ilość narodzin dla K i M dla każdego roku
# plt.subplot(1, 3, 2)
# x = df['Rok'].unique()
# kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
# mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
# plt.plot(x, kobiety, label="Kobiety")
# plt.plot(x, mezczyzni, label="Mężczyźni")
# plt.xlabel('Rok')
# #

# # wykres słupkowy, suma urodzonych dzieci w każdnym roku
# plt.subplot(1, 3, 3)
# x = df['Rok'].unique()
# y = df.groupby('Rok').agg('Liczba').sum()
# plt.bar(x, y)
# plt.xlabel('Rok')
# # wyświetlamy cały wykres
# plt.subplots_adjust(wspace=0.85)
# plt.show()


# wykres kołowy zamówień dla każdego sprzedawcy
df = pd.read_csv('zamowienia.csv', sep=';')
policzone = df.groupby('Sprzedawca')['Utarg'].sum()
print(policzone)
# explode to wysunięcie kawałka wykresu kołowego
explode = [0.0 for n in range(len(policzone.index))]
# określamy które kawałki i o ile wysunąć, tu losujemy jeden
explode[np.random.randint(0, len(policzone.index))] = 0.2
wedges, texts, autotext = plt.pie(x=policzone, labels=policzone.index,
                                  autopct=lambda pct: "{:.2f}%".format(pct), textprops=dict(color='black'), explode=explode, shadow=True)
plt.title("Procentowy udział kwot zamówień sprzedawców")
plt.show()