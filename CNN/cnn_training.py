import os
import sys, getopt
import time
import numpy
import theano
import theano.tensor as T


# from sklearn import preprocessing
from cnn import CNN
import pickle as cPickle
from logistic_sgd import LogisticRegression
from CNN_Prediction import cnn_predict

def fit(data, labels, filename = 'weights.pkl'):
    fit_predict(data, labels, filename = filename)

def predict(test_dataset, filename = 'weights.pkl' ):
    return cnn_predict(filename= filename, test_datasets=[test_dataset])


def fit_predict(data, labels, filename, learning_rate=0.01, n_epochs=100, nkerns=[32, 50, 64, 50, 32, 20], batch_size=66, seed=8000):

    rng = numpy.random.RandomState(seed)
    x = T.tensor4('x')  # the data is presented as rasterized images
    y = T.ivector('y')  # the labels are presented as 1D vector of [int] labels
    index = T.lscalar()  # index to a [mini]batch

    ######################
    # BUILD ACTUAL MODEL #
    ######################
    print '... building the model'

    # construct the CNN class
    classifier = CNN(
        rng=rng,
        input=x,
        nkerns = nkerns,
        batch_size = batch_size,
        image_size=[100,100],
        image_dimension=3
    )

    train_set_x = theano.shared(numpy.asarray(data, dtype=theano.config.floatX))
    train_set_y = T.cast(theano.shared(numpy.asarray(labels, dtype=theano.config.floatX)), 'int32')
    print train_set_y.eval()
    # valid_set_x = theano.shared(numpy.asarray(valid_set_x, dtype=theano.config.floatX))
    # valid_set_y = T.cast(theano.shared(numpy.asarray(valid_set_y, dtype=theano.config.floatX)), 'int32')



    cost = classifier.layer8.negative_log_likelihood(y)
    # create a list of gradients for all model parameters
    grads = T.grad(cost, classifier.params)

    # specify how to update the parameters of the model as a list of (variable, update expression) pairs
    updates = [
        (param_i, param_i - learning_rate * grad_i)
        for param_i, grad_i in zip(classifier.params, grads)
    ]

    # compiling a Theano function `train_model` that returns the cost, but
    # in the same time updates the parameter of the model based on the rules defined in `updates`
    train_model = theano.function(
        inputs=[index],
        outputs=cost,
        updates=updates,
        givens={
            x: train_set_x[index * batch_size: (index + 1) * batch_size],
            y: train_set_y[index * batch_size: (index + 1) * batch_size]
        }
    )

    validate_model = theano.function(
        inputs=[index],
        outputs= classifier.layer8.get_p_y_given_x(y), #get_p_y_given_x(y), #grads,
        givens={
            x: train_set_x[index * batch_size:(index + 1) * batch_size],
            y: train_set_y[index * batch_size:(index + 1) * batch_size]
        },
        on_unused_input='ignore'
    )



    ###############
    # TRAIN MODEL #
    ###############
    print '... training'

    start_time = time.clock()
    epoch = 0

    # here is an example how to print the current value of a Theano variable: print test_set_x.shape.eval()

    # start training
    while (epoch < n_epochs):

        # learning_rate = learning_rate * (1 / (1 + 0.001 * epoch))
        # print "learning rate: %f" %learning_rate

        # py,log_py = validate_model(0)
        # y_x, p_y = validate_model(0)
        # print ""
        # print y_x
        # print p_y
        print classifier.__getstate__()[0]

        epoch = epoch + 1
        print "epoch %d" %epoch
        avg_cost = train_model(0)
        print "learning cost: %f" %avg_cost

        # validation_losses, predict_y = validate_model(0)




        # if (epoch) % 5  == 0:
            # compute zero-one loss on validation set

            # print validation_losses


            # this_validation_loss = numpy.mean(validation_losses)

            # print(
            #     'epoch %i, minibatch %i/%i, validation error %f %%' %
            #     (
            #         epoch,
            #         minibatch_index + 1,
            #         n_train_batches,
            #         this_validation_loss * 100.
            #     )
            # )

    # save parameters
    f = file(filename, 'wb')
    cPickle.dump(classifier.__getstate__(), f, protocol=cPickle.HIGHEST_PROTOCOL)
    f.close()

    end_time = time.clock()
    print >> sys.stderr, ('The code ran for %.2fm' % ((end_time - start_time) / 60.))