import pyautogui
import time

f = pyautogui.prompt(text='How long would you like the timer to be?(in minutes)', title='Netflix Timer', default='')

try:
    int(f)

except:
    pyautogui.alert(text='Not compatible please try again.', title='Oops')
    quit()

Minutes = int(f) * 60
time.sleep(Minutes)

pyautogui.press('space')
