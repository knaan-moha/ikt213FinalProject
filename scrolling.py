import cv2
import pyautogui

def scrolling(img, finger_up): 
    print("here")
    if sum(finger_up[0:2]) == 2 and sum(finger_up[2:]) == 0:
                        
                    
                        cv2.putText(img, "Scrolling Up", org=(20, 200), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1.0,
                                    color=(255, 255, 0), thickness=2)
                        pyautogui.scroll(3) 
                        
    elif sum(finger_up[2:5]) == 3 and sum(finger_up[0:2]) == 0 :
                                cv2.putText(img, "Scrolling Down", org=(20, 200), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1.0,
                                        color=(255, 255, 0), thickness=2)
                                pyautogui.scroll(-3)
