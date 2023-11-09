import pyautogui
import functions as f

def perform_scrolling(img, lmList, fingers_up ): 
    """
     Performs scrolling up and down
     :param img: Frame for displaying the invoked command (i.e. scolling up or down).
     :param lmList: List of detected hand landmarks.
     :param fingers_up: Number of raised fingers.
     """



    if sum(fingers_up[0:2]) == 2 and sum(fingers_up[2:]) == 0:                 
                    
                        f.print_action(img, "Scrolling Up")
                        pyautogui.scroll(3) 
                        
    elif sum(fingers_up[2:5]) == 3 and sum(fingers_up[0:2]) == 0 :
                                f.print_action(img, "Scrolling Down")
                                pyautogui.scroll(-3)
    elif (fingers_up[0] == 1) and sum(fingers_up[1:]) == 0:
    

         
        if lmList[5][1] < lmList[6][1]:
            f.print_action(img, "Scrolling left")
            pyautogui.hscroll(20);
            
        # for the right direction
        elif lmList[5][1] > lmList[6][1]:
            f.print_action(img, "Scrolling right")
            pyautogui.hscroll(-20);


