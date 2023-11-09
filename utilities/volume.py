import pyautogui
import time
import functions as f 

import main as m 

 # https://www.geeksforgeeks.org/set-countdown-timer-to-capture-image-using-python-opencv/
def control_volume(img, fingers_up):
    """
    Performs volume control.
    :param img: Frame for displaying the invoked command (i.e. volume up/down, or mute/unmute).
    :param fingers_up: Number of raised fingers.
    """

       
    if fingers_up== [0, 0, 1 ,1, 1]:
        f.print_action(img, "Descreasing volume")  
        pyautogui.press('volumedown', presses=1)
        
        
    if fingers_up== [0, 1, 1, 1, 1]:
        f.print_action(img, "Increasing volume")  
        pyautogui.press('volumeup', presses=1)
        
    if  fingers_up==[0, 1, 0, 0, 1] and time.time()-m.timer_volume>=3:

        f.print_action(img, "Mute/Unmute Volume")  
        pyautogui.press('volumemute', presses=1)
        m.timer_volume=time.time()
    elif fingers_up==[0, 1, 0, 0, 1] and time.time()-m.timer_volume<3: 
         f.print_action(img, "Mute/Unmute function available in "+str(4-(time.time()-m.timer_volume))[0])
