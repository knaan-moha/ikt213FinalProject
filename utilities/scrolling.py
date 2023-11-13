import pyautogui
import functions as f
import platform

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
    

         
        if lmList[5][1] < lmList[6][1] and  lmList[17][1] < lmList[18][1]:
            f.print_action(img, "Scrolling left")

            if platform.system()=="Windows": 
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("shift")
            
                pyautogui.scroll(50)
                pyautogui.keyUp("ctrl")
                pyautogui.keyUp("shift")       
            elif platform.system()=="Darwin":
                pyautogui.hscroll(50);
           
        
        # for the right direction
        elif lmList[5][1] > lmList[6][1] and  lmList[17][1] > lmList[18][1]:
            f.print_action(img, "Scrolling right")
            if platform.system()=="Windows":
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("shift")
            
                pyautogui.scroll(-50)
                pyautogui.keyUp("ctrl")
                pyautogui.keyUp("shift")
            elif platform.system()=="Darwin": 
                pyautogui.hscroll(-50);


