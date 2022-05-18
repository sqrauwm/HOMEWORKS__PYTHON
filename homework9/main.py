import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Zadanie 1

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# grupa = df.groupby('Rok').agg({'Liczba':['sum']})
# grupa.plot(kind='line', xlabel='Rok', ylabel='Ilosc imion',
#             rot=0, title='Ilosc imion w danym roku')
# plt.show()

# Zadanie 2

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# grupa = df.groupby('Plec').agg({'Liczba':['sum']})
# grupa.plot(kind='bar', xlabel='Płeć', ylabel='Ilośc imion w mln',
#             rot=0, title='Ilość imion w zależności od płci')
# plt.show()

# Zadanie 3

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
grupa = df[df['Rok']>2011].groupby('Plec').agg({'Liczba':['sum']})
grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20)
plt.show()

# Zadanie 4 ??
