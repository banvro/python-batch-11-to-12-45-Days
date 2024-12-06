import cv2

capture = cv2.VideoCapture(0)

while True:
    x, y = capture.read()
    
    cv2.putText(y, "Hellow Word", (400, 100), 1, 3, (125, 250, 80), 5)

    cv2.imshow("xyz", y)

    if cv2.waitKey(10) and 0xFF == ord("e"):
        break


