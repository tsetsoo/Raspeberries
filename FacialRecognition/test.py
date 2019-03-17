from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import os

 to build a custom face recognition datasetPython

# load OpenCV's Haar cascade for face detection from disk
detector = cv2.CascadeClassifier(args["cascade"])

# initialize the video stream, allow the camera sensor to warm up,
# and initialize the total number of example faces written to disk
# thus far
print("[INFO] starting video stream...")
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
total = 0
frame = vs.read()
orig = frame.copy()
frame = imutils.resize(frame, width=400)
     
        # detect faces in the grayscale frame
rects = detector.detectMultiScale(
cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
             
                # loop over the face detections and draw them on the frame
for (x, y, w, h) in rects:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

