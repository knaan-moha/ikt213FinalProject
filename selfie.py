import cv2 
import pyautogui
import keyboard
import time

from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.9, maxHands=1) 

video = cv2.VideoCapture(0)


while True:

    ret, frame = video.read()
   
    hands, imge= detector.findHands(frame)
    
    cv2.rectangle(imge, (0, 480), (300, 425), (255, 0, 0), -2)
    cv2.rectangle(imge, (640, 480), (400, 425), (255, 0, 0), -2)
    cv2.imshow("GeeksForGeeks", frame)
    

    if keyboard.is_pressed('b'):
        cv2.imwrite("selfie.png", frame)
    
    k = cv2.waitKey(1)
    if k == ord("q"): 
        break


