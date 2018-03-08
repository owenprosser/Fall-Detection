import cv2, numpy as np, time

class angleMonitor:
    count = 0

    def Detect(self, frame, curFrame):
        print("angleMonitor",curFrame)

        _, contours, hierarchy = cv2.findContours(frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cnt = contours[0]
        moments = cv2.moments(cnt)
        area = moments['m00']
        print(area)

        if len(cnt) > 4:
            ellipse = cv2.fitEllipseAMS(cnt)
            cv2.ellipse(frame,ellipse,(255,255,255),2)
        else:
            print("Less than 5 points in contour array")

        cv2.imshow("Current Frame", frame)

        time.sleep(1)