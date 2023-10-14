import cv2
from cvzone.HandTrackingModule import HandDetector
import HandTrackingModule as htm
import numpy as np 
import  pyautogui
import time
import HandTrackingModule as htm



def activate_mouse(img, hand_img, detector, fingers_up, frame_reduction, web_cam_width, web_cam_height, screen_width, screen_height, smoothing, prev_loc_x, prev_loc_y): 
    x_b, y_b =prev_loc_x, prev_loc_y

    Land_mark_list, bounding_box = detector.findPosition(hand_img)
    if len(Land_mark_list) != 0: 
        finger_index_tip_x, finger_index_tip_y = Land_mark_list[8][1:]; 
        middle_finger_tip_x,  middle_finger_tip_y = Land_mark_list[12][1:];
    
        #print(open_fingers)
    if fingers_up.count(1) == 1:
        pass
        # # drawing  a rectangle 
        cv2.rectangle(img, (frame_reduction, frame_reduction), (web_cam_width-frame_reduction, web_cam_height- frame_reduction), (0, 128, 0), 3)

        # # Convert the coordinates
        x3 = np.interp(finger_index_tip_x, (frame_reduction, web_cam_width-frame_reduction), (0, screen_width))
        y3 = np.interp(finger_index_tip_y, (frame_reduction, web_cam_height-frame_reduction), (0, screen_height))

        # # # smoothing mouse movements 
        current_x = prev_loc_x +(x3 -prev_loc_x)/smoothing
        current_y = prev_loc_y +(y3 -prev_loc_y)/smoothing

        # # Move the mouse cursor to the new coordinates
        pyautogui.moveTo(current_x, current_y)
        cv2.circle(img, (finger_index_tip_x, finger_index_tip_y ), 15, (128,0,128), cv2.FILLED)
        prev_loc_x, prev_loc_y = current_x, current_y
        cv2.putText(img,"Mouse", (20, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
      
        if prev_loc_x>=0 and prev_loc_y>=0: 
           return prev_loc_x, prev_loc_y
        else:
           return x_b, y_b
        