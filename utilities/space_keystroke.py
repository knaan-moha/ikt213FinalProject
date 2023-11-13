import pyautogui

import functions as f


def space_keystroke(img, lmList, fingers_up):
    """
     Triggers space keystroke.
     :param img: Frame for displaying the invoked command (i.e. space keystroke).
     :param fingers_up: Number of raised fingers.
    """
    
    print(fingers_up.count(1))
    if fingers_up.count(1) == 5 and lmList[6][1]<lmList[0][1]:

        f.print_action(img, 'Space keystroke')
        pyautogui.press('space', presses=1)
    