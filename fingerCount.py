import cv2
import time
import os
import handTrackingmodule as htm

cap = cv2.VideoCapture(0)
wCam, hCam = 640, 480
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "FingerImages"
myList = os.listdir(folderPath)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)

prevTime = 0
detector = htm.handDetector()
tipIds = [4, 8, 12, 16, 20]


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList)!=0:
        fingers=[]

        #NOTE:- Doing only for right hand
        #For Thumb
        if lmList[tipIds[0]][1]>lmList[tipIds[0]-1][1]: #open
            fingers.append(1)
        else: #closed
            fingers.append(0)

        #For remaining fingers
        for id in range(1,5):
            #Index Finger tip(id) above(<) Finger point(id-2) 
            # => Finger closed else Finger open=> count it
            if lmList[tipIds[id]][2]<lmList[tipIds[id]-2][2]: #open
                fingers.append(1)
            else: #closed
                fingers.append(0)
        #print(fingers)
        totalFingers = fingers.count(1)

        h, w, c = overlayList[totalFingers].shape
        img[0:h, 0:w] = overlayList[totalFingers]

        cv2.rectangle(img, (20,225),(170,425),(0,255,0),cv2.FILLED)
        cv2.putText(img, str(totalFingers), (45,375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
     
    currTime = time.time() 
    fps = 1/(currTime-prevTime)
    prevTime = currTime
    cv2.putText(img, 'FPS: '+str(int(fps)), (400,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("Image", img)
    key=cv2.waitKey(1)
    if key==81 or key==113:
        break