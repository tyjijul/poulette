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

import cv2
from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np


def analyse_block(name_img):
    # % -----------------------------------------------------------
    # Debut du traitement de l'image pour comptage des bacteries
    # % -----------------------------------------------------------

    im = cv2.imread(name_img)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) # mise en couleur de l'image
    gray = cv2.GaussianBlur(gray, (5,5), 0) # lissage gaussien de l'image
    im_thresholded = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, -5) # image binarisee et mise en place des contours
    labelarray, particle_count = ndimage.measurements.label(im_thresholded) # comptage du nombre de contour

    print("Le nombre de particule est :", particle_count) # Affichage du resultat

    # Affichage des images
    # titles = ['Image originale', 'Image lissee', 'Image binarisee pour comptage']
    # images = [im, gray, im_thresholded]
    # plt.figure(1)
    # for i in xrange(3):
    #     plt.subplot(1,3,i+1),plt.imshow(images[i])
    #     plt.title(titles[i])
    #     plt.xticks([]),plt.yticks([])
    # plt.show()

    # % --------------------------------------------------------------------------
    # Separation de l'image et analyse, binarisation et selection en 16 blocks
    # % --------------------------------------------------------------------------

    print(' Analyse de l image par block ')

    num = 16 # nombre de blocks dont sera composee l'image fragmentee
    pas = int(np.sqrt(num))

    j = 0
    coordonnee = np.zeros((num, 2))
    compt = 0 #coompteur de bloks a analyser

    for k in range(pas):
        i=0
        for l in range(pas):
            a = im_thresholded[i:i+num, j: j+num]
            if np.any(a == 255) == True:
                print ('%s %d %d %s' % ('block', i, j, 'a analyser'))
                coordonnee[compt, 0] = i #releve de l'abscisse du block
                coordonnee[compt, 1] = j #releve de l'ordonnee du block
                compt = compt + 1
            i = i + num
        j = j + num

    # % --------------------------------------------------------------------------
    # Separation de l'image et analyse, binarisation et selection en 64 blocks
    # % --------------------------------------------------------------------------

    #print(' Analyse de l image par block ')
    #
    #num = 64 # nombre de blocks dont sera composee l'image fragmentee
    #pas = int(np.sqrt(num))
    #
    #j = 0
    #for k in range(pas):
    #    i=0
    #    for l in range(pas):
    #        a = im_thresholded[i:i+pas, j: j+pas]
    #        if np.any(a == 255) == True:
    #            print ('%s, %d, %d, %s' % ('block', i, j, 'a analyser'))
    #            coordonnee[compt, 0] = i #releve de l'abscisse du block
    #            coordonnee[compt, 1] = j #releve de l'ordonnee du block
    #            compt = compt + 1  
    #        i = i + pas
    #    j = j + pas

    coordonnee = coordonnee[:compt, :]
    print('%s %d' % ('nombre de blocks a analyser =', compt))
    print('%s'% ('coordonnees des blocks a analyser :'))
    print(coordonnee)

    return coordonnee



if __name__ == '__main__':
    analyse_block('Image_billes_couronne.jpg')


