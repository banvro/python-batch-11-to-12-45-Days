
import cv2
import mediapipe as mp
import time

class MyHandTrackingModule:
    def __init__(self, mode=False, maxHands=2, mdectionCofi = 0.5, mintrackingcoi = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.mdectionCofi = mdectionCofi
        self.map_hands = mp.solutions.hands
        self.hands = self.map_hands.Hands()
        self.show_landmarks = mp.solutions.drawing_utils
        self.change_landmarks_color = self.show_landmarks.DrawingSpec(color = (23, 240, 7), thickness = 5)
        self.change_connection_cawingSolor = self.show_landmarks.DrawingSpec(color = (146, 235, 52), thickness = 2)
        self.result = None
    

    def HandDetector(self, img, draw = True):
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(rgb_img)
        ptime = 0
        ctime = 0

        if self.result.multi_hand_landmarks:
            for hand_landmarks in self.result.multi_hand_landmarks:
                self.show_landmarks.draw_landmarks(img, hand_landmarks, self.map_hands.HAND_CONNECTIONS, self.change_landmarks_color, self.change_connection_cawingSolor)

        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime

        cv2.putText(img, f"fps is : {str(fps)[:4]}", (5, 40), 1, 2, (237, 17, 61), 2)
    

    def HandCordinates(self, img, numofHands = 0, draw = True):
        lmlst = []
        if self.result.multi_hand_landmarks:
            myhand =  self.result.multi_hand_landmarks[numofHands]
            for id, lm in enumerate(myhand.landmark):
                h, w, c = img.shape
                cx, cy = (int(lm.x * w), int(lm.y*h))
                lmlst.append([id, cx, cy])

        return lmlst
