import cv2
import os
import logger



def gray_pic(dossierE, dossierS):
    files = os.listdir(dossierE)
    for f in files:
        img = cv2.imread(f"{dossierE}/{f}")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f"{dossierS}/{f}", gray)
        logger.log(f'gray_pic={f}')
        break
