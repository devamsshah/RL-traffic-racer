import mss
import cv2, re
import numpy as np
import time
import pyautogui as py
import pytesseract
from PIL import Image

debug = False

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

def read_text(frame = get_frame(debug), print_text = debug):
    if frame is None:
        raise ValueError("Frame is None! Check your image capture logic.")
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(Image.fromarray(gray))

    if print_text:
        print(text)

    return text

def is_terminated(frame = get_frame()):
    text = read_text(frame)
    if "YOUR SCORE" in text:
        return True
    else:
        return False


def get_score(no_score, frame = get_frame(), again=0):
    if no_score >=100:
        raise ValueError("Score not Found")
    text = read_text(frame)
    pattern = re.compile(
            r"YOUR\s+SCORE\b(?:\s|\n)*([\d]{1,3}(?:,\d{3})*)",
            flags=re.IGNORECASE
        )
    m = pattern.search(text)
    if not m:
        print("TEXT: ", text)
        pattern = re.compile(
                r"([\d]{1,3}(?:,\d{3})*)\s*(?:\n|\s)*SCORES\b",
                flags=re.IGNORECASE
        ) 
        m = pattern.search(text)
        if not m:
            print("TEXT: ", text)
            time.sleep(0.5)
            if again >= 3:
                no_score +=1
            else:
                get_score(again=again+1, no_score=no_score)
    if m:
        raw = m.group(1)
        score = int(raw.replace(",",""))
        print("------------------> S C O R E : ", score)
    #time.sleep(0.2)
    #py.moveTo(x=1473, y=1069)
    #py.click()
        return score, no_score
    return 0, no_score
