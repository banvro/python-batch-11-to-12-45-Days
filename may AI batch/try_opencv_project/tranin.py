import cv2
import os
import numpy as np


face_detector = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")

peoples = ["alone_musk", "kristina_pemenova"]

path = r"C:\Users\17nru\OneDrive\Desktop\ee\images"

features = []
labels = []

for person in peoples:
    folder_path = os.path.join(path, person)

    label = peoples.index(person)

    for images in os.listdir(folder_path):
        images_path = os.path.join(folder_path, images)

        images_array = cv2.imread(images_path)

        image_gray = cv2.cvtColor(images_array, cv2.COLOR_RGB2GRAY)

        face_region = face_detector.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=3)

        for (x, y, w, h) in face_region:
            # cv2.rectangle(images_array, (x, y), (x+w, y+h), (23, 34, 45), 6)
            # cv2.imshow("Ee", images_array)

            # cv2.waitKey(0)
            face_roi = image_gray[y : y+h, x : x + w]
            features.append(face_roi)
            labels.append(label)

features_array = np.array(features, dtype = "object")

labels = np.array(labels)

 
train_data = cv2.face.LBPHFaceRecognizer_create()


train_data.train(features_array, labels)


train_data.save("face_predictor_model_new.yml")