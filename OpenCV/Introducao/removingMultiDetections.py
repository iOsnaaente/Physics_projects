import numpy as np 
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
cap.set(  3, 1280 )
cap.set(  4, 720  )
cap.set( 10, 150  )

# Configuration of the detection threshold
NMS_THRESHOLD = 0.20  
THRESHOLD     = 0.45 

# Init to get the webcam images 
while True: 
    success, img = cap.read() 

    # This is the step of img is put in the dnn net 
    classIds, confs, bbox = net.detect( img, confThreshold = THRESHOLD )

    bbox  = list( bbox )
    confs = list( map( float, np.array(confs).reshape(1,-1)[0]) ) 


    indices = cv2.dnn.NMSBoxes( bbox, confs, THRESHOLD, NMS_THRESHOLD )
    
    for i in indices:
        if type(i) == list:
            box = bbox[i[0]]
        else: 
            box = bbox[i]
        x, y, w, h = box
        cv2.rectangle( img, box, color = [255, 0, 0], thickness = 2 )
        cv2.putText  ( img, classNames[classIds[i]-1].upper(), [box[0]+10, box[1]+30], cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 2 )
        #cv2.putText  ( img, str(round(confidence*100,2)), [box[0]+10, box[1]+50], cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 2 )

    # Shows the image 
    cv2.imshow( "WebCam Detect", img )

    # Press key Q to exit  
    if cv2.waitKey( 1 ) & 0xFF == ord('q'): 
        break 
