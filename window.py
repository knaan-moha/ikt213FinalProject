import pyautogui
import platform
import functions as f 
import time 

import main as m


def manage_window(img, fingers_up): 
    print(time.time()-m.timer)
    if time.time()-m.timer >=3:
      
        if fingers_up==[0,1,0,0,1]: 
            pyautogui.click()
            if platform.system()=="Windows":
                pyautogui.keyDown("win")
                pyautogui.press("down")
                pyautogui.keyUp("win")
            elif platform.system()=="macOS":
                pyautogui.hotkey("command", "m")
            m.timer=time.time()
           
            
        if fingers_up==[0,1,1,1,0]:
            pyautogui.click()
            if platform.system()=="Windows":
             pyautogui.hotkey("alt", "f4")
            elif platform.system()=="macOS":
             pyautogui.hotkey("command", "w")
            m.timer=time.time()
       