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

        while(cap != None):
            if (self.curFrame % 1 == 0):
                ret, frame = cap.read()

                fgmask = fgbg.apply(frame,0)
                bgrThresh = fgmask
                _, bgrThresh = cv2.threshold(fgmask,250,255,cv2.THRESH_BINARY)
                
                bgrThresh = cv2.erode(bgrThresh,self.kernel, iterations = 1)
                bgrThresh = cv2.morphologyEx(bgrThresh, cv2.MORPH_CLOSE, self.kernel)
                bgrThresh = cv2.morphologyEx(bgrThresh, cv2.MORPH_OPEN, self.kernel)
                bgrThresh = cv2.dilate(bgrThresh,self.kernel, iterations = 1)

                if cv2.countNonZero(bgrThresh) > 0:
                    det.Detect(bgrThresh, self.curFrame)
                fall.check()

                self.curFrame += 1
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                    break

        cap.release()
        cv2.destroyAllWindows()
        return 0

bgRemove = backgroundSub()
fall = fallAction.fallAction()

det = angleMonitor.angleMonitor()

bgRemove.MOG()