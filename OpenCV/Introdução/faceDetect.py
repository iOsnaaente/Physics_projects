import cv2 
import os

PATH = os.path.dirname( __file__ )

faceCascade = cv2.CascadeClassifier( PATH + '/resources/haarcascade_frontalface.xml' )
faceCascade = cv2.CascadeClassifier( PATH + '/resources/haarcascade_eye.xml' )

cap = cv2.VideoCapture( 0 )
cap.set( 3, 640 )

while True: 
    success, img = cap.read() 
    imgGray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
    
    faces = faceCascade.detectMultiScale( imgGray, 1.1, 4 )
    for (x, y, w, h) in faces: 
        cv2.rectangle( img, (x, y), (x+w, y+h), [255,0,0], 2  )

    cv2.imshow( "WebCam", img )
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break