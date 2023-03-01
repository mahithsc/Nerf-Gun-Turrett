import cv2
from FaceRecognition import FaceRecognition

if __name__ == '__main__':
    detector = FaceRecognition()
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        recs = detector.get_recognitions(img = img)
        print(recs)
