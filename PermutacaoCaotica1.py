import itertools

def eh_caotica(p):
    for i, valor in enumerate(p):     # percorre posição (i) e valor do elemento
        if valor == i + 1:            # compara: está na posição original?
            return False              # se sim, não é caótica
    return True                       # se nenhum estava, é caótica

elementos = [1, 2, 3, 4, 5, 6]
todas = list(itertools.permutations(elementos))

caoticas = []

for p in todas:
    if eh_caotica(p):          
        caoticas.append(p)     

#Exibição dos resultados
print("Total de permutações geradas:", len(todas))
print(" ")
print("Exibindo o total de permutações: ")
print(" ")
print(todas)
print("Permutações caóticas encontradas:")
for perm in caoticas:
    print(perm)
print("Quantidade total de permutações caóticas:", len(caoticas))
