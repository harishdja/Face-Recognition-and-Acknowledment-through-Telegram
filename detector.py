import telegram

from io import BytesIO

import cv2

import numpy as np

import sqlite3

import telegram

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)







19

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('trainer.yml')

auth_token = '417489646:AAG0ZJ09qVJhykNOyHrLb9wPdg_iGCYekaM' bot = telegram.Bot(token=auth_token) admin = bot.get_me()

channel_id ='@gotnotf'

i=0

while True:

ret, frame = camera.read()

gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

face = face_classifier.detectMultiScale(gray_frame,1.3,5)

ig=BytesIO(frame)

for x,y,w,h in face:

cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),10)

faceid, confi = recognizer.predict(gray_frame[y:y+h,x:x+w])

print(faceid, " ", confi)

conn = sqlite3.connect('mydbb')

cur = conn.cursor()

faceid=str(faceid)

cur.execute("SELECT name,relationship FROM familydata WHERE ID=?", (faceid,))

rows = cur.fetchone()

cv2.putText(frame,rows[0],(x,y-

5),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(255,255,255),10)

big="your"+rows[1]

bot.sendMessage(chat_id=channel_id,text=big)if i==0:

cv2.imwrite("1"+"."+"jpg",frame)

bot.send_photo(chat_id=channel_id,photo=open('1.jpg', 'rb'))

cv2.imshow('my face',frame)

k = cv2.waitKey(1)

if k==ord('q'):

break

camera.release()

cv2.destroyAllWindows()
