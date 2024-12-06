import cv2

capture = cv2.VideoCapture(r"D:\video parts\4828605-uhd_4096_2160_25fps.mp4")

while True:
    is_True, frame = capture.read()

    cv2.imshow("My Video", frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break