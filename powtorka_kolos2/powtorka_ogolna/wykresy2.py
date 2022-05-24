import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# wykres liniowy --------------------------------------------
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-') # oś x, oś y, styl
plt.axis([0, 6, 0, 20]) # x_min, x_max, y_min, y_max
plt.show()

# dwa wykresy liniowe na jednym png --------------------------------------------
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r') # r - red
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o') # o - punkty
plt.axis([0, 6, 0, 20]) # x_min, x_max, y_min, y_max
plt.show()

# kilka wykresów w jednym wywołaniu --------------------------------------------
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
# r-- == red przerywana, bs == blue kwadraty(squares), g^ == green trójkąty
plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])
plt.show()

from PIL import Image

x = np.linspace(0, 2, 100)
# wykresy dodawane pojedynczo --------------------------------------------
plt.plot(x, x, label='liniowa')
plt.plot(x, x ** 2, label='kwadratowa')
plt.plot(x, x ** 3, label='szescienna')
#etykiety osi x
plt.xlabel('etykieta x')
plt.ylabel('etykieta y')
#tytuł wykresu
plt.title('prosty wykres')
#włączenie legendy
plt.legend()

plt.savefig('wykres matplot.png') # ?
plt.show()
im1 = Image.open('wykres matplot.png')
im1 = im1.convert('RGB')
im1.save('nowy.jpg') # to jest chyba zapis do pliku, a to wyzej to nwm (jakiś temp-file?)

# sinus --------------------------------------------
x = np.arange(0, 10, 0.1)
s = np.sin(x)
plt.plot(x, s, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Wykres sin(x)')
plt.legend()
plt.show()

# wykres bombelkowy(?) --------------------------------------------
# słownik, może być też DataFrame
data = {'a': np.arange(50),
        'kolory': np.random.randint(0, 50, 50),
        'skale': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['skale'] = np.abs(data['skale']) * 100

# parametr c == kolory,  parametr s == skala,
plt.scatter('a', 'b', c='kolory', s='skale', data=data)
plt.xlabel('wartosc a')
plt.ylabel('wartosc b')
plt.show()

# podwykresy ------------------------------------------------
# funkcja subplot przyjmuje rozmieszczenie wykresów na zdjęciu i indeks obecnego podwykresu
x1 = np.arange(0, 2, 0.02)
x2 = np.arange(0, 2, 0.02)

y1 = np.sin(2 * np.pi * x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1) # 2 wiersze, 1 kolumna, 1-wszy indeks podwykresu
plt.plot(x1, y1, '-') # styl linia ciągła (domyślnie niebieska?)
plt.title('wykres sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')

ax = plt.subplot(2, 1, 2) # to samo co wczesniej tylko 2-gi indeks podwykresu
# nie wiem po co przypisanie do zmiennej 'ax', pewnie nie potrzebne
plt.plot(x2, y2, 'r-') # styl czerwona linia ciągła
plt.title('wykres cos(x)')
plt.xlabel('x')
plt.ylabel('cos(x)')

plt.subplots_adjust(hspace=0.5) # odległosc w pionie miedzy wykresami
plt.show()

# podwykresy CD --------------------------------------------------
x1 = np.arange(0, 2, 0.02)
x2 = np.arange(0, 2, 0.02)

y1 = np.sin(2 * np.pi * x1)
y2 = np.cos(2 * np.pi * x2)

fig, axs = plt.subplots(3, 2, ) #siatka wykresów 3x2, bez indeksu bo mamy zmienną 'axs' do tego

axs[0, 0].plot(x1, y1, '-') # wykres lewy-górny
axs[0, 0].set_title('wykres sin(x)')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('sin(x)')

axs[1, 1].plot(x2, y2, '-') # wykres prawy-środek
axs[1, 1].set_title('wykres cos(x)')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('cos(x)')

axs[2, 0].plot(x2, y2, '-') # wykres lewy-duł
axs[2, 0].set_title('wykres cos(x)')
axs[2, 0].set_xlabel('x')
axs[2, 0].set_ylabel('cos(x)')

# trzeba jeszcze wyjebac nie użyte wykresy za pomocą zmiennej 'fig'
fig.delaxes(axs[0, 1])
fig.delaxes(axs[1, 0])
fig.delaxes(axs[2, 1])

plt.show()

# wykres słupkowy -------------------------------------
data = {'Kraj': ['Polska', 'Francja', 'Niemcy'],
        'Stolica': ['Warsz', 'Paris', 'Berlino'],
        'Kontynent': ['Ojro', 'Ojro', 'CosInnego'],
        'Populacja': [40, 60, 80]}
df = pd.DataFrame(data)
group = df.groupby('Kontynent')
etykiety = list(group.groups.keys())
wartosci = list(group.agg('Populacja').sum())

plt.bar(x=etykiety, height=wartosci, color=['yellow', 'green', 'red'])
plt.xlabel('Kontynenty')
plt.ylabel('Populacja')
plt.show()

# histogramy ------------------------------------------------
# bins == ilość słupków
# facecolor == kolor słupków
# alpha == przezroczystość
# density == czy suma ilości ma być znormalizowana

x = np.random.randn(10000)
plt.hist(x, bins=50, facecolor='g', alpha='0.75', density=True)
plt.xlabel('Wartości')
plt.ylabel('Prawdopodobieństwo')
plt.title('Histogram')
plt.grid()
plt.show()

# wykres kołowy --------------------------------------------------
df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
seria = df.groupby('Imie i nazwisko')['Wartość zamówienia'].sum()

wedges, texts, autotext = plt.pie(x=seria, labels=seria.index, autopct=lambda pct: '{:.1f}%'.format(pct),
                                  textprops=dict(color='black'), colors=['red', 'green'])

plt.title('Suma zamówień')
plt.legend(loc='lower right')
plt.ylabel('Procentowy wynik zamówienia')
plt.show()