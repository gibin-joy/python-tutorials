## face detection

import cv2

img=cv2.imread('/home/user/Music/bd-sept/python-tutorials/face_detection/ana-de-armas.jpeg')

#read har cascade file for detection

face_cascade= cv2.CascadeClassifier('face_detection/haarcascade_frontalface_default.xml')
grey_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#pass image to face_cascade
faces =face_cascade.detectMultiScale(grey_img)

print(faces)

for (x,y,w,h) in faces:  #x-x,y-y,w-width,h-height
    cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=3)


cv2.imshow('face_detection',img)
cv2.waitKey(5000) 
cv2.destroyAllWindows()