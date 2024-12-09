import cv2

img = cv2.imread("imgx.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("image", gray_img)

invert_img = 255 - gray_img
# cv2.imshow("invert image", invert_img)

blur_img = cv2.GaussianBlur(invert_img, (49, 49), 0)

invert_blur = 255 - blur_img

satch = cv2.divide(gray_img, invert_blur, scale = 150)
cv2.imshow("satch image", satch)

cv2.imwrite("image_sketch.png", satch)

cv2.waitKey(0)