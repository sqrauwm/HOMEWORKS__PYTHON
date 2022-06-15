import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
# x = np.arange(0.5,10+0.1,0.1)
# y1 = np.log10(2*x)
# y2 = -4*x+2
# y3 = 2 * np.cos(x)
# plt.plot(x,y1,'b:',label='log(2x)')
# plt.plot(x,y2,label='-4x+2',marker='x')
# plt.plot(x,y3,'m--',label='2cos(x)')
# plt.xlabel('x',size=20,color='r')
# plt.grid(color='m')
# plt.ylabel('f(x)',size=20)
# plt.legend()
# plt.savefig('chuj.png')
# chuj=Image.open('chuj.png')
# chuj=chuj.convert('RGB')
# chuj.save('matusiak to.jpg')
# plt.show()
# xlsx = pd.ExcelFile('ceny41.xlsx')
# df = pd.read_excel(xlsx,header=0)
# mrch = df[df['Rodzaje towarów i usług']=='marchew - za 1 kg']
# cbl = df[df['Rodzaje towarów i usług']=='cebula - za 1 kg']
# zmn = df[df['Rodzaje towarów i usług']=='ziemniaki - za 1 kg']
# sm=mrch['Wartosc'].mean()
# sc=cbl['Wartosc'].mean()
# sz=zmn['Wartosc'].mean()
# # print(sm)
# # print(sc)
# # print(sz)
# # print(df)
# x=df['Miesiące'].unique()
# plt.plot(x,mrch["Wartosc"],'chocolate',linestyle=':',label='Marchew')
# plt.plot(x,cbl["Wartosc"],'darkkhaki',linestyle='-.',label='Cebula')
# plt.plot(x,zmn["Wartosc"],'tab:brown',linestyle='--',label='Ziemnior')
# plt.xticks(rotation=45, size=7.5)
# plt.xlim(['styczeń','grudzień'])
# plt.grid()
# plt.ylabel("Wartosci tego ceny",size=15)
# plt.figtext(0.01,0.07,'siusiak',size=15)
# plt.legend()
# plt.show()
data=pd.read_csv('cechy41.csv',sep=';',decimal=',')
print(data)
cecha1 = data["Cecha1"].values
cecha2 = data["Cecha2"].values
fig, axs = plt.subplots(1,2)
axs[0].barh(np.arange(1, 545, 1), cecha1)
axs[1].barh(np.arange(1, 545, 1), cecha2)
fig.suptitle("matusiak to")
axs[0].set_title('chiu')
axs[1].set_title('shaq')
plt.show()
