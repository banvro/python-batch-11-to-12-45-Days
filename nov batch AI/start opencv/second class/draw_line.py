import cv2
import numpy as np

img = np.zeros((700, 700, 3), dtype = "uint8")

cv2.line(img, (200, 200), (500, 500), (255, 34, 23), 5)

cv2.line(img, (100, 100), (600, 100), (3, 252, 65), 10)

cv2.imshow("blank image", img)

cv2.waitKey(0)



# BGR 