import cv2
import pyautogui
import functions as f

def scrolling(img, finger_up): 

    if sum(finger_up[0:2]) == 2 and sum(finger_up[2:]) == 0:
                        
                    
                        f.print_action(img, "Scrolling Up")
                        
                        pyautogui.scroll(3) 
                        
    elif sum(finger_up[2:5]) == 3 and sum(finger_up[0:2]) == 0 :
                                f.print_action(img, "Scrolling Down")
                        
                                pyautogui.scroll(-3)




