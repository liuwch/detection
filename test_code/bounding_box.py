from PIL import Image
import sys
import cv2
import d2lzh_pytorch as d2l
sys.path.append("/home/Data1/liuwch/Datasets/DIDL")

# d2l.set_figsize()
# img = Image.open()
# img.show()
path = '/home/Data1/liuwch/Datasets/DIDL/docs/img/catdog.jpg'
image = cv2.imread(path)
cv2.imshow('img', image)
cv2.waitKey(2000)


def bbox_to_rect(bbox, color):  # 本函数已保存在d2lzh_pytorch中方便以后使用
    # 将边界框(左上x, 左上y, 右下x, 右下y)格式转换成matplotlib格式：
    # ((左上x, 左上y), 宽, 高)
    return d2l.plt.Rectangle(
        xy=(bbox[0], bbox[1]), width=bbox[2]-bbox[0], height=bbox[3]-bbox[1],
        fill=False, edgecolor=color, linewidth=2)

img_rect = bbox_to_rect(image, 'blue')
cv2.imshow('img_rect', img_rect)
cv2.waitKey(2000)
# img_rect.show()