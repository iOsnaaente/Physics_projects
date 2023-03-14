import numpy as np 
import cv2 
import os

PATH = os.path.dirname(__file__)

def empty( x ):
    pass

HUE_Min = 0
HUE_Max = 0
Sat_Min = 0
Sat_Max = 0
Val_Min = 0
Val_Max = 0

cv2.namedWindow   ( 'HSV TrackBar' )
cv2.resizeWindow  ( 'HSV TrackBar', 640, 240)
cv2.createTrackbar( 'HUE Min', 'HSV TrackBar', 84 , 179, empty )
cv2.createTrackbar( 'HUE Max', 'HSV TrackBar', 138, 179, empty )
cv2.createTrackbar( 'Sat Min', 'HSV TrackBar', 83 , 255, empty )
cv2.createTrackbar( 'Sat Max', 'HSV TrackBar', 255, 255, empty )
cv2.createTrackbar( 'Val Min', 'HSV TrackBar', 0  , 255, empty )
cv2.createTrackbar( 'Val Max', 'HSV TrackBar', 255, 255, empty )

while True:

    img = cv2.imread( PATH + '/imgs/alice.png' )
    imgHSV = cv2.cvtColor( img, cv2.COLOR_BGR2HSV )

    HUE_Min = cv2.getTrackbarPos('HUE Min', 'HSV TrackBar')
    HUE_Max = cv2.getTrackbarPos('HUE Max', 'HSV TrackBar')
    Sat_Min = cv2.getTrackbarPos('Sat Min', 'HSV TrackBar')
    Sat_Max = cv2.getTrackbarPos('Sat Max', 'HSV TrackBar')
    Val_Min = cv2.getTrackbarPos('Val Min', 'HSV TrackBar')
    Val_Max = cv2.getTrackbarPos('Val Max', 'HSV TrackBar')

    lower = np.array( [ HUE_Min, Sat_Min, Val_Min ] )
    upper = np.array( [ HUE_Max, Sat_Max, Val_Max ] )
    mask  = cv2.inRange( imgHSV, lower, upper ) 

    print( 'lower: ', HUE_Min, Sat_Min, Val_Min )   # lower:  89 29 14
    print( 'upper: ', HUE_Max, Sat_Max, Val_Max )   # upper:  145 255 255

    result = cv2.bitwise_and( img, img, mask = mask)

    imgs = np.hstack( [img, imgHSV, result] )
    cv2.imshow( 'Alice imgs' , imgs )
    cv2.imshow( 'Alice mask' , mask )
    cv2.waitKey( 1 )

