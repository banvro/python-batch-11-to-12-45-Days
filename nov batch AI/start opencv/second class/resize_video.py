import cv2

capture = cv2.VideoCapture("videoo.mp4")

while True:
    x, y = capture.read()

    resized_fram = cv2.resize(y, (500, 500))

    cv2.imshow("my video", y)

    cv2.imshow("resized video", resized_fram)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break