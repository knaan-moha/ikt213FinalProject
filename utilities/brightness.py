from HandTrackingModuleWindows import HandDetector
import cv2
import screen_brightness_control as sbc
import functions as f 
# https://github.com/cvzone/cvzone

import platform 
def control_brightness(img, detector, lmList, fingers_up):
    """
     Performs brigthness control.
     :param img: Frame for displaying the invoked command (i.e. brightness percentage).
     :param detector: Instance of Hand Detector class.
     :param lmList: List of detected hand landmarks. 
     :param fingers_up: Number of raised fingers.
     """
     
    if fingers_up==[1, 1, 0, 0, 0] and platform.system()=="Windows":    
        length, info, img = detector.findDistance(lmList[4][0:2], lmList[8][0:2], img, color=(255, 0, 255),
                                                    scale=10)
       
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
        else: 
            cv2.putText(img, str(length), (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
 