import pyautogui
import time
#3456-by-2234 pixels on the screen
#(0,0) is top left, the iphone mirrored screen is expected to be in the bottom right corner

## make this adaptive to any screen by calling the pixels in proportion
#allows you to know the size of your screen and the current position of your cursor
#mine is currently (width=1728, height=1117)
print(pyautogui.size())
print(pyautogui.position())


###Test
#if doesnt work, check system settings, privacy and security, accessibility and make sure terminal/ other app is on. 
