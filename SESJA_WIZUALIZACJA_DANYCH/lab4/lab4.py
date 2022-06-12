# zad1
lista = [x * 2 for x in range(0, 31)]
plik = open('dane.txt', 'w+')
plik.writelines(str(lista))
plik.close()

# zad2
plik = open('dane.txt', 'r')
print(plik.readlines())
plik.close()

# zad3
with open('dane.txt', 'a+') as plik:
    for x in range(0, 5):
        plik.writelines('nowa linia nr: ' + str(x))
plik = open('dane.txt', 'r')
print(plik.readlines())
plik.close()

# zad 4


class NaZakupy:
    def __init__(self, nazwa, ilosc, jednostka, cena_jd):
        self.nazwa = nazwa
        self.ilosc = ilosc
        self.jednostka = jednostka
        self.cena_jd = cena_jd

    def wyswietl_produkt(self):
        print(self.nazwa + ' ' + self.ilosc + ' ' + self.jednostka + ' ' + self.cena_jd)

    def ile_produktu(self):
        print(self.ilosc + ' ' + self.jednostka)

    def ile_kosztuje(self):
        print((self.ilosc * self.cena_jd))

# zad 5


class Ciong:
    def __init__(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n
        self.ciong = [a1 + r * x for x in range(0, n)]

    def pobierz_element(self, index):
        if index > self.n -1 or index < 0:
            print('Wrong index')
            return -1
        return self.ciong[index]

    def pobierz_parametry(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n
        self.ciong = [a1 + r * x for x in range(0, n)]

    def policz_sume(self):
        suma = 0
        for x in range(0, self.n):
            suma += self.ciong[x]
        return suma

    def ile_elementuw(self):
        return self.n
        """ ?????? """

mujciong = Ciong(0, 1, 10)
print(mujciong.ciong)
print(mujciong.pobierz_element(9))
mujciong.pobierz_parametry(0, 2, 10)
print(mujciong.ciong)
print(mujciong.policz_sume())
print(mujciong.ile_elementuw())


# zad 6


class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_n(self, ile):
        self.y += ile * self.krok

    def idz_e(self, ile):
        self.x += ile * self.krok

    def idz_s(self, ile):
        self.y -= ile * self.krok

    def idz_w(self, ile):
        self.x -= ile * self.krok

    def gdzie_jestes(self):
        print('x: ' + str(self.x) + ', y: ' + str(self.y))


mujrobaczek = Robaczek(5, 10, 1)
mujrobaczek.gdzie_jestes()
mujrobaczek.idz_n(5)
mujrobaczek.gdzie_jestes()
mujrobaczek.idz_e(3)
mujrobaczek.gdzie_jestes()
mujrobaczek.idz_s(6)
mujrobaczek.gdzie_jestes()
mujrobaczek.idz_w(1)
mujrobaczek.gdzie_jestes()
