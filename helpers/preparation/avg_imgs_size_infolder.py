from os import listdir
from os.path import isfile, join
import Image
import pickle

import numpy as np
import matplotlib.pyplot as plt


def read_files(folderPath):
    onlyfiles = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]
    return onlyfiles


def get_imgs_sizes(filesList, folder):
    sizes = np.zeros((len(filesList), 2))

    for idx in range(len(filesList)):
        jpgfile = np.array(Image.open(join(folder, filesList[idx])))

        sizes[idx, 0] = jpgfile.shape[0]
        sizes[idx, 1] = jpgfile.shape[1]
    return sizes

def sum_sizes_number(pos):
    pos_sizes_avg = np.zeros((len(pos), 3))
    for idx in range(len(pos)):
        x = pos[idx][0]
        y = pos[idx][1]

        c = -1
        for j in range(len(pos_sizes_avg)):

            if pos_sizes_avg[j][2] == 0:
                c = j
                break

            if pos_sizes_avg[j][0] == x:
                if pos_sizes_avg[j][1] == y:
                    pos_sizes_avg[j][2] += 1
                    break

        if c > -1:
            pos_sizes_avg[c][0] = x
            pos_sizes_avg[c][1] = y
            pos_sizes_avg[c][2] = 1

    return pos_sizes_avg[pos_sizes_avg[:, 2] > 0, :]




# positive_folder = r'/hdd1T/frames_concert/Tomorrowland Belgium 2016 cropped faces/1/pos'
# negative_folder = r'/hdd1T/frames_concert/Tomorrowland Belgium 2016 cropped faces/1/neg'
#
# file_names = read_files(positive_folder)
# pos_sizes = get_imgs_sizes(file_names,positive_folder)
#
# file_names = read_files(negative_folder)
# neg_sizes = get_imgs_sizes(file_names, negative_folder)
#
# dataset = [pos_sizes, neg_sizes]
#
##save ple file
# output = open("pos_neg_sizes.pkl", 'wb')
# pickle.dump(dataset, output)
# output.close()


#Load pkl file
pkl_file = open('pos_neg_sizes.pkl', 'rb')
mydict2 = pickle.load(pkl_file)
pkl_file.close()

pos, neg = mydict2

pos_sizes_avg = sum_sizes_number(pos)
neg_sizes_avg = sum_sizes_number(neg)

test = pos_sizes_avg[pos_sizes_avg[:, 0] > 100, :]
test = test[test[:, 1] > 100, :]

print sum(test[:,2])


# print len(test)
# plt.hist(test[:,1], bins=30, range=(0, 300))
# # plt.hist(pos[:,1], bins=15, range=(0, 300))
# plt.show()

# print len(pos_sizes_avg)
# print len(neg_sizes_avg)

# print len(pos)
# test = pos_sizes_avg[pos_sizes_avg[:, 2] > 10, :]
# print sum(test[:,2])
#
# # plt.hist(test[:,2], bins=15, range=(0, 150))
# # plt. show()
#
# test = pos_sizes_avg[pos_sizes_avg[:, 2] > 50, :]
# test = test[test[:, 2] < 60, :]
# print sum(test[:,2])
# print len(test)
#
# # plt.scatter(test[:,0],test[:,1],s=test[:,2])
# # plt.show()
# # print len(test)
# #
# for idx in xrange(len(test)):
#     print test[idx]
# #
# # print sum(test[:,2])plt.hist(pos_sizes_avg[:,2], bins=15, range=(0, 150))
# plt. show()
# x = xrange(len(test))
# plt.bar(x, test[:,2])
# plt. show()
# #
# #
# #
