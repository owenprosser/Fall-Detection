import cv2, numpy as np

class angleMonitor:
    init = False
    count = 0
    def Detect(self, frame, curFrame):
        if self.init == False:
            print("angleMonitor",curFrame)
            cv2.imshow('Single Frame',frame)
            #self.init = True