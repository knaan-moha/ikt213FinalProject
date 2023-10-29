import cv2
import time
from HandTrackingModuleWindows import HandDetector
import functions as f 
import main as m 
# ! write doc string for this: 

def test_activate_selfie(img, detector, finger_up):
   
    if finger_up==[0,1,1, 0, 0]:
        
        
        if time.time()-m.timer_selfie>=3:
           cv2.waitKey(1000)
           cv2.imwrite('camera.jpg', img)
           m.timer_selfie=time.time()
        else:
            f.print_action(img, "Selfie in:"+str(4-(time.time()-m.timer_selfie))[0])
        
