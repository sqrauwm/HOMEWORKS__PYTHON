import numpy as np

# a = np.arange(12).reshape((3, 4))

# print(a)
# print(a.sum(axis=0)) # suma kolumn
# print(a.sum(axis=1)) # suma wierszów
# print(a.cumsum(axis=0)) # skumulowana suma ??
# print(a.cumsum(axis=1))

# mnożenie macierzy
# a = np.arange(3)
# b = np.arange(3)
# print(a)
# print(b)
# print(a.dot(b))
# print(np.dot(a, b))

# funkcje elementarne
# a = np.arange(3)
# print(a)
# print(np.exp(a)) # e ^ x
# print(np.sqrt(a)) # x ^ 0.5
# c = np.array([2., -1., 4.])
# print(c)
# print(np.add(a, c))

# iteracja tablic
# a = np.arange(6).reshape((3, 2))
# print(a)
# for b in a:
#     print(b)
# for b in a.flat:
#     print(b)

# przekształcenia
# a = np.arange(6)
# print(a.shape)
# b = np.array([np.arange(3), np.arange(3), np.arange(3)])
# print(b.shape)
#
# c = b.ravel()
# print(c)
# print(b)
# print(b.T)