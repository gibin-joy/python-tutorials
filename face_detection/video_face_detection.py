import cv2
video=cv2.VideoCapture('opencv/VID-20240509-WA0000.mp4')

face_cascade= cv2.CascadeClassifier('face_detection/haarcascade_frontalface_default.xml')
eye_cascade= cv2.CascadeClassifier('face_detection/haarcascade_eye.xml')

while True:
    success,frame = video.read()
    grey_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(grey_img)
    eyes= eye_cascade.detectMultiScale(grey_img)

    print(faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),color=(0,255,0),thickness=5)
    
    for (x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),color=(0,255,0),thickness=5)



    cv2.imshow('face detection',frame)
    if cv2.waitKey(1) & 0XFF==27:
        break

cv2.release()
cv2.destroyAllWindows()