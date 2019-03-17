import cv2
import numpy as np
import os
from sklearn import preprocessing

class LabelEncoding(object):
# Method to encode labels from words to numbers
    def encoding_labels(self, label_wordings):
        self.le = preprocessing.LabelEncoder()
        self.le.fit(label_wordings)

    def word_to_number(self, label_wordings):
        return int(self.le.transform([label_wordings])[0])

    def number_to_word(self, label_number):
        return self.le.inverse_transform([label_number])[0]
def getting_images_and_labels(path_input):
    label_wordings = []
    for roots, dirs, files in os.walk(path_input):
        for fname in (x for x in files if x.endswith('.jpg')):
            fpath = os.path.join(roots, fname)
            label_wordings.append(fpath.split('\\')[-2])

    images = []
    le = LabelEncoding()
    le.encoding_labels(label_wordings)
    labels = []
    # Parse the input directory
    for roots, dirs, files in os.walk(path_input):
        for fname in (x for x in files if x.endswith('.jpg')):
            fpath = os.path.join(roots, fname)

            img = cv2.imread(fpath, 0)
            names = fpath.split('\\')[-2]

            face = faceCascade.detectMultiScale(img, 1.1, 2, minSize=(100,100))

            for (x, y, w, h) in face:
                images.append(img[y:y+h, x:x+w])
                labels.append(le.word_to_number(names))
    return images, labels, le
if __name__=='__main__':
    path_cascade = "haarcascade_frontalface_alt.xml"
    train_img_path = 'C:\\Users\\Bonorose\\Desktop\\Ocado - Rasberies\\SmartHome\\SmartHome\\Images\\train'
    path_img_test = 'C:\\Users\\Bonorose\\Desktop\\Ocado - Rasberies\\SmartHome\\SmartHome\\Images\\test'

faceCascade = cv2.CascadeClassifier(path_cascade)
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
imgs, labels, le = getting_images_and_labels(train_img_path)

print "nTraining..."
#face_recognizer.train(imgs, np.array(labels))
face_recognizer.read("trained.xml")
print 'nPerforming prediction on test images...'
flag_stop = False
for roots, dirs, files in os.walk(path_img_test):
    for fname in (x for x in files if x.endswith('.jpg')):
        fpath = os.path.join(roots, fname)

        predicting_img = cv2.imread(fpath, 0)
        # Detect faces
        face = faceCascade.detectMultiScale(predicting_img, 1.1,2, minSize=(100,100))
        # Iterate through face rectangles
        for (x, y, w, h) in face:
        # Predict the output
            index_predicted, config = face_recognizer.predict(
            predicting_img[y:y+h, x:x+w])
            print index_predicted
        # Convert to word label
            person_predicted = le.number_to_word(index_predicted)
        # Overlay text on the output image and display it
            cv2.putText(predicting_img, 'Prediction: ' +
            person_predicted,
            (10,60), cv2.FONT_HERSHEY_SIMPLEX, 2,
            (255,255,255), 6)
            cv2.imshow("Recognizing face", predicting_img)
            a = cv2.waitKey(0)
            if a == 27:
                flag = True
                break
            if flag_stop:
                break