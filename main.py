import pandas as pd

# zad 1
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)

# zad 2

# a)
# print(df[df['Liczba'] > 1000])


# b)
# print(df[df['Imie'] == '...'])

# c)
# print(df.agg({'Liczba': ['sum']}))

# d)
# print(df[df['Rok'] <= 2005].groupby(['Rok']).agg({'Liczba': ['sum']}))

# e)
# print(df.groupby(['Plec']).agg({'Liczba': ['sum']}))

# f)
# print(df.groupby(['Rok', 'Plec'])['Liczba'].max()) popraw

# g)
# print(df.groupby(['Plec'])['Liczba'].max()) popraw

# zad 3
df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
print(df)

# a)
# print(df['Sprzedawca'].unique())

# b)
# print(df.nlargest(5, 'Utarg'))

# c)
# print(df.groupby(['Sprzedawca'])['idZamowienia'].count().reset_index(name='ilosc zamowien'))

# d)
# print(df.groupby(['Kraj']).agg({'Utarg': ['sum']}))

# e)
# print(df[((df['Kraj'] == 'Polska') & ((df['Data zamowienia'] >= '2005-01-01') &
#           (df['Data zamowienia'] <= '2005-12-31')))].groupby(['Sprzedawca']).agg({'Utarg': ['sum']}))

# f)
# print(df[((df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]
#       ['Utarg'].mean().round(2))

# g)
df[((df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]\
    .to_csv('zamowienia_2004.csv', index=False)

df[((df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31'))]\
    .to_csv('zamowienia_2005.csv', index=False)
