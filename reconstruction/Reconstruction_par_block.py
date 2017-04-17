"""
##############################################################################
## MICROBS - COMPRESSIVE SENSING
##############################################################################

19.01.2017 : creation ELepine

DESCRIPTION


Entree :
    - La  taille de la matrice Phi
    
Sortie :
    - ".mat" MATLAB de la matrice contenant les pattern utilises pour la
      modulation spatiale
    - ".txt" contenant les signaux PhD pour chaque patterns
    
##############################################################################
"""

import numpy as np
from time import time
from spgl1.spgl1 import spgl1, spg_lasso, spg_bp, spg_bpdn, spg_mmv, spgSetParms
from scipy.io.matlab import mio
import scipy.io as sio
from PIL import Image
from matplotlib import pyplot as plt
import scipy.misc
import cv2


        
# % -----------------------------------------------------------
# % Solve the basis pursuit (BP) problem:
# %
# %    minimize ||x||_1 subject to Ax = b
# %
# % -----------------------------------------------------------

print(' Debut Resolution par SPGL1 ')

nb = 388 # nombre de patterns en partant de 0
taille = 64 # Taille de l'image

# Chargement de M_phi_use (matrices d'hadamard en lignes) et M_signal (signal de la photodiode)
M_phi_use = mio.loadmat('M_phi_use_08.mat')
M_signal_use = np.loadtxt('M_signal_use_08.txt')


M_phi_use = M_phi_use['M_phi_use'] # Cette matrice est definie comme un didctionnaire par Python, on selectionne donc la matrice qui nous interesse

l = 0

for k in range(compt):
    
    print('%s %d %s' %('Debut Resolution numero', k, 'par SPGL1'))
    
    M_signal = M_signal_use[l: l + nb]
    
    x,resid,grad,info = spg_bp(M_phi_use, M_signal)
    
    x = x.reshape((taille,taille))
    x[0,0] = 0 # Par defaut, on definie le premier pixel comme etant un pixel noir
    
    # Sauvegarde du fichier
    scipy.misc.imsave('%s %d %s' %('Image_block', k, '.jpg'), x)
    
    l = l + nb

print(' Fin de la reconstruction ')


