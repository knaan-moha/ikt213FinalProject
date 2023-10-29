
import cv2

def print_action(img, input):
     """
     Prints out the test associated with the invoked command/feature.
     :param img: Image where the text is inserted.
     :param input: Text to be inserted.
     """
     cv2.putText(img,input, (20, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    

def get_fps(img, current_frame_time, prev_frame_time): 
    """
     Prints Frames Per Second (FPS).
     :img: the frame where to insert FPS.
     :param current_frame_time: Time of the current frame.
     :param prev_frame_time: Time of the previous frame.
     """    
    fps = 1/(current_frame_time- prev_frame_time)
    position = (20, 50)
    color = (255, 0, 0)
    cv2.putText(img, f"FPS: {str(int(fps))}", position, cv2.FONT_HERSHEY_PLAIN, 3, color, 3)
    
    return fps