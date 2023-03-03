import cv2
import mediapipe as mp
import time
from serial_connection import create_connection

class FaceRecognition:
    def __init__(self) -> None:
        self.recognitions = []

        # getting the mediapipe module
        self.faceDetection = mp.solutions.face_detection.FaceDetection()
    

    def get_recognitions(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.faceDetection.process(imgRGB)
        self.recognitions = results.detections

        return results.detections
    
    def draw_landmarks(self, img):
        if self.recognitions:
            for id, detection in enumerate(self.recognitions):
                # print(detection)
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                cv2.rectangle(img, bbox, (255, 0, 255), 3)
                cv2.putText(img, f'Penis Length:  {id + 1} inches | Confidence: {int(detection.score[0] * 100)}%', (bbox[0], bbox[1]), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        return img


