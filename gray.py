import cv2
import os



def gray_pic(dossierE, dossierS):
    files = os.listdir(dossierE)
    for f in files:
        print(f)
        img = cv2.imread(f"{dossierE}/{f}")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f"{dossierS}/{f}", gray)
