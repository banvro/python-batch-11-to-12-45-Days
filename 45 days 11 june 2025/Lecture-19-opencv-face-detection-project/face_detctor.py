import cv2

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img = cv2.imread("proimg.jpg")



face_roi = face_detector.detectMultiScale(img, 1.2, 3)

print(len(face_roi))

for x, y, w, h in face_roi:
    cv2.rectangle(img, (x, y), (x+h, y+w), (10, 244, 39), 5)

cv2.imshow("img", img)

cv2.waitKey(0)