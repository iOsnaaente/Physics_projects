import numpy as np 
import cv2 
import os

PATH = os.path.dirname(__file__)

img = cv2.imread( PATH + '/imgs/alice.png' )

imgsH = np.hstack( (img, img) )
imgsV = np.vstack( (imgsH, imgsH) )

cv2.imshow( 'Alice Stack', imgsV )
cv2.waitKey( 0 )

