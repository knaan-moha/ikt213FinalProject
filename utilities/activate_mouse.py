import cv2
import os,sys 

from HandTrackingModuleWindows import HandDetector
import numpy as np 
import  pyautogui
import time

import main as m 
import functions as f 

smoothing  =  4; 
frame_reduction = 100; 
web_cam_width, web_cam_height = 640, 480; 
screen_width, screen_height = pyautogui.size(); 

def activate_mouse(img, hand_img, detector, fingers_up, prev_loc_x, prev_loc_y): 
    """
     Invokes cursor control and click.
     :param img: Image where the hand is detected.
     :param hand_img: Image of the detected hand.
     :param detector: Instance of Hand Detector class.
     :param: fingers_up: Number of raised fingers.
     :param: prev_loc_x: Previous x location of the cursor.
     :param: prev_loc_y: Previous y location of the cursor.

    """
    
    if fingers_up==[0, 1, 0, 0, 0] or fingers_up==[0,1,1,0,0]: 
        x_b, y_b =prev_loc_x, prev_loc_y

        Land_mark_list, _ = detector.findPosition(hand_img)
        if len(Land_mark_list) != 0: 
            finger_index_tip_x, finger_index_tip_y = Land_mark_list[8][1:]; 
           
        
            
        if fingers_up.count(1) == 1:
            
            # drawing  a rectangle 
            cv2.rectangle(img, (frame_reduction, frame_reduction), (web_cam_width-frame_reduction, web_cam_height- frame_reduction), (0, 128, 0), 3)

            # Convert the coordinates
            x3 = np.interp(finger_index_tip_x, (frame_reduction, web_cam_width-frame_reduction), (0, screen_width))
            y3 = np.interp(finger_index_tip_y, (frame_reduction, web_cam_height-frame_reduction), (0, screen_height))

            # smoothing mouse movements 
            current_x = prev_loc_x +(x3 -prev_loc_x)/smoothing
            current_y = prev_loc_y +(y3 -prev_loc_y)/smoothing

            # Move the mouse cursor to the new coordinates

            pyautogui.moveTo(current_x, current_y)
         
            cv2.circle(img, (finger_index_tip_x, finger_index_tip_y ), 15, (128,0,128), cv2.FILLED)
            prev_loc_x, prev_loc_y = current_x, current_y
            
            f.print_action(img, "Mouse")
        
        
            if prev_loc_x>=0 and prev_loc_y>=0: 
                return prev_loc_x, prev_loc_y
            else:
                return x_b, y_b
            
        if fingers_up.count(1)==2:
                       
                        length, _, img = detector.findDistance(Land_mark_list[8][1:], Land_mark_list[12][1:], img, color=(255, 0, 255),
                                                    scale=10)
                        if length<35 and time.time()-m.timer_click>=3: 
                            f.print_action(img, "Perform Click")
                            cv2.circle(img, (finger_index_tip_x, finger_index_tip_y ), 15, (0,128, 0), cv2.FILLED)
                            pyautogui.click()
                            m.timer_click=time.time()
                        elif length<35 and time.time()-m.timer_click<3: 
                            
                            f.print_action(img, "Click will be available in: "+str(4-(time.time()-m.timer_click))[0])
                        
      