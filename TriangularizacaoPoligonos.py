# ---------------------------------------------------------
# total de triangulações = C_{n-2} ou ainda T_{n+2} = C_n
# ---------------------------------------------------------
import math
import numpy as np
import matplotlib.pyplot as plt

def catalan(n: int) -> int:
    """C_n = (1/(n+1)) * binom(2n, n)."""
    return math.comb(2*n, n) // (n + 1)

# ------------ Parâmetro: número de vértices ------------
n_polygon = 7  # n >= 3
# -------------------------------------------------------

# Total de triangulações
total = catalan(n_polygon - 2)

# Coordenadas de um polígono regular no círculo unitário
theta = np.linspace(0, 2*np.pi, n_polygon, endpoint=False)
R = 1.0
xs = R * np.cos(theta)
ys = R * np.sin(theta)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal', 'box')

# 1) Desenha a borda do polígono
for i in range(n_polygon):
    j = (i + 1) % n_polygon
    ax.plot([xs[i], xs[j]], [ys[i], ys[j]], linewidth=2)

# 2) Desenha uma triangulação válida (a partir do vértice 0)
root = 0
for k in range(2, n_polygon - 1):
    ax.plot([xs[root], xs[k]], [ys[root], ys[k]], linewidth=1)

ax.set_title(
    f"Triangulação de um {n_polygon}-gono\n"
    f"Número total de triangulações = C_{n_polygon-2} = {total}"
)
ax.axis('off')
plt.tight_layout()
plt.show()
