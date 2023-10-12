import cv2
import time
from cvzone.HandTrackingModule import HandDetector
import selfie as s
import volume as v
import brightness as b
import trex_game as t
import scrolling as sc


detector = HandDetector(detectionCon=0.9, maxHands=2)

# https://www.geeksforgeeks.org/python-opencv-selectroi-function/

cap = cv2.VideoCapture(0)

def main(cap, detector): 
    while True: 
        ret, img = cap.read()
        hands, hand_img = detector.findHands(img, draw=True, flipType=True)
        k= cv2.waitKey(125)
     
        hand_roi=img
        if hands:   
            hand1 = hands[0]
            finger_up = detector.fingersUp(hand1)  
            lmList1=hand1["lmList"]
            x, y, w, h = hand1["bbox"]
  
         
        
            # https://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python
            hand_roi =img[y:y+h, x:x+w]
        
          
            if len(hands)==1:
              if hands[0]["type"]=="Left":  
                  if finger_up==[0,1,1, 0, 0]:
                    s.test_activate_selfie(cap, detector)
                  
                  
                  v.test2_control_volume(img, finger_up) 
                  if finger_up==[1, 1, 0, 0, 0]:   
                    b.test_control_brightness(img, detector, lmList1)
                 
                
                  # v.test2_control_volume(img, finger_up) 
          
              if hands[0]["type"]=="Right": 
                if finger_up.count(1)==5: 
                   t.space_keystroke(img, finger_up)
                else: 
                  sc.scrolling(img, finger_up)

        cv2.imshow('PC_Control_System', img)
        
        if k == 27:
            break
       

main(cap, detector)