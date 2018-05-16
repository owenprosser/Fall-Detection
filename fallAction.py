import cv2, numpy as np, collections

class fallAction:
    init = False
    detectedAngles = collections.deque(5*[0], 5)

    def check(self, angle):
        if not self.init:
            
            self.detectedAngles.appendleft(angle)
            
        if all(i >= 70 for i in self.detectedAngles) and all(i <= 100 for i in self.detectedAngles):
            print("Fall Detected!!!")
            