import cv2
import os
from PIL import Image
path = "images"
os.chdir(path)


sum_width = 0
sum_height = 0
num_images = 0
files = os.listdir(".")
for file in files:
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
       keep = Image.open(file)
       img_width,img_height = keep.size
       sum_width+=img_width
       num_images+=1
       sum_height+=img_height

average_height = sum_height//num_images
average_width = sum_width//num_images
for file in files:
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
       keep = Image.open(file)
       img_resize = keep.resize((average_width,average_height),Image.Resampling.LANCZOS)
       img_resize.save(file,"JPEG",quality = 95)

print(average_height,average_width)



