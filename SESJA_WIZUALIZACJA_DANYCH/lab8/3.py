import pandas as pd

df = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal='.')

# ---------------------------

# names = []
#
# for x in df['Sprzedawca']:
#     if not names.__contains__(x):
#         names.append(x)
#
# print("Ilosc unikatowych sprzedawcow: {}".format(len(names)))


# ---------------------------


# new_df = df.sort_values(by='Utarg')
# print(new_df.tail(5))


# ---------------------------


# dic = {}
#
# for x in df['Sprzedawca']:
#     if not dic.__contains__(x):
#         dic[x] = 1
#     else:
#         dic[x] += 1
#
# for x in dic:
#     print("{}, ilosc zamowien: {}".format(x, dic[x]))


# ---------------------------


# gr = df.groupby(['Kraj'])
#
# cashFlow = gr.agg({'Utarg': 'sum'})
#
# print(cashFlow)


# ---------------------------


# cashFlow = df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] > '2005') & (df['Data zamowienia'] < '2006')].agg({'Utarg': 'sum'})
#
# print(cashFlow)


# ---------------------------


# cashFlow = df[(df['Data zamowienia'] > '2004') & (df['Data zamowienia'] < '2005')].agg({'Utarg': 'sum'})
# cashFlow2 = df[(df['Data zamowienia'] > '2004') & (df['Data zamowienia'] < '2005')]
#
# num = 0
# for x in cashFlow2:
#     num += 1
#
#
# print("Srednia z 2014: {}".format(cashFlow[0] / num))


# ---------------------------


gr2004 = df[(df['Data zamowienia'] > '2004') & (df['Data zamowienia'] < '2005')]
gr2005 = df[(df['Data zamowienia'] > '2005') & (df['Data zamowienia'] < '2006')]

gr2004.to_csv('zamowienia_2004', index=False)
gr2005.to_csv('zamowienia_2005', index=False)