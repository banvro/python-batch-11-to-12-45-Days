# pip install opencv-python

# pip install opencv-contrib-python

import cv2


# cap = cv2.VideoCapture("3141208-uhd_3840_2160_25fps.mp4")

cap = cv2.imread("Asana3808_Dashboard_Standard.jpg")

# while True:
#     done, frame = cap.read()

cv2.imshow("My Video", cap)

cv2.waitKey(0)