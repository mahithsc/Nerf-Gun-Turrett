import cv2
from face_recognition import FaceRecognition
from serial_connection import create_connection
import time

if __name__ == '__main__':
    conn = create_connection()
    cap = cv2.VideoCapture(0)
    detector = FaceRecognition()

    while True:
        success, img = cap.read()
        recs = detector.get_recognitions(img = img)

        cv2.imshow("Image", detector.draw_landmarks(img=img))
        cv2.waitKey(1)

        if (recs != None):
            if(len(recs) >= 1):
                conn.write(b"FOUND\n")