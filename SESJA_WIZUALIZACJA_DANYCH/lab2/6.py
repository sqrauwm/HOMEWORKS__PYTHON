#zad6
a = input("Podaj a: ")
b = input("Podaj b: ")
c = input("Podaj c: ")

if (a > b):
    if (a > c):
        print(a)
    else:
        print(c)
else:
    if (b > c):
        print(b)
    else:
        print(c)