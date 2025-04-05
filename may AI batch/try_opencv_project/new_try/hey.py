import cv2
import cv2.data

zx = cv2.VideoCapture(0)

my_model = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

while True:
    x, f = zx.read()


    roi = my_model.detectMultiScale(f, 1.1, 3)
    
    for (x, y, w, h) in roi:
        cv2.rectangle(f, (x, y), (x+w, y+h), (255, 223, 34), 2)

    cv2.imshow("eee", f)

    if cv2.waitKey(20) & 0xff == ord("x"):
        break
