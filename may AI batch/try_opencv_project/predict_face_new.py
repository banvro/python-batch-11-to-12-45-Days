import cv2

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")

peoples = ["alone_musk", "kristina_pemenova"]
predict_who = cv2.face.LBPHFaceRecognizer_create()
predict_who.read("face_predictor_model_new.yml")

capture = cv2.VideoCapture(0)


while True:
    isdone, frame = capture.read()

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    get_face = face_detector.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=3)

    for (x, y, w, h) in get_face:
        face_roi = gray_image[y:y+h, x:x+w]
        labell, confidence = predict_who.predict(face_roi)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 4)
        cv2.putText(frame, peoples[labell], (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 34), 3)

    cv2.imshow("predict", frame)

    if cv2.waitKey(10) & 0xff == ord("x"):
        break