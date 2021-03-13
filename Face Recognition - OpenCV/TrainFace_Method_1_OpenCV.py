import cv2
import os
from PIL import Image 
import numpy as np
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
image_dir =os.path.join(BASE_DIR,"images")   

face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer=cv2.face.LBPHFaceRecognizer_create() #this is a recognizer

current_id=0
label_ids={}
x_train=[] #empty list
y_label=[] #    "

for root, dirs, files in os.walk(image_dir):
	for file in files:
		if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
			path=os.path.join(root, file)  #root is actually the os.path.dirname(path)
			label= os.path.basename(root).replace(" ","-").lower()
			#print(label,path) #this will show label eg;Prem and path
			if not label in label_ids:
				label_ids[label]=current_id
				current_id+=1

			id_=label_ids[label]
			#print(label_ids)
			#y_label.append(label) adds label to list ( some number)
			#x_train.append(path) verify this image, turn to numpy array, grey
			pil_image=Image.open(path).convert("L")  # .convert(L) converts it into grayscale
			size=(550,550)
			final_image=pil_image.resize(size, Image.ANTIALIAS)
			image_array= np.array(pil_image,"uint8") 
			#print(image_array)

			faces=face_cascade.detectMultiScale(image_array,1.32,5)
			for(x,y,w,h) in faces:
				roi=image_array[y:y+h, x:x+w]
				x_train.append(roi)
				y_label.append(id_)

# IN THE ABOVE CODE WE HAVE GIVEN EACH FACE FOLDER AN ID LIKE 0TH FOLDER 1ST FOLDER 2ND FOLDER

with open("labels.pickle",'wb') as f:
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_label))
print('Training done !!')
recognizer.save("trainner.yml")





 