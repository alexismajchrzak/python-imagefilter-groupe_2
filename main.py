import cv2

image1 = cv2.imread('imgs/img1.jpeg')
gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)


cv2.imwrite('imgsModif/img1.jpeg', gray)



