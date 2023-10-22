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



current_x, current_y = 0,  0; 

# geting the screen width and height
# screen_width, screen_height = pyautogui.size(); 
#print(screen_height, screen_width)
# defining the preview and current frame time 
prev_frame_time = 0; 
prev_loc_x, prev_loc_y = 0, 0; 

#* defining the width and height of the webcam 
# web_cam_width, web_cam_height = 640, 480; 

# resizing the capture of the video
# cap.set(3, web_cam_width); 
# cap.set(4, web_cam_height)
cap.set(3, 640); 
cap.set(4, 480)

detector = HandDetector(detectionCon=0.9,maxHands=1)
def main(cap, detector): 
    global prev_loc_x
    global prev_loc_y
 
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
                
                  s.test_activate_selfie(cap, detector, finger_up)
              
                  v.control_volume(img, finger_up) 
                 
                  b.control_brightness(img, detector, lmList1, finger_up)
    
                 
              if hands[0]["type"]=="Right": 
              
               t.space_keystroke(img, finger_up)
                  
               sc.scrolling(img, finger_up)
              
               try:
                  coordinates = m.activate_mouse(img, hand_img, detector, finger_up, prev_loc_x, prev_loc_y)
                  if coordinates is not None:
                    prev_loc_x, prev_loc_y = coordinates
                   
               except Exception as e:
                  print(f"An error occurred: {e}")
              
        current_frame_time = time.time();   
        f.get_fps(img, current_frame_time, prev_frame_time) 
        prev_frame_time = current_frame_time; 

        cv2.imshow('PC_Control_System', img)
        
        if k == 27:
            break
       

main(cap, detector)