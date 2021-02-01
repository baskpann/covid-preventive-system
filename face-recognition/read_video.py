import json
import os
from datetime import date, datetime
from json import dumps

import cv2
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import face_recog as fr
# dictionary declared stored here
from user_data import name


def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

now = datetime.now()
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('attendancesheet-293208-852324a98bf2.json', scope)

gc = gspread.authorize(credentials)
wks = gc.open('Attendance').worksheet(now.strftime("%d/%m/%Y"))
label_set = {-1}

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Give path of where trainingData.yml is saved
path_to_trained_data = 'face-recognition/train-images/training_data.yml'
face_recognizer.read(path_to_trained_data)
cam = cv2.VideoCapture(0) 

while True:

    ret, test_img = cam.read()
    faces_detected, gray_img = fr.faceDetection(test_img)
    print("Face detected: ", faces_detected)

    for (x,y,w,h) in faces_detected:
        cv2.rectangle(test_img, (x, y), (x + w, y + h), (0, 255, 0), thickness=5)

    for face in faces_detected:
        (x, y, w, h) = face
        roi_gray = gray_img[y : y + h, x : x + h]
        label, confidence = face_recognizer.predict(roi_gray)
        
        print ("Confidence :", confidence)
        print("Label :", label)
        
        # to show that the face is detected
        fr.draw_rect(test_img, face)

        predicted_name = name[label]["name"]
        predicted_id = name[label]["id"]

        fr.put_text(test_img, predicted_name, x, y)

        # to make updation once on the sheet
        if(label in label_set):
            # forces the next iter 
            continue
        else:
        	# this is to make user that only one entry is made.	
            label_set.add(label)
            wks.append_row([predicted_id, predicted_name, now.strftime("%I:%M:%S %p")])

    output_image = cv2.resize(test_img, (700,500))

    cv2.imshow("Face detector ", output_image)
    if cv2.waitKey(10) == ord('q'):
        break
