import cv2
pika_img = cv2.imread("pika.png",1)
cv2.imshow("pika",pika_img)

#convertion to a grayscale image
gray_pika = cv2.cvtColor(pika_img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray pikachu", gray_pika)

#convertion to a hsv image
# h = hue, hue is the colour, S = saturation, saturation is the intensity of the colour and v = value, value is the brightness of the image
hsv_pika = cv2.cvtColor(pika_img,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv_pikachu",hsv_pika)


#Rotation of an image
norm_pika = cv2.imread("pika.png",1)
rows,coloums = norm_pika.shape[0:2]
matrix = cv2.getRotationMatrix2D((coloums/2,rows/2),60,1)
rotated_pika = cv2.warpAffine(norm_pika,matrix,((coloums,rows)))
cv2.imshow("rotated pika",rotated_pika)
cv2.waitKey(0)



