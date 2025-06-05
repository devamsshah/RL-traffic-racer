from play_from import focus_on_iphone, enter_to_allow
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

import subprocess
import tempfile
import numpy as np
from PIL import Image
import os

def get_frame2(x = 1070, y = 810, width = 660, height = 300):
    # Create a temporary file path
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_file:
        tmp_path = tmp_file.name

    try:
        # Run the screencapture command with region
        region = f"{x},{y},{width},{height}"
        subprocess.run(['screencapture', '-R' + region, tmp_path], check=True)

        # Open the image and convert to numpy array
        img = Image.open(tmp_path)
        img_array = np.array(img)

        return img_array

    finally:
        # Clean up the temporary file
        if os.path.exists(tmp_path):
            os.remove(tmp_path)



def get_frame(display_frame=False):
    with mss.mss() as sct:
        # Capture a single frame
        img = sct.grab(monitor_region)

        # Convert to NumPy array and display
        frame = np.array(img)
        enter_to_allow()
        time.sleep(0.05)
        focus_on_iphone()        
        #print(frame)
        #print("frame dim = ", frame.shape)

        if display_frame:
            cv2.imshow("Captured Region", frame)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            focus_on_iphone()
