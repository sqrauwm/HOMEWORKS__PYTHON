# # Zadanie. 1 Wygeneruj liczby z przedziału <0,30>, następnie pomnóż je przez 2 i zapisz do pliku
#
# lista = [2 * x for x in range(0, 31)]
# plik = open('homework4.txt', 'w+')
# plik.writelines(str(lista))
# plik.close()
#
# # Zadanie. 2 Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość
# plik = open('homework4.txt','r')
# print(plik.readlines())
# plik.close()
#
# # Zadanie. 3 Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.
#
# with open('homework4.txt', 'w+') as plik:
#     for x in range(1, 10):
#         plik.writelines('cyfra ujemna:'+ str(-x))
#         plik.writelines(' cyfra dodatnia: ' + str(x) +  "\n")
# plik = open('homework4.txt', 'r')
# print(plik.readlines())
# plik.close
#
# # Zadanie. 4 Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
# class NaZakupy:
#     def __init__(self, nazwa, ilosc, jednostka, cena_jd):
#         self.nazwa = nazwa
#         self.ilosc = ilosc
#         self.jednostka = jednostka
#         self.cena_jd = cena_jd
#
#     def wyswietl_produkt(self):
#         print(self.nazwa + ' ' + self.ilosc + ' ' + self.jednostka + ' ' + self.cena_jd)
#
#     def ile_produktu(self):
#         print(self.ilosc + ' ' + self.jednostka)
#
#     def ile_kosztuje(self):
#         print((self.ilosc * self.cena_jd))

# Zadanie. 5 Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako atrybut. Klasa powinna mieć metody:
#
# class ciagxd:
#     def __init__(self, a1, r, n):
#         self.a1 = a1
#         self.r = r
#         self.n = n
#         self.ciagx = [a1 + r * x for x in range(0, n)]
#
#     def pobierz_elementy(self, index):
#         if index > self.n - 1 or index < 0:
#             print('Zly index')
#             return -1
#         return self.ciagx[index]
#
#     def pobierz_parametry(self, a1, r, n):
#         self.a1 = a1
#         self.r = r
#         self.n = n
#         self.ciagx = [a1 + r * x for x in range(0, n)]
#
#     def policz_sume(self):
#         suma = 0
#         for x in range(0, self.n):
#             suma += self.ciagx[x]
#         return suma
#
#     def policz_elementy(self):
#         return self.n
#         """ ??? """
#
#
# ciag = ciagxd(3, 2, 10)
# print(ciag.ciagx)
# print(ciag.pobierz_elementy(5))
# ciag.pobierz_parametry(1, 3, 10)
# print(ciag.ciagx)
# print(ciag.policz_sume())
# print(ciag.policz_elementy())


# Zadanie. 6 TWORZYMY ROBAKA
#
# class Robaczek:
#     def __init__(self, x, y, krok):
#         self.x = x
#         self.y = y
#         self.krok = krok
#
#     def idz_gora(self, ile):
#         self.y += ile * self.krok
#
#     def idz_prawo(self, ile):
#         self.x += ile * self.krok
#
#     def idz_dol(self, ile):
#         self.y -= ile * self.krok
#
#     def idz_lewo(self, ile):
#         self.x -= ile * self.krok
#
#     def gdzie_jestes(self):
#         print('x: ' + str(self.x) + ', y: ' + str(self.y))
#
# robak = Robaczek(10, 10, 1)
# robak.gdzie_jestes()
# robak.idz_gora(5)
# robak.gdzie_jestes()
# robak.idz_lewo(1)
# robak.gdzie_jestes()
# robak.idz_dol(6)
# robak.gdzie_jestes()
# robak.idz_prawo(3)
# robak.gdzie_jestes()


