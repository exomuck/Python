from math import sqrt

def vector_distance(v1, v2, **kwargs):
    norm = kwargs.get('norm')
    if norm == 'manhattan':
        return sum(abs(x1 - x2) for x1, x2 in zip(v1, v2))
    elif norm == 'cosine':
        product = sum(x1 * x2 for x1, x2 in zip(v1, v2))
        v1_magnitude = sqrt(sum(x ** 2 for x in v1))
        v2_magnitude = sqrt(sum(x ** 2 for x in v2))
        return round(product / (v1_magnitude * v2_magnitude), 9)
    else:
        return round(sqrt(sum((x1 - x2) ** 2 for x1, x2 in zip(v1, v2))), 9)