from PIL import Image
import sys
import cv2
import d2lzh_pytorch as d2l
sys.path.append("/home/Data1/liuwch/Datasets/DIDL")

path = '/home/Data1/liuwch/Datasets/DIDL/docs/img/catdog.jpg'
image = cv2.imread(path)
cv2.imshow('img', image)
cv2.waitKey(2000)

dog_bbox, cat_bbox = [60, 45, 378, 516], [400, 112, 655, 493]

cv2.rectangle(image,dog_bbox,(0,255,0),3)
cv2.rectangle(image,cat_bbox,(0,0,255),3)



cv2.imshow('image_rect', image)
cv2.waitKey(2000)
