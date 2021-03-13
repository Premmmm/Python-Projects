import cv2
import pickle
import numpy as np

recognizer=cv2.face.LBPHFaceRecognizer_create() #this is a recognizer
face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer.read("trainner.yml")

labels={"person_name":1}
with open("labels.pickle",'rb') as f:
    og_labels=pickle.load(f)
    labels={v:k for k,v in og_labels.items()}


cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret, frame=cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.47,3)
    for x,y,w,h in faces:
        #print(x,y,w,h)
        roi_gray=gray[y:y+h, x:x+w] #roi is region of interest
        roi_color = frame[y:y+h, x:x+w]
        img_item="7.png"
        id_, conf= recognizer.predict(roi_gray)
        if conf>50:
            print(id_)
            print(labels[id_], conf)
            font=cv2.FONT_HERSHEY_SIMPLEX
            name=labels[id_]   
            cv2.putText(frame, name,(x,y), font, 1.5 ,(255,255,255),3,cv2.LINE_AA)
               
        cv2.imwrite(img_item,roi_color) #to get the face
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),3)

    cv2.imshow('Frame',frame)
    if cv2.waitKey(20) & 0xff ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

