import pyautogui as py
import time
from screen_view import focus_on_iphone, get_frame
import pytesseract
from PIL import Image
import re 
import cv2

debug = False #add function that allows to turn debug on

def brake(t=0.3):
    focus_on_iphone()
    py.moveTo(x=1395, y=1045)
    py.mouseDown()
    time.sleep(t)
    py.mouseUp()

def right(t=0.3):
    focus_on_iphone()
    py.moveTo(x=1670, y=1045)
    py.mouseDown()
    time.sleep(t)
    py.mouseUp()

def left(t=0.3):
    focus_on_iphone()
    py.moveTo(x=1120, y=1045)
    py.mouseDown()
    time.sleep(t)
    py.mouseUp()

def pause_game(now=False):
    if not now:
        time.sleep(3.2)
    py.moveTo(1697, 830)
    py.click()

def continue_game():
    py.moveTo(1392, 900)
    time.sleep(0.2)
    py.click()

#def enter_to_allow():
#    py.moveTo(x=854, y=502)
#    py.click()
#    py.moveTo(901, 520)
#    py.click()
#
#    #py.press('enter')

   
def click_on_play():
    focus_on_iphone()
    py.moveTo(1639, 978) 
    py.click() #click on play

def choose_car(car='audi'):#default is audi for now
    focus_on_iphone()
    if(car=='audi'):
        py.moveTo(1654, 1076)
        py.click() #chosen car and click play

def game_mode(mode='one way'):#default is 'one way' on for now
    focus_on_iphone()
    py.moveTo(1198, 937)
    py.click() #chosen game mode and clicked endless one way

def choose_location(location='forest'):#default is 'forest' on for now
    focus_on_iphone()
    py.moveTo(1554, 937)
    py.dragTo(1198, 937, 1, button='left')
    py.moveTo(x=1395, y=982)
    py.click() #chosen location: Forest 
    
def play_again():
    focus_on_iphone()
    py.moveTo(x=1473, y=1069)
    py.click() 

def read_text(frame = None, print_text = debug):
    if frame == None:
        frame = get_frame(debug)
    if frame is None:
        raise ValueError("Frame is None! Check your image capture logic.")
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    # Resize to enhance small text 
#    scale_percent = 200
#    width = int(gray.shape[1] * scale_percent / 100)
#    height = int(gray.shape[0] * scale_percent / 100)
#    gray = cv2.resize(gray, (width, height), interpolation=cv2.INTER_CUBIC)
#    #_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#    # Use pytesseract with a better config for small/regular text
#    config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(Image.fromarray(gray))

    if print_text:
        print(text)

    return text
def play(car='audi', mode='one way', location='forest'):
    focus_on_iphone()
    text = read_text()
    here = False    
    if "YOUR SCORE" in text:
        play_again()
        pattern = re.compile(
            r"YOUR\s+SCORE\b\s*([\d]{1,3}(?:,\d{3})*)",
            flags=re.IGNORECASE
        )
        m = pattern.search(text)
        if not m:
            raise ValueError("Couldn't find a score in the text")
        raw = m.group(1)
        score = int(raw.replace(",",""))
        print("------------------> S C O R E : ", score)
        return score
    if text == '' or "SETTINGS" in text:
        click_on_play()
        here = True
    if "BRAKING" in text or here:
        choose_car(car)
        here = True
    if "GAME MODE" in text or here:
        game_mode(mode)
        here = True
    if "LOCATION" in text or here:
        choose_location(location)
    if "CONTINUE" in text:
        continue_game()
        time.sleep(1.8)
