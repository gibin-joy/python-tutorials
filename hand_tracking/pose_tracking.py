import cv2
import mediapipe as mp
mp_pose = mp.solutions.pose
mp_drawings = mp.solutions.drawing_utils

pose= mp_pose.Pose()

video = cv2.VideoCapture(0)

while True:
    x,frame = video.read()
    frame = cv2.resize(frame,(500,500))
    results = pose.process(frame)
    if results.pose_landmarks:
        mp_drawings.draw_landmarks(
            image=frame, 
            landmark_list= results.pose_landmarks,
            connections = mp_pose.POSE_CONNECTIONS
            )

    cv2.imshow('human_body_reader',frame)
    if cv2.waitKey(1) & 0xFF==27:               
        break
video.release()
cv2.destroyAllWindows()