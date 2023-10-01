from cvzone.HandTrackingModule import HandDetector
import cv2
import screen_brightness_control as sbc
# https://github.com/cvzone/cvzone


# Initialize the webcam to capture video
# The '2' indicates the third camera connected to your computer; '0' would usually refer to the built-in camera

def control_brightness(cap, detector):
# Continuously get frames from the webcam
    while True:
        # Capture each frame from the webcam
        # 'success' will be True if the frame is successfully captured, 'img' will contain the frame
        success, img = cap.read()

        # Find hands in the current frame
        # The 'draw' parameter draws landmarks and hand outlines on the image if set to True
        # The 'flipType' parameter flips the image, making it easier for some detections
        hands, img = detector.findHands(img, draw=True, flipType=True)

        # Check if any hands are detected
        if hands:
            # Information for the first hand detected
            hand1 = hands[0]  # Get the first hand detected
            lmList1 = hand1["lmList"]  # List of 21 landmarks for the first hand
            bbox1 = hand1["bbox"]  # Bounding box around the first hand (x,y,w,h coordinates)
            center1 = hand1['center']  # Center coordinates of the first hand
            handType1 = hand1["type"]  # Type of the first hand ("Left" or "Right")

            # Count the number of fingers up for the first hand
            fingers1 = detector.fingersUp(hand1)
            print(f'H1 = {fingers1.count(1)}', end=" ")  # Print the count of fingers that are up

            # Calculate distance between specific landmarks on the first hand and draw it on the image
            length, info, img = detector.findDistance(lmList1[4][0:2], lmList1[8][0:2], img, color=(255, 0, 255),
                                                    scale=10)
            cv2.rectangle(img, (0, 480), (300, 425), (255, 0, 0), -2)
            if(handType1!="Left" and  len(hands)!=2):
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
            # ! brightness
            else: 
                cv2.putText(img, "do nothing", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
            #    sbc.set_brightness(100, display=0)
            # Check if a second hand is detected
            if len(hands) == 2:
                # Information for the second hand
                hand2 = hands[1]
                lmList2 = hand2["lmList"]
                bbox2 = hand2["bbox"]
                center2 = hand2['center']
                handType2 = hand2["type"]

                # Count the number of fingers up for the second hand
                fingers2 = detector.fingersUp(hand2)
                print(f'H2 = {fingers2.count(1)}', end=" ")

                # Calculate distance between the index fingers of both hands and draw it on the image
                # length, info, img = detector.findDistance(lmList1[8][0:2], lmList2[8][0:2], img, color=(255, 0, 0),
                #                                           scale=10)
                cv2.rectangle(img, (0, 480), (300, 425), (255, 0, 0), -2)
                
                cv2.putText(img, "do nothing", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

            print(" ")  # New line for better readability of the printed output

        # Display the image in a window
        cv2.imshow("a", img)

        # Keep the window open and update it for each frame; wait for 1 millisecond between frames
     
        k = cv2.waitKey(1)
        # quite if the user presses the q 
        if k == ord("q"): 
            break
