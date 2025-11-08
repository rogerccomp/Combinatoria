import math
import matplotlib.pyplot as plt

# Parâmetros (você pode alterar):
n_objetos = 50   # quantidade de objetos (pombos)
n_caixas = 12     # quantidade de caixas (casas)

# Cálculo do pior caso (distribuição mais uniforme possível)
base = n_objetos // n_caixas
resto = n_objetos % n_caixas
contagens = [base + (1 if i < resto else 0) for i in range(n_caixas)]

# Prepara dados para o gráfico
xs = list(range(n_caixas))
ys = contagens

# Limite garantido pelo Princípio da Casa dos Pombos
limite = math.ceil(n_objetos / n_caixas)

plt.figure(figsize=(8,4))
plt.bar(xs, ys, edgecolor="black")
plt.axhline(limite, linestyle="--", linewidth=1)  # linha mostrando o limite garantido

plt.title(f"{n_objetos} objetos distribuídos em {n_caixas} caixas — Pior Caso\n"
          f"máx = ceil({n_objetos}/{n_caixas}) = {limite}")
plt.xlabel("Caixa (índice)")
plt.ylabel("Número de objetos")

# Exibe os valores numéricos acima das barras
for x, y in zip(xs, ys):
    plt.text(x, y + 0.1, str(y), ha='center', va='bottom', fontsize=10)

plt.ylim(0, max(ys) + 1)
plt.tight_layout()
plt.show()
