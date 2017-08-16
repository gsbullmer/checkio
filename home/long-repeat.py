def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    if len(line) == 0:
        return 0

    max_count = 1
    working_count = 1

    for i in range(0, len(line) - 1):
        if line[i] == line[i+1]:
            working_count += 1
            if working_count > max_count:
                max_count = working_count
        else:
            working_count = 1

    return max_count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
