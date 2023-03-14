import matplotlib.pyplot as plt
import numpy as np 
import cv2 
import os


PATH = os.path.dirname(__file__)

img = cv2.imread( PATH + '/imgs/cards.png' )

# To get the points 
# imgGray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY ) 
# plt.imshow( imgGray, cmap='gray' )
# plt.colorbar()
# plt.show() 

p11 = 45, 285 
p12 = 336, 271
p21 = 61, 715
p22 = 365, 703

width, height = 200, 300

imgPoints   = np.float32( [p11, p12, p21, p22] )
framePoints = np.float32( [[0,0], [width, 0], [0,height], [width, height]]  ) 

matrix = cv2.getPerspectiveTransform( imgPoints, framePoints )
imgOut = cv2.warpPerspective( img, matrix, [width, height] )


cv2.imshow( "cards", img    )
cv2.imshow( "card" , imgOut )
cv2.waitKey( 0 )

