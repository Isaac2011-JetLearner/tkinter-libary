import cv2
import numpy

video = cv2.VideoCapture("video.mp4")

for i in range(60):
    returnvalue,background = video.read()
    if returnvalue == False:
        continue

print("hello")
while video.isOpened():
    returnvalue,image = video.read()
    if returnvalue == False:
        break

    hsv_img = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    lower_red = numpy.array([100,40,40])
    higher_red = numpy.array([100,255,255])
    mask_1 = cv2.inRange(hsv_img,lower_red,higher_red)

    lower_red_2 = numpy.array([150,40,40])
    higher_red_2 = numpy.array([180,255,255])
    mask_2 = cv2.inRange(hsv_img,lower_red_2,higher_red_2)

    mask_1 = mask_1+mask_2
    mask_1 = cv2.morphologyEx(mask_1,cv2.MORPH_OPEN,kernel= numpy.ones((3,3),numpy.uint8),iterations= 1,)
    mask_2 = cv2.bitwise_not(mask_1)
    result_1 = cv2.bitwise_and(background,background,mask= mask_1)
    result_2 = cv2.bitwise_and(image,image,mask= mask_2)
    final_result = cv2.addWeighted(result_1,1,result_2,1,0)
    cv2.imshow("show img",final_result)
    key = cv2.waitKey(10)
    if key == 27:
        break


