import cv2
import numpy as np
import os
import sys

IOError = OSError
#-----------
frontalface_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')


#----------------
if frontalface_cascade.empty():
    raise IOError('Unable to load the face cascade classifier xml file')

capture = cv2.VideoCapture(usePiCamera=True)

scale_factor = 0.4

# Loop until you hit the Esc key
while True:
    ret, frame = capture.read()

    frame = cv2.resize(frame, None, fx=scale_factor, fy=scale_factor,
    interpolation=cv2.INTER_AREA)
    
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_rectangle = frontalface_cascade.detectMultiScale(gray_image, 1.3, 5)

    for (x,y,w,h) in face_rectangle:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

    cv2.imshow('Face Detector', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()


