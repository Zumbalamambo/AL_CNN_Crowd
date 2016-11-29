from os import listdir
from os.path import isfile, join
import Image
import cv2
from math import floor

import pickle

import numpy as np
import matplotlib.pyplot as plt

requiredSize = 100, 100

def read_files(folderPath):
    onlyfiles = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]
    return onlyfiles


def read_images(folder, filesList):
    Imgs = []
    for idx in range(len(filesList)):
        jpgfile = np.array(Image.open(join(folder, filesList[idx])))
        # jpgfile = resizeimage.resize_cover(jpgfile, requiredSize)
        resized = cv2.resize(jpgfile, requiredSize, interpolation=cv2.INTER_AREA)
        Imgs.append(resized)
    return np.array(Imgs)

def shuffle_set(dataset):
    c = list(dataset)
    np.random.shuffle(c)
    return c

#     c = list(dataset) #zip(Train_set_x,Train_set_y)
#     np.random.shuffle(c)
#     a,b = zip(*c)

def create_sets(set_pos, set_neg):
    pos = np.array(shuffle_set(set_pos))
    neg = np.array(shuffle_set(set_neg))

    train_pos_size = int(floor((pos.shape[0] * 70)/100))
    valid_pos_size = int(floor((pos.shape[0] * 20) / 100))
    test_pos_size = pos.shape[0] - train_pos_size - valid_pos_size

    train_neg_size = int(floor((neg.shape[0] * 70) / 100))
    valid_neg_size = int(floor((neg.shape[0] * 20) / 100))
    test_neg_size = neg.shape[0] - train_neg_size - valid_neg_size

    # train_size = int(floor(((pos.shape[0] + neg.shape[0]) * 70)/100))
    # valid_size = int(floor(((pos.shape[0] + neg.shape[0]) * 20)/100))
    # test_size = (pos.shape[0] + neg.shape[0]) - train_size - valid_size

    Train_set_pos_x = pos[0:train_pos_size]
    Train_set_neg_x = neg[0:train_neg_size]

    Train_set_pos_y = np.ones(Train_set_pos_x.shape[0])
    Train_set_neg_y = np.zeros(Train_set_neg_x.shape[0])

    Train_set_x = np.concatenate((Train_set_pos_x,Train_set_neg_x), axis=0)
    Train_set_y = np.concatenate((Train_set_pos_y,Train_set_neg_y), axis=0)

    c = shuffle_set(zip(Train_set_x,Train_set_y))
    Train_set_x, Train_set_y = zip(*c)


    valid_set_pos_x = pos[train_pos_size:train_pos_size+valid_pos_size]
    valid_set_neg_x = neg[train_neg_size:train_neg_size+valid_neg_size]

    valid_set_pos_y = np.ones(valid_set_pos_x.shape[0])
    valid_set_neg_y = np.zeros(valid_set_neg_x.shape[0])

    Valid_set_x = np.concatenate((valid_set_pos_x, valid_set_neg_x), axis=0)
    Valid_set_y = np.concatenate((valid_set_pos_y, valid_set_neg_y), axis=0)

    c = shuffle_set(zip(Valid_set_x, Valid_set_y))
    Valid_set_x, Valid_set_y = zip(*c)


    test_set_pos_x = pos[train_pos_size + valid_pos_size:]
    test_set_neg_x = neg[train_neg_size + valid_neg_size:]

    test_set_pos_y = np.ones(test_set_pos_x.shape[0])
    test_set_neg_y = np.zeros(test_set_neg_x.shape[0])



    Test_set_x = np.concatenate((test_set_pos_x, test_set_neg_x), axis=0)
    Test_set_y = np.concatenate((test_set_pos_y, test_set_neg_y), axis=0)

    c = shuffle_set(zip(Test_set_x, Test_set_y))
    Test_set_x, Test_set_y = zip(*c)


    return [(np.array(Train_set_x),Train_set_y), (np.array(Valid_set_x), Valid_set_y), (np.array(Test_set_x), Test_set_y)]


positive_folder = r'/hdd1T/frames_concert/Tomorrowland Belgium 2016 cropped faces/1/pos'
negative_folder = r'/hdd1T/frames_concert/Tomorrowland Belgium 2016 cropped faces/1/neg'

file_names = read_files(positive_folder)
posImgs_x = read_images(positive_folder, file_names)

file_names = read_files(negative_folder)
negImgs_x = read_images(negative_folder, file_names)

Dataset = create_sets(posImgs_x, negImgs_x)

# train,valid,test = Dataset
#
# tr_x , tr_y = test
#
# for idx in xrange(len(tr_y)):
#     print tr_y[idx]
#     plt.imshow(tr_x[idx])
#     plt.show()


output = open("TLand_2016_faces_13516pos_4279neg.pkl", 'wb')
pickle.dump(Dataset, output)
output.close()

