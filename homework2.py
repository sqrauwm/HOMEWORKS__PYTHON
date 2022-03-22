# Zad 1. 

# lista = ['siata', 'pila', 'kosz']
# print(lista)
# lista.reverse()
# print(lista)
# lista.append('pingpong')
# lista.append('plywanie)
# print(lista)

# Zad 2. 

# slownik = {'naura':'pospolite do widzenia',"wtf":'co kurcze?', 'lol':'laughing out loud' }
# print(slownik['naura'])
# print(slownik['wtf'])
# print(slownik['lol'])

# Zad 3. 

# slownik = {'val':'valorancik',"lol":'league of legends', 'cs':'counter strike ' }
# print(len(dict.keys(slownik)))

# Zad 4. 

# napis = input("Wpisz se cos: ")
# print(napis.count('a'))

# Zad 5. 

# import sys as system
# system.stdout.write("Wpisz 3 liczby: ")
# a = system.stdin.readline()
# a=int(a)
# b = system.stdin.readline()
# b=int(b)
# c = system.stdin.readline()
# c=int(c)
# d = a*b + c
# d = str(d)
# system.stdout.write(d)

# Zad 6. 

# a = input('Wpisz 3 liczby')
# b = input()
# c = input()
# a=int(a)
# b=int(b)
# c=int(c)
# print(max(a, b, c ))

# Zad 7. 

# lista = [ 9, 43, 86, 5.25, 2.78, 9.99, 1.23]
# for x in lista:
#     print(type(x))
# for x in lista:
#     print(x*x)

# Zad 8. 

# a=0
# lista = []
# while(a<10):
#     b=int(input("Wpisz liczbe: "))
#     if(b%2==0):
#         lista.append(b)
#
#     a+=1
# print(lista)

# Zad. 9.

import math
a = int(input('Wpisz liczbe: '))
if(a<0):
    print('cos poszlo nie tak!')
else:
    print(math.sqrt(a))
