import cv2

from HandTrackingModuleWindows import HandDetector
import selfie as s
import volume as v
import brightness as b
import space_keystroke as t
import scrolling as sc
import functions as f 
import activate_mouse as m
import time 
import window as win
import platform as pl

# https://www.geeksforgeeks.org/python-opencv-selectroi-function/
# https://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python
cap = cv2.VideoCapture(0)

current_x, current_y = 0,  0; 
prev_loc_x, prev_loc_y = 0, 0; 


prev_frame_time = 0; 

cap.set(3, 640); 
cap.set(4, 480)

showHand=True

timer=time.time()    
timer_click=time.time()
timer_selfie=time.time()
timer_volume=time.time()
detector = HandDetector(detectionCon=0.9,maxHands=1) 

def main(cap, detector): 
    try: 
      global prev_loc_x
      global prev_loc_y    
      global timer    
      global showHand
      showHand=True            
     
      prev_frame_time = 0; 
      while True: 
         
          _, img = cap.read()
          hands, hand_img = detector.findHands(img, draw=showHand, flipType=True)
          k= cv2.waitKey(1)
      
          if hands:   
              hand = hands[0]
              fingers_up = detector.fingersUp(hand)  
              lmList=hand["lmList"]
              x, y, w, h = hand["bbox"]
            
              if len(hands)==1:          
                if hands[0]["type"]=="Left":  
                                              
                    showHand=s.activate_selfie(img, fingers_up)
                
                    v.control_volume(img, fingers_up) 
                    
                    b.control_brightness(img, detector, lmList, fingers_up)
      
                  
                if hands[0]["type"]=="Right": 
            
                  t.space_keystroke(img, fingers_up)
                      
                  sc.scrolling(img, fingers_up)
                  
                  win.manage_window(img, fingers_up)
                
                  coordinates = m.activate_mouse(img, hand_img, detector, fingers_up, prev_loc_x, prev_loc_y)
                  if coordinates is not None:
                      prev_loc_x, prev_loc_y = coordinates
                        
                
          current_frame_time = time.time();   
          f.get_fps(img, current_frame_time,
                    prev_frame_time) 
          prev_frame_time = current_frame_time; 

          cv2.imshow('PC_Control_System', img) 
          
          if k == 27:
              break
    except Exception as e:
                  print(f"An error occurred: {e}") 

if __name__ =="__main__": 
    main(cap, detector)

