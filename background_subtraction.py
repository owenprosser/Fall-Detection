import numpy as np
import cv2

cap = cv2.VideoCapture(0)
origVideo = cv2.createBackgroundSubtractorMOG2(10000, 5, 3)

while(1):
    ret, frame = cap.read()

    fgmask = origVideo.apply(frame)
 
    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)

    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()