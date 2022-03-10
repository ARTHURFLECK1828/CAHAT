import cv2
import time
import os
import sys
import pyautogui
import handTrackingmodule as htm
import time

sys.path.append('C:/NEERAJ/HACKATHON/Smart-India-Hackathon-2022/Gesture_Control')
import volume_control as vc
import brightness_control as bc
# from tkinter import * 
# from tkinter import messagebox


def fingerCount():
    cap = cv2.VideoCapture(0)
    wCam, hCam = 640, 480
    cap.set(3, wCam)
    cap.set(4, hCam)

    folderPath = "C:/NEERAJ/HACKATHON/Smart-India-Hackathon-2022/Gesture_Control/FingerImages"
    myList = os.listdir(folderPath)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        overlayList.append(image)

    prevTime = 0
    detector = htm.handDetector()
    tipIds = [4, 8, 12, 16, 20]

    count = 0
    totalFingers1, totalFingers2 = 0, 0

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
            
            #---------------Initiating Brightness Control-------------------
            if(fingers.count(1)==3 and fingers[0]==1 and fingers[1]==1 and fingers[4]==1):
                time.sleep(5)
                cap.release()  
                cv2.destroyAllWindows()  
            
                bc.control()

                cap = cv2.VideoCapture(0)
                wCam, hCam = 640, 480
                cap.set(3, wCam)
                cap.set(4, hCam)
                time.sleep(3)
                continue
            #------------------------------------------------------------
            
            #---------------Initiating Volume Control-------------------
            if(fingers.count(1)==2 and fingers[1]==1 and fingers[4]==1):
                time.sleep(5)
                cap.release()  
                cv2.destroyAllWindows()  
            
                vc.control()

                cap = cv2.VideoCapture(0)
                wCam, hCam = 640, 480
                cap.set(3, wCam)
                cap.set(4, hCam)
                time.sleep(3)
                continue
            #------------------------------------------------------------

            totalFingers1 = fingers.count(1)
            if(totalFingers1==totalFingers2):
                count+=1
            else:
                count=0
            totalFingers2 = fingers.count(1)

            ##
            if(count==60):
                ip=int(totalFingers1)
                # if ip==0:
                #     cv2.putText(img, 'Shutting down', (200, 25),
                #       cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 25), 3)
                #     os.system("shutdown /r /t  1")
                if ip==1:
                    cv2.putText(img, 'Saving', (200, 25),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 25), 3)
                    time.sleep(3)
                    pyautogui.hotkey('ctrl','s')
                if ip==2:
                    cv2.putText(img, 'Closing', (200, 25),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 25), 3)
                    # root = Tk()  
                    # root.geometry("100x100")  
                    # response=messagebox.askquestion("Would you like to close the window", "Are you sure?")
                    # print(response)
                    # if response=="Yes":
                    #     root.destroy()
                    # else:
                    #     root.destory()
                    time.sleep(3)
                    # root.mainloop()  
                    pyautogui.hotkey('alt', 'F4')
                if ip==3:
                    cv2.putText(img, 'Copying', (200, 25),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 25), 3)
                    time.sleep(3)
                    pyautogui.hotkey('ctrl','c')
                if ip==4:
                    cv2.putText(img, 'Printing', (200, 25),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 25), 3)
                    time.sleep(3)
                    pyautogui.hotkey('ctrl','p')
                if ip==5:
                    cv2.putText(img, 'Pasting', (200, 25),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 25), 3)
                    time.sleep(3)
                    pyautogui.hotkey('ctrl','v')
                time.sleep(3)
            ##
            h, w, c = overlayList[totalFingers1].shape
            img[0:h, 0:w] = overlayList[totalFingers1]

            cv2.rectangle(img, (20,225),(170,425),(0,255,0),cv2.FILLED)
            cv2.putText(img, str(totalFingers1), (45,375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

        cv2.imshow("Image", img)
        key=cv2.waitKey(1)
        if key==81 or key==113:
            break