import cv2
import mediapipe as mp

import cv2
import mediapipe as mp
import time
from serial_connection import create_connection

class BodyRecognition:
    def __init__(self) -> None:
        self.recognitions = []

        # getting the mediapipe module
        self.poseDetection = mp.solutions.pose.Pose()
        self.mppDraw = mp.solutions.drawing_utils
    

    def get_recognitions(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.poseDetection.process(imgRGB)
        self.recognitions = results.pose_landmarks

        return results.pose_landmarks
    
    def draw_landmarks(self, img):
        if self.recognitions:
            landmarks = self.recognitions.landmark
            if landmarks[12] and landmarks[11] and landmarks[23] and landmarks[24]:
                ih, iw, ic = img.shape
                top_left = (int(landmarks[12].x*iw), int(landmarks[12].y*ih))
                bottom_right = (int(landmarks[11].x * iw), int(landmarks[23].y*ih))
                cv2.rectangle(img, top_left, bottom_right, (255, 0, 255), 3)
                return img
        return img


