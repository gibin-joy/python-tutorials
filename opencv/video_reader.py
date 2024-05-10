import cv2

video= cv2.VideoCapture(0)   # or path in brackets

while True:
    success , frame =video.read()
    print(success)

    cv2.imshow('video_reader',frame)
    if cv2.waitKey(1) & 0xFF==27:               # 0xff==27 escape key
        break

video.release()
cv2.destroyAllWindows()

#webcam index : 0,1,2,-1,-2  (enter any of these values as path)


