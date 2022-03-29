import math
from math import *
# a, b = 3, 8
# print("a:",a,"\nb:",b)
# c= 3.125
# print('to jest c: %(z1)d'%{'z1':c})


# a = input('Podaj pierwsza liczbe: ')
# b = input('Podaj druga liczbe: ')
# c = input('Jakie dzialanie chcesz wykonac? ')
# a=float(a)
# b=float(b)
#
# if c=='+':
#     print("Wynik dzialania %(z1)d + %(z2)d = %(z3)d" %{'z1':a, 'z2':b,'z3':a+b})
# elif c=='-':
#     print("Wynik dzialania %(z1)d - %(z2)d = %(z3)d" %{'z1':a, 'z2':b,'z3':a-b})
# elif c=='*':
#     print("Wynik dzialania %(z1)d * %(z2)d = %(z3)d" %{'z1':a, 'z2':b,'z3':a*b})
#
# elif c == '/':
#     print("Wynik dzialania %(z1)d / %(z2)d = %(z3)d" %{'z1':a, 'z2':b,'z3':a/b})
# else:
#     print("Zly znak!!!")
#

#
# lista = ['kosz','noga','pingpong','chuj','zuzia']
# print(lista)
# lista.reverse()
# lista.append('cipa')
# print(lista)

# slownik = {'kosz':'xd','lol':'liga legend','zuz':'zuzia'}
# slownik['klucz']=5
# del slownik['lol']
# print(slownik)
# print(len(slownik))

# zdanie=(input("Wpisz zdanie: "))
# print(zdanie.count("a"))
#

# import sys
# print("Podaj a: ")
# a = sys.stdin.readline()
# a=int(a)
#
# print("Podaj b: ")
# b = sys.stdin.readline()
# b=int(b)
#
# print("Podaj c: ")
# c = sys.stdin.readline()
# c=int(c)
#
# d=a**b+c
# d=str(d)
# sys.stdout.write(d)

# a = input('Wpisz 3 liczby')
# b = input()
# c = input()
# a=int(a)
# b=int(b)
# c=int(c)
# print(max(a, b, c ))

# lista = [1, 2.5, 3.89, 9, 10, 8.125]
# lista2 = [x**2 for x in lista]
# print(lista)
# print(lista2)

# lista = []
# for x in range(0,10):
#     b=int(input(" Podaj liczbe: "))
#     if b%2==0:
#         lista.append(b)
#
# print(lista)

# import math
# a = int(input("Podaj liczbe, ktora bedzie pod pierwiastkiem: "))
# if a>=0:
#     print(math.sqrt(a))
# else:
#     print(" Liczba jest mniejsza od 0")

# A = [1-x for x in range(1,11)]
# print(A)
# B=[4**x for x in range(0,8)]
# print(B)
# C=[x for x in B if x%2==0]
# print(C)

# import random
# from math import *
# lista1 = [random.randint(0,10) for x in range(0,10)]
# print(lista1)
#
# # lista2 =[random.randint(0,10) for x in range(0,10) if random.randint(0,10)%2==0]
# lista3 = []
# while len(lista3)<10:
#     c= random.randint(0,10)
#     if c%2==0:
#         lista3.append(c)
# print(lista3)

# slownik = {'ziemniaki':'kg','cukierki':'sztuki','chleb':'sztuki'}
# print(slownik)
# slownik2 = [a for a in slownik if b=='sztuki']

# slownik = {'mleko': 'sztuki', 'ziemiaki': 'kg', 'jogurt': 'sztuki'}
# lista = {a for (a,b) in slownik.items() if b == 'sztuki'}
# print(lista)

# import math
# def czy_trojkat(a,b,c):
#     if(a**2 + b**2 == c**2):
#         return "Trojkat jest prostokatny"
#     else:
#         return "Trojkat nie jest prostokatny"
# print(czy_trojkat(12,5,14))
#

# def trapez(a=2,b=3,h=10):
#     return (a+b)*h/2
# print(trapez(1,2,3))

