import HandTrackModule as htm 
import time 
import cv2 
import os 


# PATH FILE
PATH = os.path.dirname( __file__ ) +  '\\Images' 
FINGERS = os.listdir( PATH )
FINGERS_IMG = [] 


# Get the absolute path to the images 
for imgPath in FINGERS:
    image = cv2.imread( PATH + "\\" + imgPath )
    # image.resize([200,125,3])
    FINGERS_IMG.append( image )


# Hands detector
detector = htm.HandDetector( max_num_hands = 1 )


# Initalize the webcam 
wCam, hCam = 1200, 800

cap = cv2.VideoCapture( 0 )
cap.set( 3, wCam )
cap.set( 4, hCam )


# To detect fingers 
tipIds = [ 4, 8, 12, 16, 20 ]
cTime = 0
pTime = 0 

while True:
    # Read the webcam image 
    success, img = cap.read( )

    # Detect hands in the image 
    img = detector.findHands( img )
    lmList = detector.findPosition( img )


    # Count the fingers up 
    fingers = 0
    if lmList:
        # Dedão 
        if lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1]:
            fingers += 1
        # Outros dedos 
        for id in range(1, 5):
            if lmList[tipIds[id]][2]  < lmList[tipIds[id]-2][2]: 
                fingers += 1<<id 
        

    # Count the fingers up
    totalFingers = 0  
    for n in range(0,5):
        if ((fingers >> n) & 0x01) == 1:
            totalFingers += 1 
    print( 'Total de dedos levantados:', totalFingers )


    # Put the image in the image 
    h, w, c = FINGERS_IMG[totalFingers-1].shape
    img[10 : h+10, 10 : w+10] = FINGERS_IMG[totalFingers-1] 
    

    # Frame rate 
    cTime = time.time() 
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText( img, f'FPS : {int(fps)}', (40,70), fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 1, color = (255,0,0), thickness = 3 )


    cv2.imshow( 'Fingers count', img )
    cv2.waitKey( 1 )