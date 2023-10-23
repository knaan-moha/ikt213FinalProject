import cv2 
import pyautogui

import functions as f


def space_keystroke(img, finger_up):
    """
     Triggers space keystroke.
     :param img: Frame for displaying the invoked command (i.e. space keystroke).
     :param fingers_up: Number of raised fingers.
    """

    if finger_up.count(1) == 5:

        f.print_action(img, 'Space keystroke')
        pyautogui.press('space', presses=1)
    