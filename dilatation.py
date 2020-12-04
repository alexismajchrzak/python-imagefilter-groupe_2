import cv2
import numpy as np
import os
import logger


def dilatation_pic(dossierE, dossierS, dilate_level):
    """
    Applies a dilatation effect on all img from the directory "imgs", catching errors (such as wrong name, or wrong type of file) if encountered
        :param dossierE: the directory from which we get the images to modify
        :param dossierS: the directory where the modified images are saved

    """
    files = os.listdir(dossierE)
    kernel = np.ones((dilate_level, dilate_level), np.uint8)
    for f in files:
        if f.endswith('.jpg'):
            print("1er if (pour .jpg)")
            try:
                print(f)
                img = cv2.imread(f"{dossierE}/{f}")
                dilation = cv2.dilate(img, kernel, 20)
                cv2.imwrite(f"{dossierS}/{f}", dilation)
                logger.log(f'dilatation_pic={f}')
            except NameError as e:
                print(f"image inexistante, erreur : {e}")
                logger.log(f"image inexistante, erreur : {e}")
        elif f.endswith('.jpeg'):
            print("elif (pour .jpeg)")
            try:
                print(f)
                img = cv2.imread(f"{dossierE}/{f}")
                dilation = cv2.dilate(img, kernel, 20)
                cv2.imwrite(f"{dossierS}/{f}", dilation)
                logger.log(f'dilatation_pic={f}')
            except NameError as e:
                print(f"image inexistante, erreur : {e}")
                logger.log(f"image inexistante, erreur : {e}")
        elif f.endswith('.png'):
            print("2ème elif (pour .png)")
            try:
                print(f)
                img = cv2.imread(f"{dossierE}/{f}")
                dilation = cv2.dilate(img, kernel, 20)
                cv2.imwrite(f"{dossierS}/{f}", dilation)
                logger.log(f'dilatation_pic={f}')
            except NameError as e:
                print(f"image inexistante, erreur : {e}")
                logger.log(f"image inexistante, erreur : {e}")
        else:
            print("else   Erreur : Le fichier que vous essayez d'ouvrir n'est pas une image.")
            logger.log("else   Erreur : Le fichier que vous essayez d'ouvrir n'est pas une image.")
            print(f)


