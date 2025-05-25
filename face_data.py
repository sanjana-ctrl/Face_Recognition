import cv2
import numpy as np

cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

skip=0
face_data=[]
dataset_path="./face_dataset/"

file_name=input("Enter the name of person:")

while True:
    ret,frame=cap.read()

    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if ret==False:
        continue

    faces=face_cascade.detectMultiScale(gray_frame,1.3,5)
    if len(faces)==0:
        continue

    k=1

    faces=sorted(faces,key=lambda x: x[2]*x[3],reverse=True)