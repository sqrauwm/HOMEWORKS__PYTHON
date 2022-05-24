import numpy as np

#inicjalizacja tablicy
a = np.array([0, 1])
print(a)
#lub drugi sposób
a = np.arange(2)
print(a)

#wypisanie typu zmiennej tablicy (nie jej elementów) -ndarray
print(type(a))
#sprawdzenie typu danych tablicy
print(a.dtype)

#inicjalizacja tablicy z konkertnym typem danych
a = np.arange(2, dtype='int64')
print(a.dtype)

#zapisywanie kopii tablicy jako tablicy z innym typem
b = a.astype('float')
print(b.dtype)

#stworzenie tablicy wielowymiarowej może wyglądać tak
m = np.array([np.arange(10), np.arange(10)])
print(m.shape)

#możemy w łatwy sposób stworzyć macierz danego rozmiaru wypełnioną zerami lub jedynkami
zera = np.zeros((5, 5), dtype='int64')
jedynki = np.ones((4, 4))
print(zera)
print(jedynki)

#do elementów tablicy możemy odwołać się tak jak do elementów np. listy czyli podając indeksy
element = zera[0, 0]
print(element)

#tworzenie macierzy 2x2 wraz z uzupełnieniem
macierz = np.array([[1, 2], [3, 4]])
print(macierz)

#funkcja arange potrafi takrze tworzyć ciągi liczb zmiennoprzecinkowych
liczby = np.arange(1, 2, 0.1)
print(liczby)

#podobnie działa funkcja linspace
liczby_lin = np.linspace(1, 2, 5)
print(liczby_lin)

#a teraz możemy utworzyć dwie macierze, najpierw wartości interowane są w kolumnie a następnie w wierszu
z = np.indices((3, 5))
print(z)

#wielowymiarowe macierze możemy również generować funkcją mgrid
x, y = np.mgrid[0:5, 0:5]
print(x)
print(y)

#podobnie jak w MATLAB-ie możemy tworzyć macierze diagonalne
mat_diag = np.diag([a for a in range(5)])
print(mat_diag)

#macierz diagonalna przesunienta
mat_diag_k = np.diag([a for a in range(5)], -1)
print(mat_diag_k)

#cięcie (slicing) tablicy numpy można wykonać za pomocą wartości z funkcji slice lub range
a = np.arange(10)
print(a)
s = slice(2, 7, 2)
print(a[s])
s = range(2, 7, 2) # to samo co wyzej
print(a[s])

#możemy ciąć tablice również w sposób znany z cięcia list (efekt jak wyżej)
print(a[2:7:2]) #od 2 do 7 (wyłącznie) co 2
print(a[3:]) #od 3 do końca
print(a[2:3]) #od 2 do 3 (wyłącznie)

#cięcia talic wielowymiarowych (macierzy)
mat = np.arange(25)
print(mat)
mat = mat.reshape((5, 5))
print(mat)
print(mat[1:]) #od drugiego wiersza
print(mat[:,1]) #druga kolumna jako wektor
print(mat[:,-1:]) #ostatnia kolumna
print(mat[2:6, 1:3]) # 2 i 3 kolumna dla 3,4,5 wierszy
print(mat[:, range(2,6,2)]) # 3 i 5 kolumna

#bardziej zaawansowane, lecz trudniejsze do zrozumienia cięcia można osiągnąć wg. poniższego przykładu
# #y będzie tablicą zawierającą wierzchołki macierzy x

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print(y)