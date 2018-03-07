import cv2, numpy as np

def  MOG():
    cap = cv2.VideoCapture('video2.mp4')
    fgbg = cv2.createBackgroundSubtractorMOG2(500,64,True)
    kernel = np.ones((3,3),np.uint8)

    while(1):
        ret, frame = cap.read()

        fgmask = fgbg.apply(frame)

        _, bgrThresh = cv2.threshold(fgmask,250,255,cv2.THRESH_BINARY)
        
        bgrThresh = cv2.erode(bgrThresh,kernel,iterations = 3)
        bgrThresh = cv2.morphologyEx(bgrThresh, cv2.MORPH_CLOSE, kernel)
        bgrThresh = cv2.morphologyEx(bgrThresh, cv2.MORPH_OPEN, kernel)
        bgrThresh = cv2.dilate(bgrThresh,kernel,iterations = 4)

        #_,contours,hierarchy = cv2.findContours(bgrThresh, 1, 2)
        #cnt = contours[0]

        #ellipse = cv2.fitEllipse2(cnt)
        #cv2.ellipse(bgrThresh,ellipse,(0,255,0),2)

        #cv2.imshow('Original Video',frame)
        cv2.imshow('Background Removed',bgrThresh)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    MOG()