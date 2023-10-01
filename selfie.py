
import cv2
import time
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.9, maxHands=1)
  
# SET THE COUNTDOWN TIMER
# for simplicity we set it to 3
# We can also take this as input
TIMER = int(3)
   
# Open the camera
cap = cv2.VideoCapture(0)
   
  
while True:
      
    # Read and display each frame
    ret, img = cap.read()
    hands, imge= detector.findHands(img)
    
    cv2.rectangle(imge, (0, 480), (300, 425), (255, 0, 0), -2)
    cv2.rectangle(imge, (640, 480), (400, 425), (255, 0, 0), -2)
    cv2.imshow('a', img)
  
    # check for the key pressed
    k = cv2.waitKey(125)
  
    # set the key for the countdown
    # to begin. Here we set q
    # if key pressed is q
    if hands:
        lmlist = hands[0]
        
        # the fingersUp method finds how many fingers are open and returns to in a list 
        
        finger_up = detector.fingersUp(lmlist)
    # https://www.geeksforgeeks.org/set-countdown-timer-to-capture-image-using-python-opencv/
        if finger_up.count(1) == 2:
           
            prev = time.time()
    
            while TIMER >= 0:
                ret, img = cap.read()
                hands, imge= detector.findHands(img)
                finger_up = detector.fingersUp(lmlist)
                # Display countdown on each frame
                # specify the font and draw the
                # countdown using puttext
                cv2.rectangle(img, (0, 480), (300, 425), (255, 0, 0), -2)
              
                cv2.putText(img, str(TIMER), (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                cv2.imshow('a', img)
                cv2.waitKey(125)
    
                # current time
                cur = time.time()
    
                # Update and keep track of Countdown
                # if time elapsed is one second 
                # then decrease the counter
                if cur-prev >= 1:
                    prev = cur
                    TIMER = TIMER-1
                if hands: 
                      lmlist = hands[0]
        
        # the fingersUp method finds how many fingers are open and returns to in a list 
        
                      finger_up = detector.fingersUp(lmlist)
                if (finger_up.count(1) == 5): 
                     cv2.rectangle(img, (0, 480), (300, 425), (255, 0, 0), -2)
              
                     cv2.putText(img, "LOL", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                     TIMER = int(3)
                     break
            else:
                ret, img = cap.read()
                cv2.imshow('a', img)
                cv2.waitKey(1000)
                cv2.imwrite('camera.jpg', img)
    
                TIMER = int(3)
    
        # Press Esc to exit
        elif k == 27:
            break
  
# close the camera
cap.release()
   
# close all the opened windows
cv2.destroyAllWindows()