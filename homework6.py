import numpy as np

# # Zadanie 1
# a = 4 * (np.arange(1, 21))
# print(a)

# # Zadanie 2
# b = np.arange(5, dtype='float')
# print(b)
# c = b.astype('int32')
# print(c)

# # Zadanie 3
# def poteg(n):
#     mat = np.arange(1, n*n+1)
#     mat = mat.reshape(n, n)
#     print(2**mat)
#
#
# poteg(int(input("n: ")))

# # Zadanie 4
# def poteg2(n, i):
#     return np.logspace(1, i, num=i, endpoint=True, base=n)
#
#
# print(poteg2(int(input("n: ")), int(input("i: "))))

# # Zadanie 5
# def niewiem(n):
#     wektor = np.arange(n, 0, -1)
#     print(wektor)
#     mat_diag_k = np.diag(wektor, k=2)
#     print(mat_diag_k)
#
#
# niewiem(int(input("n: ")))

# Zadanie 6 ???

# # Zadanie 7
# def krotnosci(n):
#     a = np.diag(np.linspace(2, 2, num=n, dtype=int))
#     for i in range(n - 1):
#         b = np.diag(np.linspace(2 * (i + 2), 2 * (i + 2), num=n, dtype=int), k=i + 1)
#         b = b[:n, :n]
#         c = np.diag(np.linspace(2 * (i + 2), 2 * (i + 2), num=n, dtype=int), k=-i - 1)
#         c = c[:n, :n]
#         a = a + b + c
#     return a
#
#
# print(krotnosci(int(input("n: "))))

# # Zadanie 8
# def ciac(n, kierunek):
#     if n % 2 == 1:
#         print("Prosze wpisac parzyste n")
#     else:
#         if n < 0:
#             print("Prosze wpisac dodatnie n")
#         else:
#             macierz = np.arange(1, n * n + 1)
#             macierz = macierz.reshape(n, n)
#             print(macierz)
#             if kierunek == 'poziomo':
#                 print(macierz[:(n // 2)])
#                 print(macierz[(n // 2):])
#             if kierunek == 'pionowo':
#                 print(macierz[:, :(n // 2)])
#                 print(macierz[:, (n // 2):])
#
# ciac(int(input("n: ")), input("kierunek: "))

# # Zadanie 9
# a1 = int(input("a1: "))
# r = int(input("r: "))
# n = a1 + 25 * r
# wynik = np.arange(a1, n, r)
# wynik = wynik.reshape(5, 5)
# print(wynik)
