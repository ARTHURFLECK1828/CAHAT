import sys
import time
import ctypes
from tkinter import * 
from tkinter import messagebox
import tkinter as tk
import threading
import tkinter
from tkinter import Label, Tk
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
        messagebox.showwarning("Warning Face not Found", "Warning")
        #ctypes.windll.user32.LockWorkStation()
        exit(0)
    else:
        # top = Tk()
        # messagebox.showwarning("Input is unLocked")
        # top.quit()
        # time.sleep(1)
        # top.mainloop()
        # w = tk.Tk()
        # messagebox.showwarning("Input is unLocked")
        # w.after(3000, lambda: w.destroy()) # Destroy the widget after 30 seconds
        # w.mainloop()
        # root = tkinter.Tk()
        # tkinter.Frame(root, width=250, height=100).pack()
        # tkinter.Label(root, text='Input is unlocked').place(x=10, y=10)
        # threading.Timer(3.0, root.destroy).start()
        root = Tk()
        prompt = 'Input is Unlocked'
        label1 = Label(root, text=prompt,width=100,height=10)
        label1.pack()

        def close_after_4s():
            root.destroy()

        root.after(4000, close_after_4s)
        root.mainloop()

        
        time.sleep(2)
        fingerCount.fingerCount()
except:
    exit(0)