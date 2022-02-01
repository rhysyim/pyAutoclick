from pynput.keyboard import Key, Listener
import pyautogui
import random
import time

def clicking():
    for i in range(n):
        pyautogui.leftClick()
        ran = random.randrange(1,10)/100
        time.sleep(ran)
    ran2 = random.randrange(10,30)/100
    time.sleep(ran2)

def on_press(key):
    if str(key) == 'Key.enter':
        clicking()

print("Number of clicks")
n = int(input())

with Listener(on_press=on_press) as listener :
    listener.join()
    