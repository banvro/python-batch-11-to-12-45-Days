import cv2
from HandLandmarkModule import MyHandTrackingModule

capture = cv2.VideoCapture(0)
HandModule = MyHandTrackingModule()

while True:
    isDone, frame = capture.read()

    HandModule.HandDetector(frame)

    landmarkPoints = HandModule.HandCordinates(frame)
    # print(landmarkPoints, "ee")

    if landmarkPoints:
        if landmarkPoints[8][2] < landmarkPoints[6][2]:
            print("Hand open")
        else:
            print("Hand Close")

    cv2.imshow("Check hand open or close", frame)

    if cv2.waitKey(3) & 0xff == ord("q"):
        break