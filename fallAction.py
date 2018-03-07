import cv2, numpy as np

class fallAction:
    init = False
    def fallAlarm(self):
        if self.init == False:
            print("fallAlarm")
            self.init = True