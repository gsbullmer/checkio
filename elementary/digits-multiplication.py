from functools import reduce


def checkio(number):
    """
    Return the product of the digits in the number, excluding `0`.
    """
    digits = [int(d) for d in str(number) if d is not "0"]
    return reduce(lambda x, y: x * y, digits)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
