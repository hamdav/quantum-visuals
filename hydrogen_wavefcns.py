# By David Hambraeus - https://github.com/hamdav

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import matplotlib.colors as mcolors
from matplotlib.widgets import TextBox
from spherical_harmonics import Ylm

# The convention used is PHI for azimuthal angle and THETA for polar.
def psi_nlm(n, l, m, R, THETA, PHI):
    a = 0.529e-10 # m - bohrs constant
    psi = np.sqrt((2 / (n * a))**3 * np.prod(np.arange(n+l, n-l-1, -1)) / (2*n)) \
        * np.exp(-R/(n*a)) * (2 * R/ (n*a))**l \
        * sp.assoc_laguerre(2*R/(n*a), n-l-1, 2*l+1) \
        * Ylm(l, m, THETA, PHI)
    return PSI


# - - - - Visualization no 1: planes - - - - 
# Should create an animation 

fig, ax = plt.subplots()

