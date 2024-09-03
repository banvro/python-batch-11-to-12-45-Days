from HandLandmarkModule import MyHandTrackingModule
import cv2

module = MyHandTrackingModule()

capture = cv2.VideoCapture(0)

while True:
    isDone, img = capture.read()

    module.HandDetector(img)
    cv2.imshow("Get Frame", img)

    cv2.waitKey(3)

