
import cv2
import sys, os

from HandTrackingModuleWindows import HandDetector

sys.path.append(os.path.dirname(os.path.abspath("utilities")))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath("utilities")), 'utilities'))

import utilities.selfie as s
import utilities.volume as v
import utilities.brightness as b
import utilities.space_keystroke as t
import utilities.scrolling as sc
import utilities.functions as f 
import utilities.activate_mouse as m
import time 
import utilities.window as win
import platform as pl

# https://www.geeksforgeeks.org/python-opencv-selectroi-function/
# https://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python
cap = cv2.VideoCapture(0)


# variables used to store the current location of the cursor 
current_x, current_y = 0,  0; 
# variables uses to store the previous location of the cursor 
prev_loc_x, prev_loc_y = 0, 0; 



prev_frame_time = 0; 

cap.set(3, 640); 
cap.set(4, 480)

# boolean to display the boudning box of the hand 
showBBox =True

#timers used for countdowns to avoid redundant activation of the invoked commands 
timer_window=time.time()    
timer_click=time.time()
timer_selfie=time.time()
timer_volume=time.time()


# an instance of the HandDetector class that is used to detect a hand within an image 
detector = HandDetector(detectionCon=0.9,maxHands=1) 

def main(cap, detector): 
    try: 
    #   mark variables as globals so that they are not perceived as local variables by the interpreter 
      global prev_loc_x, prev_loc_y     
      global prev_frame_time
      global showBBox 
      global timer_window, timer_click, timer_selfie, timer_volume
      showBBox =True            
      
       
      while True: 
         
          _, img = cap.read()
        #   find hands and draw the bouding box
          hands, hand_img = detector.findHands(img, draw=showBBox , flipType=True)
          k= cv2.waitKey(1)
        #   if hand is detected 
          if hands:   
            detected_hand = hands[0]
            # get the number of raised fingers 
            fingers_up = detector.fingersUp(detected_hand)  
            # get the hand landmarks associated with the detected hand 
            lmList=detected_hand["lmList"]
            x, y, w, h = detected_hand["bbox"]
            
            # If the detected hand is the left hand 
            if hands[0]["type"]=="Left":  
                                            
                showBBox =s.activate_selfie(img, fingers_up)
            
                v.control_volume(img, fingers_up) 
                
                b.control_brightness(img, detector, lmList, fingers_up)
    
            # if the detected hand is the right hand 
            if hands[0]["type"]=="Right": 

                t.space_keystroke(img, fingers_up)
                    
                sc.perform_scrolling(img, fingers_up)
                
                win.manage_window(img, fingers_up)
            
                coordinates = m.activate_mouse(img, hand_img, detector, fingers_up, prev_loc_x, prev_loc_y)
                if coordinates is not None:
                    # store the cursor coordinates 
                    prev_loc_x, prev_loc_y = coordinates
                        
           
          current_frame_time = time.time();   
          f.get_fps(img, current_frame_time,
                    prev_frame_time) 
          prev_frame_time = current_frame_time; 

          cv2.imshow('PC_Control_System', img) 
          
          if k == 27:
              break
    except Exception as e:
                  print(f"Error: {e}") 



if __name__ !="__main__": 
    main(cap, detector)


