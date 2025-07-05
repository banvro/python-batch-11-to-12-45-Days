import cv2

img = cv2.imread("myimg.jpg")

cv2.putText(img, "this is hellow owrld", (100, 100), 1, 2.0, (10, 240, 30), 2)

cv2.imshow("myimg", img)


cv2.waitKey(0)