import cv2 
import pyautogui
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.9, maxHands=1) # max hand we increase to 2 that we can used to both hands. 

vidoe = cv2.VideoCapture(0) #? using the default cam 

# we loop through 

while True:
    
    ret, frame = vidoe.read()
    #display the cam 
    hands, imge= detector.findHands(frame)
    
    cv2.rectangle(imge, (0, 480), (300, 425), (255, 0, 0), -2)
    cv2.rectangle(imge, (640, 480), (400, 425), (255, 0, 0), -2)
    
    # we check for the  hands 
    if hands:
        
        for hand in hands: 
            if hand["type"] == "Right":
            
                lmlist = hands[0]
                
                # the fingersUp method finds how many fingers are open and returns to in a list 
                
                finger_up = detector.fingersUp(lmlist)
                
                # we check if the finger up and count it to display the number of it 
                if finger_up == [0, 0, 0, 0 ,0]: 
                    
                    cv2.putText(frame, "Finger count: 0", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                    cv2.putText(frame, "Not Jumping ", (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                    
                        
                if finger_up == [0, 1, 0, 0 ,0]: 
                    
                    cv2.putText(frame, "Finger count: 1", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                    cv2.putText(frame, "Not Jumping ", (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                
                if finger_up == [0, 1, 1, 0 ,0]: 
                    
                    cv2.putText(frame, "Finger count: 2", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                    cv2.putText(frame, "Not Jumping ", (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                
                if finger_up == [0, 1, 1, 1 ,0]: 
                    
                    cv2.putText(frame, "Finger count: 3", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                    cv2.putText(frame, "Not Jumping ", (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                
                if finger_up == [0, 1, 1, 1 ,1]: 
                    
                    cv2.putText(frame, "Finger count: 4", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA) 
                    cv2.putText(frame, "Not Jumping ", (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                
                if finger_up == [1, 1, 1, 1 ,1]: 
                    
                    
                    
                    cv2.putText(frame, "Finger count: 5", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA) 
                    cv2.putText(frame, "Jumping ", (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
                    
                    pyautogui.press('space')
                
        
       #  print(finger_up)
    
    # print the hands 

    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    # quite if the user presses the q 
    if k == ord("q"): 
        break
    
# release the video 

vidoe.release()
cv2.destroyAllWindows()