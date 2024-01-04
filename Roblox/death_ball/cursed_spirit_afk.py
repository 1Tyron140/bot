# encore en dev
# utilise un thread pour pouvoir quitter à tout moment
import random
import keyboard
import pyautogui
import time
import pydirectinput
import os
from threading import Thread

def quit_program():
    while True:
        if keyboard.is_pressed('ctrl+alt+q'):  # if key 'ctrl+alt+q' is pressed 
            print('[+] Exiting the script')
            os._exit(0) # exiting the script



if __name__ == "__main__":
    t1 = Thread(target=quit_program)
    t1.start()
    time.sleep(2)
    print('[+] Starting the script')
    print('[+] press CLRL+ALT+Q to quit')
    pyautogui.click()
    while 1==1:
        time.sleep(random.uniform(2, 7))
        pydirectinput.press("space")
