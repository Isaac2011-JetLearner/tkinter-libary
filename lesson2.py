import cv2
import numpy as np
keep = cv2.imread("gliter_background.png",1)
cv2.imshow("gliter",keep)
img1 = cv2.resize(keep,(400,500))
cv2.imshow("gliter_resize",img1)# resizing of images

keep = cv2.imread("flowers-background.png",1)
cv2.imshow("flowers_background",keep)
img2 = cv2.resize(keep,(400,500))
cv2.imshow("flowers_resize",img2)

joined_image = cv2.addWeighted(img1,0.3,img2,0.7,2)
cv2.imshow("joined image",joined_image)# adding images together


# subraction of images
keep_1 = cv2.imread("diamond.jpg",1)
cv2.imshow("diamond-background",keep_1)


keep_2 = cv2.imread("star.jpg",1)
cv2.imshow("star_background",keep_2)


store = cv2.subtract(img2,img1)
cv2.imshow("subracted_image",store)


# erosion of a image
kobe = cv2.imread("kobe.jpg",1)
cv2.imshow("kobe_image",kobe)

kernel = np.ones((1,1),np.uint8)
image = cv2.erode(kobe,kernel)
cv2.imshow("eroded_image",image)


# bordering a image
kobe = cv2.imread("kobe.jpg",1)
cv2.imshow("kobe_image",kobe)
# solid border
stored_img = cv2.copyMakeBorder(kobe,5,5,5,5,cv2.BORDER_CONSTANT,value= 1)
cv2.imshow("stored_img",stored_img)
cv2.waitKey(0)