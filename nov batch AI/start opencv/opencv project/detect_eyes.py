import cv2
import time

import cv2.data

capture = cv2.VideoCapture(0)

nft = 0
pft = 0

while True:
    is_Ture, framex = capture.read()

    gray_img = cv2.cvtColor(framex, cv2.COLOR_BGR2GRAY)

    face_dector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    faces = face_dector.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors = 3, minSize = (30, 30))


    for (x, y, w, h) in faces:
        cv2.rectangle(framex, (x, y), (w+x, h+y), (4, 255, 80), 4)

    nft = time.time()
    fps = 1 / (nft - pft)
    pft = nft

    cv2.putText(framex, f"fps value : {fps}", (30, 20), 1, 2, (0, 255, 3), 3)

    cv2.imshow("my video", framex)

    if cv2.waitKey(20) & 0xff == ord("x"):
        break


# mediapipe