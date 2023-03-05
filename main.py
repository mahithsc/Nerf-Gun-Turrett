import cv2
from face_recognition import FaceRecognition
from body_recognition import BodyRecognition
from serial_connection import create_connection, get_port_name
from arduino import Arduino
import time
import json

if __name__ == '__main__':
    # getting the names of the available arduino ports and creating a serial connection
    # port_name = get_port_name()
    # conn = create_connection(port_name)

    board = Arduino()

    # video cap.
    cap = cv2.VideoCapture(0)

    # instantiating the different classification libraris
    face_detector = FaceRecognition()
    body_detector = BodyRecognition()

    while True:
        # getting feed from webcam
        success, img = cap.read()
        ih, iw, ic = img.shape

        # cross-air
        xmid, ymid = (int(iw/2), int(ih/2))

        # creates the landmarks for the face and the body
        body_recs = body_detector.get_recognitions(img = img)
        face_recs = face_detector.get_recognitions(img = img)

        # updates the image to draw landmarks
        body_detector.draw_landmarks(img=img)
        face_detector.draw_landmarks(img = img)

        # cross hair
        cv2.putText(img, "+", (xmid, ymid), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        if (face_recs != None):
            # if there is a face found
            if(len(face_recs) >= 1):
                index = 0
                current = face_recs[0].location_data.relative_bounding_box
                xmin, ymin, xmax, ymax = int(current.xmin * iw), int(current.ymin * ih), int((current.xmin + current.width)*iw), int((current.ymin + current.height)*ih)


                # checking to make sure the cross air is on the head
                if ((xmin < xmid and xmid < xmax) and (ymin < ymid and ymid < ymax)):

                    board.on()
                    
                    data = {'command': 'FIRE'}
                    data = json.dumps(data)

                    print("FIRE")
                    # conn.write(data.encode())

                
                else:
                    board.off()
                    data = {'command': 'DONTFIRE'}
                    data = json.dumps(data)
                    
                    print("DONTFIRE")
                    # conn.write(data.encode())
        else:
            board.off()
            data = {'command': 'DONTFIRE'}
            data = json.dumps(data)
            
            print("DONTFIRE")
            # conn.write(data.encode())

        cv2.imshow("Image", img)
        cv2.waitKey(1)

        

       

