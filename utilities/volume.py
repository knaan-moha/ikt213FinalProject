import pyautogui
import time
import functions as f 
import platform 
import subprocess

import main as m 

 # https://www.geeksforgeeks.org/set-countdown-timer-to-capture-image-using-python-opencv/
def control_volume(img, fingers_up):
    """
    Performs volume control.
    :param img: Frame for displaying the invoked command (i.e. volume up/down, or mute/unmute).
    :param fingers_up: Number of raised fingers.
    """

       
    if fingers_up== [0, 0, 1 ,1, 1]:
        
        if platform.system()=="Windows":
            f.print_action(img, "Descreasing volume")  
            pyautogui.press('volumedown')
        elif platform.system()=="Darwin":
            f.print_action(img, "Descreasing volume") 
            subprocess.run(['osascript', '-e', 'set volume output volume (output volume of (get volume settings) - 5) --100%'])
            
        
    if fingers_up== [0, 1, 1, 1, 1]:
        
        if platform.system()=="Windows":
            f.print_action(img, "Increasing volume")  
            pyautogui.press('volumeup', presses=1)
        elif platform.system()=="Darwin":
            f.print_action(img, "Increasing volume") 
            subprocess.run(['osascript', '-e', 'set volume output volume (output volume of (get volume settings) + 5) --100%'])
            
            
    if  fingers_up==[0, 1, 0, 0, 1] and time.time()-m.timer_volume>=3:
        

        if platform.system()=="Windows":
            f.print_action(img, "Mute/Unmute Volume")  
            pyautogui.press('volumemute', presses=1)
           
    
        elif platform.system()=="Darwin":
            f.print_action(img, "Mute/Unmute Volume")  
            subprocess.run(['osascript', '-e', 'set volume output volume 0'])
        m.timer_volume=time.time()
    elif fingers_up==[0, 1, 0, 0, 1] and time.time()-m.timer_volume<3:
         time_remaining = 4 - (time.time() - m.timer_volume)
         f.print_action(img, f"Mute/Unmute available in {str(time_remaining)[0]} seconds")