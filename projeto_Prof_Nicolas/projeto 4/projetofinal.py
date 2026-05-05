import trimesh
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# LOAD MODEL 
mesh = trimesh.load('Female Head.obj', process=True)

# corrigir orientação
R = trimesh.transformations.rotation_matrix(
    np.radians(90),
    [1, 0, 0]
)
mesh.apply_transform(R)

# centralizar e normalizar
mesh.vertices -= mesh.center_mass
mesh.vertices /= mesh.scale

base = mesh.vertices
faces = mesh.faces

# CAMADAS
bone = base * 0.95
muscle = base * 0.98
skin = base

# FIGURA
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

def draw(v, color, alpha, z):
    ax.plot_trisurf(
        v[:,0], v[:,1], v[:,2],
        triangles=faces,
        color=color,
        linewidth=0,
        shade=True,
        antialiased=True,
        alpha=alpha,
        zorder=z
    )

def update(frame):
    ax.clear()

    ax.set_facecolor("black")
    fig.patch.set_facecolor("black")

    ax.set_proj_type('persp')
    ax.computed_zorder = False

    # ordem correta (interno → externo)
    draw(bone,   (0.9, 0.9, 0.9), 1.0, 1)   # osso (opaco)
    draw(muscle, (0.8, 0.2, 0.2), 0.8, 2)   # músculo
    draw(skin,   (0.6, 0.4, 0.2), 0.9, 3)   # pele

    ax.view_init(elev=20, azim=frame)
    ax.set_axis_off()
    ax.set_box_aspect([1,1,1])

# MEDIR TEMPO DE RENDER
start_time = time.time()

ani = FuncAnimation(fig, update, frames=60, interval=30)

ani.save("female_head_layers.gif", writer="pillow", fps=30)

end_time = time.time()

print(f"Tempo de renderização: {end_time - start_time:.2f} segundos")

plt.show()