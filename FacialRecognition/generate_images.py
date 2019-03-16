#Image Collector

import cv2
import numpy as np
import os

IOError = OSError
#-----------
frontalface_cascade = cv2.CascadeClassifier('D:\OpenCV\opencv\sources\data\haarcascades\haarcascade_frontalface_alt.xml')


#----------------
if frontalface_cascade.empty():
    raise IOError('Unable to load the face cascade classifier xml file')

capture = cv2.VideoCapture(0)
baseNameFile = 'tsetso'
nameFile = '';
counter = 1;

scale_factor = 0.4

# Loop until you hit the Esc key
while True:
    ret, frame = capture.read()
    
    cv2.imwrite( str(nameFile) + ".jpg",frame)
    nameFile = baseNameFile + str(counter)
    counter += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
