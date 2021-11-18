# note : iteration looks at rows first
def scoreThisCell(game, x, y, n, s):
    num_eval_states = 0
    currentSymbol = game.player_turn  # the current player's symbol
    otherSymbol = None  # other player's symbol
    if currentSymbol == 'X':
        otherSymbol = 'O'
    else:
        otherSymbol = 'X'
    score = 0
    numCurrentSymbols = 0
    numOtherSymbols = 0
    # note : x coordinate is rows
    rowStreak = 0
    # first checking row associated with this cell
    for col in range(0, n):
        if game.current_state[x][col] == currentSymbol or game.current_state[x][col] == '.':
            rowStreak += 1
            if game.current_state[x][col] == currentSymbol:
                numCurrentSymbols += 1
        else:
            rowStreak = 0
            if game.current_state[x][col] == otherSymbol:
                numOtherSymbols += 1
    if rowStreak >= s:
        # if there is the possibility of making a winning streak, get the score
        score = score + pow(2, numCurrentSymbols) - pow(2, numOtherSymbols)
        # print("score with row is : ", score)
    # y is columns
    colStreak = 0
    numCurrentSymbols = 0
    numOtherSymbols = 0
    # now checking the column associated with this cell
    for row in range(0, n):
        if game.current_state[row][y] == currentSymbol or game.current_state[row][y] == '.':
            colStreak += 1
            if game.current_state[row][y] == currentSymbol:
                numCurrentSymbols += 1
        else:
            colStreak = 0
            if game.current_state[row][y] == otherSymbol:
                numOtherSymbols += 1
    if colStreak >= s:
        # if there is the possibility of making a winning streak, get the score
        score = score + pow(2, numCurrentSymbols) - pow(2, numOtherSymbols)
        # print("score with added column is : ", score)

    diag1Streak = 0  # diag1 is from topleft to bottomright
    numCurrentSymbols = 0
    numOtherSymbols = 0
    # now checking the diagonal from top left to bottom right passing by this cell
    step = abs(x - y)
    xval = x - step
    yval = y - step
    while xval < n and yval < n:
        if game.current_state[xval][yval] == currentSymbol or game.current_state[xval][yval] == '.':
            diag1Streak += 1
            if game.current_state[xval][yval] == currentSymbol:
                numCurrentSymbols += 1

        else:
            diag1Streak = 0
            if game.current_state[xval][yval] == otherSymbol:
                numOtherSymbols += 1
        xval += 1
        yval += 1
    if diag1Streak >= s:
        # if there is the possibility of making a winning streak, get the score
        score = score + pow(2, numCurrentSymbols) - pow(2, numOtherSymbols)
        # print("score with added diagonal 1 is : ", score)

    diag2Streak = 0  # diag2 is from topright to bottomleft
    numCurrentSymbols = 0
    numOtherSymbols = 0
    # now checking the diagonal from top right to bottom left passing by this cell
    step = min((n - x), (n - y)) - 1
    xval = x + step
    yval = y + step
    while xval >= 0 and yval >= 0:
        if game.current_state[xval][yval] == currentSymbol or game.current_state[xval][yval] == '.':
            diag2Streak += 1
            if game.current_state[xval][yval] == currentSymbol:
                numCurrentSymbols += 1

        else:
            diag2Streak = 0
            if game.current_state[xval][yval] == otherSymbol:
                numOtherSymbols += 1
        xval -= 1
        yval -= 1
    if diag2Streak >= s:
        # if there is the possibility of making a winning streak, get the score
        score = score + pow(2, numCurrentSymbols) - pow(2, numOtherSymbols)
        # print("score with added diagonal 2 is (total score for this cell): ", score)

    return score
