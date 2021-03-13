import cv2
import numpy as np

face_cascade= cv2.CascadeClassifier("haarcascade_fullbody.xml")

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
a=1

while True:
    ret, frame=cap.read()
    if a==1:
        print(ret)
        a+=1
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.045,5)
    for x,y,w,h in faces:
        roi_gray=gray[y:y+h, x:x+w] #roi is region of interest
        roi_color = frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x,y), (x+w,y+h),(115,215,100),3)

    cv2.imshow('Frame',frame)
    if cv2.waitKey(20) & 0xff ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

