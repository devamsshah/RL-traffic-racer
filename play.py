import pyautogui as py
import time
import screen_view as sv

debug = False #add function that allows to turn debug on

def brake(t=0.3):
    #sv.focus_on_iphone()
    py.moveTo(x=1395, y=1045)
    py.mouseDown()
    time.sleep(t)
    py.mouseUp()

def right(t=0.3):
    #sv.focus_on_iphone()
    py.moveTo(x=1670, y=1045)
    py.mouseDown()
    time.sleep(t)
    py.mouseUp()

def left(t=0.3):
    #sv.focus_on_iphone()
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

def click_on_play():
    sv.focus_on_iphone()
    py.moveTo(1639, 978) 
    py.click() #click on play

def choose_car(car='audi'):#default is audi for now
    sv.focus_on_iphone()
    if(car=='audi'):
        py.moveTo(1654, 1076)
        py.click() #chosen car and click play

def game_mode(mode='one way'):#default is 'one way' on for now
    sv.focus_on_iphone()
    py.moveTo(1198, 937)
    py.click() #chosen game mode and clicked endless one way

def choose_location(location='forest'):#default is 'forest' on for now
    sv.focus_on_iphone()
    py.moveTo(1554, 937)
    py.dragTo(1198, 937, 1, button='left')
    py.moveTo(x=1395, y=982)
    py.click() #chosen location: Forest 
    
def play_again():
    sv.focus_on_iphone()
    time.sleep(0.2)
    py.moveTo(x=1473, y=1069)
    py.click()

def play(car='audi', mode='one way', location='forest'):
    sv.focus_on_iphone()
    text = sv.read_text()
    here = False    
    if "YOUR SCORE" in text:
        play_again()
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
