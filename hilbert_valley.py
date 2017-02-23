import matplotlib.pyplot as plt
# These use my repo's python scripts. See bbusemeyer on github for them.
try:
  import plot_tools as pt
  pt.matplotlib_header() 
except ImportError:
  pass 

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

def valley(x,y):
  return 0.5*x**6 + abs(2*y)**2 + 0.2*np.sin(5*x) + 0.1*np.sin(3*y)

# Domain
X = np.linspace(-1,1, 200)
Y = np.linspace(-0.5,0.5, 200)

# Plot a surface.
Xm, Ym = np.meshgrid(X, Y)
Z = valley(Xm,Ym)
surf = ax.plot_surface(Xm, Ym, Z, cmap=cm.jet, vmax=1,alpha=0.5,
                       linewidth=0.01, antialiased=False)

## Lines along the surface.
#Xp=-0.5*X**2+0.7 # Excited state DMC optimization.
Xp=0.8*X**3-0.2 # Ground state DMC optimization.
Xp=0.4*X**3-0.6 # Another state DMC optimization.
Yp=Y
PC=[valley(x,y) for x,y in zip(Xp,Yp)]
line = ax.plot(Xp,Yp,PC,'k',linewidth=2)

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
