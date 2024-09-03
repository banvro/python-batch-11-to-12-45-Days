import cv2
import numpy as np

# (h, w, c)
frame = np.zeros((500, 600, 3), dtype = "uint8")

cv2.rectangle(frame, (100, 100), (300, 350), (73, 252, 3), -1)

cv2.circle(frame, (300, 350), 80, (252, 3, 206), -1)



cv2.imshow("My Frame", frame)

cv2.waitKey(0)








