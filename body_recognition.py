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
        if self.recognitions[12] and self.recognitions[11] and self.recognitions[24] and self.recognitions[23]:
            self.mppDraw.draw_landmarks(img, self.recognitions, mp.solutions.pose.POSE_CONNECTIONS)
        return img


