from gray import gray_pic
from dilatation import dilatation_pic
from blur import blur_pic
import sys
import cv2
import logger

import numpy as np
import os

import numpy
#<<<<<<< Updated upstream

dossierE = "imgs"
dossierS = "ImgsModif"
blur_level = 11

blur_pic(dossierE, dossierS, blur_level)
dilatation_pic(dossierE,dossierS)
gray_pic(dossierS, dossierS)


image = cv2.imread('imgs/image1.jpg')
image_gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('ImgsModif/image1.jpg', image_gray)



logger.dump_log()