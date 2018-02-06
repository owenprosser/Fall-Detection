import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
ret, first = cap.read()

# Save the first image as reference
first_gray = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (21, 21), 0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # In each iteration, calculate absolute difference between current frame and reference frame
    difference = cv2.absdiff(gray, first_gray)

    # Apply thresholding to eliminate noise
    thresh = cv2.threshold(difference, 100, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=3)

    cv2.imshow("thresh", thresh)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key is pressed, break from the lop
    if key == ord("q"):
        break

cap.release()