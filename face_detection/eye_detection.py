## face detection

import cv2

img=cv2.imread('/home/user/Music/bd-sept/python-tutorials/face_detection/ana-de-armas.jpeg')

#read har cascade eye file for detection

eye_cascade= cv2.CascadeClassifier('/home/user/Music/bd-sept/python-tutorials/face_detection/haarcascade_eye.xml')
grey_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#pass image to face_cascade
eyes =eye_cascade.detectMultiScale(grey_img)

print(eyes)

for (x,y,w,h) in eyes:  #x-x,y-y,w-width,h-height
    cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=3)


cv2.imshow('eye_detection',img)
cv2.waitKey(5000) 
cv2.destroyAllWindows()