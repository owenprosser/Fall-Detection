import numpy as np
import cv2

capture = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

ret, firstFrame = capture.read()
firstGray = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)

while(1):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    difference = cv2.absdiff(gray, firstGray)

    cv2.imshow("difference", difference)

    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()