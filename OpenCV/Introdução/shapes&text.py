from random import randint as rand
import numpy as np 
import cv2 


img = np.zeros( (512, 512, 3), np.uint8 )
print( img.shape ) 

img[ rand(0,512) : , rand(0,512) : ] = [ rand(0,255), 0, 0 ]
img[ : rand(0,512) , : rand(0,512) ] = [ 0, rand(0,255), 0 ]
img[ : rand(0,512) , rand(0,512) : ] = [ 0, 0, rand(0,255) ]


cv2.line     ( img, pt1 = (0,0), pt2 = (rand(0,512), rand(0,512)), color = [255,255,255], thickness = 3 )
cv2.rectangle( img, pt1 = (0,0), pt2 = (rand(0,512), rand(0,512)), color = [255,255,255], thickness = 3 ) # Thickness can be cv2.FILLED
cv2.circle   ( img, center = [255,255], radius = rand(50,150)       , color = [100,100,100], thickness = 3 )

cv2.putText  ( img, "OpencCV First Steps", org = [0,100], fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 1, color = [200,100,200], thickness = 2 )

cv2.imshow( 'blankImg', img )
cv2.waitKey( 0 )