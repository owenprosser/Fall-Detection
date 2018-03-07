import cv2, numpy as np

class angleMonitor:
    window = False
    count = 0
    def Detect(self, frame):
        if self.window == False:
            cv2.imshow('Single Frame',frame)
            self.window = True