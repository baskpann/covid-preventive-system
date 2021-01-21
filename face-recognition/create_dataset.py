import cv2
import sys
cpt = 0

cam = cv2.VideoCapture(0)

while True:

    ret, frame = cam.read() # read frame and return code.
    
    cv2.imshow("dataset creating script", frame) # show image in window

    tmp_path = "train-images/tmp/image%04i.jpg"
    #cv2.imwrite("C:\\Users\\Bas\\Documents\\College\\Project\\Face-Recognition\\train-images\\0\\image%04i.jpg" %cpt, frame)
    cv2.imwrite(tmp_path %cpt, frame)
    cpt += 1    
    
    if cv2.waitKey(10) == ord('q'):
        break