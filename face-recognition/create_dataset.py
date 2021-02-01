import sys

import cv2

cpt = 0

cam = cv2.VideoCapture(0)

while True:

    ret, frame = cam.read() # read frame and return code.
    
    cv2.imshow("dataset creating script", frame) # show image in window

    path = "face-recognition/train-images/tmp/image%04i.jpg"

    cv2.imwrite(path %cpt, frame)
    cpt += 1    
    
    if cv2.waitKey(10) == ord('q'):
        break
