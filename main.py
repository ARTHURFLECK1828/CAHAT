import sys
import time
import ctypes
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('C:/NEERAJ/HACKATHON/Smart-India-Hackathon-2022/Gesture_Control')
import fingerCount
sys.path.append('C:/NEERAJ/HACKATHON/Smart-India-Hackathon-2022/face_unlock')
import main_video
# sys.path.insert(1, 'C:/NEERAJ/HACKATHON/Smart-India-Hackathon-2022/Gesture_Control/fingerCount')
# sys.path.insert(0, 'C:/NEERAJ/HACKATHON/Smart-India-Hackathon-2022/face_unlock/main_video')
try:
    name = main_video.main_video()
    if(name=="unknown"):
        print('Get a new face')
        ctypes.windll.user32.LockWorkStation()
        exit(0)
    else:
        time.sleep(2)
        fingerCount.fingerCount()
except:
    exit(0)
