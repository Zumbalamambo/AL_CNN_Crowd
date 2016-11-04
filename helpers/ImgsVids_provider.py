import copy
import numpy as np
from os import listdir
from os.path import isfile, join

import cv2
from PyQt4.QtGui import *


def findImages(mypath):

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    return onlyfiles

def convert_cv2_pixmap(img):
    cvRGBImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    qimg = QImage(cvRGBImg.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
    return QPixmap(qimg)

#slice full imag into small patches
#//TODO this is first draft. It needs more work to optimize
def Image_slicer(img, head_locations):
    stride = 100
    h = img.shape[0]
    w = img.shape[1]
    c= 0
    grapper =[]


    for j in range(0,h,stride):
        for i in range(0, w, stride):

            if (j+stride) < h and (i + stride) < w:
                c +=1
                image_slice = img[j:j+stride,i:i+stride]
                # grapper.append(slice)
                # points = []
                # if len(head_locations) > 0:
                #     for idx in xrange(len(head_locations)):
                #         if i  <= head_locations[idx][0] and head_locations[idx][0] <= i + stride:
                #             if j < head_locations[idx][1] and head_locations[idx][1] <= j + stride:
                #                 # print('Image x: %d, y: %d' % (head_locations[idx][0], head_locations[idx][1]))
                #                 # print "x range from %d to %d" %(i, i + stride)
                #                 # the problem is with this function how to handle the array and the pointer to have the image and points on the same locations
                #                 x = head_locations[idx][0]- i
                #                 y = head_locations[idx][1] - j
                #                 locations = np.array([x,y])
                #                 points.append(locations)
                # data = np.array([image_slice, points])
            elif (j+stride) < h and (i + stride) > w:
                image_slice = np.zeros((100, 100, 3))
                image_slice[0:stride, 0:w-i] = img[j:j + stride, i:w]
                # cv2.imwrite('imgs/test%d.png'%j, img_zeros)
            elif (j+stride) > h and (i + stride) < w:
                image_slice = np.zeros((100, 100, 3))
                image_slice[0:h-j, 0:stride] = img[j:h, i:i+stride]
            else:
                image_slice = np.zeros((100, 100, 3))
                image_slice[0:h - j, 0:w-i] = img[j:h, i:w]

            points = []
            if len(head_locations) > 0:
                for idx in xrange(len(head_locations)):
                    if i <= head_locations[idx][0] and head_locations[idx][0] <= i + stride:
                        if j < head_locations[idx][1] and head_locations[idx][1] <= j + stride:
                            # print('Image x: %d, y: %d' % (head_locations[idx][0], head_locations[idx][1]))
                            # print "x range from %d to %d" %(i, i + stride)
                            # the problem is with this function how to handle the array and the pointer to have the image and points on the same locations
                            x = head_locations[idx][0] - i
                            y = head_locations[idx][1] - j
                            locations = np.array([x, y])
                            points.append(locations)
                data = np.array([image_slice, points])
            else:
                data = np.array(image_slice)
            grapper.append(data)


    # preview_img_points(grapper)
    return grapper

#convert image slices into flatten array and create the training array in the convoloution network dimensions
#fit the data into the network with reference to it is batch size which in this case is one
#the image size depends on the stride size in the slicing function ex. 100x100

def Image_predicted_labels(img, labels):
    stride = 100
    h = img.shape[0]
    w = img.shape[1]
    c = 0

    for j in range(0,h,stride):
        for i in range(0, w, stride):
            if (j+stride) < h and (i + stride) < w:
                if labels[c] == 1:
                    img[j:j+stride, i:i+stride, 2] = 0
            elif (j+stride) < h and (i + stride) > w:
                if labels[c] == 1:
                    img[j:j + stride, i:w, 2] = 0
            elif (j+stride) > h and (i + stride) < w:
                if labels[c] == 1:
                    img[j:h, i:i+stride, 2] = 0
            else:
                if labels[c] == 1:
                    img[j:h, i:w, 2] = 0

            c += 1

    return img

def preview_img_points(grapper):
    img,points = grapper[30]
    if len(points) > 0:
        test_image = copy.copy(img)
        print len(points)
        for idx in xrange(len(points)):
            x = points[idx][0]
            y = points[idx][1]
            cv2.circle(test_image, (x, y), 3, (0, 0, 255), -1)
        cv2.imshow('img', test_image)
        cv2.waitKey(0)