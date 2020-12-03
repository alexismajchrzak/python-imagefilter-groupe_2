import cv2
import numpy as np
import os


def dilatation_pic(dossierE, dossierS):
    files = os.listdir(dossierE)
    kernel = np.ones((20, 20), np.uint8)

    for f in files:
        if f.endswith('.jpg'):
            print("1er if (pour .jpg)")
            try:
                print(f)
                img = cv2.imread(f"{dossierE}/{f}")
                dilation = cv2.dilate(img, kernel, 20)
                cv2.imwrite(f"{dossierS}/{f}", dilation)
            except NameError as e:
                print(f"image inexistante, erreur : {e}")
        elif f.endswith('.jpeg'):
            print("elif (pour .jpeg)")
            try:
                print(f)
                img = cv2.imread(f"{dossierE}/{f}")
                dilation = cv2.dilate(img, kernel, 20)
                cv2.imwrite(f"{dossierS}/{f}", dilation)
            except NameError as e:
                print(f"image inexistante, erreur : {e}")
        elif f.endswith('.png'):
            print("2ème elif (pour .png)")
            try:
                print(f)
                img = cv2.imread(f"{dossierE}/{f}")
                dilation = cv2.dilate(img, kernel, 20)
                cv2.imwrite(f"{dossierS}/{f}", dilation)
            except NameError as e:
                print(f"image inexistante, erreur : {e}")
        else:
            print("else   Erreur : Le fichier que vous essayez d'ouvrir n'est pas une image.")
            print(f)
