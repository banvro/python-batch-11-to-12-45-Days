import cv2

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

peoples = ["elon musk", "joker", "kristina_pemenova"]

# face_predctor_model.yml

face_dector_model = cv2.face.LBPHFaceRecognizer_create()
face_dector_model.read("face_predctor_model.yml")


capture = cv2.VideoCapture(0)

while True:
    isTrue, image = capture.read()
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("gray_image", gray_img)


    image_face = face_detector.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors = 4)

    for (x, y, w, h) in image_face:
        image_roi = gray_img[y:y+h, x:x+h]

        label, confiidence = face_dector_model.predict(image_roi)

        # print(f"lable is : {label}")
        # print(f"confidence is : {confiidence}")

        cv2.rectangle(image, (x, y), (x+w, y+h), (100, 255, 50), 4)

        cv2.putText(image, peoples[label], (x - 10, y-10), cv2.FONT_HERSHEY_PLAIN, 2, (100, 255, 50), 3)

        cv2.imshow("unknown image", image)



    if cv2.waitKey(10) & 0xFF == ord("x"):
        break





# image
# gray
# face 

# model <------

# index number, coffidence




