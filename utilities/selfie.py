
import cv2
import time
import functions as f 
import main as m 


def activate_selfie(img, fingers_up):
    """
    Takes selfie and saves it in the project repository. 
    Returns the False or True boolean value that is used to hide or display the bounding box of the hand, respectively. 
    :param img: Frame for notifying when the command can be invoked (i.e. countdown for selfie)
    :param fingers_up: Number of raised fingers.
    """
   
    if fingers_up==[0,1,1, 0, 0]:
        

        if time.time()-m.timer_selfie>=3:
          
           
           cv2.imwrite('taken_selfie.jpg', img)
       
       
           cv2.waitKey(1000)
           m.timer_selfie=time.time()
           return True
           
        else:
            f.print_action(img, "Selfie in "+str(4-(time.time()-m.timer_selfie))[0])
            return False 
    else: 
        m.timer_selfie =time.time()
        return True        
        


