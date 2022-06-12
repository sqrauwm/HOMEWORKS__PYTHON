import numpy as np

#napisz funkcje ktora przyjmuje parametr 'n' w postaci int i zwraca tablice o wymiarach n*n kolejnych poteg liczby 2

def tablica(n):
    a = np.zeros((n*n), dtype='int32')
    for i in range(0, len(a)):
        a[i] = 2 ** i
    tab = a.reshape((n, n))
    return tab

print(tablica(5))

#funkcja przyjmujaca 2 parametry: 'liczba' - podstawa potęgowania, 'ilosc' - ile wygenerowac

def generuj(liczba, ilosc):
    return np.logspace(1, ilosc, num=ilosc, base=liczba)

print(generuj(2, 4))

# jakas wykreslanka z pizdy

malina = np.array(list('malina'))
mrowka = np.array(list('mrówka'))
armata = np.array(list('armata'))
#armata = np.flip(armata)

#wykreslanka = np.zeros((6, 6), dtype='str')


wykreslanka = np.diag(mrowka)
wykreslanka[:, 0] = malina
# wykreslanka[5,::-1] = armata
wykreslanka[5, :] = armata
print(wykreslanka)

print("")
wykreslanka[:, 0] = mrowka
wykreslanka[5, ::-1] = armata
for a in range(5):
    wykreslanka[a, a] = malina[a]

print(wykreslanka)

# zad7
def macierz(n):
    mac = np.zeros((n, n), dtype='int32')
    mac += np.diag([2 for _ in range(n)])
    for i in range(1, n):
        mac += np.diag([2+(2*i) for _ in range(n-i)], k=i)
        mac += np.diag([2+(2*i) for _ in range(n-i)], k=-i)
    print(mac)

macierz(3)

# funkcja która dzieli tablice na pół w zależnosci od parametru kierunek
def podziel(tab, kierunek='poziomo'):
    print(tab)
    if kierunek == 'poziomo':
        # nieparzysta liczba wierszy
        if tab.shape[0] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę wierszy")
            return
        p1 = tab[0:int(tab.shape[0]/2), :]
        p2 = tab[int(tab.shape[0]/2):, :]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)
    elif kierunek == "pionowo":
        if tab.shape[1] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę kolumn")
            return
        p1 = tab[:, 0:int(tab.shape[1]/2)]
        p2 = tab[:, int(tab.shape[1] / 2):]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)


podziel(np.arange(36).reshape((6, 6)), kierunek='pionowo')