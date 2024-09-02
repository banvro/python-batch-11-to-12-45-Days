# install opencv

# command : pip install opencv-contrib-python

# install mediapipe

# command : pip install mediapipe


import cv2
import mediapipe as mp

map_hands = mp.solutions.hands
hands = map_hands.Hands()
show_landmarks = mp.solutions.drawing_utils


capture = cv2.VideoCapture(0)
 
while True:
    isDone, frame = capture.read()

    if not isDone:
        print("faild to capture image...")
        break

    # opencv --> bgr
    # mediapie ---> images ---> rgb
    rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb_img)

    # for hands in 
    print(result.multi_hand_landmarks)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            show_landmarks.draw_landmarks(frame, hand_landmarks, map_hands.HAND_CONNECTIONS)


    cv2.imshow("My Video", frame)
 
    cv2.waitKey(3)
 