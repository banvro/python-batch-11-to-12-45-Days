import cv2

img = cv2.imread("imgx.png")
cv2.imshow("image", img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image", gray_img)

hsv_color = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv color", hsv_color)


cv2.waitKey(0)