import numpy as np
import pandas as pd

#Series - jednowymiarowe -------------------------------------------

# s = pd.Series([1, 3, 5, np.nan, 9, 11])
# print(s)
# s = pd.Series([1, 2, 3], index=['lol', 'ok', 'nwm'])
# print(s)

#DataFrame - dwuwymiarowe -------------------------------------------

# data = {'Kraj': ['Belgia', 'Holandia', 'Polska'],
#         'Stolica': ['Bruksela', 'Amsterdam', 'Warszawa'],
#         'Populacja': [10, 20, 30]}
#
# df = pd.DataFrame(data)
# print(df)
# print(df.dtypes)
#
# daty = pd.date_range('20210303', periods=5, freq='Y')
# print(daty)
# df = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))
# print(df)

# openpyxl -------------------------------------------

# xlsx = pd.ExcelFile('imiona.xlsx')
#
# header - ktory wiersz to nazwy kolumn
# df = pd.read_excel(xlsx, header=0)
# print(df)
# df.to_excel('wyniki.xlsx', sheet_name='arkusz costam') # zapis do pliku

# pobieranie danych -------------------------------------------

# s = pd.Series([1, 2, 3], index=['lol', 'ok', 'nwm'])
# print(s['lol'])
# print(s.lol)

# data = {'Kraj': ['Belgia', 'Holandia', 'Polska'],
#         'Stolica': ['Bruksela', 'Amsterdam', 'Warszawa'],
#         'Populacja': [10, 20, 30]}

# df = pd.DataFrame(data)
# od zerowego do drugiego wiersza (wyłącznie)
# print(df[0:2])

# cała kolumna po etykiecie
# print(df['Kraj'])

# pojedynczy element po indeksie wiersza i kolumny
# print(df.iloc[[0], [1]])

# pojedynczy element po indeksie wiersza i nazwie kolumny
# print(df.loc[[0], ['Populacja']])

# to samo co wyzej, ale pozwala wyłuskać typ pierwotny np. int
# a = df.at[0, 'Populacja']
# print(type(a))

# df.sample() # jeden losowy element
# df.sample(n=2) # n losowych elementów
# df.sample(frac=0.5) # 50% losowych elementów
# df.sample(n=10, replace=True) # n losowych elementów z powtórzeniami

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df.head(1)) # n elementów z początku
# print(df.tail(1)) # n elementów od końca

# df.describe() # statystyka jakas nwm ocb
# print(df.T) # transpozycja

# filtrowanie serii --------------------------------------------------

# s = pd.Series([11, 21, 31, 41, 51, 61, 72, 82, 91])
# wyświetla te wiersze gdzie warunek
# print(s[(s > 60) & (s % 2 == 0)])
# to samo co wyżej, ale wiersze nie spełniające warunku mają wartość NaN
# print(s.where((s > 60) & (s % 2 == 0)))
# print(s.where((s > 60) & (s % 2 == 0), 'chwdp'))

# to samo co wyżej, ale zmienia zawartość oryginału zamiast zwracania kopii
# seria = s.copy()
# seria.where((s > 60) & (s % 2 == 0), 'chwdp', inplace=True)

# filtrowanie dataFrame ----------------------------------

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)

# print(df[df['Rok'] > 2015])
# print(df[(df['Rok'] > 2012) & (df['Rok'] <= 2015)])
# print(df[df.index.isin([0, 2])]) # isin zwraca True jeśli index należy do [0,2]
# szukaj = ['JAKUB', 'KACPER']
# print(df.isin(szukaj)) # zwraca DataFrame z wartościami True/False w zależności od szukaj

# dodawanie danych -------------------------
# s = pd.Series([1, 2, 3], index=['lol', 'ok', 'nwm'])
# print(s)
# s['lol'] = 3 # zmiana
# s['halko'] = 5 # dodanie
# print(s)

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

# df.loc[3] = 'dodane' # cały wiersz
# print(df)
# df.loc[[3], ['Imie']] = 'dodane' # jeden element
# print(df)
# df.loc[3] = [2000, 'BRAJAN', 666, 'NaN'] # cały wiersz jako lista(?)
# print(df)

# df.drop([3], inplace=True) # usuwa n-ty wiersz
# print(df)
# df.drop('Imie', axis=1, inplace=True) # usuwa kolumne po nazwie
# print(df)

# agregacja DataFrame --------------------------

# df.sort_values(by='Rok', ascending=False, inplace=True)
# print(df)

group = df.groupby(['Rok'])
print(group.get_group(2013))

print(group.agg({'Liczba': ['sum']}))