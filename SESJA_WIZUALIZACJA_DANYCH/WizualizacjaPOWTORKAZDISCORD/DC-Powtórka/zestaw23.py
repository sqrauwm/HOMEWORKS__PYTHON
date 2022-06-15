import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FormatStrFormatter
from PIL import Image

#Zadanie 2
x = np.arange(0.1, 3 * (np.pi) + 0.1, 0.1)
y1 = np.log(x)
y2 = 3 * x - 5
y3 = 2 * np.cos(x)

plt.plot(x, y1, 'b:', label='log(x)')
plt.plot(x, y2, 'r.', label='3x - 5')
plt.plot(x, y3, 'g--', label='2cos(x)')
plt.grid()
plt.title('chuj')
plt.legend()
plt.figtext(0, 0, 'chuj', size=15)
# plt.savefig('chuj.png')
plt.show()

xlsx = pd.ExcelFile('mieszkania23.xlsx')
df = pd.read_excel(xlsx, header=0)
lata = df.groupby('Rok')['Wartość'].sum()
print(lata)

typ1 = df[df['Formy budownictwa'] == 'indywidualne']
typ2 = df[df['Formy budownictwa'] == 'spółdzielcze']
typ3 = df[df['Formy budownictwa'] == 'komunalne']

indyk = df.groupby('Formy budownictwa')['Wartość'].sum()
print(indyk)

plt.bar(df['Rok'].unique()-0.2, typ1['Wartość'].values, 0.2, zorder=3, label='Indywidualne')
plt.bar(df['Rok'].unique(), typ2['Wartość'].values, 0.2, zorder=3, label='Spółdzielcze')
plt.bar(df['Rok'].unique()+0.2, typ3['Wartość'].values, 0.2, zorder=3, label='Komunalne')
plt.xticks([2015, 2016, 2017, 2018])
plt.legend()
plt.title('Wykresy chuj')
plt.figtext(0.9,0,'chuj', size=15)
plt.grid()
plt.savefig('wykreschuj.pdf', format='pdf')
plt.show()

#Zadanie 3
xslx = pd.ExcelFile('turystyka23.xlsx')
df = pd.read_excel(xslx, header=None).transpose()
fig, axs = plt.subplots(1,2)
rok1 = df[df[1] == '2014']
rok2 = df[df[1] == '2019']
x1 = rok1[2].values
x2 = rok2[2].values
axs[0].pie(x1, labels=rok1[0], autopct='%.1f %%', colors=['moccasin', 'dodgerblue', 'slateblue', 'peru', 'lavender'], startangle=-60)
axs[1].pie(x2, labels=rok2[0], autopct='%.1f %%', colors=['moccasin', 'dodgerblue', 'slateblue', 'peru', 'lavender'], startangle=-70)
axs[0].set_title('wykres1')
axs[1].set_title('wykres2')
fig.suptitle('HOTELE')
plt.show()