# def iloczyn_ciagu(a=1,b=3,ile=4):
#     ciag = [a*(b**x) for x in range(ile)]
#     print(ciag)
#     for x in range(ile):
#         a *= ciag[x]
#     return a
# print(iloczyn_ciagu())

# def iloczyn(*liczby):
#     if len(liczby)==0:
#         return "brak wyrazow w ciagu"
#     else:
#         zadanie7 = [x for x in liczby]
#         print(zadanie7)
#         iloczyn_wyrazow_ciagu = 1
#         for x in liczby:
#             iloczyn_wyrazow_ciagu *= x
#         return iloczyn_wyrazow_ciagu
#
# print(iloczyn())

# def produkty(**zakupy):
#     koszt_zakupow=0
#     for koszt in zakupy:
#         koszt_zakupow = koszt_zakupow + zakupy[koszt]
#     return "Ilosc zakupow: %d "%len(zakupy),"Laczny koszt zakupow: %.2f"%(koszt_zakupow)
# print(produkty(ciastka = 3.89, chipsy = 5.49, woda = 100.99, wudeczka = 23.99, liqudzior = 74.99))


# from ciagi import *
# print(ciag_a.n_ty_wyraz(6,2,2))
# print(ciag_a.suma_ciagu(6, 16, 6))
# print(ciag_g.n_ty_wyraz(1, 4, 11))


# zad1 = [x*2 for x in range(0,31)]
# print(zad1)
# plik = open('homework.txt','w+')
# plik.writelines(str(zad1))
# plik.close()
#
# plik = open('homework.txt','r')
# zad2 = plik.readlines()
# plik.close()
# print(zad2)
#
# with open('zadanie3.txt','w+') as zad3:
#     for x in range(0,10):
#         zad3.writelines('siema elllo ' + str(x) + '\n')
#
# with open('zadanie3.txt', 'r') as zad3:
#     for a in zad3:
#         print(a)


# class NaZakupy():
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed, waluta):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#         self.waluta = waluta
#
#     def wyswietl_produkt(self):
#         return "{}, {} {}, {} {}".format(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed, self.waluta )
#
#     def ile_produktu(self):
#         return "{} {}".format(self.ilosc, self.jednostka_miary)
#
#     def ile_kosztuje(self):
#         return "{} {}, kosztuje {} {}".format(self.ilosc, self.jednostka_miary, self.ilosc*self.cena_jed, self.waluta)
#
# mleko = NaZakupy('mleko', 5, 'szt', 2.50, 'zl')
# print(mleko.wyswietl_produkt())
# print(mleko.ile_produktu())
# print(mleko.ile_kosztuje())
# cola = NaZakupy('CocaCola', 4, 'szt', 6.99, 'zl')
# print(" ")
# print(cola.wyswietl_produkt())
# print(cola.ile_produktu())
# print(cola.ile_kosztuje())

class Robaczek():
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_gora(self, ilekrok):
        self.y = self.y + ilekrok * self.krok
        return "WSPOLRZEDNE:   x: {}, y: {}".format(self.x, self.y)

    def idz_dol(self, ilekrok):
        self.y = self.y - ilekrok * self.krok
        return "WSPOLRZEDNE:   x: {}, y: {}".format(self.x, self.y)

    def idz_lewo(self, ilekrok):
        self.x = self.x - ilekrok * self.krok
        return "WSPOLRZEDNE:   x: {}, y: {}".format(self.x, self.y)

    def idz_prawo(self, ilekrok):
        self.x = self.x + ilekrok * self.krok
        return "WSPOLRZEDNE:   x: {}, y: {}".format(self.x, self.y)

    def gdzie(self):
        return "WSPOLRZEDNE:   x: {}, y: {}".format(self.x, self.y)

robak = Robaczek(0, 0, 1)
print(robak.idz_prawo(4))
print(robak.idz_gora(4))
print(robak.idz_dol(3))
print(robak.idz_gora(10))

print(" ")
zuzia = Robaczek(10,10, 1)
print(zuzia.gdzie())


