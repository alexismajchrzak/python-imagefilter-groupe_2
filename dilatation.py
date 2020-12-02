import cv2
import gray
import numpy as np

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(gray.image,kernel,iterations = 1)
# print("-------------- dilatation -----------------")
def dilatation_pic(image):
    dilatation = cv2.dilate(gray.image,kernel,iterations = 1)
    cv2.imshow('Image avec dilatation', dilatation)
    print('dilatation image')