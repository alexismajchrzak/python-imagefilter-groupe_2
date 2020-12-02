import cv2
import gray
import blur
import dilatation

gray.gray_pic(gray.image)
blur.blur_pic(gray.image)
dilatation.dilatation_pic(gray.image)

cv2.waitKey(0)
cv2.destroyAllWindows()


