import cv2
import cv2.data
import numpy as np
import os

# people = []

# for x in os.listdir(r"C:\Users\17nru\OneDrive\Desktop\face reoginizer\images"):
#     people.append(x)

# print(people)

# peoples = ["elon musk"]
peoples = ["elon musk", "joker", "kristina_pemenova"]
path = r"C:\Users\17nru\OneDrive\Desktop\face reoginizer\images"

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

features = []
lables = []

for perons in peoples:
    folder_path = os.path.join(path, perons)
    lable = peoples.index(perons)
    
    for images in os.listdir(folder_path):
         images_path = os.path.join(folder_path, images)    

         image_array = cv2.imread(images_path)

         gray_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)


         face_region = face_detector.detectMultiScale(gray_image, scaleFactor = 1.1, minNeighbors = 3)

         for (x, y, w, h) in face_region:
              face_roi = gray_image[y:y+h, x:x+w]
              features.append(face_roi)
              lables.append(lable)


print(len(features))
print(len(lables))


fetaures_array = np.array(features, dtype="object")

lables_array = np.array(lables)


train_data = cv2.face.LBPHFaceRecognizer_create()

train_data.train(fetaures_array, lables_array)


np.save("featutus.npy", fetaures_array)

np.save("lables.npy", lables_array)




        #       cv2.rectangle(gray_image, (x, y), (x + w, y + h), (20, 255, 90), 3)

        #  cv2.imshow("elon musk", gray_image)

        #  cv2.waitKey(0)