def set_union(A, B):
    union = set()

    for element in A:
        union.add(element)

    for element in B:
        union.add(element)
    return union

def set_intersection(A, B):
    intersection = set()

    for element in A:
        if element in B:
            intersection.add(element)
    return intersection