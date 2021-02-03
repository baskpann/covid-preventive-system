import os

import cv2
import numpy as np

import face_recog as fr
from user_data import name

#Give path to the image which you want to test
test_img=cv2.imread('train-images/0/image0000.jpg')

faces_detected, gray_img = fr.faceDetection(test_img)
print("Face detected: ", faces_detected)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

#Give path of where trainingData.yml is saved
face_recognizer.read('train-images/training_data.yml')  

for face in faces_detected:
    (x, y, w, h) = face
    roi_gray = gray_img[y : y + h, x : x + h]
    label, confidence = face_recognizer.predict(roi_gray)
    print ("Confidence : ", confidence)
    print("Label : ", label)

    fr.draw_rect(test_img, face)

    predicted_name = name[label]["name"]
    
    fr.put_text(test_img, predicted_name, x, y)

output_image = cv2.resize(test_img, (1000, 700))

cv2.imshow("Detected from image ", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
