import cv2

def getFps(img, current_frame_time, prev_frame_time): 
    
    fps = 1/(current_frame_time- prev_frame_time)
    position = (20, 50)
    color = (255, 0, 0)
    cv2.putText(img, f"FPS: {str(int(fps))}", position, cv2.FONT_HERSHEY_PLAIN, 3, color, 3)
    
    return fps
    
    