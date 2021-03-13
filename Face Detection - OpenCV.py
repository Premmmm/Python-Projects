import cv2
#reading face classifier
face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#reading image as it is
img= cv2.imread("C:\\Users\\HP\\Pictures\\Mee\\premm.jpg",1)

#reading image as gray scale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#searching coordinates of the image
faces=face_cascade.detectMultiScale(gray_img,1.05,5)

print(type(faces))
print(faces)

for x,y,w,h in faces:
	img=cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)

resized=cv2.resize(img,(700,700))

cv2.imshow("gray", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
