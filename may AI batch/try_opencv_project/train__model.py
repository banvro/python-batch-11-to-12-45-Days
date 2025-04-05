import cv2

zx = cv2.VideoCapture(0) 

while True:
    isDOne, frame = zx.read()

    cv2.imshow("my cam video", frame)

    if cv2.waitKey(20) & 0xff == ord("x"):
        break