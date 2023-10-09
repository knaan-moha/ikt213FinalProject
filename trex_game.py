import cv2 
import pyautogui
from cvzone.HandTrackingModule import HandDetector



def space_keystroke(img, finger_up):

    # we loop through 

        
    cv2.rectangle(img, (0, 480), (300, 425), (255, 0, 0), -2)
    cv2.rectangle(img, (640, 480), (400, 425), (255, 0, 0), -2)
        
        # we check for the  hands 

                
    if finger_up.count(1) == 5:
        
        
        
        cv2.putText(img, "Finger count: 5", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA) 
        cv2.putText(img, "Jumping ", (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        pyautogui.press('space')

    else: 
        cv2.putText(img, "Finger count: 4", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA) 
        cv2.putText(img, "Not Jumping ", (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

    #  print(finger_up)

    # print the hands 

  