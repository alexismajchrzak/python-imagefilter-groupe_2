import cv2
import gray

#print("-------------- blur -----------------")
def blur_pic(image):
    blur = cv2.GaussianBlur(gray.image,(3,3),3)
    cv2.imshow('Image floue', blur)
    print('blur image')