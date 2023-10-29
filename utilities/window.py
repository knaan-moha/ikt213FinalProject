import sys, os

import pyautogui
import platform
import functions as f 
import time 
import main as m


def manage_window(img, fingers_up): 
    """
    Performs window management.
    :param img: Frame for displaying the invoked command (i.e. minimize\close window) or notifying when the command can be invoked.
    :param fingers_up: Number of raised fingers.
    """
  
    if time.time()-m.timer_window >=3:
      
        if fingers_up==[0,1,0,0,1]: 
            pyautogui.click()
            if platform.system()=="Windows":
                pyautogui.hotkey('win', 'down')
                pyautogui.keyUp('win')
                pyautogui.keyUp('down')
            
            elif platform.system()=="Darwin":
                pyautogui.hotkey("command", "m")
            m.timer_window=time.time()
           
            
        if fingers_up==[0,1,1,1,0]:
            pyautogui.click()
            if platform.system()=="Windows":
             pyautogui.hotkey('alt', 'f4')
             pyautogui.keyUp('alt')
             pyautogui.click()
            elif platform.system()=="Darwin":
             pyautogui.hotkey("command", "w")
             pyautogui.click()
            m.timer_window=time.time()
    elif time.time()-m.timer_window <3: 
        if fingers_up==[0,1,0,0,1] or fingers_up==[0,1,1,1,0]: 
            f.print_action(img, "Window Management Functions available in "+str(4-(time.time()-m.timer_window))[0]) 
      
   