import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np
import math
import seaborn as sns


df=pd.read_csv('nieruchomosci2.csv',header=0,sep=';',decimal='.')
print(df)
dane={'rodzaj rynku':[],'metraz':[],'ilosc sztuk':[]}
df=pd.DataFrame(dane)
df.loc[0]=['rynek pierwotny','do 40m2',16266]
df.loc[1]=['rynek pierwotny','od 40m2 do 60',37236]
df.loc[2]=['rynek pierwotny','od 60 do 80',2050]
df.loc[3]=['rynek pierwotny','od 80',769]
df.loc[4]=['rynek wtorny','do 40m2',3314]
df.loc[5]=['rynek wtorny','od 40m2 do 60',5413]
df.loc[6]=['rynek wtorny','od 60 do 80',2421]
df.loc[7]=['rynek wtorny','od 80',10234]
print(df)

grupa=df.where(df['rodzaj rynku']=='rynek pierwotny')
grupa=grupa.groupby('metraz').agg({'ilosc sztuk':'sum'})
grupa.plot(kind='pie',subplots=True,autopct='%.2f %%',fontsize=10,figsize=(8,8),colors=['red','green','violet','yellow'])
plt.legend(title='metraż')
plt.title('wykres przedstawiający stosunek ilości mieszkań poszczególnych metraży sprzedanych w 2018 roku')

grupa2=df.where(df['rodzaj rynku']=='rynek wtorny')
grupa2=grupa2.groupby('metraz').agg({'ilosc sztuk':'sum'})
grupa2.plot(kind='pie',subplots=True,autopct="%.2f %%",fontsize=10,figsize=(8,8),colors=['red','green','violet','yellow'])
plt.legend(title='metraż')
plt.title('wykres przedstawiający stosunek ilości mieszkań poszczególnych metraży sprzedanych w 2018 roku')
plt.ylabel('wykres kołowy')

plt.show()