import cv2

img = cv2.imread("imgx.png")

cv2.imshow("image", img)

blured_image = cv2.GaussianBlur(img, (89, 89), 0)

cv2.imshow("blured image", blured_image)

cv2.waitKey(0)