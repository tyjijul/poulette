"""
##############################################################################
## MICROBS - Comptage et cartographie des bacteries
##############################################################################

17.02.2017 : creation ELepine
22.02.2017 : amelioration ELepine

DESCRIPTION
Ce programme a pour objectif de traiter les images de bacteries reconstruites
par les algorithmes SPGL1 et NESTA et de compter le nombre de bacteries.
##############################################################################
"""

from scipy import ndimage
import scipy
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
from PIL import Image
import skimage
from skimage import filters

n = 64

# % -----------------------------------------------------------
# Debut du traitement de l'image pour comptage des bacteries
# % -----------------------------------------------------------
def analyse_block2(name_img):
    im = Image.open(name_img)
    im = np.array(im)

    # gray = skimage.filters.median(im)
    #gray = scipy.ndimage.filters.gaussian_filter(im, 1)
    gray = scipy.ndimage.filters.median_filter(im, 5)

    #gray = gray.astype(int)

    seuil = skimage.filters.threshold_otsu(gray)
    im_thresholded = gray > seuil

    gray = np.uint8(gray)

    labelarray, particle_count = ndimage.measurements.label(im_thresholded) # comptage du nombre de contour

    print("Le nombre de particule est :", particle_count )# Affichage du resultat

    # # Affichage des images
    # titles = ['Image originale', 'Image lissee', 'Image binarisee pour comptage']
    # images = [im, gray, im_thresholded]
    # plt.figure(1)
    # for i in range(3):
    #     plt.subplot(1,3,i+1),plt.imshow(images[i])
    #     plt.title(titles[i])
    #     plt.xticks([]),plt.yticks([])
    # plt.show()

    # % --------------------------------------------------------------------------
    # Separation de l'image et analyse, binarisation et selection en 256 blocks
    # % --------------------------------------------------------------------------

    print(' Analyse de l image par block ')

    num = 64 # nombre de blocks dont sera composee l'image fragmentee
    pas = 16

    j = 0
    coordonnee = np.zeros((num, 2))
    compt = 0 #coompteur de bloks a analyser

    for k in range(num):
        i=0
        for l in range(num):
            if np.any(im_thresholded[i:i+pas, j: j+pas] == True):
                print ('%s %d %d %s' % ('block', i, j, 'a analyser'))
                coordonnee[compt, 0] = i #releve de l'abscisse du block
                coordonnee[compt, 1] = j #releve de l'ordonnee du block
                compt = compt + 1
            i = i + pas
        j = j + pas

    coordonnee = coordonnee[:compt, :]
    print('%s %d' % ('nombre de blocks a analyser =', compt))
    print('%s'% ('coordonnees des blocks a analyser :'))
    print(coordonnee)
    return(coordonnee)

if __name__ == '__main__':
    analyse_block2('Image_billes_couronne.jpg')




