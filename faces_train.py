import cv2 as cv
import os
import numpy as np

stars = ['sachin', 'gavaskar', 'lara']
DIR = r'Train'

features = []
labels = []
haar_cascade = cv.CascadeClassifier('haar_face.xml')

def create_train():
    for person in stars:
        path = os.path.join(DIR, person)
        label = stars.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
# print(f'length of features = {len(features)}')
# print(f'length of labels= {len(labels)}')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recongnizer = cv.face.LBPHFaceRecognizer_create()
face_recongnizer.train(features, labels)
face_recongnizer.save('face_trained.yml')

# np.save('features.npy', features)
# np.save('labels.npy', labels)
