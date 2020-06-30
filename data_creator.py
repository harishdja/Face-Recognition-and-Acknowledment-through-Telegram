import cv2 as c
import sqlite3

camera = c.VideoCapture(0)
classifier = c.CascadeClassifier('haarcascade_frontalface_default.xml')




regno = input("Enter the ID no:");



i=0

while True:
     ret, frame = camera.read()
     gray_frame = c.cvtColor(frame,c.COLOR_BGR2GRAY)
     face = classifier.detectMultiScale(gray_frame,1.3,5)
     for x,y,w,h in face:
          c.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),5)
          c.imshow("myface", frame)
          
          c.imwrite("facedata/students."+str(regno)+"."+str(i)+".jpg",gray_frame[y:y+h,x:x+w])
          i = i+1
     if c.waitKey(1) & 0xFF == ord('q'):
          break
     elif i>100:
          break

camera.release()
c.destroyAllWindows()
     
     
















     

