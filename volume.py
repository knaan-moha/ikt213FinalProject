import pyautogui
import cv2
import time
from cvzone.HandTrackingModule import HandDetector
import functions as f 

 # https://www.geeksforgeeks.org/set-countdown-timer-to-capture-image-using-python-opencv/
def control_volume(img, finger_up):
          
       
            if finger_up== [0, 0, 1 ,1, 1]:
                f.print_action(img, "Descreasing volume")  
                pyautogui.press('volumedown', presses=1)
                
       
                
            if finger_up== [0, 1, 1, 1, 1]:
                f.print_action(img, "Increasing volume")  
                pyautogui.press('volumeup', presses=1)
                

            if finger_up==[0, 1, 0, 0, 1]: 
                f.print_action(img, "Mute/Unmute Volume")  

                pyautogui.press('volumemute', presses=1, interval=0.35)
               
           
        # check for the key pressed
        
                

