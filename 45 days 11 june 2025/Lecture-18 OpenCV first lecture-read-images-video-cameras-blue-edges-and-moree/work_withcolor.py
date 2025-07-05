import cv2

img = cv2.imread("myimg.jpg")
cv2.imshow("myimg", img)

# to change color
# cvtcolor

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image", gray_img)

hlv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv image", hlv)

cv2.waitKey(0)