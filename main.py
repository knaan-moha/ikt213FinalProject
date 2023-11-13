
import cv2
import sys, os
from HandTrackingModuleWindows import HandDetector

# storing the path of the utilities folder in the system path 
# so that the files in the utilities folder can be used in main.py
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


# https://www.geeksforgeeks.org/python-opencv-selectroi-function/
# https://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python
cap = cv2.VideoCapture(0)
# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-set
cap.set(cv2.CAP_PROP_FRAME_WIDTH, m.web_cam_width); 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, m.web_cam_height)



# variables used to store the current location of the cursor 
current_x, current_y = 0,  0; 
# variables uses to store the previous location of the cursor 
prev_loc_x, prev_loc_y = 0, 0; 

# the time of the previous time (used in the beginning)
prev_frame_time = 0; 


# boolean to display the boudning box of the hand 
showBBox =True

#timers used for count ups to avoid redundant activation of the invoked commands 
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
      # the variable used to hide and display the boudnif box of the detected hand 
      showBBox =True            
      
       
      while True: 
         
          _, img = cap.read()
        #  find hands and draw the bouding box
          hands, hand_img = detector.findHands(img, draw=showBBox , flipType=True)
          k= cv2.waitKey(1)
        #  if hand is detected   
          if hands:   
            detected_hand = hands[0]
            # get the number of raised fingers 
            fingers_up = detector.fingersUp(detected_hand)  
            # get the hand landmarks associated with the detected hand 
            lmList=detected_hand["lmList"]
           
            
            # If the detected hand is the left hand 
            if hands[0]["type"]=="Left":  
            # activate_selfie returns False if a selfie is being taken
            # otherwise returns True  
                showBBox =s.activate_selfie(img, fingers_up)
            # volume control function:
                v.control_volume(img, fingers_up) 
            #  brightness control function
                b.control_brightness(img, detector, lmList, fingers_up)
    
            # if the detected hand is the right hand 
            elif hands[0]["type"]=="Right": 
              
            # space keystroke 
                t.space_keystroke(img, lmList, fingers_up)
            # scrolling function 
                sc.perform_scrolling(img, lmList, fingers_up)
            # window management function
                win.manage_window(img, fingers_up)
            # cursor control function tht returns the "saved" coordinates of the cursor 
                coordinates = m.activate_mouse(img, hand_img, detector, fingers_up, prev_loc_x, prev_loc_y)
                if coordinates is not None:
                    # store the cursor coordinates 
                    prev_loc_x, prev_loc_y = coordinates
                        
          # calculating fps:  
          current_frame_time = time.time();   
          f.get_fps(img, current_frame_time,
                    prev_frame_time) 
          prev_frame_time = current_frame_time; 

          cv2.imshow('PC_Control_System', img) 
          
          if k == 27:
              break
    except Exception as e:
                  print(f"Error: {e}") 



if __name__ =="__main__": 
    main(cap, detector)


