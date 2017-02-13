import matplotlib.pyplot as plt
# These use my repo's python scripts. See bbusemeyer on github for them.
#import plot_tools as pt
#pt.matplotlib_header() 

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.linspace(-1,1, 200)
Y = np.linspace(-0.5,0.5, 200)
X, Y = np.meshgrid(X, Y)
Z = 0.5*X**6 + abs(2*Y)**2 + 0.2*np.sin(5*X) + 0.1*np.sin(3*Y)


## Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.jet, vmax=1,alpha=0.5,
                       linewidth=0.01, antialiased=False)
# Plot the surface.
#surf = ax.plot_wireframe(X, Y, Z, cmap=cm.jet,
#                       linewidth=0.01, antialiased=False)

# Customize the z axis.
ax.set_ylim(-1.0,1.0)
ax.set_xticklabels(())
ax.set_yticklabels(())
ax.set_zticklabels(())
#ax.set_zlim(0,1)
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
#fig.colorbar(surf, shrink=0.5, aspect=5,label='$E-E_0$')
ax.set_xlabel(r"$p_i$",size='large')
ax.set_ylabel(r"$p_j$",size='large')
ax.set_zlabel(r"$\langle \Psi| \mathcal{H} |\Psi \rangle$",size='large')

fig.tight_layout()
plt.show()
