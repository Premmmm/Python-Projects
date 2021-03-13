import cv2
import numpy as np
import os
import TrainFace_Method_2 as fr
import sys

test_img = cv2.imread("C:\\Users\\HP\\Pictures\\Saved Pictures\\mehh.jpeg")
faces_detected, gray = fr.facedetection(test_img)
print("faces detected", faces_detected)

faces, faceid = fr.labels_for_training_data("images1")
face_recognizer = fr.train_classifier(faces, faceid)
face_recognizer.save('trainingData.yml')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainingData.yml')

name = {0: "Mom", 1: "Prem", 2: "Scar_joo", 3: "lokesh"}


for face in faces_detected:  # it is faces_detected and not faces
    (x, y, w, h) = face

    roi_gray = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(roi_gray)
    print("confidence: ", confidence)
    print("label: ", label)
    fr.draw_rect(test_img, face)
    predicted_name = name[label]
    if confidence > 35:
        continue
    fr.put_text(test_img, predicted_name, x, y)

resized_img = cv2.resize(test_img, (500, 500))
cv2.imshow("face detection tutorial", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
