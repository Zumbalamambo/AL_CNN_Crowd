import numpy
import theano.tensor as T
from cnn_structure import *

class CNN:
    def __init__(self, batch_size = 66):
        seed = 8000
        rng = numpy.random.RandomState(seed)

        nkerns = [32, 50, 64, 50, 32, 20]

        x = T.tensor4('x')  # the data is presented as rasterized images
        classifier = CNN_struct(
            rng=rng,
            input=x,
            nkerns=nkerns,
            batch_size=batch_size,
            image_size=[100, 100],
            image_dimension=3
        )

        #//TODO check if the wieghts file exist in the folder load the parameters otherwise keep it initial.
        return classifier
