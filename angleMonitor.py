import cv2, numpy as np, time

class angleMonitor:
    init = False
    count = 0

    def Detect(self, frame, curFrame):
        if self.init == False:
            print("angleMonitor",curFrame)

            _, contours, hierarchy = cv2.findContours(frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            cnt = contours[0]
            moments = cv2.moments(cnt)
            area = moments['m00']
            print(area)

            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            cv2.imshow("Current Frame",frame)
            #self.init = True
            time.sleep(1)