import cv2
import time
import handTrackingmodule as htm
import numpy as np
import math
import screen_brightness_control as sbc

def control():
    wCam, hCam = 640, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)

    detector = htm.handDetector(detectionCon=0.7)

    brightnessBar = 400
    brightness = 0

    tipIds = [4, 8, 12, 16, 20]

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        if len(lmList) != 0:
            # Thumb and Index finger points
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]
            cv2.circle(img, (x1, y1), 10, (255, 255, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (255, 255, 0), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 0), 3)
            # center of the line
            cx, cy = (x1+x2)//2, (y1+y2)//2
            cv2.circle(img, (cx, cy), 10, (255, 255, 0), cv2.FILLED)
            length = math.hypot(x2-x1, y2-y1)  # hypotenuse

            if length < 18:
                cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
            # Hand range length from 18 to 175
            # Brightness range 0 to 100
            brightnessBar = np.interp(length, [18, 175], [400, 150])
            brightness = np.interp(length, [18, 175], [0, 100])
            sbc.set_brightness(int(brightness))

            #To go back to fingerCount.py if same gesture is detected
            if((lmList[tipIds[0]][2] < lmList[tipIds[0]-2][2]) 
                and (lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2])
                and (lmList[tipIds[4]][2]<lmList[tipIds[4]-2][2])):
                time.sleep(5)
                cap.release()  
                cv2.destroyAllWindows()  
                return

        cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
        cv2.rectangle(img, (50, int(brightnessBar)), (85, 400),
                      (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(brightness))+'%', (40, 450),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 25), 3)
        cv2.putText(img, 'Controlling Brightness', (0, 25),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 25), 3)
        cv2.imshow("Image", img)

        key = cv2.waitKey(1)
        if(key == 81 or key == 113):
            break