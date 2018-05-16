import cv2, numpy as np, Queue

class fallAction:
    init = False
    detectedAnlges = Queue.Queue(5)

    def check(self, angle):
        if self.init == False:
            #print("fallAlarm")

            self.detectedAnlges.put(angle)

            #print(self.detectedAnlges)
            print(self.detectedAnlges.qsize())

            #self.init = True