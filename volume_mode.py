import pyautogui
import cv2
import time
from cvzone.HandTrackingModule import HandDetector


pyautogui.press('volumedown', presses=3)

def control_volume(cap, detector):
    TIMER = int(3)
    while True:
        
        # Read and display each frame
        ret, img = cap.read()
        cv2.rectangle(img, (950, 00), (1500, 60), (100, 160, 100), -2)
        cv2.putText(img, "Mode 4: Volume", (950, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        hands, imge= detector.findHands(img)
        cv2.rectangle(img, (0, 480), (400, 425), (255, 0, 0), -2)
       
    
        # set the key for the countdown
        # to begin. Here we set q
        # if key pressed is q
        if hands:
            lmlist = hands[0]
            
            # the fingersUp method finds how many fingers are open and returns to in a list 
            
            finger_up = detector.fingersUp(lmlist)
        # https://www.geeksforgeeks.org/set-countdown-timer-to-capture-image-using-python-opencv/
            if finger_up.count(1) == 2:
                
                cv2.putText(img,"Descreasing volume", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
              
                pyautogui.press('volumedown', presses=1)
                
       
                
      
                
            if finger_up.count(1) == 3:
                pyautogui.press('volumeup', presses=1)
               
                cv2.putText(img,"Increasing volume", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        
        cv2.imshow('a', img)
       
        # check for the key pressed
        k = cv2.waitKey(125)  
        if k == 27:
            break
                
                
    
    
