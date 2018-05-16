import cv2, numpy as np, time

class angleMonitor:
    count = 0
    font = cv2.FONT_HERSHEY_PLAIN

    def Detect(self, frame, curFrame, origFrame):
        #print("angleMonitor",curFrame)
        returnAngle = None

        _, contours, hierarchy = cv2.findContours(frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        maxContour = max(contours, key = cv2.contourArea)
        cnt = contours[0]

        rows,cols = frame.shape[:2]
        [vx,vy,x,y] = cv2.fitLine(maxContour, cv2.DIST_L2,0,0.01,0.01)
        lefty = int((-x*vy/vx) + y)
        righty = int(((cols-x)*vy/vx)+y)

        frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2RGB)
        screenText = ""

        if len(maxContour) > 4:
            (x,y),(MA,ma),angle = cv2.fitEllipse(maxContour)
            returnAngle = angle
            maxArea = cv2.contourArea(maxContour)
            #print(maxArea)
            if maxArea > 100:
                try:
                    ellipse = cv2.fitEllipse(maxContour)
                    #cv2.ellipse(frame,ellipse,(0,255,0),2)
                    #cv2.line(frame,(cols-1,righty),(0,lefty),(0,0,255),2)

                    cv2.ellipse(origFrame,ellipse,(0,255,0),2)
                    cv2.line(origFrame,(cols-1,righty),(0,lefty),(0,0,255),2)
                except OverflowError:
                    print("OverflowError: signed integer is less than minimum")
                
                screenText = 'Angle: '+str(round(angle, 1))#+' maxArea: '+str(maxArea)
            else:
                screenText = "Area too small: "+str(maxArea)
        else:
            print("Less than 5 points in contour array")
            screenText = "Less than 5 points in contour array"

        cv2.putText(origFrame,screenText ,(3,25), self.font, 2,(242, 238, 26),2,cv2.LINE_AA)
        cv2.imshow("Fall Detection", origFrame)
        cv2.imshow("Background Removal", frame)

        return returnAngle