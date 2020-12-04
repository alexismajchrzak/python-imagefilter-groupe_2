import cv2
import os
import logger


def blur_pic(dossierE, dossierS, blur_level):
    """
    Applies a blured effect on all the imgs of the directory 'imgs', catching errors
    (such as wrong name, or wrong type of file & wrong blur value (negative or even)) if encountered.
    :param dossierS: the directory from which we get the images to modify
    :param dossierS: the directory where the modified images are saved
    :param blur_level: the blurred level

    """
    if blur_level <= 0 or blur_level % 2 == 0:
        logger.log(f'blur_level invalide : {blur_level}')
    else:

        files = os.listdir(dossierE)
        for f in files:
            if f.endswith('.jpg'):
                print("1er if (pour .jpg)")
                try:
                    print(f)
                    img = cv2.imread(f"{dossierE}/{f}")
                    blur = cv2.GaussianBlur(img, (blur_level, blur_level), cv2.BORDER_DEFAULT)
                    cv2.imwrite(f"{dossierS}/{f}", blur)
                    logger.log(f' blur_pic ={f}')
                except NameError as e:
                    logger.log(f"image inexistante, erreur : {e}")
                    print(f"image inexistante, erreur : {e}")
            elif f.endswith('.jpeg'):
                print("elif (pour .jpeg)")
                try:
                    print(f)
                    img = cv2.imread(f"{dossierE}/{f}")
                    blur = cv2.GaussianBlur(img, (blur_level, blur_level), cv2.BORDER_DEFAULT)
                    cv2.imwrite(f"{dossierS}/{f}", blur)
                    logger.log(f' blur_pic ={f}')
                except NameError as e:
                    logger.log(f"image inexistante, erreur : {e}")
                    print(f"image inexistante, erreur : {e}")
            elif f.endswith('.png'):
                print("2ème elif (pour .png)")
                try:
                    print(f)
                    img = cv2.imread(f"{dossierE}/{f}")
                    blur = cv2.GaussianBlur(img, (blur_level, blur_level), cv2.BORDER_DEFAULT)
                    cv2.imwrite(f"{dossierS}/{f}", blur)
                    logger.log(f' blur_pic ={f}')
                except NameError as e:
                    logger.log(f"image inexistante, erreur : {e}")
                    print(f'image inexistante, erreur : {e}')
            else:
                logger.log("else   Erreur : Le fichier que vous essayez d'ouvrir n'est pas une image.")
                print(f)





