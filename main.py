import cv2
from FaceRecognition import FaceRecognition

if __name__ == '__main__':

    # getting the webcam
    cap = cv2.VideoCapture(0)

    # initializing the facial recognition module
    detector = FaceRecognition()

    while True:
        # getting image from webcam
        success, img = cap.read()
        # getting deteted faces
        recs = detector.get_recognitions(img = img)
        # printing image to screen
        cv2.imshow("Image", detector.draw_landmarks(img=img))
        cv2.waitKey(1)
