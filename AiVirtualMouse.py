import cv2
from cvzone.HandTrackingModule import HandDetector

import numpy as np 
import  pyautogui
import time
import HandTrackingModule as htm

# disabling the pyAutoGui when the mouse moves to corner. 
pyautogui.FAILSAFE = False

def virtual_mouse(): 
    
    frame_reduction = 100; 
    smoothing  =  4; 
    prev_loc_x, prev_loc_y = 0, 0; 
    current_x, curent_y = 0,  0; 
    
    # geting the screen width and height
    screen_width, screen_height = pyautogui.size(); 
    #print(screen_height, screen_width)

    # defining the preview and current frame time 
    prev_frame_time = 0; 
    # defining the hands landmark detector
    detector = htm.handDetector(maxHands=1)


    #* defining the width and height of the webcam 
    web_cam_width, web_cam_height = 640, 480; 
    cap = cv2.VideoCapture(0)
    # resizing the capture of the video
    cap.set(3, web_cam_width); 
    cap.set(4, web_cam_height)

    
    while True:
        succ, img = cap.read()
        
        # finding the hands landmark 
        img = detector.findHands(img)
        Land_mark_list, bounding_box = detector.findPosition(img)
    
        # get the tip of the in dex and middle fingers
        
        if len(Land_mark_list) != 0: 
            
            finger_index_tip_x, finger_index_tip_y = Land_mark_list[8][1:]; 
            middle_finger_tip_x,  middle_finger_tip_y = Land_mark_list[12][1:];
            
            # print(finger_index_tip_x, middle_finger_tip_y, middle_finger_tip_x, middle_finger_tip_y)
        
            # tracking which fingers is open 
        open_fingers = detector.fingersUp(); 
            #print(open_fingers)
        if open_fingers.count(1) == 1 and open_fingers.count(2) == 0:
            
            # draw a rectangle 
            cv2.rectangle(img, (frame_reduction, frame_reduction), (web_cam_width-frame_reduction, web_cam_height- frame_reduction), (0, 128, 0), 3)
        
            # Convert the coordinates
            x3 = np.interp(finger_index_tip_x, (frame_reduction, web_cam_width-frame_reduction), (0, screen_width))
            y3 = np.interp(finger_index_tip_y, (frame_reduction, web_cam_height-frame_reduction), (0, screen_height))
        
            # smoothing mouse movements 
            current_x = prev_loc_x +(x3 -prev_loc_x)/smoothing
            curent_y = prev_loc_y +(y3 -prev_loc_y)/smoothing
        
        # Move the mouse cursor to the new coordinates
            pyautogui.moveTo(current_x, curent_y)
            cv2.circle(img, (finger_index_tip_x, finger_index_tip_y ), 15, (128,0,128), cv2.FILLED)
            prev_loc_x, prev_loc_y = current_x, curent_y
        
        # finding the distance of both fingers 
        if open_fingers[1] == 1 and open_fingers[2] == 1:
            
            length, img,  _ = detector.findDistance(8, 12, img)
            # check if the length is less than 35 perform click
            
            if length<35: 
                
                cv2.circle(img, (finger_index_tip_x, finger_index_tip_y ), 15, (0,128, 0), cv2.FILLED)
                pyautogui.click()

        ## scrolling 
        
        def scrolling (): 
            
            if open_fingers.count(0) ==1 and open_fingers.count(1) == 0:
                text_color = (0,0,255)
                cv2.putText(img, "Scrolling Up", org=(20, 200), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=3.0, color=(255,255,0), thickness=2)
                pyautogui.scroll(3)
        
        # calling the scrolling function
        scrolling()
        #? calculating the Rate frame
        current_frame_time = time.time();  
        fps = 1/(current_frame_time - prev_frame_time); 
        prev_frame_time = current_frame_time; 
        
        position = (20, 50)
        color = (255, 0, 0)
        cv2.putText(img, str(int(fps)), position, cv2.FONT_HERSHEY_PLAIN, 3, color, 3)
        
        cv2.imshow("The frame", img )
        quite =  cv2.waitKey(1) & 0xFF; 
        
        if quite == ord("q"): 
            break
    cap.release()
    cv2.destroyAllWindows()
    




def main(): 
    virtual_mouse()
    

if __name__ =="__main__": 
    main()


