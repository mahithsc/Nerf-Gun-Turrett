import cv2
import mediapipe as mp
import time
from serial_connection import create_connection

serialInst = create_connection()

# getting the video through vudeo captue
cap = cv2.VideoCapture(0)
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)

    if results.detections:
        for id, detection in enumerate(results.detections):
            # print(detection)
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img, bbox, (255, 0, 255), 3)
            cv2.putText(img, f'Index:  {id + 1} | Confidence: {int(detection.score[0] * 100)}%', (bbox[0], bbox[1]), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
            # serialInst.write("FOUND")
    # serialInst.write("NOT_FOUND")

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime 
    cv2.putText(img, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)