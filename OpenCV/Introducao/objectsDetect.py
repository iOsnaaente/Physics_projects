import pyautogui as auto
import numpy as np
import cv2 
import os 

# Workspace of the files used in this code 
PATH = os.path.dirname( __file__ )

# To use an image from the files 
# img = cv2.imread( PATH + '/imgs/alice.png' ) 
 
classNames = [] 
classFile  = PATH + '\\files\\coco.names'

# Read the class names 
with open( classFile, 'rt' ) as f:
    classNames = f.read().rstrip('\n').split('\n') 
    print( classNames)
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
cap = np.asarray(auto.screenshot()) 

# Init to get the webcam images 
while True: 
    cap = auto.screenshot().convert('RGB') 
    img = np.array( cap )
    img = img[:, :, ::-1].copy()

    scale_percent = 50 
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    success, img = ( True , resized )

    # This is the step of img is put in the dnn net 
    classIds, confs, bbox = net.detect( img, confThreshold = 0.7 )

    # If have some classId detected in the image it will draw the rectangle and put the name of it
    if len( classIds ) != 0: 
        for classId, confidence, box in zip( classIds.flatten(), confs.flatten(), bbox ):
            cv2.rectangle( img, box, color = [255, 0, 0], thickness = 2 )
            cv2.putText  ( img, classNames[classId-1], [box[0]+10, box[1]+30], cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 2 )
            cv2.putText  ( img, str(round(confidence*100,2)), [box[0]+10, box[1]+50], cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 2 )

    scale_percent = 200
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    # Shows the image 
    cv2.imshow( "WebCam Detect", resized )

    # Press key Q to exit  
    if cv2.waitKey( 1 ) & 0xFF == ord('q'): 
        break 
