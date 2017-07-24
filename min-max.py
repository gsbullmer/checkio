def min(*args, **kwargs):
    """
    Returns the smallest item in an iterable or the smallest of two or more
    arguments. If one positional argument is provided, it should be an
    iterable. The smallest item in the iterable is returned. If two or more
    positional arguments are provided, the smallest of the positional
    arguments is returned. The optional keyword-only key argument specifies a
    function of one argument that is used to extract a comparison key from
    each list element (for example, key=str.lower). If multiple items are
    minimal, the function returns the first one encountered.
    """
    key = kwargs.get("key", None)
    args = list(args[0] if len(args) is 1 else args)
    smallest = args[0]

    for a in args:
        if key:
            if key(a) < key(smallest):
                smallest = a
        elif a < smallest:
            smallest = a

    return smallest


def max(*args, **kwargs):
    """
    Return the largest item in an iterable or the largest of two or more
    arguments. If one positional argument is provided, it should be an
    iterable. The largest item in the iterable is returned. If two or more
    positional arguments are provided, the largest (smallest) of the
    positional arguments is returned. The optional keyword-only key argument
    specifies a function of one argument that is used to extract a comparison
    key from each list element (for example, key=str.lower). If multiple items
    are maximal, the function returns the first one encountered.
    """
    key = kwargs.get("key", None)
    args = list(args[0] if len(args) is 1 else args)
    largest = args[0]

    for a in args:
        if key:
            if key(a) > key(largest):
                largest = a
        elif a > largest:
            largest = a

    return largest


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    assert min(abs(i) for i in range(-10, 10)) == 0, "generator"
