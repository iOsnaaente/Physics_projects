import numpy as np 
import cv2 
import os

PATH = os.path.dirname(__file__)

img = cv2.imread( PATH + '/imgs/alice.png' )
print( img.shape )

imgResize = cv2.resize( img, (200, 200) )
print( imgResize.shape )

imgCropped = imgResize[:100, 100:200] 

cv2.imshow( 'imgOriginal', img        )
cv2.imshow( 'imgResize'  , imgResize  )
cv2.imshow( 'imgCropped' , imgCropped )
cv2.waitKey( 0 )