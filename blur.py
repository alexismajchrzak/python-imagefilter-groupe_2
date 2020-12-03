import cv2
import os
import logger


def blur_pic(dossierE, dossierS):

    files = os.listdir(dossierE)
    for f in files:
        img = cv2.imread(f"{dossierE}/{f}")
        blur = cv2.GaussianBlur(img, (35, 35), cv2.BORDER_DEFAULT)
        cv2.imwrite(f"{dossierS}/{f}", blur)
        logger.log(f' blur_pic ={f}')
        break

