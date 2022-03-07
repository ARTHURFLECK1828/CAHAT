from time import sleep
import cv2
import os

cam = cv2.VideoCapture(0)
images_path = 'C:/NEERAJ/HACKATHON/Smart-India-Hackathon-2022/face_unlock/images'
name=input("Enter your name  ")
while True:
    ret, frame = cam.read()
    if not ret:
        break
    cv2.imshow("Press Space to Capture Image",frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        break
    elif k%256 == 32:
        # SPACE pressed -> to click picture
        
        img_name = name+".png"
        cv2.imwrite(os.path.join(images_path , img_name), frame)
        sleep(1)
        cam.release()
        cv2.destroyAllWindows()