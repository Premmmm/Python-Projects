import cv2
import numpy as np
import os

def facedetection(test_img):
	gray= cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
	face_cascade=cv2.CascadeClassifier("C:\\Users\\HP\\sample python programs\\haarcascade_frontalface_default.xml")
	faces=face_cascade.detectMultiScale(gray,1.4,4)
	return faces,gray


def labels_for_training_data(directory):
	faces=[]
	faceid=[]

	for path,subdirnames,filenames in os.walk(directory):
		for filename in filenames:
			if filename.startswith("."):
				print("Skipping system file")
				continue
			id=os.path.basename(path)
			img_path=os.path.join(path,filename)
			print("img_path: ",img_path)
			print("ID: ",id)
			test_img=cv2.imread(img_path)
			if test_img is None:
				print("Image not loaded properly")
				continue

			faces_rect,gray=facedetection(test_img)
			if len(faces_rect)!=1:
				continue   # we are assuming only single persons face is there
			(x,y,w,h)=faces_rect[0]
			roi_gray=gray[y:y+h,x:x+w]
			faces.append(roi_gray)
			faceid.append(int(id))
	return faces,faceid


def train_classifier(faces,faceid):
	face_recognizer=cv2.face.LBPHFaceRecognizer_create()
	face_recognizer.train(faces,np.array(faceid))
	return face_recognizer

def draw_rect(test_img,face):
	(x,y,w,h)=face
	cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,255,0),4)

def put_text(test_img,text,x,y):
	cv2.putText(test_img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),5)
	#cv2.putText(confidence,(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),5)

#def put_text1(text,confidence):
	#cv2.putText(text,confidence,2,(255,255,255),5)


