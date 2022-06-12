#zad8
lista = []
x = 0
while (x < 10):
    y = int(input('Podaj liczbe: '))
    x = x + 1
    if (y % 2 == 0):
        lista.append(y)

print(lista)