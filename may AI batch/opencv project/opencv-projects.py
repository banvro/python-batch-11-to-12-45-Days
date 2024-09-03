# install opencv

# command : pip install opencv-contrib-python

# install mediapipe

# command : pip install mediapipe


import cv2
import mediapipe as mp
import time

map_hands = mp.solutions.hands
hands = map_hands.Hands()
show_landmarks = mp.solutions.drawing_utils

change_landmarks_color = show_landmarks.DrawingSpec(color = (23, 240, 7), thickness = 5)

change_connection_cawingSolor = show_landmarks.DrawingSpec(color = (228, 7, 240), thickness = 10)

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
    ptime = 0
    ctime = 0
    # for hands in 
    # print(result.multi_hand_landmarks)

    lmlst = []

    if result.multi_hand_landmarks:
        myhand =  result.multi_hand_landmarks[0]
        for id, lm in enumerate(myhand.landmark):
            h, w, c = frame.shape
            cx, cy = (int(lm.x * w), int(lm.y*h))
            # print(id, cx, cy)
            lmlst.append([id, cx, cy])

        for hand_landmarks in result.multi_hand_landmarks:
            show_landmarks.draw_landmarks(frame, hand_landmarks, map_hands.HAND_CONNECTIONS, change_landmarks_color, change_connection_cawingSolor)

    print(lmlst)
    
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(frame, f"fps is : {str(fps)[:4]}", (5, 40), 1, 2, (237, 17, 61), 2)
    
    cv2.imshow("My Video", frame)
 
    if cv2.waitKey(3) & 0xff == ord("q"):
        break
 