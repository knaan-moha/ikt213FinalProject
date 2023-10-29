import cv2
import pyautogui
import functions as f
import cvzone

import platform

import pygetwindow

system_platform = platform.system()

active_window  = pygetwindow.getActiveWindow()

def scrolling(img, lmList, fingers_up): 
    """
     Performs scrolling up and down
     :param img: Frame for displaying the invoked command (i.e. scolling up or down).
     :param fingers_up: Number of raised fingers.
     """
    
    get_thumb_direction_pointing_right  = lmList[4][0] > lmList[3][0]

    if sum(fingers_up[0:2]) == 2 and sum(fingers_up[2:]) == 0:                 
                    
                        f.print_action(img, "Scrolling Up")
                        pyautogui.scroll(3) 
                        
    elif sum(fingers_up[2:5]) == 3 and sum(fingers_up[0:2]) == 0 :
                                
                                f.print_action(img, "Scrolling Down")
                                pyautogui.scroll(-3)
    elif (fingers_up[0] == 1) and sum(fingers_up[1:]) == 0:
        if get_thumb_direction_pointing_right: 
            f.print_action(img, "Scrolling right")
            pyautogui.click()
            pyautogui.hscroll(3);
            return
        
        else:
            f.print_action(img, "Scrolling left")
            pyautogui.click()
            pyautogui.hscroll(-3);
    





        
            
            
        
        
        
        
        
        
    

