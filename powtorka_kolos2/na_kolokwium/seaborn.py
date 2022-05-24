import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# wykres liniowy

sns.set(rc={'figure.figsize': (8, 8)}) # rc - skala siatki
sns.lineplot(x=[1, 2, 3, 4], y=[1, 4, 9, 16],
             label='linia nr1', color='red', marker='o', linestyle=':')
sns.lineplot(x=[1, 2, 3, 4], y=[1, 3, 7, 12],
             label='linia nr2', color='green', marker='^', linestyle=':')

# wykres liniowy z pd.Series
s = pd.Series(np.random.randn(1000))
s = s.cumsum()
sns.set()
wykres = sns.relplot(kind='line', data=s, label='linia')
wykres.fig.set_size_inches(8, 6)
wykres.fig.suptitle('Wykres liniowy')
wykres.set_xlabels('indeksy')
wykres.set_ylabels('wartości')
wykres.add_legend()
wykres.figure.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
plt.show()

# wykres liniowy z pd.DataFrame
sns.set()
df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
wykres = sns.lineplot(data=df, x=df.index, y='sepal length', hue='class')
wykres.set_xlabels('indeksy')
wykres.set_title('Wykres liniowy danych z iris')
wykres.legend(title='Rodzaj kwiatu')
plt.show()

# wykres punktowy
sns.set()
data = {'a': np.arange(10),
        'colors': np.random.randint(0, 50, 10),
        'sizes': np.random.randn()}
data['b'] = data['a'] + 10 * np.random.randn(10)
data['sizes'] = np.abs(data['sizes']) * 100

df = pd.DataFrame(data)
plot = sns.relplot(data=df, x='a', y='b', hue='colors', palette='bright', size='sizes', legend=True)
plot.fig.set_size_inches(6, 6)
plot.set(xticks=data['a'])
plt.show()

# wykres kolumnowy
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Warszawa'],
        'Populacja': [1111111, 2222222, 23333333, 4000]}

df = pd.DataFrame(data)
sns.set()
# ----- jakis inny sposob chyba ------
plot = sns.catplot(data=df, x='Kontynent', y='Populacja', kind='bar', ci=None, hue='Kontynent',
                   estimator=np.sum, dodge=False, palette=['red', 'green', 'yellow'], legend_out=False)
plot.fig.set_size_inches(7, 6)
plot.add_legend(title='Populacja na kontynentach', loc='upper right')
plot.fig.suptitle('Populacja na kontynentach')
# --------------------------------------
plot = sns.barplot(data=df, x='Kontynent', y='Populacja', ci=None, hue='Kontynent', estimator=np.sum,
                   dodge=False, palette=['red', 'green', 'yellow'])
plot.legend(title='Populacja na kontynentach')
plot.set(title='Wykres slupkowy')
plt.show()
