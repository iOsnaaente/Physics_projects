import cv2 
import os

PATH = os.path.dirname(__file__)

cap = cv2.VideoCapture( PATH + '/test_vid.mp4' ) # To read a video file 
cap = cv2.VideoCapture( 0 )                          # To use a web can in channel 0 

cap.set( 3, 640 )
cap.set( 4, 480 )

while True: 
    success, img = cap.read() 
    cv2.imshow( "WebCam Video", img )
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break