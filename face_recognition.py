import numpy as np
import cv2 as cv
stars = ['sachin', 'gavaskar', 'lara']

haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread('Validate/v1.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Person', gray)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    cv.imshow('Cropped', faces_roi)

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {stars[label]} with confidence of {confidence}')
    cv.putText(img, str(stars[label]), (20,20), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), 2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)

    cv.imshow('Detected Face', img)

cv.waitKey(0)
