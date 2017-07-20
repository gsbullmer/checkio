def safe_pawns(pawns):
    """
    Return the number of pawns defended by another pawn.
    """

    def is_safe(pawn):
        """
        Determine the defending pawns' spaces and return if any of them
        are in the pawns list.
        """
        back_rank = str(int(pawn[1]) - 1)
        left_file = chr(ord(pawn[:1]) - 1)
        right_file = chr(ord(pawn[:1]) + 1)

        defenders = {
            "".join([left_file, back_rank]),
            "".join([right_file, back_rank])
        }

        return True if defenders & pawns else False

    safe = [is_safe(pawn) for pawn in pawns]

    return safe.count(True)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
