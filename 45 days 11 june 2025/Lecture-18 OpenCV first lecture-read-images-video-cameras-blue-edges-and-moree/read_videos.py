import cv2

cap = cv2.VideoCapture(r"C:\Users\17nru\Videos\2025-06-18 11-02-58.mp4")

# Open --> frames

while True:
    is_True, frame = cap.read()

    cv2.imshow("myvideo", frame)

    cv2.waitKey(20)