import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
# wykres liniowy, liczba urodzonych dzieci dla każdego roku
# roczniki = df['Rok'].unique()
# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
# wykres = grupa.plot()
# wykres.set_ylabel('Liczba urodzonych dzieci')
# wykres.set_xticks(roczniki)
# wykres.tick_params(axis='x', labelrotation=40)
# wykres.legend()
# plt.subplots_adjust(left=0.15, right=0.9, bottom=0.15, top=0.9)
# plt.title("Liczba urodzonych dzieci dla każdego roku")
# plt.show()

# wykres słupkowy, liczba M i K z całego zbioru
# grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
# wykres = grupa.plot.bar(ylabel='Liczba urodzeń')
# wykres.legend()
# plt.xticks(rotation=0)
# plt.title("Liczba urodzonych chłopców i dziewczynek")
# plt.show()

# wykres kołowy z % udziałem urodzeń K i M z ostatnich 5 lat datasetu
# grupa = df[df['Rok'] > 2012].groupby(['Plec']).agg({'Liczba':['sum']})
# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20)
# plt.legend()
# plt.show()

# wykres słupkowy z ilościami zamówień dla poszczególnych sprzedawców
df = pd.read_csv('zamowienia.csv', delimiter=';')
policzone = df.groupby('Sprzedawca').size()
policzone.plot.bar()
plt.ylabel("liczba zamówień")
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.9)
plt.title('Ilość zamówień sprzedawców')
plt.show()