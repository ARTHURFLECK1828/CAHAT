import cv2
from simple_facerec import SimpleFacerec
import time
timeout=time.time()+30

def main_video():
    # Encode faces from a folder
    sfr = SimpleFacerec()
    sfr.load_encoding_images("C:/NEERAJ/HACKATHON/Smart-India-Hackathon-2022/face_unlock/images/")
    # Load Camera
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 100, 200), 4)
        
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27 or time.time()>timeout or name!="Unknown":
            cap.release()
            cv2.destroyAllWindows()
            return name
        cap.release()
        cv2.destroyAllWindows()
        
#main_video()