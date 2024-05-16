import mediapipe as mp
import cv2

img = cv2.imread('hand_tracking/EyhYUTcWQAAloVc.jpeg')
converted =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)   #media pi[e cant read BGR, only process RGB
mp_hands=mp.solutions.hands
hands= mp_hands.Hands(static_image_mode=True,max_num_hands=2)

result=hands.process(img)
print(result.multi_handedness)

cv2.imshow('hand_tracking',img)
cv2.waitKey()
cv2.destroyAllWindows()