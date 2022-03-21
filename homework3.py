# # Zadanie 1
#
# zadanieA=[1-x for x in range(1,11)]
# print(zadanieA)
#
# zadanieB=[4**x for x in range(0,8)]
# print(zadanieB)
#
# zadanieC=[x for x in zadanieB if x%2==0]
# print(zadanieC)


# # Zadanie 2
#
# import random
# lista1 = [random.randint(1,30) for x in range(0,10)]
# print(lista1)
#
# lista2 = [x for x in lista1 if x%2==0]
# print(lista2)

# # Zadanie 3
#
# produkty = {'ziemniaki':'kg',"czekolada":'sztuki', 'mleko':'litry',"baterie":'sztuki',"loudy":'sztuki'}
# na_sztuki = {a:b for (a,b) in produkty.items() if b == 'sztuki'}
# print(na_sztuki)

# # Zadanie 4
#
# import math
# def czy_prosto(a,b,c):
# # C JEST NAJWIEKSZE #
#     if (c>a)&(c>b):
#         if((a**2)+(b**2)==(c**2)):
#             return ('Trojkat jest prostokatny.\n')
#         else:
#             return ('Trojkat nie jest prostokatny.\n')
# # A JEST NAJWIEKSZE #
#     elif(a > b) & (a > c):
#         if ((b ** 2) + (c ** 2) == (a ** 2)):
#             return ('Trojkat jest prostokatny.\n')
#         else:
#             return ('Trojkat nie jest prostokatny.\n')
# # B JEST NAJWIEKSZE #
#     elif (b > a) & (b > c):
#         if ((a ** 2) + (c ** 2) == (b ** 2)):
#             return ('Trojkat jest prostokatny.\n')
#         else:
#             return ('Trojkat nie jest prostokatny.\n')
#     else:
#         return ('Trojkat nie jest prostokatny.\n')
# ######################################################################
# print(czy_prosto(3,4,5))

# # Zadanie 5
#
# import math
# def pole_trapezu(a=2, b=10, h=3):
#     return ( (a+b)*h / 2 )
# print(pole_trapezu())

# # Zadanie 6
#
# import math
# def ciagXD(a=1, b=4, ile=10):
#     zadanie6 = [a+(b*x) for x in range(ile)]
#     print(zadanie6)
#     iloczyn_wyrazow_ciagu=1
#     for x in range(ile):
#         iloczyn_wyrazow_ciagu *= zadanie6[x]
#     return iloczyn_wyrazow_ciagu
# print(ciagXD())

# # Zadanie 7
#
# import math
# def ciagXD(* liczby):
#     if len(liczby)==0:
#         return 0
#     else:
#         zadanie7 = [x for x in liczby]
#         print(zadanie7)
#         iloczyn_wyrazow_ciagu = 1
#         for x in liczby:
#             iloczyn_wyrazow_ciagu *= x
#         return iloczyn_wyrazow_ciagu
# print(ciagXD(1,5,9,13))

# Zadanie 8 DO ZROBIENIA ?????????????????????????????????????????????????????????????????????????????????

def lista_zakupow(** rzeczy):
    for cos in rzeczy:
        print("Liczba produktow: " + len(str(rzeczy)) + "\n")
        print("Laczny koszt produktow: " + sum(value(rzeczy)) + "\n")


lista_zakupow(czekolada=['3'], chipsy=['5'], woda=['2'],wudeczka=['23'],liqudzior=['70'])

# # Zadanie 9

# from pakiety import ciag_g
# from pakiety import ciag_a
# ciag_g.geo()
# ciag_a.aryt()