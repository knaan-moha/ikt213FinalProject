import cv2
import pyautogui
import functions as f

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




