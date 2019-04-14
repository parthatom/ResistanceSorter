import cv2
import numpy as np

img = 'resistance3.jpg'
frame = cv2.imread(img, cv2.IMREAD_COLOR)
hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#Orange:
lower_orange = np.array([5,50,50])
upper_orange = np.array([10,255,255])
orangemask = cv2.inRange(hsv, lower_orange, upper_orange)
#Background Green:
#lower_green = np.array([50,20,50])
#upper_green = np.array([90,255,255])
#greenmask = cv2.inRange(hsv, lower_green, upper_green)

#mask=cv2.bitwise_or(orangemask, greenmask)

#Blue:
lower_blue = np.array([90,50,50])
upper_blue = np.array([120,255,255])
bluemask = cv2.inRange(hsv, lower_blue, upper_blue)
mask=cv2.bitwise_or(bluemask, orangemask)

#Yellow:
lower_yellow = np.array([20,50,50])
upper_yellow = np.array([30,255,255])
yellowmask = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask=cv2.bitwise_or(yellowmask,mask)

#red
lower_red = np.array([0,140,0])
upper_red = np.array([9,255,255])
redmask = cv2.inRange(hsv, lower_red, upper_red)
mask=cv2.bitwise_or(redmask, mask)

#brown
lower_brown = np.array([0,40,0])
upper_brown = np.array([8,130,255])
brownmask = cv2.inRange(hsv, lower_brown, upper_brown)
mask=cv2.bitwise_or(brownmask,mask)

#Violet:
lower_violet = np.array([128,51,0])
upper_violet = np.array([164,255,255])
violetmask = cv2.inRange(hsv, lower_violet, upper_violet)
mask= cv2.bitwise_or(violetmask,mask)

#black:
lower_black=np.array([0,0,0])
upper_black=np.array([180,255,30])
blackmask = cv2.inRange(hsv, lower_black, upper_black)
mask=cv2.bitwise_or(blackmask,mask)

#Green
lower_green = np.array([60,100,100])
upper_green = np.array([60,255,255])
greenmask = cv2.inRange(hsv, lower_green, upper_green)
mask=cv2.bitwise_or(greenmask,mask)

res = cv2.bitwise_and(frame,frame, mask= mask)

#median = cv2.medianBlur(res,3)
blur=cv2.GaussianBlur(res,(3,3),0)
mask=cv2.GaussianBlur(mask,(3,3),0)

whites = []
bshape=np.shape(mask)  #180,481,3
#print(np.shape(mask[0,0]))
for i in range(bshape[1]):
    #whites.append([])
    for j in range(bshape[0]):
        k=(mask[j,i])
        if(k==255):
            whites.append(i)
            break
    if(k==255):
        break
for i in range(bshape[1]-1,0,-1):
    #whites.append([])
    for j in range(bshape[0]):
        k=(mask[j,i])
        if(k==255):
            whites.append(i)
            break
    if(k==255):
        break
for i in range(bshape[0]):
    #whites.append([])
    for j in range(bshape[1]):
        k=(mask[i,j])
        if(k==255):
            whites.append(i)
            break
    if(k==255):
        break
for i in range(bshape[0]-1,0,-1):
    #whites.append([])
    for j in range(bshape[1]):
        k=(mask[i,j])
        if(k==255):
            whites.append(i)
            break
    if(k==255):
        break
        #print(k)
        #c=c+1
        #if(np.array_equal(mask[i,j],[0, 0, 0])):
        #    whites.append(i)

#print(blur)
firstinst=[whites[2],whites[0]]
lastinst=[whites[3],whites[1]]
print(firstinst)
print(lastinst)
#print(c)
#rectangle=mask[firstinst[0]:lastinst[0],firstinst[1]:lastinst[1]]
#cv2.rectangle(rectangle,(62,222), (113,259), (255,0,0),3)
cv2.imshow('frame', frame)
cv2.imshow('mask', mask)
cv2.imshow('res', res)
#cv2.imshow('median blur', median)
cv2.imshow('Gaussian blur', blur)
cv2.imshow("rectangle", rectangle)

cv2.waitKey(0)
cv2.destroyAllWindows()
