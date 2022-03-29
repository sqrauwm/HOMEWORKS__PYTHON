def n_ty_wyraz(a1, q, n):
    return a1 * q**(n-1)


def suma(a1, n, q):
    if q == 1:
        return a1*n
    else:
        return a1 * (1-q**n)/(1-q)