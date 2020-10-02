import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')

xs = np.linspace(-1,1)
ys = np.linspace(-1,1)
zs = np.linspace(-1,1,4)
X, Y, Z = np.meshgrid(xs, ys, zs)
F = X**2 + Y**2 + Z**2

# Plot contour curves
cset = ax.contour(X, Y, Z, cmap=cm.coolwarm)

ax.clabel(cset, fontsize=9, inline=1)

plt.show()
