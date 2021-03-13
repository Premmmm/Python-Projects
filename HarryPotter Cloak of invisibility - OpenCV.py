import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
time.sleep(2)

background = 0
 
for i in range(30):
	ret,background =cap.read()  # background is captured (ret is bool)


while(cap.isOpened()):  # loop will run till capturing happens
	ret,img = cap.read()  # capturing image here (ret is bool)

	if not ret:
		break

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #hsv is hugh saturation value
	
	#for RED COLOUR DETECTION 

	lower_red = np.array([0, 120, 70])  # ([ min , saturation, brightness])
	upper_red = np.array([8, 255, 255])
	mask1= cv2.inRange(hsv, lower_red, upper_red)

	lower_red=np.array([170,120,70])
	upper_red=np.array([180, 255, 255])
	mask2= cv2.inRange(hsv, lower_red, upper_red)

	mask1 = mask1 + mask2  # or operatin
	
	mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=2) #noise removal, 2 ietrations to reduce noise as much as possible
	mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations=1) # dilate is to increase smoothness of the image after noise removal
	mask2= cv2.bitwise_not(mask1)  #everything except cloak

	#to superimpose background image with cloak image

	res1=cv2.bitwise_and(background, background, mask=mask1) # used for segmentation of color
	res2=cv2.bitwise_and(img, img, mask=mask2) #used to substitute the cloak part
	
	#final output will be additon of result 1 and result 2
	final_output=cv2.addWeighted(res1, 1, res2, 1,0)

	cv2.imshow('Ooo lala laa!!!',final_output)
	k = cv2.waitKey(10)
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()