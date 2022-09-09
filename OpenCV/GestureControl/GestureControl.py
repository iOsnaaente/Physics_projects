import HandTrackModule as htm 
import numpy as np 
import time
import cv2 

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume 
from ctypes import cast, POINTER 
from comtypes import CLSCTX_ALL 

# Variables 
wCam, hCam = 480, 340  
volBar = 400 
pTime = 0 
vol = 0 


# Webcam initialization 
cap = cv2.VideoCapture( 0 )
cap.set( 3, wCam ) 
cap.set( 4, hCam ) 


# Hands detector 
detector  = htm.HandDetector( max_num_hands = 1, min_detection_confidence = 0.75 ) 


# Volume control objects 
devices   = AudioUtilities.GetSpeakers()
interface = devices.Activate( IAudioEndpointVolume._iid_, CLSCTX_ALL, None )
volume    = cast( interface, POINTER( IAudioEndpointVolume))


# Volume configurations by default  
MIN_VOL, MAX_VOL, _ = volume.GetVolumeRange( )
volume.SetMasterVolumeLevel( 0, None )


while True:
    success, img = cap.read()

    # Find hand 
    img = detector.findHands( img )
    lmList, bbox = detector.get_limits( img, get_list = True, draw = True )

    if lmList : 

        # Filter based on size
        area = ((bbox[2]-bbox[0])*(bbox[3]-bbox[1]))//100
        print( area ) 
        if 100 < area < 600:
            print( 'Control working' )


        # Find distance between index and Thumb 
        lenght, img, lineInfo = detector.findDistance( 4, 8, img )


        # Convert volume 
        volBar = np.interp( lenght, [50, 150], [400, 150] )
        volPer = np.interp( lenght, [50, 150], [  0, 100] )
        

        # Reduce Resolution to make it smoother
        smoothness = 5
        volPer = smoothness * round( volPer/smoothness)
        

        # Check fingers up 
        fingers = detector.fingersUp()
        

        # If Pinky is down set Volume 
        if ((fingers >> 4) & 0x01) == 1:
            volume.SetMasterVolumeLevelScalar( volPer/100, None ) # Values between [0,1] 
            cv2.circle(img, (lineInfo[4], lineInfo[5]), 20, (0,255, 0), cv2.FILLED )
        

        # Drawings 
        if lenght<50:
            cv2.circle(img, (lineInfo[4], lineInfo[5]), 20, (0,255, 0), cv2.FILLED )


    # Draw the volume bar 
    cv2.putText  ( img, 'Vol.', (40, 125), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 3)
    cv2.rectangle( img, (50,         150 ), (85, 400), (0,255,0), 3 )
    cv2.rectangle( img, (50, int(volBar)),  (85, 400), (10,200,0), cv2.FILLED )

    
    # Frame rate 
    cTime = time.time() 
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText( img, f'FPS : {int(fps)}', (40,70), fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 1, color = (255,0,0), thickness = 3 )


    cv2.imshow( 'Volume control project', img )
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
