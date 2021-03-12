import numpy as np
import cv2


# The main link to use the arquives in the folder 
main_link = 'D:\Desktop\git\Tracker\\'

video_src = main_link + '1.mp4'

# To use the notebook's camera.  
capture = cv2.VideoCapture( video_src )

# Dimensões da tela a partir do frame
frame = capture.read()[1]
w, h, c = frame.shape 
p_line    = round(w/2)
p_inicial = ( 0, p_line )
p_final   = ( h, p_line )

backsub = cv2.createBackgroundSubtractorMOG2( )             # background subtraction to isolate moving cars

count = 0
sen = 0 

x_ant = 0
y_ant = 0 
def vector_pos( x, y, x_ant, y_ant):
    dif_x = x - x_ant 
    dif_y = y - y_ant
    return (dif_x, dif_y)


while True:
    frame = capture.read()[1]

    fgmask = backsub.apply( frame, None, 0.01 )

    erode = cv2.erode( fgmask, None, iterations = 3 )       # erosion to erase unwanted small contours

    moments = cv2.moments( erode, True )                    # moments method applied

    area = moments['m00']

    try:
        x_ant = x
        y_ant = y
    except:
        x_ant = 0
        y_ant = 0 

    if moments['m00'] >= 600:
        x = int(moments['m10'] / moments['m00'])
        y = int(moments['m01'] / moments['m00'])

        _, dif_y = vector_pos( x, y, x_ant, y_ant )

        if dif_y > 6: 
            if y < p_line:
                sen = sen << 1
            else:
                sen = (sen << 1) | 1
                sen = sen & 0x03
            if sen == 1:
                count = count + 1
                

    cv2.circle( frame, (x, y), 25, (0, 0, 255), -1)          # center, radius, colour, -1=fill
    cv2.line( frame, p_inicial, p_final, (0, 255, 0), 2)
    
    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(frame, 'count:'+str(count), (10, 30), font, 1, (255, 0, 0), 2)
    cv2.putText(frame, 'x='+str(x)+' y='+str(y), (10,60), font, 1, (255, 0, 0), 2)

    cv2.imshow('erode', erode)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
