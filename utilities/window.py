import pyautogui
import platform
import functions as f 
import time 
import main as m


def manage_window(img, fingers_up): 
    """
    Performs window management.
    :param img: Frame for displaying the invoked command (i.e. minimize\close window) or notifying when the command can be invoked.
    :param fingers_up: Number of raised fingers.
    """
    # check if the count up timer has reached 3 seconds (or more)
    if time.time()-m.timer_window >=3:
        # check if the raised fingers are the index finger and pinky finger
        if fingers_up==[0,1,0,0,1]: 
            # perform click
            pyautogui.click()
            # check if the code is running on Windows 
            if platform.system()=="Windows":
                # perform a Windows shortcut to minimize the selected window
                pyautogui.hotkey('win', 'down')
            # check if the code is running on macOS 
            elif platform.system()=="Darwin":
                 # perform a macOS shortcut to minimize the selected window
                pyautogui.hotkey("command", "m")
            # update the count up timer 
            m.timer_window=time.time()
           
        # check if the raised finegrs are the index finger, the middle finger, and the ring finger 
        if fingers_up==[0,1,1,1,0]:
            # perform click 
            pyautogui.click()
            # check if the code is running on Windows
            if platform.system()=="Windows":
             # perform a Windows shortcut to close the selected window
             pyautogui.hotkey('alt', 'f4')
            # check if the code is running on macOS 
            elif platform.system()=="Darwin":
             # perform a macOS shortcut to close the selected window
             pyautogui.hotkey("command", "w")
            #  update the count up timer 
            m.timer_window=time.time()
    # check if the count up timer has not reached 3 seconds  
    elif time.time()-m.timer_window <3: 
        if fingers_up==[0,1,0,0,1] or fingers_up==[0,1,1,1,0]: 
            f.print_action(img, "Window Management Functions available in "+str(4-(time.time()-m.timer_window))[0]) 
      
   