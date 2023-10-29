import pyautogui
import platform
import functions as f 
import time 

import main as m


def manage_window(img, fingers_up): 
  
    if time.time()-m.timer >=3:
      
        if fingers_up==[0,1,0,0,1]: 
            pyautogui.click()
            if platform.system()=="Windows":
                pyautogui.hotkey('win', 'down')
                pyautogui.keyUp('win')
                pyautogui.keyUp('down')
            elif platform.system()=="Darwin":
                pyautogui.hotkey("command", "m")
                print("Testes! ")
            m.timer=time.time()
           
            
        if fingers_up==[0,1,1,1,0]:
            pyautogui.click()
            if platform.system()=="Windows":
             pyautogui.hotkey('alt', 'f4')
             pyautogui.keyUp('alt')
             pyautogui.click()
            elif platform.system()=="Darwin":
             pyautogui.hotkey("command", "w")
             pyautogui.click()
            m.timer=time.time()
       