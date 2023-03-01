import cv2
from FaceRecognition import FaceRecognition

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    detector = FaceRecognition()

    while True:
        success, img = cap.read()
        recs = detector.get_recognitions(img = img)
        cv2.imshow("Image", detector.draw_landmarks(img=img))
        cv2.waitKey(1)
