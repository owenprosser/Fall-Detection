import numpy as np
import cv2

cap = cv2.VideoCapture('test2.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((3,3),np.uint8)

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    _, bgrThresh = cv2.threshold(fgmask,254,255,cv2.THRESH_BINARY)

    bgrThresh = cv2.morphologyEx(bgrThresh, cv2.MORPH_OPEN, kernel)
    bgrThresh = cv2.morphologyEx(bgrThresh, cv2.MORPH_CLOSE, kernel)
    bgrThresh = cv2.erode(bgrThresh,kernel,iterations = 3)
    
    #cv2.imshow('fgmask',frame)
    cv2.imshow('Background Removed',bgrThresh)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()