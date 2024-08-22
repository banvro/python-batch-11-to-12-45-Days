import cv2
import numpy as np

frame = np.zeros((500, 500, 3), dtype = 'uint8')

cv2.line(frame, (100, 50), (100, 400), (60, 247, 47), 3)
cv2.line(frame, (100, 50), (400, 50), (230, 34, 77), 3)
cv2.line(frame, (400, 50), (100, 400), (255, 255, 255), 3)

cv2.putText(frame, "Draw Line", (100, 40), 1, 2, (255, 255, 255), 1)

cv2.imshow("my frame", frame)

cv2.waitKey(0)