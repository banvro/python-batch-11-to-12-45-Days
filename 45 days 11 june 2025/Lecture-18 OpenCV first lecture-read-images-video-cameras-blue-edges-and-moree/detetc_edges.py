import cv2

img = cv2.imread("myimg.jpg")
cv2.imshow("orignal image", img)

detect_edges = cv2.Canny(img, 100, 100)
cv2.imshow("oignal image edges", detect_edges)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image", gray_img)

detect_edges_gray = cv2.Canny(gray_img, 300, 300)
cv2.imshow("gray image edges", detect_edges_gray)

cv2.waitKey(0)