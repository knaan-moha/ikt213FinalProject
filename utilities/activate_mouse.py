import cv2
from HandTrackingModuleWindows import HandDetector
import numpy as np 
import  pyautogui
import time

import main as m 
import functions as f 
# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-set

# set failsafe to False to prevent the program from crashing if the cursor 
# gets outside the screen 
pyautogui.FAILSAFE = False
# https://www.youtube.com/watch?v=8gPONnGIPgw&t=460s
# https://www.investopedia.com/terms/i/interpolation.asp#:~:text=Interpolation%20is%20a%20mathematical%20technique,helps%20fill%20in%20the%20blanks.

smoothing  =  4; 
# value that will be used to calcualte the "reduced" version of the real screen (i.e. the small scale screen)
frame_reduction = 100; 
# set the width and height of the video frame 
web_cam_width, web_cam_height = 640, 480; 
# get the size of the screen 
screen_width, screen_height = pyautogui.size(); 

def activate_mouse(img, hand_img, detector, fingers_up, prev_loc_x, prev_loc_y): 
    """
     Invokes cursor control and click.
     :param img: Image where the hand is detected.
     :param hand_img: Image of the detected hand.
     :param detector: Instance of Hand Detector class.
     :param fingers_up: Number of raised fingers.
     :param prev_loc_x: Previous x location of the cursor.
     :param prev_loc_y: Previous y location of the cursor.

    """
    # if the index finger is raised 
    # or 
    # if the raised fingers are the index and middle fingers 
    if fingers_up==[0, 1, 0, 0, 0] or fingers_up==[0,1,1,0,0]: 
        stored_x_coordinate, stored_y_coordinate =prev_loc_x, prev_loc_y
        # get the coordinates of hand landmarks 
        Land_mark_list, _ = detector.findPosition(hand_img)
        if len(Land_mark_list) != 0: 
            # get the tip of the index finger which is stored in landmark nr 8
            finger_index_tip_x, finger_index_tip_y = Land_mark_list[8][1:]; 
           
        
        # if the index finger is the only finger raised (i.e. one finger)
        if fingers_up.count(1) == 1:
            
            # drawing a green rectangle for the reduced version of the screen 
            cv2.rectangle(img, (frame_reduction, frame_reduction), (web_cam_width-frame_reduction, web_cam_height- frame_reduction), (0, 128, 0), 3)

            # provide the coordinates of the tip of the finger in relation to the reduced version of the screen 
            # and find the coordinates in relation to the real screen 
            converted_x_coordinate = np.interp(finger_index_tip_x, (frame_reduction, web_cam_width-frame_reduction), (0, screen_width))
            converted_y_coordinate = np.interp(finger_index_tip_y, (frame_reduction, web_cam_height-frame_reduction), (0, screen_height))

            # smoothing mouse movements to prevent jiggling 
            current_x = prev_loc_x +(converted_x_coordinate -prev_loc_x)/smoothing
            current_y = prev_loc_y +(converted_y_coordinate -prev_loc_y)/smoothing

            # Move the mouse cursor to the new coordinates

            pyautogui.moveTo(current_x, current_y)
            # draw a circle around the tip of the index finger 
            cv2.circle(img, (finger_index_tip_x, finger_index_tip_y ), 15, (128,0,128), cv2.FILLED)
            # update the coordinates of the cursor 
            prev_loc_x, prev_loc_y = current_x, current_y
            
            f.print_action(img, "Mouse")
        
            # check if the coordinates have been found 
            # prevents the program from crashing in some instances 
            if prev_loc_x>=0 and prev_loc_y>=0: 
                # return the updated coordinates
                return prev_loc_x, prev_loc_y
            else:
                # return the coordinates that have not beed updated 
                return stored_x_coordinate, stored_y_coordinate
        # if the index and middle fingers are raised (i.e. two fingers)
        if fingers_up.count(1)==2:
                        # find the distance between the tip of the index finger (i.e. landmark 8) 
                        # and the tip of the index finger (i.e. landmark 12 )
                        length, _, img = detector.findDistance(Land_mark_list[8][1:], Land_mark_list[12][1:], img, color=(255, 0, 255),
                                                    scale=10)
                        # check if the distance between the fingers is less than 35
                        # check if the count up timer has reached 3 seconds (or more) 
                        if length<35 and time.time()-m.timer_click>=3: 
                            f.print_action(img, "Perform Click")
                            cv2.circle(img, (finger_index_tip_x, finger_index_tip_y ), 15, (0,128, 0), cv2.FILLED)
                            # perform click
                            pyautogui.click()
                            m.timer_click=time.time()
                        # if the distance is less than 35 but the count up timer has not reached 3 seconds
                        elif length<35 and time.time()-m.timer_click<3: 
                            
                            f.print_action(img, "Click will be available in: "+str(4-(time.time()-m.timer_click))[0])
                        
      