import numpy as np
import cv2

cap = cv2.VideoCapture(0)
first_iter = True
result = None
while True:
    ret, frame = cap.read()
    if frame is None:
        break

    if first_iter:
        avg = np.float32(frame)
        first_iter = False

    cv2.accumulateWeighted(frame, avg, 0.005)
    result = cv2.convertScaleAbs(avg)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    cv2.imshow("Current Result", result)

cv2.imshow("result", result)
cv2.imwrite("averaged_frame.jpg", result)
cv2.waitKey(0)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()