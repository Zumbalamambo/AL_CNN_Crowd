from os import listdir, rename
from os.path import isfile, join
from string import join as jo
import numpy as np
import Image


def read_files(folderPath):
    onlyfiles = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]
    return onlyfiles


def remove_images(folder, filesList):
    folder_to_move = r'/hdd1T/frames_concert/Tomorrowland Belgium 2016 cropped faces/1/neg/'
    for idx in range(len(filesList)):
            rename(join(folder,filesList[idx]), join(folder_to_move,filesList[idx]))



positive_folder = r'/hdd1T/frames_concert/Tomorrowland Belgium 2016 cropped faces/1/pos/small'
negative_folder = r'/hdd1T/frames_concert/Tomorrowland Belgium 2016 cropped faces/1/neg/small'

file_names = read_files(negative_folder)
remove_images(negative_folder, file_names)




