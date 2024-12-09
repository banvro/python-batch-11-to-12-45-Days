import cv2

img = cv2.imread('imgx.png')
cv2.imshow("Image", img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grat image", gray_img)

blue_image = cv2.GaussianBlur(gray_img, (49, 49), 0)
cv2.imshow("blue image", blue_image)


detect_edges = cv2.Canny(blue_image, 10, 10)
cv2.imshow("detect_edges", detect_edges)


cv2.waitKey(0)