import cv2
from cvzone.HandTrackingModule import HandDetector

import numpy as np 
import  pyautogui
import time
import HandTrackingModule as htm
import fpsFile as fps





# disabling the pyAutoGui when the mouse moves to corner. 
pyautogui.FAILSAFE = False
cap = cv2.VideoCapture(0)
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
    detector = htm.handDetector(detectionCon=0.9,maxHands=1)


    #* defining the width and height of the webcam 
    web_cam_width, web_cam_height = 640, 480; 
    
    # resizing the capture of the video
    cap.set(3, web_cam_width); 
    cap.set(4, web_cam_height)

    
    while True:
        succ, img = cap.read()
        
        # finding the hands landmark 
        hands, img = detector.findHands(img)
        Land_mark_list, bounding_box = detector.findPosition(img)
     
        if hands: 
            for hand in hands: 
                
                #tracking hand type
                if hand["type"] == "Right":    
                # get the tip of the index and middle fingers
                    if len(Land_mark_list) != 0: 
                        finger_index_tip_x, finger_index_tip_y = Land_mark_list[8][1:]; 
                        middle_finger_tip_x,  middle_finger_tip_y = Land_mark_list[12][1:];
                        # print(finger_index_tip_x, middle_finger_tip_y, middle_finger_tip_x, middle_finger_tip_y)
                        # tracking which fingers is open 
                    open_fingers = detector.fingersUp(); 
                        #print(open_fingers)
                    if open_fingers.count(1) == 1 and open_fingers.count(2) == 0:
    
                        # drawing  a rectangle 
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
                        cv2.putText(img,"Mouse", (20, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                    
                        # finding the distance of both fingers 
                    if open_fingers[1] == 1 and open_fingers[2] == 1:
                        length, img, _ = detector.findDistance(8, 12, img)
                        # check if the length is less than 35 perform click
                        if length<35: 
                            cv2.putText(img,"Perform Click", (20, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                            cv2.circle(img, (finger_index_tip_x, finger_index_tip_y ), 15, (0,128, 0), cv2.FILLED)
                            pyautogui.click()
                        
                        #Performing scroll up by tracking the index finger and thumb
                    if sum(open_fingers[0:2]) == 2 and sum(open_fingers[2:]) == 0:
                        
                        cv2.putText(img,"Scrolling Up", (20, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                        pyautogui.scroll(3) 
                        pyautogui.scroll(3) 
                         #Performing scroll up by tracking the index finger and thumb
                    elif sum(open_fingers[2:5]) == 3 and sum(open_fingers[0:2]) == 0 :
                                
                                cv2.putText(img,"Scrolling Down", (20, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                                pyautogui.scroll(-3)
                            
 
                            
                    #? calculating the Rate frame
                    current_frame_time = time.time();  
                    fps.getFps(img, current_frame_time, prev_frame_time) 
                    prev_frame_time = current_frame_time; 
                    
                    
                    
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


