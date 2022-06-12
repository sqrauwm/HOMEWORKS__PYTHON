import sys as system
#zad5
system.stdout.write('Podaj a: ')
a = int(system.stdin.readline())
system.stdout.write('Podaj b: ')
b = int(system.stdin.readline())
system.stdout.write('Podaj c: ')
c = int(system.stdin.readline())
system.stdout.write('a ^ b + c = {0}'.format(a ** b + c))