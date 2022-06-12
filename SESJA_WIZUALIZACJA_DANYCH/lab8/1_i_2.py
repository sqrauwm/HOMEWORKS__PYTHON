import pandas as pd

# zad 1 i 2

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

# -------------------------------

# new_df = df[df['Liczba'] > 1000]
# print(new_df)

# -------------------------------

# new_df = df[df['Imie'] == 'ANDRZEJ']
# print(new_df)

# -------------------------------

# suma = df.agg({'Liczba' : 'sum'})
# print(suma)

# -------------------------------

# suma = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)].agg({'Liczba' : 'sum'})
# print(suma)

# -------------------------------

# sumaM = df[df['Plec'] == 'M'].agg({"Liczba" : 'sum'})
# sumaK = df[df['Plec'] == 'K'].agg({"Liczba" : 'sum'})
# print(sumaM)
# print(sumaK)

# -------------------------------

# new_df = df.sort_values(by='Rok')
# firstYear = new_df.at[0, "Rok"]
# lastYear = new_df.at[16416, "Rok"]
#
# for year in range(firstYear, lastYear + 1):
#     gr = df.groupby(['Rok']).get_group(year)
#
#     maxM = gr[gr['Plec'] == 'M'].agg({"Liczba": 'max'})
#     maxK = gr[gr['Plec'] == 'K'].agg({"Liczba": 'max'})
#
#     print(df[(df['Plec'] == 'M') & (df['Liczba'] == maxM[0])])
#     print(df[(df['Plec'] == 'K') & (df['Liczba'] == maxK[0])])
#     print("------------------------")

# -------------------------------

# maxM = df[df['Plec'] == 'M'].agg({"Liczba": 'max'})
# maxK = df[df['Plec'] == 'K'].agg({"Liczba": 'max'})
#
# print(df[(df['Plec'] == 'M') & (df['Liczba'] == maxM[0])])
# print(df[(df['Plec'] == 'K') & (df['Liczba'] == maxK[0])])