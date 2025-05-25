import cv2
cap=cv2.VideoCapture(0) #open web cam
while True: #check if web cam recording if false move out of loop
    ret,frame=cap.read() 
    if ret==False:
        continue
    cv2.imshow("video frame",frame)

    key_pressed=cv2.waitKey(1)&0xFF  #bitwise logic later in data collection
    if key_pressed==ord('q'): #'q' breaks loop and closes camera 
        break
cap.release()
cv2.destroyAllWindows()