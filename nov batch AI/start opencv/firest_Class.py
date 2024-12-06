# OpenCV ---> computer vission Library

# basic:
#     image ---> read 
#     video ---> read()

#     web cam ---> read


# Projects ---> face detect
# eyes detection


# Hand Detect ----> mediapipe


# read images 


# pip install opencv-contrib-python 


import cv2

img = cv2.imread("myimags/hey.jpg")

cv2.putText(img, "Hellow Word", (400, 100), 1, 3, (125, 250, 80), 5)

cv2.imshow("My Image", img)

cv2.waitKey(0)










