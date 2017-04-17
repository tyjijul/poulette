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
from reconstruction.spgl1.spgl1 import spgl1, spg_lasso, spg_bp, spg_bpdn, spg_mmv, spgSetParms
from scipy.io.matlab import mio
import scipy.io as sio
from PIL import Image
from matplotlib import pyplot as plt
import scipy.misc
import cv2



def tic():
    #Homemade version of matlab tic and toc functions
    import time
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

def toc():
    import time
    if 'startTime_for_tictoc' in globals():
        print("Elapsed time is " + str(time.time() - startTime_for_tictoc) + " seconds.")
    else:
        print("Toc: start time not set")
        
# % -----------------------------------------------------------
# % Solve the basis pursuit (BP) problem:
# %
# %    minimize ||x||_1 subject to Ax = b
# %
# % -----------------------------------------------------------

def reconstructionSPGL1(PathToIMG, XP_name,M_phi_in, M_signal_in):
    tic()
    print(' Debut Resolution par SPGL1 ')

    taille = 64 # Taille de l'image

    # Chargement de M_phi_use (matrices d'hadamard en lignes) et M_signal (signal de la photodiode)
    #M_phi_use = mio.loadmat('M_phi_use_010.mat')
    M_phi_use = mio.loadmat(M_phi_in)
    #M_signal_use = np.loadtxt('M_signal_use_010.txt')
    M_signal_use = np.loadtxt(M_signal_in)

    M_phi_use = M_phi_use['M_phi_use'] # Cette matrice est definie comme un didctionnaire par Python, on selectionne donc la matrice qui nous interesse

    ###############################################################################
    ## Selection des valeurs "interessantes" aux alentours de la moyenne
    #delta = 12000
    #indice = np.where( np.logical_and( M_signal_use<=(np.mean(M_signal_use) + delta), M_signal_use>=(np.mean(M_signal_use) - delta)));
    #
    #M_signal_use = np.delete(M_signal_use,indice);
    #M_phi_use = np.delete(M_phi_use,indice,0);

    ###############################################################################

    x,resid,grad,info = spg_bp(M_phi_use, M_signal_use)

    x = x.reshape((taille,taille))
    x[0,0] = 0 # Par defaut, on definie le premier pixel comme etant un pixel noir
    #plt.imshow(x)

    # Sauvegarde du fichier
    scipy.misc.imsave(PathToIMG + XP_name + '.jpg', x)
    print(' Fin de la reconstruction ')
    toc()

    return XP_name + '.jpg'


if __name__ == '__main__':
    reconstructionSPGL1('M_phi_use_08.mat', 'M_signal_use_08.txt')
