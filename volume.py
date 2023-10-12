import pyautogui
import cv2
import time
from cvzone.HandTrackingModule import HandDetector


def test2_control_volume(img, finger_up):
          
        # https://www.geeksforgeeks.org/set-countdown-timer-to-capture-image-using-python-opencv/
            if finger_up.count(1) == 3:
                
                cv2.putText(img,"Descreasing volume", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
              
                pyautogui.press('volumedown', presses=1)
                
       
                
            if finger_up.count(1) == 4:
                pyautogui.press('volumeup', presses=1)
               
                cv2.putText(img,"Increasing volume", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

            if finger_up==[0, 1, 0, 0, 1]: 
                cv2.putText(img, "Mute", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                pyautogui.press('volumemute', presses=1, interval=0.35)
                print("mute")
           
        # check for the key pressed
        
                