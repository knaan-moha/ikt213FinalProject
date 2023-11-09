import cv2 
import pyautogui

import functions as f


def space_keystroke(img, finger_up):
    """
     Triggers space keystroke.
     :param img: Frame for displaying the invoked command (i.e. space keystroke).
     :param fingers_up: Number of raised fingers.
    """

    if finger_up[0] == 1 and sum(finger_up[1:]) == len(finger_up) - 1:

        f.print_action(img, 'Space keystroke')
        pyautogui.press('space', presses=1)
    