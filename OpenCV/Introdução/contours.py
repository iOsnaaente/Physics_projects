import numpy as np 
import cv2 
import os 

PATH = os.path.dirname( __file__ )

img        = cv2.imread( PATH + '/imgs/alice.png' )
imgContour = img.copy()
imgGray    = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
imgBlur    = cv2.GaussianBlur( imgGray, (7,7), 1 )
imgCanny   = cv2.Canny( imgBlur, 50, 50 ) 

contours, hierarchy = cv2.findContours( imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE ) # Detect the external contours
for cnt in contours:
    area = cv2.contourArea( cnt )
    if area:
        cv2.drawContours( imgContour, cnt, -1, (255,0,0), 3 )
        perimeter = cv2.arcLength( cnt, True )
        approx = cv2.approxPolyDP( cnt, 0.02*perimeter, True )
        x, y, w, h = cv2.boundingRect( approx )
        cv2.rectangle( imgContour, (x,y), (x+w, y+h), (0,255,0), 2)
        

imgs = np.hstack( [img, imgContour] ) 

cv2.imshow( 'imgs', imgs )
cv2.waitKey( 0 )