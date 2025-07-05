import cv2

cap = cv2.VideoCapture(0)

while True:
    x, frame = cap.read()
    cv2.imshow("video", frame)

    black_vid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray_video", black_vid)

    blur = cv2.GaussianBlur(frame, (15, 15), 0)
    cv2.imshow("blue video", blur)

    edges = cv2.Canny(frame, 200, 200)
    cv2.imshow("edges video", edges)

    if cv2.waitKey(20) & 0xff == ord("q"):
        break