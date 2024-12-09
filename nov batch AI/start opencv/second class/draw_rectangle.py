import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")


cv2.rectangle(img, (200, 100), (300, 400), (2, 255, 5), -1)

cv2.circle(img, (300, 400), 100, (120, 230, 100), -1)

cv2.imshow("imgx", img)

cv2.waitKey(0)