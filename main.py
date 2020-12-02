import cv2
import numpy as np
import os

dossierE = "imgs"
dossierS = "ImgsModif"
files = os.listdir(dossierE)

for f in files:
    img = cv2.imread(f"{dossierE}/{f}")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img, (35, 35), cv2.BORDER_DEFAULT)
    kernel = np.ones((20, 20), np.uint8)
    dilation = cv2.dilate(img, kernel, 20)
    cv2.imwrite(f"{dossierS}/{f}", dilation)




