import cv2
import numpy as np

img = 'resistance4.jpg'#input('enter file name\n')
frame = cv2.imread(img, cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_red = np.array([0,0,14])
upper_red = np.array([180,255,30])


mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(frame,frame, mask= mask)

median=cv2.medianBlur(res,5)

cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.imshow('median blur',median)

cv2.waitKey(0)
cv2.destroyAllWindows()
