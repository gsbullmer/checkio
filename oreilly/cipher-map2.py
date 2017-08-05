def recall_password(cipher_grille, ciphered_password, password=""):
    """
    Return the password contained in `ciphered_password` by using the provided
    `cipher_grille`.
    """
    if len(password) is sum(len(row) for row in ciphered_password):
        return password

    for row1, row2 in zip(cipher_grille, ciphered_password):
        for char in zip(row1, row2):
            if char[0] is "X":
                password = password + char[1]

    rotated_cipher = tuple("".join(row) for row in zip(*cipher_grille[::-1]))
    return recall_password(rotated_cipher, ciphered_password, password)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
