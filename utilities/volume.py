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
    :param img: Frame for displaying the invoked command (i.e. increasing/decreasing volume, or mute/unmute).
    :param fingers_up: Number of raised fingers.
    """

    # check if the raised fingers are the middle finger, ring finger, and pinky finger   
    if fingers_up== [0, 0, 1 ,1, 1]:
        # check if the code is running on Windows
        if platform.system()=="Windows":
            f.print_action(img, "Descreasing volume")  
            pyautogui.press('volumedown')
        # check if the code is running on macOS 
        elif platform.system()=="Darwin":
            f.print_action(img, "Descreasing volume") 
            subprocess.run(['osascript', '-e', 'set volume output volume (output volume of (get volume settings) - 5) --100%'])
            
    # check if the raised fingers are the index finger, middle finger, ring finger, and pinky finger
    if fingers_up== [0, 1, 1, 1, 1]:
        # check if the code is runnng on Windows
        if platform.system()=="Windows":
            f.print_action(img, "Increasing volume")  
            pyautogui.press('volumeup', presses=1)
         # check if the code is running on macOS
        elif platform.system()=="Darwin":
            f.print_action(img, "Increasing volume") 
            subprocess.run(['osascript', '-e', 'set volume output volume (output volume of (get volume settings) + 5) --100%'])
            
    # check if the raised fingers are the index finger and the pinky finger  
    # and 
    # check if the count up timer has reached 3 seconds 
    if  fingers_up==[0, 1, 0, 0, 1] and time.time()-m.timer_volume>=3:
        
        # check if the code is running on Windows 
       
        if platform.system()=="Windows":
            f.print_action(img, "Mute/Unmute Volume")  
            pyautogui.press('volumemute', presses=1)
           
        # chheck if the code is running on macOS
        elif platform.system()=="Darwin":
            f.print_action(img, "Mute/Unmute Volume")  
            subprocess.run(['osascript', '-e', 'set volume output volume 0'])
        # update the count up timer
        m.timer_volume=time.time()
    # check if the raised fingers are the index finger and the pinky finger  
    # and 
    # check if the count up timer has not reached 3 seconds
    elif fingers_up==[0, 1, 0, 0, 1] and time.time()-m.timer_volume<3:
         time_remaining = 4 - (time.time() - m.timer_volume)
         f.print_action(img, f"Mute/Unmute available in {str(time_remaining)[0]} seconds")