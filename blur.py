import cv2
import os


def blur_pic(dossierE, dossierS):

    files = os.listdir(dossierE)
    for f in files:
        print(f)
        img = cv2.imread(f"{dossierE}/{f}")
        blur = cv2.GaussianBlur(img, (35, 35), cv2.BORDER_DEFAULT)
        cv2.imwrite(f"{dossierS}/{f}", blur)