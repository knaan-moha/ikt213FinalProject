import pyautogui
import functions as f
import platform

def perform_scrolling(img, lmList, fingers_up ): 
    """
     Performs scrolling up and down
     :param img: Frame for displaying the invoked command (i.e. scolling up/down/left/right).
     :param lmList: List of detected hand landmarks.
     :param fingers_up: Number of raised fingers.
     """


    # check if the raised fingers are the thumb and the index finger 
    if sum(fingers_up[0:2]) == 2 and sum(fingers_up[2:]) == 0:                 
                    
                        f.print_action(img, "Scrolling Up")
                        # perform scrolling up 
                        pyautogui.scroll(3) 
    # check if the raised fingers are the middle finger, ring finger, and pinky finger  
    elif sum(fingers_up[2:5]) == 3 and sum(fingers_up[0:2]) == 0 :
                                f.print_action(img, "Scrolling Down")
                                # perform scrolling down
                                pyautogui.scroll(-3)
    # check if the thumb is the only raised finger  
    elif (fingers_up[0] == 1) and sum(fingers_up[1:]) == 0:
    

        #  check if the kuckles are visible
        if lmList[5][1] < lmList[6][1] and  lmList[17][1] < lmList[18][1]:
            f.print_action(img, "Scrolling left")
            # check if the code is running on Windows 
            if platform.system()=="Windows": 
                # simulate a Windows shortcut associated with scrolling to the left 
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("shift")
                pyautogui.scroll(50)
                pyautogui.keyUp("ctrl")
                pyautogui.keyUp("shift")       
            # check if the code is running on macOS
            elif platform.system()=="Darwin":
                # perform scrolling to the left 
                pyautogui.hscroll(50);
           
        
        # check if the knuckles are not visible 
        elif lmList[5][1] > lmList[6][1] and  lmList[17][1] > lmList[18][1]:
            f.print_action(img, "Scrolling right")
            # check if the code is running on Windows 
            if platform.system()=="Windows":
                # perform a Windows shortcut associated with scrolling to the right  
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("shift")
                pyautogui.scroll(-50)
                pyautogui.keyUp("ctrl")
                pyautogui.keyUp("shift")
            elif platform.system()=="Darwin": 
                # perform scrolling to the right 
                pyautogui.hscroll(-50);


