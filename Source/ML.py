import numpy


def leaky_relu(x: float, alpha: float = 0.01):
    return numpy.maximum(alpha * x, x)


def leaky_relu_derivative(x: float, alpha: float = 0.01):
    return numpy.where(x > 0, 1, alpha)


def softmax(x: numpy.ndarray) -> numpy.ndarray:
    e_x = numpy.exp(x - numpy.max(x))
    return e_x / e_x.sum()


def mean_squared_difference(predicted: numpy.ndarray, true: numpy.ndarray) -> float:
    return ((predicted - true) ** 2).sum()
