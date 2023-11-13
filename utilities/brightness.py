import cv2
import screen_brightness_control as sbc
import functions as f 
import subprocess

import platform 
# https://github.com/cvzone/cvzone


def control_brightness(img, detector, lmList, fingers_up):
    """
     Performs brigthness control.
     :param img: Frame for displaying the invoked command (i.e. brightness percentage, increasing/decreasing brightness).
     :param detector: Instance of Hand Detector class.
     :param lmList: List of detected hand landmarks. 
     :param fingers_up: Number of raised fingers.
     """
     
    if fingers_up==[1, 1, 0, 0, 0]:  
        # find the distance between the tip of the index finger (i.e. landmark nr 8)
        # and the tip of the thumb (i.e. landmark nr 4)  
        length, _, img = detector.findDistance(lmList[4][0:2], lmList[8][0:2], img, color=(255, 0, 255),
                                                    scale=10)    
        # if the code is running of windows
        if platform.system()== "Windows":      
            # set the brightness to a certain value 
            # depending on the distance between the tip of the index finger and thumb
            if (length>360): 
                f.print_action(img, "Brightness: 100 ")
                sbc.set_brightness(100, display=0)
            elif (length<=360 and length>320): 
                f.print_action(img, "Brightness: 90 ")
                sbc.set_brightness(90, display=0)
            elif (length<=320 and length>280): 
                f.print_action(img, "Brightness: 80 ")
                sbc.set_brightness(80, display=0)
            elif (length<=280 and length>240): 
                f.print_action(img, "Brightness: 70 ")
                sbc.set_brightness(70, display=0)
            elif (length<=240 and length>200): 
                f.print_action(img, "Brightness: 60 ")
                sbc.set_brightness(60, display=0)
            elif (length<=200 and length>160): 
                f.print_action(img, "Brightness: 50 ")
                sbc.set_brightness(50, display=0)
            elif (length<=160 and length>120): 
                f.print_action(img, "Brightness: 40 ")
                sbc.set_brightness(40, display=0)
            elif (length<=120 and length>80): 
                f.print_action(img, "Brightness: 30 ")
                sbc.set_brightness(30, display=0)
            elif (length<=80 and length>40): 
                f.print_action(img, "Brightness: 20 ")
                sbc.set_brightness(20, display=0)
            elif (length<=40 and length>0): 
                f.print_action(img, "Brightness: 10 ")
                sbc.set_brightness(10, display=0)
            
        # if the code is running on macOS
        elif platform.system()=="Darwin":
                # either increase or decrease brightness 
                # depending on the distance between the tip of the index finger and thumb 
                
                if 360>length and 100<=length: 
                        f.print_action(img, "Increasing Brightness")
                        subprocess.run(['osascript', '-e', 'tell application "System Events"', '-e', 'key code 144', '-e', 'end tell'])
            
                elif length<100 and length>0: 
                        f.print_action(img, "Decreasing Brightness")
                        subprocess.run(['osascript', '-e', 'tell application "System Events"', '-e', 'key code 145', '-e', 'end tell'])
                
        
                       