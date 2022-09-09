from tkinter import Pack
import cv2 
import os 

# Workspace of the files used in this code 
PATH = os.path.dirname( __file__ )

# To use an image from the files 
img = cv2.imread( PATH + '/imgs/alice.png' ) 
 
classNames = [] 
classFile  = PATH + '/files/coco.names'

# Read the class names 
with open( classFile, 'rt' ) as f:
    classNames = f.read().rstrip('\n').split('\n')
#print( classNames )


configPath = PATH + '/files/mobilenet.pbtxt'
weightPath = PATH + '/files/pesos_mobilenet.pb'

# DNN configurations 
net = cv2.dnn_DetectionModel( weightPath, configPath ) 
net.setInputSize  ( 320, 320 )
net.setInputScale ( 1.0 / 127.5 )
net.setInputMean  ( [127.5, 127.5, 127.5] ) 
net.setInputSwapRB( True )

# To get the webcam images 
cap = cv2.VideoCapture( 0 )
cap.set( 3, 640 )
cap.set( 4, 480 )


# Init to get the webcam images 
while True: 
    success, img = cap.read() 

    # This is the step of img is put in the dnn net 
    classIds, confs, bbox = net.detect( img, confThreshold = 0.5 )

    # If have some classId detected in the image it will draw the rectangle and put the name of it
    if len( classIds ) != 0: 
        for classId, confidence, box in zip( classIds.flatten(), confs.flatten(), bbox ):
            cv2.rectangle( img, box, color = [255, 0, 0], thickness = 2 )
            cv2.putText  ( img, classNames[classId-1], [box[0]+10, box[1]+30], cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 2 )
            cv2.putText  ( img, str(round(confidence*100,2)), [box[0]+10, box[1]+50], cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 2 )

    # Shows the image 
    cv2.imshow( "WebCam Detect", img )

    # Press key Q to exit  
    if cv2.waitKey( 1 ) & 0xFF == ord('q'): 
        break 
