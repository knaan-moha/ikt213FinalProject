import pyautogui
import cv2
import time
import functions as f 

 # https://www.geeksforgeeks.org/set-countdown-timer-to-capture-image-using-python-opencv/
def control_volume(img, finger_up):
    """
    Performs volume control.
    :param img: Frame for displaying the invoked command (i.e. volume up/down, or mute/unmute).
    :param fingers_up: Number of raised fingers.
    """

       
    if finger_up== [0, 0, 1 ,1, 1]:
        f.print_action(img, "Descreasing volume")  
        pyautogui.press('volumedown', presses=1)
        
        
    if finger_up== [0, 1, 1, 1, 1]:
        f.print_action(img, "Increasing volume")  
        pyautogui.press('volumeup', presses=1)
        

    if finger_up==[0, 1, 0, 0, 1]: 
        f.print_action(img, "Mute/Unmute Volume")  

        pyautogui.press('volumemute', presses=1, interval=0.60)
