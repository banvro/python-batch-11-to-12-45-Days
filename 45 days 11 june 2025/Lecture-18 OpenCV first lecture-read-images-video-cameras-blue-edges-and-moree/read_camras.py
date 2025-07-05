import cv2

cap = cv2.VideoCapture(0)

while True:
    is_True, frame = cap.read()

    cv2.imshow("myvideo", frame)

    if cv2.waitKey(20) & 0xff == ord("x"):
        break

    cv2.waitKey(20)