import numpy
import theano

def generate_weights(filter_shape, fan_in, fan_out, activation, b_size):
    if activation == "relu":
        if len(filter_shape)==4:
            W_bound_6 = numpy.sqrt(6. / (fan_in + fan_out))
            W_bound_2 = numpy.sqrt(2. / (fan_in + fan_out))

            W_values = numpy.asarray(
                numpy.random.randn(filter_shape[0], filter_shape[1], filter_shape[2], filter_shape[3]) * W_bound_2,
                dtype=theano.config.floatX)

            # numpy.asarray(
            #         rng.uniform(low=-W_bound, high=W_bound, size=filter_shape),
            #         dtype=theano.config.floatX
            #     )
        else:
            W_bound_2 = numpy.sqrt(2. / (filter_shape[0] + filter_shape[1]))

            W_values = numpy.asarray(
                numpy.random.randn(filter_shape[0], filter_shape[1]) * W_bound_2,
                dtype=theano.config.floatX
            )

            #hidden layer
            # W_values = numpy.asarray(
            #     rng.uniform(
            #         low=-numpy.sqrt(6. / (n_in + n_out)),
            #         high=numpy.sqrt(6. / (n_in + n_out)),
            #         size=(n_in, n_out)
            #     ),
            #     dtype=theano.config.floatX
            # )

            #softmax
            # self.W = theano.shared(
            #     value=numpy.zeros(
            #         (n_in, n_out),
            #         dtype=theano.config.floatX
            #     ),
            #     name='W',
            #     borrow=True
            # )

            if activation == theano.tensor.nnet.sigmoid:
                W_values *= 4

        # the bias is a 1D tensor -- one bias per output feature map
        # initialize the baises b as a vector of n_out 0s
        b_values = numpy.zeros((b_size,), dtype=theano.config.floatX)
    # else:
    #     print "error"
    #     W_values = numpy.asarray(numpy.zeros(filter_shape[0], filter_shape[1], filter_shape[2], filter_shape[3]))
    #     b_values = numpy.asarray(numpy.zeros(b_size))

    return W_values,b_values