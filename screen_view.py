from play_from import focus_on_iphone
import mss
import cv2
import numpy as np
import time

monitor_region = {
        "top": 810,
        "left": 1070, 
        "width": 660,
        "height": 300
        }

#if the mac keeps nagging for permission to take screenshots, then refer to this stackoverflow post: https://apple.stackexchange.com/questions/480226/

def get_frame(display_frame=False):
    with mss.mss() as sct:
        # Capture a single frame
        img = sct.grab(monitor_region)

        # Convert to NumPy array and display
        frame = np.array(img)
        # enter_to_allow()
        time.sleep(0.05)
        focus_on_iphone()        
        #print(frame)
        #print("frame dim = ", frame.shape)

        if display_frame:
            cv2.imshow("Captured Region", frame)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            focus_on_iphone()
