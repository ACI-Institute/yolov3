from matplotlib import pyplot as plt
import numpy as np
from utils.utils import xywh2xyxy
from pathlib import Path
import PIL.Image as IMG
from PIL.JpegImagePlugin import JpegImageFile
from utils.datasets import LoadImagesAndLabels
from numpy import genfromtxt

def plot_images(imgs, targets, paths=None, fname='images.jpg'):
    # targets = targets[targets[:, 1] == 21]  # plot only one class

    fig = plt.figure(figsize=(10, 10))
    bs, _, h, w = imgs.shape  # batch size, _, height, width
    bs = min(bs, 16)  # limit plot to 16 images
    ns = np.ceil(bs ** 0.5)  # number of subplots

    for i in range(bs):
        boxes = xywh2xyxy(targets[targets[:, 0] == i, 2:6]).T
        boxes[[0, 2]] *= w
        boxes[[1, 3]] *= h
        plt.subplot(ns, ns, i + 1).imshow(imgs[i].transpose(1, 2, 0))
        plt.plot(boxes[[0, 2, 2, 0, 0]], boxes[[1, 1, 3, 3, 1]], '.-')
        plt.axis('off')
        if paths is not None:
            s = Path(paths[i]).name
            plt.title(s[:min(len(s), 40)], fontdict={'size': 8})  # limit to 40 characters
    fig.tight_layout()
    fig.savefig(fname, dpi=200)
    plt.close()


#imgs = np.zeros((8, 3, 416, 416))

# targets = np.array([
#  [          0,           0,     0.95956,     0.60819,    0.022063,    0.032906],
#  [          0,           0,     0.01241,     0.62168,    0.024819,     0.10984],
#  [          0,           0,    0.019764,     0.60881,    0.035703,    0.092516],
#  [          0,           0,    0.018319,     0.60389,    0.025234,    0.098422],
#  [          0,           0,    0.034085,     0.61269,    0.036094,     0.10041],
#  [          0,           0,   0.0092416,     0.61505,    0.018483,     0.11192],
#  [          0,           0,     0.13223,     0.56948,    0.024391,    0.029719],
#  [          0,           0,     0.15283,     0.58319,    0.022078,    0.050562],
#  [          1,           0,     0.72649,    0.080609,     0.34347,     0.16122],
#  [          1,           0,     0.67338,     0.63877,     0.17095,     0.43292],
#  [          1,           0,     0.98269,     0.60137,    0.034625,    0.057339],
#  [          1,           1,     0.71372,      0.4526,     0.02331,    0.041662],
# ])
img_list = [
    'data/coco/images/train2014/COCO_train2014_000000581909.jpg',
]
images = []
labels = []
for i, path in enumerate(img_list):
    images.append(np.array(IMG.open(path).resize((416, 416))))
    label_file = path.replace('images', 'labels').replace('jpg', 'txt')
    with open(label_file) as f:
        line = f.readline().split(' ')
        out = [i]
        for num in line:
            try:
                out.append(float(num))
            except:
                pass
    labels.append(out)





images = np.asarray(images)
images = np.rollaxis(images, 3, 1)
targets = np.array(labels)
#images = np.zeros((2, 3, 416, 416))

plot_images(images, targets, paths=None, fname='images.jpg')
