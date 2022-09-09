import mediapipe as mp
import numpy as np  
import time 
import cv2 

class HandDetector():

    tipIds = [ 4, 8, 12, 16, 20 ]

    def __init__(self, static_image_mode=False, max_num_hands=2, model_complexity=1, min_detection_confidence=0.5, min_tracking_confidence=0.5 ) -> None:
        self.mode = static_image_mode
        self.maxHands = max_num_hands
        self.model_comp = model_complexity
        self.detectionCon = min_detection_confidence
        self.trackCon = min_tracking_confidence

        self.mpHands = mp.solutions.hands
        self.hands   = self.mpHands.Hands( self.mode, self.maxHands, self.model_comp, self.detectionCon, self.trackCon )
        self.mpDraw  = mp.solutions.drawing_utils

        self.result = 0 
        self.lmList = [] 


    def findHands( self, img, draw = True ):
        imgRGB = cv2.cvtColor( img, cv2.COLOR_BGR2RGB )
        self.result = self.hands.process( imgRGB )
        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks( img, handLms, self.mpHands.HAND_CONNECTIONS )
        return img 
    

    def fingersUp( self ):
        fingers = 0
        # For the Thumb finger 
        if self.lmList[ self.tipIds[0]][1] < self.lmList[self.tipIds[0]-1][1]:
            fingers += 1
        # Four fingers 
        for id in range( 1, 5 ):
            if self.lmList[ self.tipIds[id]][2] < self.lmList[self.tipIds[id]-2][2]:
                fingers += 1 << id 
        return fingers
    
    
    def count_fingers( self, fingersBool ):
        totalFingers = 0  
        for n in range(0,5):
            if ((fingersBool >> n) & 0x01) == 1:
                totalFingers += 1 
        return totalFingers


    def findPosition( self, img, handNo = 0 ): 
        h, w, _ = img.shape
        self.lmList = [] 
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo]
            for id, lm in enumerate( myHand.landmark ):
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append( [id, cx, cy] )
        if self.lmList:
            return self.lmList 
        else: 
            return False 

    def get_limits( self, img, handNo = 0, get_list = False, draw = False ):
        xList = [ ]
        yList = [ ] 
        self.lmList = self.findPosition( img, handNo )
        if self.lmList:
            for _, x, y in self.lmList:
                xList.append( x )
                yList.append( y )

            xmin, xmax =  min(xList), max(xList) 
            ymin, ymax =  min(yList), max(yList) 
            bbox = xmin, ymin, xmax, ymax 

            if draw: 
                x1, y1, x2, y2 = bbox 
                cv2.rectangle( img, (x1, y1), (x2, y2), (0,255,0), 2 )

            if get_list:
                return self.lmList, bbox
            else: 
                return bbox
        else: 
            if get_list:
                return False, False
            else: 
                return False

    def findDistance( self, p1, p2, img, draw = True ): 
        x1, y1 = self.lmList[p1][1], self.lmList[4][2]
        x2, y2 = self.lmList[p2][1], self.lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2 
        lenght = np.hypot( x2 - x1, y2 - y1)
        
        if draw: 
            cv2.circle( img, (x1, y1), 15, (255,0,0), cv2.FILLED )
            cv2.circle( img, (x2, y2), 15, (255,0,0), cv2.FILLED )
            cv2.line( img, (x1, y1), (x2, y2), (255,0,0), 3)
            cv2.circle(img, (cx, cy), 20, (0,0,255), cv2.FILLED )
            return lenght, img, [x1, y1, x2, y2, cx, cy] 

        return lenght


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    detec = HandDetector( )

    pTime = 0
    while True: 
        success, img = cap.read() 
        
        img = detec.findHands( img )
        
        lmList = detec.findPosition( img )
        if lmList:
            print( lmList )

        cTime = time.time() 
        fps = 1/(cTime - pTime)
        pTime = cTime

        cv2.putText( img, f'FPS : {int(fps)}', (40,70), fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 1, color = (255,0,0), thickness = 3 )
        
        cv2.imshow( 'Image', img )
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  