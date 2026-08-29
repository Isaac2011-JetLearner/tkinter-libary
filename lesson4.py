import cv2
# How to draw a line on an image

pika_img = cv2.imread("pika.png",1)
cv2.imshow("PIKA IMAGE",pika_img)

starting_point = (0,60)
ending_point = (200,300)
width = 10
colour = (255,0,0)
line_img = cv2.line(pika_img,starting_point,ending_point,color= colour,thickness= width)
cv2.imshow("line image", line_img)


# How to make a rectangle on an image
pika_img = cv2.imread("pika.png",1)

starting_point_1 = (250,250)
ending_point_1 = (300,300)
colour = (255,255,0)
width = -1
rect_img = cv2.rectangle(pika_img,starting_point_1,ending_point_1,color= colour,thickness= width)
cv2.imshow("RECT IMG",rect_img)


# How to make a circle on an image
pika_img = cv2.imread("pika.png",1)

centre_cord = (250,275)
radius = 50
width = 300
colour =(255,0,255)
circle_img = cv2.circle(pika_img,center= centre_cord, radius= radius,color= colour,thickness= width)
cv2.imshow("CIRCLE IMG",circle_img)


# How to write tezt on the screen
pika_img = cv2.imread("pika.png",1)

size = 2
text = "Hello"
font = cv2.FONT_ITALIC
colour = (100,250,60)
cords = (50,300)
txt_img = cv2.putText(pika_img,text,cords,font,size,colour, 3,cv2.LINE_AA)
cv2.imshow("text image",txt_img)
cv2.waitKey(0)