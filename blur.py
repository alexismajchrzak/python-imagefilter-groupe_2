import cv2
import os


def blur_pic(dossierE, dossierS):

    files = os.listdir(dossierE)
    for f in files:
        if f.endswith('.jpg'):
            print("1er if (pour .jpg)")
            try:
                print(f)
                img = cv2.imread(f"{dossierE}/{f}")
                blur = cv2.GaussianBlur(img, (30, 30), cv2.BORDER_DEFAULT)
                cv2.imwrite(f"{dossierS}/{f}", blur)
            except NameError as e:
                print(f"image inexistante, erreur : {e}")
        elif f.endswith('.jpeg'):
            print("elif (pour .jpeg)")
            try:
                print(f)
                img = cv2.imread(f"{dossierE}/{f}")
                blur = cv2.GaussianBlur(img, (35, 35), cv2.BORDER_DEFAULT)
                cv2.imwrite(f"{dossierS}/{f}", blur)
            except NameError as e:
                print(f"image inexistante, erreur : {e}")
        elif f.endswith('.png'):
            print("2ème elif (pour .png)")
            try:
                print(f)
                img = cv2.imread(f"{dossierE}/{f}")
                blur = cv2.GaussianBlur(img, (35, 35), cv2.BORDER_DEFAULT)
                cv2.imwrite(f"{dossierS}/{f}", blur)
            except NameError as e:
                print(f"image inexistante, erreur : {e}")
        else:
            print("else   Erreur : Le fichier que vous essayez d'ouvrir n'est pas une image.")
            print(f)
