import cv2, numpy as np
import angleMonitor, fallAction

class backgroundSub:
    history = 500
    varThresh = 64
    detectShadows = True
    kernel = np.ones((3,3),np.uint8)

    def MOG(self):
        cap = cv2.VideoCapture('video2.mp4')
        fgbg = cv2.createBackgroundSubtractorMOG2(self.history, self.varThresh ,self.detectShadows)

        while(1):
            ret, frame = cap.read()

            fgmask = fgbg.apply(frame)

            _, bgrThresh = cv2.threshold(fgmask,250,255,cv2.THRESH_BINARY)
            
            bgrThresh = cv2.erode(bgrThresh,self.kernel, iterations = 3)
            bgrThresh = cv2.morphologyEx(bgrThresh, cv2.MORPH_CLOSE, self.kernel)
            bgrThresh = cv2.morphologyEx(bgrThresh, cv2.MORPH_OPEN, self.kernel)
            bgrThresh = cv2.dilate(bgrThresh,self.kernel, iterations = 5)

            #_,contours,hierarchy = cv2.findContours(bgrThresh, 1, 2)
            #cnt = contours[0]

            #ellipse = cv2.fitEllipse2(cnt)
            #cv2.ellipse(bgrThresh,ellipse,(0,255,0),2)

            #cv2.imshow('Original Video',frame)
            cv2.imshow('Background Removed',bgrThresh)

            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

            det.Detect(bgrThresh)

        cap.release()
        cv2.destroyAllWindows()


bgRemove = backgroundSub()
fall = fallAction.fallAction()

det = angleMonitor.angleMonitor()

bgRemove.MOG()

