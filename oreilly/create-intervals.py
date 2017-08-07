def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    if len(data) is 0:
        return []

    intervals = []
    start = None
    stop = None

    for i in range(min(data), max(data)+1):
        if i in data:
            stop = i
            if not start:
                start = i
        elif start:
            intervals.append(tuple([start, stop]))
            start = None
            stop = None

    intervals.append(tuple([start, stop]))

    return intervals

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    assert create_intervals([]) == [], "Empty"
    print('Almost done! The only thing left to do is to Check it!')
