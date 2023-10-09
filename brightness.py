from cvzone.HandTrackingModule import HandDetector
import cv2
import screen_brightness_control as sbc
# https://github.com/cvzone/cvzone


def test_control_brightness(img, detector, lmList1):

        length, info, img = detector.findDistance(lmList1[4][0:2], lmList1[8][0:2], img, color=(255, 0, 255),
                                                    scale=10)
        cv2.rectangle(img, (0, 480), (300, 425), (255, 0, 0), -2)
       
        if (length>360): 
            cv2.putText(img, str("100"), (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
            sbc.set_brightness(100, display=0)
        elif (length<=360 and length>320): 
            cv2.putText(img, str("90"), (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
            sbc.set_brightness(90, display=0)
        elif (length<=320 and length>280): 
            cv2.putText(img, str("80"), (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
            sbc.set_brightness(80, display=0)
        elif (length<=280 and length>240): 
            cv2.putText(img, str("70"), (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
            sbc.set_brightness(70, display=0)
        elif (length<=240 and length>200): 
            cv2.putText(img, str("60"), (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
            sbc.set_brightness(60, display=0)
        elif (length<=200 and length>160): 
            cv2.putText(img, str("50"), (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
            sbc.set_brightness(50, display=0)
        elif (length<=160 and length>120): 
            cv2.putText(img, str("40"), (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
            sbc.set_brightness(40, display=0)
        elif (length<=120 and length>80): 
            cv2.putText(img, str("30"), (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
            sbc.set_brightness(30, display=0)
        elif (length<=80 and length>40): 
            cv2.putText(img, str("20"), (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
            sbc.set_brightness(20, display=0)
        elif (length<=40 and length>0): 
            cv2.putText(img, str("10"), (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        else: 
            cv2.putText(img, str(length), (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
 
