import cv2

video = cv2.VideoCapture(r"images\animal_vid.avi")

"""for i in range(60):
    returnvalue,background = video.read()
    if returnvalue == False:
        continue
"""
print("hello")
while video.isOpened():
    returnvalue,image = video.read()
    if returnvalue == False:
        break
    cv2.imshow("show img",image)
    key = cv2.waitKey(60)
    if key == 27:
        break