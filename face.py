import cv2
import mediapipe as mp
import time


# getting the video through vudeo captue
cap = cv2.VideoCapture(0)

# varibable for the frame rates
pTime = 0

# baisically gettingt he face_detection model from the solutions
mpFaceDetection = mp.solutions.mediapipe.python.solutions.face_detection

# drawing utility from mediapide
mpDraw = mp.solutions.mediapipe.python.solutions.drawing_utils


# getting the specific face detection model
faceDetection = mpFaceDetection.FaceDetection()

while True:
    # gets the image for baisically every frame
    success, img = cap.read()

    # converting the frame to an rgb image
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # puts it through the model and gets the results
    results = faceDetection.process(imgRGB)

    # 
    if results.detections:
        for id, detection in enumerate(results.detections):
            # print(id, detection)
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box)

            mpDraw.draw_detection(img, detection)

   
    cTime = time.time()
    fps = 1/(cTime - pTime )
    pTime = cTime
    cv2.putText(img, f'FPS {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 2)
    
    cv2.imshow("Image", img)
    cv2.waitKey(20)