def check_line(line):
    """
    Check the line for a winner.
    """
    if len(line) == 1 and '.' not in line:
        return line.pop()


def checkio(game_result):
    """
    Check the results of a Tic-Tac-Toe game and return the winner or a draw.
    """

    lines = []
    cols = [set(), set(), set()]
    diag1 = set()
    diag2 = set()

    for x in range(3):
        lines.append(set(game_result[x]))
        cols[x].add(game_result[0][x])
        cols[x].add(game_result[1][x])
        cols[x].add(game_result[2][x])
        diag1.add(game_result[x][x])
        diag2.add(game_result[2 - x][x])

    for col in cols:
        lines.append(col)

    lines.append(diag1)
    lines.append(diag2)

    for line in lines:
        result = check_line(line)
        if result:
            return result

    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
