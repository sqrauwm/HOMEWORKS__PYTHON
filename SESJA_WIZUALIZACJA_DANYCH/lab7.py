import numpy as np

# zad 1

# a = np.arange(3).reshape((1, 3))
# b = (np.arange(3) * 5).reshape((1, 3))
#
# print(a * 3)
# print(b / 2)

# zad 2

# a = np.array([(x * 3) % 4 + 1 for x in range(0, 9)]).reshape((3, 3))
# b = np.array([(x - 2) % 7 + 1 for x in range(0, 16)]).reshape((4, 4))
#
# print(b)
# print(a)
#
# print(np.min(a, axis = 0))
# print(np.min(a, axis = 1))
# print(np.min(b, axis = 0))
# print(np.min(b, axis = 1))

# zad 3

# a = np.arange(3).reshape((1, 3))
# b = (np.arange(3) * 2).reshape((3, 1))
#
# print(np.dot(a, b))

# zad 4

# a = np.arange(3).reshape((1, 3))
# b = (np.arange(3) * 1.0).reshape((1, 3))
# #
#
# print(a * 2)
# print(b * 2.5)

# zad 5

# import math
#
# a = np.array([(x * 3) % 4 + 1 for x in range(0, 6)]).reshape((2, 3))
#
# lista = []
#
# for b in a:
#     for c in b:
#         lista.append(math.sin(c))
#
# print(lista)


# zad 6

# import math
#
# a = np.array([(x * 3) % 4 + 1 for x in range(0, 6)]).reshape((2, 3))
#
# lista = []
#
# for b in a:
#     for c in b:
#         lista.append(math.cos(c))
#
# print(lista)
