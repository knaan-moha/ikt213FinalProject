import pyautogui
import cv2
import time
from cvzone.HandTrackingModule import HandDetector


detector = HandDetector(detectionCon=0.9, maxHands=2)
  

   

cap = cv2.VideoCapture(0)
   

def control_volume(cap, detector):
    TIMER = int(3)
    while True:
        
        # Read and display each frame
        ret, img = cap.read()
        
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

            if finger_up.count(1) == 5 and hands[0]["type"]=="Left": 
                cv2.putText(img, "LOL", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                pyautogui.press('volumemute', presses=1, interval=0.35)

        
        cv2.imshow('a', img)
       
        # check for the key pressed
        k = cv2.waitKey(125)  
        if k == 27:
            break
                
                
    
    
control_volume(cap, detector)