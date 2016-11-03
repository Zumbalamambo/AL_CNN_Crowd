import numpy
import theano.tensor as T
import theano

def softmax(w, t=1.0):
    """Calculate the softmax of a list of numbers w.

    Parameters
    ----------
    w : list of numbers
    t : float

    Return
    ------
    a list of the same length as w of non-negative numbers

    Examples
    --------
    # >>> softmax([0.1, 0.2])
    array([ 0.47502081,  0.52497919])
    # >>> softmax([-0.1, 0.2])
    array([ 0.42555748,  0.57444252])
    # >>> softmax([0.9, -10])
    array([  9.99981542e-01,   1.84578933e-05])
    # >>> softmax([0, 10])
    array([  4.53978687e-05,   9.99954602e-01])
    """
    e = numpy.exp(numpy.array(w) / t)
    dist = e / numpy.sum(e)
    return dist

data =  [  258.07516479,  -258.07516479]
print softmax(data)

x = T.dvector('x')
f = theano.function([x], T.nnet.softmax(x))

print f(data)

# print theano.function(data,s)