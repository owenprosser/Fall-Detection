import cv2, numpy as np, time
import angleMonitor, fallAction

class backgroundSub:
    history = 150
    varThresh = 64
    detectShadows = False
    kernel = np.ones((3,3),np.uint8)
    curFrame = 0

    def MOG(self):
        cap = cv2.VideoCapture('testFall.mp4')
        fgbg = cv2.createBackgroundSubtractorMOG2(self.history, self.varThresh ,self.detectShadows)

        while(cap != None):
            if (self.curFrame % 1 == 0):
                ret, frame = cap.read()

                fgmask = fgbg.apply(frame,0)
                bgrThresh = fgmask
                _, bgrThresh = cv2.threshold(fgmask,254,255,cv2.THRESH_BINARY)

                bgrThresh = cv2.erode(bgrThresh,self.kernel, iterations = 1)
                bgrThresh = cv2.morphologyEx(bgrThresh, cv2.MORPH_OPEN, self.kernel)
                bgrThresh = cv2.morphologyEx(bgrThresh, cv2.MORPH_CLOSE, self.kernel)
                bgrThresh = cv2.dilate(bgrThresh,self.kernel, iterations = 3)
                bgrThresh = cv2.morphologyEx(bgrThresh, cv2.MORPH_CLOSE, self.kernel)
                bgrThresh = cv2.morphologyEx(bgrThresh, cv2.MORPH_CLOSE, self.kernel)
                bgrThresh = cv2.morphologyEx(bgrThresh, cv2.MORPH_CLOSE, self.kernel)

                if cv2.countNonZero(bgrThresh) > 0:
                    fall.check(det.Detect(bgrThresh, self.curFrame, frame))

                self.curFrame += 1
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                    print("Fall Detected")
                    break
                
                #time.sleep(0.033)

        cap.release()
        cv2.destroyAllWindows()
        return 0

bgRemove = backgroundSub()
fall = fallAction.fallAction()

det = angleMonitor.angleMonitor()

bgRemove.MOG()