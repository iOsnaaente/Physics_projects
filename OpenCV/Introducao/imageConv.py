import numpy as np 
import cv2 
import os

PATH = os.path.dirname(__file__)

img = cv2.imread( PATH + '/imgs/lena_half.jpg' )

kernel = np.ones((5,5), np.uint8 ) 

imgGray      = cv2.cvtColor    ( img           , cv2.COLOR_BGR2GRAY )
imgBlur      = cv2.GaussianBlur( imgGray       , (5,5), 0 )
imgCanny     = cv2.Canny       ( img           , 150, 200 )
imgDialation = cv2.dilate      ( imgCanny      , kernel, iterations = 1 )
imgErode     = cv2.erode       ( imgDialation  , kernel, iterations = 1 )

#cv2.imshow( "LenaGray"      , imgGray )
#cv2.imshow( "LenaBlur"      , imgBlur )
cv2.imshow( "LenaCanny"     , imgCanny )
cv2.imshow( "LenaDialation" , imgDialation )
cv2.imshow( "LenaErode"     , imgErode )
cv2.waitKey( 0 )