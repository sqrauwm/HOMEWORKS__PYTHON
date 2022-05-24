import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# wykres liniowy na podstawie Series
# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# ts.plot()
# plt.show()

# wykres kolumnowy z DataFrame'ów
data = {'Kraj': ['Polska', 'Francja', 'Niemcy'],
        'Stolica': ['Warsz', 'Paris', 'Berlino'],
        'Kontynent': ['Ojro', 'Ojro', 'CosInnego'],
        'Populacja': [40, 60, 80]}

df = pd.DataFrame(data)

group = df.groupby(['Kontynent']).agg({'Populacja': ['sum']})

# group.plot(kind='bar', xlabel='Kontynent', ylabel='Mln', rot=0, legend=True, title='Populacja kontynentów')
wykres = group.plot.bar()
wykres.set_ylabel('Mln')
wykres.set_xlabel('Kontynent')
wykres.tick_params(axis='x', labelrotation=0)
wykres.legend()
wykres.set_title('Populacja kontynentów')
# plt.xticks(rotation=0) #zmiana kierunku tekstu etykiet słupków
plt.savefig('wykres.png') #zapis do pliku?
plt.show()

# wykres kołowy
df = pd.read_csv('dane.csv', header=0, sep=";", decimal=".")
group = df.groupby(['Imie i nazwisko']).agg({'Wartość zamówienia': ['sum']})
# autopct - dokładnośc liczb bo przecinku
# figsize - wielkosc wykresu w calach
group.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=20, figsize=(6, 6), legend=(0, 0), colors=['red', 'green'])
# wykres = group.plot.pie(subplots=True, autopct='%.2f%%', fontsize=20, figsize=(6, 6), legend=(0, 0))
# plt.legend(loc='lower right)
plt.title('Suma zamówienia dla sprzedawcy')
plt.show()

# zmodyfikowana wersja pierwszego wykresu, ze średnią kroczącą
ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()
df = pd.DataFrame(ts, columns=['wartości'])
df['Średnia krocząca'] = df.rolling(window=50).mean()
df.plot()
plt.legend()
plt.show()