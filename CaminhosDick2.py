# dyck_paths_all_gif_pillow.py
# -----------------------------------------------------------
# Gera TODOS os caminhos de Dyck (R,U) com y<=x em grade n×n,
# cria contact sheet e GIF animado. Sem imageio (só Pillow).
# -----------------------------------------------------------

import os
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def catalan(n:int)->int:
    return math.comb(2*n, n)//(n+1)

def enumerate_dyck_paths(n:int):
    """Lista TODOS os caminhos de Dyck (strings de R/U) mantendo y<=x."""
    paths=[]
    def bt(x,y,path):
        if x==n and y==n:
            paths.append(''.join(path)); return
        if x<n:
            path.append('R'); bt(x+1,y,path); path.pop()
        if y<n and (y+1)<=x:
            path.append('U'); bt(x,y+1,path); path.pop()
    bt(0,0,[])
    return paths

def path_to_coords(steps):
    x=y=0; X=[x]; Y=[y]
    for s in steps:
        if s=='R': x+=1
        else: y+=1
        X.append(x); Y.append(y)
    return X,Y

def draw_dyck_path(n, steps, ax=None, title=None):
    created=False
    if ax is None:
        fig, ax = plt.subplots(figsize=(5,5)); created=True
    ax.set_aspect('equal', 'box')

    # grade
    for i in range(n+1):
        ax.plot([0,n],[i,i], linewidth=0.7)
        ax.plot([i,i],[0,n], linewidth=0.7)

    # diagonal y=x
    ax.plot([0,n],[0,n], linewidth=2)

    # caminho
    X,Y = path_to_coords(steps)
    ax.plot(X,Y, linewidth=3)
    ax.scatter(X,Y, s=18)

    ax.set_xlim(-0.2, n+0.2); ax.set_ylim(-0.2, n+0.2)
    ax.set_xticks(range(n+1)); ax.set_yticks(range(n+1))
    if title: ax.set_title(title)
    if created:
        plt.tight_layout()
        return fig, ax

def build_all_dyck_visuals(
    n:int=6,
    frame_ms:int=250,
    keep_pngs:bool=False,
    make_contact_sheet:bool=True,
    make_gif:bool=True,
    cols_contact:int=6,
    dpi:int=150
):
    out_dir = f"dyck_paths_n{n}"
    os.makedirs(out_dir, exist_ok=True)

    paths = enumerate_dyck_paths(n)
    paths.sort()
    total = len(paths)
    print(f"n={n} -> total = {total} (Catalan C_{n} = {catalan(n)})")

    # 1) Renderiza cada caminho para PNG (frames)
    frame_paths=[]
    for idx, steps in enumerate(paths, start=1):
        fig, ax = plt.subplots(figsize=(5,5))
        draw_dyck_path(n, steps, ax=ax, title=f"{idx}/{total}")
        fig.tight_layout()
        fpath = os.path.join(out_dir, f"frame_{idx:03d}.png")
        fig.savefig(fpath, dpi=dpi)
        plt.close(fig)
        frame_paths.append(fpath)

    # 2) Contact sheet (opcional)
    contact_path=None
    if make_contact_sheet:
        rows = math.ceil(total/cols_contact)
        fig_w = cols_contact*2.6
        fig_h = rows*2.6
        fig, axes = plt.subplots(rows, cols_contact, figsize=(fig_w, fig_h))
        # >>> FIX robusto: achata axes, independentemente de rows/cols
        axes = np.atleast_1d(axes).ravel()
        # limpa
        for ax in axes:
            ax.axis('off')
        # desenha
        for i, steps in enumerate(paths):
            draw_dyck_path(n, steps, ax=axes[i], title=str(i+1))
        plt.tight_layout()
        contact_path = os.path.join(out_dir, f"contact_sheet_n{n}.png")
        fig.savefig(contact_path, dpi=150)
        plt.close(fig)

    # 3) GIF animado (opcional) usando **apenas Pillow**
    gif_path=None
    if make_gif:
        images = [Image.open(p).convert("P", palette=Image.ADAPTIVE) for p in frame_paths]
        gif_path = os.path.join(out_dir, f"dyck_paths_n{n}.gif")

        # Se quiser animação "ping-pong", descomente as 3 linhas abaixo:
        # back = images[-2:0:-1]         # todos menos o primeiro/último para não duplicar
        # images = images + back
        # frame_ms = frame_ms            # (mesma duração)

        images[0].save(
            gif_path,
            save_all=True,
            append_images=images[1:],
            duration=frame_ms,
            loop=0,
            optimize=False
        )

    # 4) Limpa frames se não quiser manter
    if not keep_pngs:
        for p in frame_paths:
            try: os.remove(p)
            except OSError: pass

    return {"dir": out_dir, "count": total, "gif": gif_path, "contact": contact_path}

# Exemplo de uso:
if __name__ == "__main__":
    info = build_all_dyck_visuals(
        n=6,                # troque para 4, 5, 6, ...
        frame_ms=250,       # duração por quadro do GIF (ms)
        keep_pngs=False,    # True para manter PNGs dos frames
        make_contact_sheet=True,
        make_gif=True
    )
    print(info)
    