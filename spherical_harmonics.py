import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import matplotlib.colors as mcolors
from matplotlib.widgets import TextBox

plt.style.use('seaborn-darkgrid')


# Resultion is the number of points per 2*pi radians
# Higher numbers give prettier plots but slower interactions
# I am able to smoothly rotate plots with a resolution of around 40-50
# but this probably varies with the beefyness of your computer
resolution = 100


# Function returning grid of angles and radii given order and degree
def Ylm(l, m, n_points=40):
    theta, phi = np.linspace(0, np.pi, int(n_points/2)), np.linspace(0, 2 * np.pi, n_points)
    THETA, PHI = np.meshgrid(theta, phi)
    R = np.abs(np.sqrt((2*l+1)/(4*np.pi * np.prod(np.arange(l+m, l-m, -1)))) * np.exp(1j * m * PHI) * sp.lpmv(m, l, np.cos(THETA)))
    return R, PHI, THETA


# Converts spherical gridvalues to cartesian
def spherical_to_cart(R, PHI, THETA):
    X = R * np.sin(PHI) * np.cos(THETA)
    Y = R * np.sin(PHI) * np.sin(THETA)
    Z = R * np.cos(PHI)
    return X, Y, Z


# Create figure and axis
fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
# Make room for textboxes
plt.subplots_adjust(bottom=0.2)

# Choose the initial values for the plot and boxes
l_init, m_init = 0, 0

# Calculate the initial surface
R, PHI, THETA = Ylm(l_init, m_init)
X, Y, Z = spherical_to_cart(R, PHI, THETA)

# Create a colomap
cmap = plt.get_cmap('rainbow')
# Create a color norming function
norm = mcolors.Normalize(vmin=R.min(), vmax=R.max())
# Plot the initial surface
plot = ax.plot_surface(
    X, Y, Z, rstride=1, cstride=1, facecolors=cmap(norm(R)), 
    linewidth=0, antialiased=False, alpha=0.5)
ax.set_title(r'$\ell = 0, m=0$')

# Hide grid and axis
ax.grid(False)
ax.axis('off')

def update(_):
    l = int(l_text_box.text)
    m = int(m_text_box.text)
    # Check that the l and m are appropriate
    if l < abs(m) or l < 0:
        ax.clear()
        ax.set_title("INVALID")
        ax.grid(False)
        ax.axis('off')
        # Draw is needed to immediately update the axis
        # Otherwise it won't show until you hover over the plot
        plt.draw()
    else:
        ax.set_title(r'$\ell = $' + str(l) + r'$,m=$' + str(m) + ' Loading...')
        plt.draw()
        # Calculate the new surface from the inputted l and m
        R, PHI, THETA = Ylm(l, m, resolution)
        X, Y, Z = spherical_to_cart(R, PHI, THETA)
        # Create a new normalization as the R has change
        norm = mcolors.Normalize(vmin=R.min(), vmax=R.max())
        ax.clear()
        plot = ax.plot_surface(
            X, Y, Z, rstride=1, cstride=1, facecolors=cmap(norm(R)), 
            linewidth=0, antialiased=False, alpha=0.5)
        # Hide grid and axis
        ax.grid(False)
        ax.axis('off')
        ax.set_title(r'$\ell = $' + str(l) + r'$,m=$' + str(m))
        # Draw is needed to immediately update the axis
        # Otherwise it won't show until you hover over the plot
        plt.draw()


# Create the text boxes used to input l and m
laxbox = plt.axes([0.1, 0.05, 0.1, 0.075])
l_text_box = TextBox(laxbox, r'$\ell$  ', initial=l_init)
l_text_box.on_submit(update)

maxbox = plt.axes([0.5, 0.05, 0.1, 0.075])
m_text_box = TextBox(maxbox, r'$m$   ', initial=m_init)
m_text_box.on_submit(update)


plt.show()
