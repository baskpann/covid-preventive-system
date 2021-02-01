from __future__ import print_function

import time

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

from decrypt_jwt import decrypt

# get the webcam:  
cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)
time.sleep(2)

def decode(im) : 
    # Find qr_codes and QR codes
    decoded_objects = pyzbar.decode(im)
    # Print results
    for obj in decoded_objects:
        print('Type : ', obj.type)
        print('Data : ', obj.data,'\n')     
    return decoded_objects


font = cv2.FONT_HERSHEY_SIMPLEX

def open_cam():
  is_detected = False

  while(cap.isOpened() and not is_detected):
      # Capture frame-by-frame
      ret, frame = cap.read()
      # Our operations on the frame come here
      im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
          
      decoded_objects = decode(im)

      for decodedObject in decoded_objects: 
          points = decodedObject.polygon
      
          # If the points do not form a quad, find convex hull
          if len(points) > 4 : 
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
          else : 
            hull = points
          
          # Number of points in the convex hull
          n = len(hull)     
          # Draw the convext hull
          for j in range(0,n):
            cv2.line(frame, hull[j], hull[ (j+1) % n], (255,0,0), 3)

          x = decodedObject.rect.left
          y = decodedObject.rect.top

          qr_code = str(decodedObject.data, 'utf-8')

          if qr_code is not None:
            print(decrypt(qr_code))
            is_detected = True
            
          cv2.putText(frame, "",(x, y), font, 1, (0,255,255), 2, cv2.LINE_AA)
                
      # Display the resulting frame
      cv2.imshow('QrCode Scanner',frame)
      if cv2.waitKey(1) == ord('q'):
        break    

  # When everything done, release the capture
  cap.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  print('Initialising cam..')
  open_cam()
