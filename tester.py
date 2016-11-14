import numpy
import theano.tensor as T
import theano

def softmax(w, t=1.0):
    e = numpy.exp(numpy.array(w) / t)
    dist = e / numpy.sum(e)
    return dist

data =  [  258.07516479,  -258.07516479]
# print softmax(data)

x = T.dvector('x')
f = theano.function([x], T.nnet.softmax(x))

# print f(data)

fan_in = 27
fan_out = 9
W_bound_2 = numpy.sqrt(2. / (fan_in + fan_out))
W_bound_6 = numpy.sqrt(6. / (fan_in + fan_out))


print W_bound_2, W_bound_6

rng = numpy.random.RandomState(8000)

print numpy.asarray(rng.uniform(low=-W_bound_2, high=W_bound_2, size=(1,3,3,3)), dtype=theano.config.floatX)

print "\n"

print numpy.asarray(rng.uniform(low=-W_bound_6, high=W_bound_6, size=(1,3,3,3)), dtype=theano.config.floatX)

print "\n"
filter_shape=(1, 3, 3, 3)

print filter_shape
print numpy.random.randn(filter_shape[0], filter_shape[1], filter_shape[2], filter_shape[3]) * W_bound_2