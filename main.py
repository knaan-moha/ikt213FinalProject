import cv2

from cvzone.HandTrackingModule import HandDetector
import selfie as s
import volume as v
import brightness as b
import trex_game as t
import scrolling as sc
import functions as f 
import pyautogui
import activate_mouse as m
import time 



  # https://www.geeksforgeeks.org/python-opencv-selectroi-function/

cap = cv2.VideoCapture(0)
frame_reduction = 100; 
smoothing  =  4; 
prev_loc_x, prev_loc_y = 0, 0; 
current_x, current_y = 0,  0; 

# geting the screen width and height
screen_width, screen_height = pyautogui.size(); 
#print(screen_height, screen_width)
# defining the preview and current frame time 
prev_frame_time = 0; 


#* defining the width and height of the webcam 
web_cam_width, web_cam_height = 640, 480; 

# resizing the capture of the video
cap.set(3, web_cam_width); 
cap.set(4, web_cam_height)

detector = HandDetector(detectionCon=0.9,maxHands=1)
def main(cap, detector): 
    
    prev_frame_time = 0; 
    while True: 
        ret, img = cap.read()
        hands, hand_img = detector.findHands(img, draw=True, flipType=True)
        k= cv2.waitKey(1)
     
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
              
                  
                  v.control_volume(img, finger_up) 
                  if finger_up==[1, 1, 0, 0, 0]:   
                    b.control_brightness(img, detector, lmList1)

                 
          
              if hands[0]["type"]=="Right": 
                if finger_up.count(1)==5: 
                  t.space_keystroke(img, finger_up)
                 
                sc.scrolling(img, finger_up)
                if finger_up.count(1)==1:
                     x, y=m.activate_mouse(img, hand_img,detector, finger_up, frame_reduction, web_cam_width, web_cam_height, screen_width, screen_height, smoothing, prev_loc_x, prev_loc_y)
                if x is not None and y is not None: 
                     prev_loc_x=x
                     prev_loc_y=y
               #? calculating the Rate frame
        current_frame_time = time.time();  
        f.get_fps(img, current_frame_time, prev_frame_time) 
        prev_frame_time = current_frame_time; 

        cv2.imshow('PC_Control_System', img)
        
        if k == 27:
            break
       

main(cap, detector)