import pyautogui as py
import time

def focus_on_iphone():
    py.moveTo(x=1702, y=1091)
    py.click() #focus on iphone mirror

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
    
def play(car='audi', mode='one way', location='forest'):
    focus_on_iphone()
    click_on_play()
    choose_car(car)
    game_mode(mode)
    choose_location(location)

