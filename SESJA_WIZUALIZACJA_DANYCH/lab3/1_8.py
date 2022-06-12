import random

# zad2
lista = [random.randrange(0, 100) for x in range(0, 11)]
lista2 = [x for x in lista if x % 2 == 0]

print(lista)
print(lista2)

# zad3
slownik = {
    "Ziemniaki": "KG",
    "Kapusta": "Szt",
    "Cos innego": "Szt"
}

listaP = [key for key, value in slownik.items() if value == "Szt"]
print(listaP)


# zad4
def czy_pros(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


print(czy_pros(3, 4, 5))


# zad5
def pole_trapezu(a=5, b=3, h=5):
    return ((a + b) / 2) * h


print(pole_trapezu(5, 10, 3))


# zad6

def iloczyn_elementuw(a1, q, n):
    iloczyn = 1
    for x in range(1, n):
        a1 *= q
        iloczyn *= a1
    return iloczyn


print(iloczyn_elementuw(1, 2, 4))

# zad7

def iloczyn_elementuw2(*arg):
    iloczyn = 1
    for x in arg:
        iloczyn *= x
    return iloczyn


print(iloczyn_elementuw2(1, 2, 4, 8))

# zad8


def policz_produkty(** produkty):
    ilosc = 0
    suma = 0
    for pr in produkty:
        ilosc += 1
        suma += int(produkty[pr])
    print('Ilosc: ' + str(ilosc) + ', suma: ' + str(suma))



policz_produkty(chleb = 3, maslo = 2, cukier = 20)
