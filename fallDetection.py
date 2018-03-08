import cv2, numpy as np
import angleMonitor, fallAction

class backgroundSub:
    history = 500
    varThresh = 64
    detectShadows = True
    kernel = np.ones((3,3),np.uint8)
    curFrame = 0

    def MOG(self):
        cap = cv2.VideoCapture('video2.mp4')
        fgbg = cv2.createBackgroundSubtractorMOG2(self.history, self.varThresh ,self.detectShadows)

        while(1):
            self.curFrame += 1
            ret, frame = cap.read()

            fgmask = fgbg.apply(frame,0)
            bgrThresh = fgmask
            _, bgrThresh = cv2.threshold(fgmask,250,255,cv2.THRESH_BINARY)
            
            bgrThresh = cv2.erode(bgrThresh,self.kernel, iterations = 3)
            bgrThresh = cv2.morphologyEx(bgrThresh, cv2.MORPH_CLOSE, self.kernel)
            bgrThresh = cv2.morphologyEx(bgrThresh, cv2.MORPH_OPEN, self.kernel)
            bgrThresh = cv2.dilate(bgrThresh,self.kernel, iterations = 5)

            #cv2.imshow('Background Removed',bgrThresh)

            if (self.curFrame % 2 == 0) & cv2.countNonZero(bgrThresh) > 0:
                det.Detect(bgrThresh, self.curFrame)
            fall.check()

            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

        cap.release()
        cv2.destroyAllWindows()


bgRemove = backgroundSub()
fall = fallAction.fallAction()

det = angleMonitor.angleMonitor()

bgRemove.MOG()