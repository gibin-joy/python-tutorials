import cv2
import mediapipe as mp
 

mp_hands=mp.solutions.hands
mp_drawings = mp.solutions.drawing_utils
hands = mp_hands.Hands()




video= cv2.VideoCapture(0) 

while True:
    success,frame = video.read()
    frame=cv2.resize(frame,(500,500))

    results = hands.process(frame)

    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for hand_no,hand_landmarks in enumerate(results.multi_hand_landmarks):
            mp_drawings.draw_landmarks(
                image=frame, 
                landmark_list= results.hand_landmarks,
                connections = mp_hands.HAND_CONNECTIONS
                )


    cv2.imshow('webcam_hand_reader',frame)
    if cv2.waitKey(1) & 0xFF==27:               
        break

video.release()
cv2.destroyAllWindows()