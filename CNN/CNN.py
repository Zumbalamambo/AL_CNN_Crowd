import numpy
import theano.tensor as T
from cnn_structure import *
from cnn_training import fit_predict
from cnn_Prediction import cnn_predict

import pickle as cPickle
import os.path

class CNN:
    def __init__(self,filename, batch_size = 66, learning_rate = 0.0001):

        seed = 8000
        rng = numpy.random.RandomState(seed)
        nkerns = [32, 50, 64, 50, 32, 20]

        self.batch_size = batch_size
        self.x = T.tensor4('x')  # the data is presented as rasterized images

        ######################
        # BUILD ACTUAL MODEL #
        ######################
        print '... building the model'

        # construct the CNN class
        self.classifier = CNN_struct(
            rng=rng,
            input=self.x,
            nkerns=nkerns,
            batch_size=batch_size,
            image_size=[100, 100],
            image_dimension=3
        )


        self.file_name = filename
        if(os.path.isfile(filename)):
            f = open(filename, 'rb')
            self.classifier.__setstate__(cPickle.load(f))
            f.close()
            print ("Parameters loaded")
        else:
            print "No trained parameteres exist. network is initiated"

    def fit(self, data, labels):
        fit_predict(self.classifier, self.x, data, labels, self.batch_size)

        # save parameters
        f = file(self.file_name, 'wb')
        cPickle.dump(self.classifier.__getstate__(), f, protocol=cPickle.HIGHEST_PROTOCOL)
        f.close()
        print ("parameters saved")


    def predict(self, test_dataset):
        return cnn_predict(self.classifier, self.x, test_dataset, self.batch_size)

