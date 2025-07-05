import numpy as np
import cv2

black_screen = np.zeros((700, 800))

cv2.line(black_screen, (100, 100), (500, 600), (10, 255, 34), 3)

cv2.rectangle(black_screen, (50, 60), (500, 500), (10, 45, 23), -1)

img = cv2.imshow("xyz", black_screen)

cv2.waitKey(0)
