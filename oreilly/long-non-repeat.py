def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    max_string = ""
    working_string = ""

    for i in range(len(line)):
        if line[i] not in working_string:
            working_string += line[i]
        else:
            char_idx = working_string.index(line[i])
            working_string = working_string[char_idx + 1:] + line[i]

        if len(working_string) > len(max_string):
            max_string = working_string[:]

    return max_string

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')
