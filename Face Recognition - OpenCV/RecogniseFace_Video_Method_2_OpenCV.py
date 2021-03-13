import cv2
import numpy as np
import os
import TrainFace_Method_2_OpenCV as fr


face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainingData.yml')

name={0:"Mom",1:"Prem",2:"Scarlet",3:"lokesh"}

cap=cv2.VideoCapture(0)

while True:
	ret,test_img=cap.read()
	faces_detected,gray=fr.facedetection(test_img)

	#for(x,y,w,h) in faces_detected:
		#cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),4)

	resized_img=cv2.resize(test_img,(650,650))
	#cv2.imshow('',resized_img)
	#cv2.waitKey(1)

	for face in faces_detected:
		(x,y,w,h)=face
		roi_gray=gray[y:y+h,x:x+w]
		label,confidence=face_recognizer.predict(roi_gray)
		print('Conf: ',confidence)
		print("label: ",label)
		fr.draw_rect(test_img,face)
		predicted_name=name[label]
		if confidence<65:
			fr.put_text(test_img,predicted_name,x,y)
			#fr.put_text1('c',confidence)

	resized_img=cv2.resize(test_img,(700,500))
	cv2.imshow('',resized_img)
	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()





