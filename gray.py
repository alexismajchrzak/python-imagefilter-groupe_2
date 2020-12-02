import cv2

#print("-------------- gray -----------------")
# je récupère l'image
image = cv2.imread('./imgs/plage.jpg')

def gray_pic(image):
    # j'applique l'effet noir et blanc sur l'image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original image', image)
    cv2.imshow('Gray image', gray)