import cv2
import pyautogui
import functions as f

import platform

import pygetwindow

system_platform = platform.system()

active_window  = pygetwindow.getActiveWindow()

def scrolling(img, fingers_up): 
    """
     Performs scrolling up and down
     :param img: Frame for displaying the invoked command (i.e. scolling up or down).
     :param fingers_up: Number of raised fingers.
     """
    

    if sum(fingers_up[0:2]) == 2 and sum(fingers_up[2:]) == 0:                 
                    
                        f.print_action(img, "Scrolling Up")
                        pyautogui.scroll(3) 
                        
    elif sum(fingers_up[2:5]) == 3 and sum(fingers_up[0:2]) == 0 :
                                
                                f.print_action(img, "Scrolling Down")
                                pyautogui.scroll(-3)




def macMinimize(img, fingers_up):
    
    
    if fingers_up==[0,1,0,0,1]:
        if system_platform == "Darwin": 
            f.print_action(img, "minimize window")
            pyautogui.click()
            pyautogui.hotkey("command", "w")

        
           
    

