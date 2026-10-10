import cv2
import os

imgs  = "data_sets"
person = "isaac"
print(hasattr(cv2,"CascadeClassifier"))
path = os.path.join(imgs,person)
if not os.path.isdir(path):
    os.mkdir(path)

webcam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
for i in range(30):
    answer,frame = webcam.read()
    if answer == False:
        break
    face_grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(face_grey,1.3,4)
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        face = face_grey[y:y+h,x:x+w]
        face_resize = cv2.resize(face,(130,100))
        cv2.imwrite("%s/%s.png"%(path,i+1),face_resize)
        
    cv2.imshow("picture",frame)
    key = cv2.waitKey(10)
    if key == 27:
        break



    
