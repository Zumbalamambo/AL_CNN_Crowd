import copy
import numpy as np
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt

import cv2
from PyQt4.QtGui import *


def findImages(mypath):

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    return onlyfiles

def convert_cv2_pixmap(img):
    cvRGBImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    qimg = QImage(cvRGBImg.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
    return QPixmap(qimg)

def draw_boxes(img):
    stride = 100
    h = img.shape[0]
    w = img.shape[1]

    for j in range(0,h,stride):
        for i in range(0, w, stride):
            start_top_left_y = j
            start_top_left_x = i
            end_bottom_right_y = j + stride
            end_bottom_right_x = i + stride
            cv2.rectangle(img, (start_top_left_x, start_top_left_y),
                          (end_bottom_right_x, end_bottom_right_y),
                          (0, 0, 255),
                          1)
    return img


#slice full imag into small patches
def Image_slicer(img, head_locations, Loc):
    stride = 100
    h = img.shape[0]
    w = img.shape[1]
    c= 0
    grapper =[]


    for j in range(0,h,stride):
        for i in range(0, w, stride):

            if (j+stride) < h and (i + stride) < w:
                c +=1
                image_slice = img[j:j+stride,i:i+stride,:]
            elif (j+stride) < h and (i + stride) > w:
                image_slice = np.zeros((100, 100, 3))
                image_slice[0:stride, 0:w-i,:] = img[j:j + stride, i:w,:]
                # cv2.imwrite('imgs/test%d.png'%j, img_zeros)
            elif (j+stride) > h and (i + stride) < w:
                image_slice = np.zeros((100, 100, 3))
                image_slice[0:h-j, 0:stride,:] = img[j:h, i:i+stride,:]
            else:
                image_slice = np.zeros((100, 100, 3))
                image_slice[0:h - j, 0:w-i,:] = img[j:h, i:w,:]

            points = []
            if Loc:
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


def Image_deSlicer(img_src, image_slices):
    stride = 100
    img = copy.copy(img_src)
    h = img.shape[0]
    w = img.shape[1]
    c= 0

    for j in range(0,h,stride):
        for i in range(0, w, stride):
            # print "c: %d;   j: %d;   i: %d" %(c, j,i)
            if (j+stride) < h and (i + stride) < w:
                img[j:j + stride, i:i + stride] = image_slices[c]
            elif (j+stride) < h and (i + stride) > w:
                img[j:j + stride, i:w]  = image_slices[c][:stride, :img.shape[1] - i]
            elif (j+stride) > h and (i + stride) < w:
                img[j:h, i:i+stride] = image_slices[c][:img.shape[0] - j, :stride]
            else:
                img[j:h, i:w]  = image_slices[c][:img.shape[0] - j, :img.shape[1] - i]
            c += 1

    # cv2.imshow('test', img)
    # cv2.waitKey(0)


def visualize_convoulved_imgs(conv):

    stride = conv.shape[1]
    # to recover the structure from previous slicing function original image width was 1024 and hieght was 576
    # stride w =  1024 / 100 = 10 + 1 = 11
    # stride h =  576 / 100 = 5 + 1 = 6
    # h = (stride * 5) + 75
    # w = (stride * 10) + 23
    # img = np.zeros((h,w))

    # c = 0
    # for j in range(5):
    #     for i in range(10):
    #         start_j = j * stride
    #         end_j = (j + 1) * stride
    #         start_i = i * stride
    #         end_i = (i + 1) * stride
    #
    #         if c >= 0 and c < 10:
    #             img[start_j:end_j, start_i:end_i] = conv[c]
    #             print c
    #         elif c >= 11 and c < 20:
    #             img[start_j:end_j, start_i:end_i] = conv[c]
    #             print c
    #         elif c >= 21 and c < 30:
    #             img[start_j:end_j, start_i:end_i] = conv[c]
    #             print c
    #         elif c >= 31 and c < 40:
    #             img[start_j:end_j, start_i:end_i] = conv[c]
    #             print c
    #         elif c >= 41 and c < 50:
    #             img[start_j:end_j, start_i:end_i] = conv[c]
    #             print c
    #
    #         c += 1


    # c= 0
    # for j in range(0,h,stride):
    #     for i in range(0, w, stride):
    #         # print "c: %d;   j: %d;   i: %d" %(c, j,i)
    #         if (j+stride) < h and (i + stride) < w:
    #             img[j:j + stride, i:i + stride] = conv[c]
    #         elif (j+stride) < h and (i + stride) > w:
    #             img[j:j + stride, i:w]  = conv[c][:stride, :img.shape[1] - i]
    #         elif (j+stride) > h and (i + stride) < w:
    #             img[j:h, i:i+stride] = conv[c][:img.shape[0] - j, :stride]
    #         else:
    #             img[j:h, i:w]  = conv[c][:img.shape[0] - j, :img.shape[1] - i]
    #         c += 1

    h = (stride * 6)
    w = (stride * 11)
    img = np.zeros((h, w))

    c = 0
    for j in range(0, h, stride):
        for i in range(0, w, stride):
            img[j:j + stride, i:i + stride] = conv[c]
            c += 1

    return img
    # plt.imshow(img, cmap = 'Greys_r')
    # plt.show()
    # cv2.imshow('test', img)
    # cv2.waitKey(0)


#convert image slices into flatten array and create the training array in the convoloution network dimensions
#fit the data into the network with reference to it is batch size which in this case is one
#the image size depends on the stride size in the slicing function ex. 100x100
def Image_predicted_labels(img_src, labels):

    img = copy.copy(img_src)
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


def construct_W_image(params):
    """
    :param network wieghts and bases in this structure:
     (layer3.W, layer3.b,
      layer2.W, layer2.b,
      layer1.W, layer1.b,
      layer0.W, layer0.b)
    :return: Construct image from the weight matrix and return the image
    """
    # w, b  = params.get_value()
    # w = np.reshape(w, (32, 9))
    # # print ("len lay_0 W: ", layer1_w.shape)
    # # print ("len lay_0 b: ", len(layer1_b))
    #
    # f, s = 8, 4
    # image =  Image.fromarray(
    #     tile_raster_images(
    #         X=w,
    #         img_shape=(3, 3, 3),
    #         tile_shape=(f, s),
    #         tile_spacing=(1, 1)
    #     )
    # )
    #
    # save_image(image, "layer_0.png")
