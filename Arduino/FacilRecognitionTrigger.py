from imutils.video import VideoStream
import time
import cv2
import imutils

realLabels = {0: "simo", 1: "tsetso"}

detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

def trigger():
    print("[INFO] starting video stream...")
    vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)
    frame = vs.read()
    frame = cv2.resize(frame, (640,480))
     
    rects = detector.detectMultiScale(
    cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))
    
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read("trained.xml")
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        index_predicted, config = face_recognizer.predict(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)[y:y+h, x:x+w])
        cv2.destroyAllWindows()
        vs.stop()
        return realLabels[index_predicted]

    cv2.destroyAllWindows()
    vs.stop()
