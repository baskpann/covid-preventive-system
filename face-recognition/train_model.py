import os

import cv2
import numpy as np

import face_recog as fr
from user_data import name

test_img=cv2.imread("face-recognition/train-images/0/image0000.jpg")  #Give path to the image which you want to test


faces_detected, gray_img = fr.faceDetection(test_img)
print("face Detected: ", faces_detected)

# Give path to the train-images folder
faces, faceID = fr.labels_for_training_data("train-images/")
face_recognizer = fr.train_classifier(faces, faceID)

# It will save the trained model.
face_recognizer.save("face-recognition/train-images/training_data.y.ml")


for face in faces_detected:
    (x, y, w, h) = face
    roi_gray = gray_img[y : y + h, x : x + h]
    label, confidence = face_recognizer.predict(roi_gray)
    
    print ("Confidence : ", confidence)
    print("Label : ", label)
    
    fr.draw_rect(test_img, face)

    predicted_name = name[label]["name"]
    fr.put_text(test_img, predicted_name, x, y)

output_image = cv2.resize(test_img, (1000,700))

cv2.imshow("face detection ", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
