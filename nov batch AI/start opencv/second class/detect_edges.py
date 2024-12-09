import cv2

img = cv2.imread('imgx.png')

cv2.imshow("Image", img)

detect_edges = cv2.Canny(img, 100, 100)
cv2.imshow("detect_edges", detect_edges)


cv2.waitKey(0)