#Author: Dilshad khan
#Features: Tracking Red,Blue,Yellow color from static frame and   	#enclousing in a frame with a label.
#importing modules

import cv2   
import numpy as np


while(1):
	img = cv2.imread('/home/dilshad/Pictures/dil.png',1)
	cv2.imshow('image',img)
	#converting frame(img i.e BGR) to HSV (hue-saturation-value)

	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	#definig the range of blue color
	blue_lower=np.array([110,100,50],np.uint8)
	blue_upper=np.array([130,255,255],np.uint8)

	#defining the Range of red color
	red_lower=np.array([0,100,100],np.uint8)
	red_upper=np.array([22, 255, 255],np.uint8)
	
	#defining the Range of green color
	yellow_lower=np.array([50, 100 ,100],np.uint8)
	yellow_upper=np.array([70,255,255],np.uint8)

	#finding the range of red,blue and yellow color in the image
	red=cv2.inRange(hsv, red_lower, red_upper)
	blue=cv2.inRange(hsv,blue_lower,blue_upper)
	yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
	
	#Morphological transformation, Dilation  	
	kernal = np.ones((5 ,5), "uint8")

        red=cv2.dilate(red, kernal)
	res=cv2.bitwise_and(img, img, mask = red)

	blue=cv2.dilate(blue,kernal)
	res1=cv2.bitwise_and(img, img, mask = blue)

	yellow=cv2.dilate(yellow,kernal)
	res2=cv2.bitwise_and(img, img, mask = yellow)    


	#Tracking the Red Color
	(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>100):
			
			x,y,w,h = cv2.boundingRect(contour)	
			img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,100),2)
			cv2.putText(img,"RED color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))

	#cv2.imshow("Color Tracking",img)		
	#Tracking the Blue Color
	(_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>100):
			x,y,w,h = cv2.boundingRect(contour)	
			img = cv2.rectangle(img,(x,y),(x+w,y+h),(100,0,0),2)
			cv2.putText(img,"Blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
	#cv2.imshow("Color Tracking",img)
	#Tracking the yellow Color
	(_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>100):
			x,y,w,h = cv2.boundingRect(contour)	
			img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,100,0),2)
			cv2.putText(img,"green  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))  
            
           
    	#cv2.imshow("Redcolour",red)
    	cv2.imshow("Color Tracking",img)
    	#cv2.imshow("red",res) 	
    	if cv2.waitKey(10) & 0xFF == ord('q'):
    		cv2.destroyAllWindows()
    		break  
          

    
