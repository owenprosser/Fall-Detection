import cv2, numpy as np, time

class angleMonitor:
    count = 0
    font = cv2.FONT_HERSHEY_PLAIN

    def Detect(self, frame, curFrame):
        print("angleMonitor",curFrame)

        _, contours, hierarchy = cv2.findContours(frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cnt = contours[0]
        moments = cv2.moments(cnt)
        area = moments['m00']

        frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2RGB)

        if len(cnt) > 4:
            maxContour = max(contours, key = cv2.contourArea)
            (x,y),(MA,ma),angle = cv2.fitEllipse(maxContour)
            ellipse = cv2.fitEllipse(maxContour)
            cv2.ellipse(frame,ellipse,(0,255,0),2)
            cv2.putText(frame,'Angle: '+str(angle) ,(5,25), self.font, 2,(242, 238, 26),2,cv2.LINE_AA)
        else:
            print("Less than 5 points in contour array")
            cv2.putText(frame,'Less than 5 points in contour array',(5,25), self.font, 2,(242, 238, 26),2,cv2.LINE_AA)

        cv2.imshow("Current Frame", frame)
        time.sleep(0.5)