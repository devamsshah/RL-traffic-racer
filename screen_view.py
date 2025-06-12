import mss
import cv2
import numpy as np
import time
import pyautogui as py
monitor_region = {
        "top": 810,
        "left": 1070, 
        "width": 660,
        "height": 300
        }

#if the mac keeps nagging for permission to take screenshots, then refer to this stackoverflow post: https://apple.stackexchange.com/questions/480226/

def focus_on_iphone():
    py.moveTo(x=1702, y=1091)
    py.click() #focus on iphone mirror

def get_frame(display_frame=False):
    with mss.mss() as sct:
        # Capture a single frame
        img = sct.grab(monitor_region)
        frame = np.array(img)
        # Convert to NumPy array and display
        if display_frame:
            cv2.imshow("Captured Region", frame)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            focus_on_iphone()
        
        return frame
