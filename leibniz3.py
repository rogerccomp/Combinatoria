from math import factorial, prod
from itertools import product

def coef_polynomial_power_multinomial(n, terms, m):
    
    r = len(terms)
    total = 0

    for ks in product(range(n + 1), repeat=r):
        if sum(ks) != n:
            continue
        grau = sum(b * k for (c, b), k in zip(terms, ks))
        if grau != m:
            continue
        multin = factorial(n) // prod(factorial(k) for k in ks)
        coef_factor = prod((c ** k) for (c, b), k in zip(terms, ks))
        total += multin * coef_factor

    return total

# Modifique aqui os parâmetros na expansão via polinômio de Leibniz
n = 8
m = 15
terms = [(1, 0), (1, 2), (1, 3)]
c2_mult = coef_polynomial_power_multinomial(n, terms, m)
print(f"O coeficiente de x^{m} procurado pela expansão de Leibniz é {c2_mult}")
