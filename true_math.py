import math


def divide(first, second):
    result = None
    if second == 0:
        result = math.inf
    else:
        result = first / second
    return result
