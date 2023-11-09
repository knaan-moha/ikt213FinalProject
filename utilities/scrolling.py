import cv2
import pyautogui
import functions as f

def perform_scrolling(img, fingers_up,  thumb_tips_right, thumb_base_right, thumb_tips_left, thumb_base_left ): 
    """
     Performs scrolling up and down
     :param img: Frame for displaying the invoked command (i.e. scolling up or down).
     :param fingers_up: Number of raised fingers.
     """
    
    ##get_thumb_direction_pointing_right  = lmList[4][0] > lmList[17][0]
    ##get_thumb_direction_pointing_left = lmList[4][0] < lmList[17][0]
    
  


    if sum(fingers_up[0:2]) == 2 and sum(fingers_up[2:]) == 0:                 
                    
                        f.print_action(img, "Scrolling Up")
                        pyautogui.scroll(3) 
                        
    elif sum(fingers_up[2:5]) == 3 and sum(fingers_up[0:2]) == 0 :
                                f.print_action(img, "Scrolling Down")
                                pyautogui.scroll(-3)
    elif (fingers_up[0] == 1) and sum(fingers_up[1:]) == 0:
         # for the left direction
        if thumb_tips_right[0] < thumb_base_right[0]:
            f.print_action(img, "Scrolling left")
            pyautogui.hscroll(60);
            
        # for the right direction
        elif thumb_tips_left[0] < thumb_base_left[0]:
            f.print_action(img, "Scrolling right")
            pyautogui.hscroll(-60);




