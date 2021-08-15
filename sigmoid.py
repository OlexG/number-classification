import math
import numpy
e = 2.71828
def getSigmoid(x):
    return numpy.array(numpy.reciprocal(1 + numpy.power(e, -1 * x)), dtype=float)