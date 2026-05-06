import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LightSource

#gerar dados
x = np.linspace(-5, 5, 300)
y = np.linspace(-5, 5, 300)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

#luz efeito de relevo
ls = LightSource(azdeg=315, altdeg=45)
rgb = ls.shade(Z, cmap=plt.cm.plasma)

#criar grafico 3d
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(
    X, Y, Z,
    facecolors=rgb,
    linewidth=0,
    alpha=0.95,
    shade=False
)
z_offset = Z.min() - 0.5
levels = np.linspace(-1, 1, 40)
ax.contour(X, Y, Z,levels=levels,zdir='z',offset=0,cmap='plasma',linewidths=1.2)

# Ajustes
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.set_zlabel("Eixo Z")
ax.set_zlim(z_offset, Z.max())

plt.tight_layout()
plt.savefig("projeto_Prof_Nicolas/projeto_3/img3.png", dpi=300)
plt.show()
