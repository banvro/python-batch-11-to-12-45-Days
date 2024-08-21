import cv2

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("3141208-uhd_3840_2160_25fps.mp4")

while True:
    done, frame = cap.read()

    # cv2.putText(frame, "My Camera", (10, 10), 10, 4, (52, 250, 250), 4)

    cv2.putText(frame, "My Cat", (50, 150), 20, 3, (51, 245, 29), 10, cv2.FONT_ITALIC)

    cv2.imshow("Start Cemra", frame)

    if cv2.waitKey(20) & 0xFF == ord("x"):
        break

    cv2.waitKey(3)