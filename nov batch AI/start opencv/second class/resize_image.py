# read images

import cv2

img = cv2.imread("pexels-pixabay-45201.jpg")

resized_image = cv2.resize(img, (400, 400))

cv2.imshow("cat", img)

cv2.imshow("resized image", resized_image)

cv2.waitKey(0)