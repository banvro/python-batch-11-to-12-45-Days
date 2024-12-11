import cv2

img = cv2.imread("my_image.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_dector = cv2.CascadeClassifier("detect_face.xml")

faces = face_dector.detectMultiScale(gray_img, scaleFactor = 1.4, minNeighbors = 3, minSize = (10, 10))


for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (w+x, h+y), (4, 255, 80), 4)



# print(faces)

# x, y, width, height

# [180 557  56  56]


cv2.imshow("Image", img)

cv2.waitKey(0)