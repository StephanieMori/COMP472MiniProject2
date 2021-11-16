# note : iteration looks at rows first
def scoreThisCell(game, x, y, n, s):
        currentSymbol = game.player_turn #the current player's symbol
        otherSymbol = None #other player's symbol
        if currentSymbol == 'X':
                otherSymbol = 'O'
        else:
                otherSymbol = 'X'
        score = 0
        numCurrentSymbols = 0
        numOtherSymbols = 0
        # note : x coordinate is rows
        #first checking row associated with this cell
        for col in range(0,n):
                if game.current_state[x][col] == currentSymbol:
                        numCurrentSymbols += 1
                if game.current_state[x][col] == otherSymbol:
                        numOtherSymbols += 1
        #get the score
        score = score + pow(2, numCurrentSymbols) - pow(2, numOtherSymbols)
        print("score with row is : ", score)

        #y is columns
        numCurrentSymbols = 0
        numOtherSymbols = 0
        #now checking the column associated with this cell
        for row in range(0,n):
                if game.current_state[row][y] == currentSymbol:
                        numCurrentSymbols += 1
                if game.current_state[row][y] == otherSymbol:
                        numOtherSymbols += 1
        #get the score
        score = score + pow(2, numCurrentSymbols) - pow(2, numOtherSymbols)
        print("score with added column is : ", score)

        numCurrentSymbols = 0
        numOtherSymbols = 0
        #now checking the diagonal from top left to bottom right passing by this cell
        step = abs(x-y)
        xval = x-step
        yval = y-step
        while xval < n and yval < n :
                if game.current_state[xval][yval] == currentSymbol:
                        numCurrentSymbols += 1
                if game.current_state[xval][yval] == otherSymbol:
                        numOtherSymbols += 1
                xval += 1
                yval += 1
        #get the score
        score = score + pow(2, numCurrentSymbols) - pow(2, numOtherSymbols)
        print("score with added diagonal 1 is : ", score)

        numCurrentSymbols = 0
        numOtherSymbols = 0
        #now checking the diagonal from top right to bottom left passing by this cell
        step = min((n-x), (n-y)) -1
        xval = x+step
        yval = y+step
        while xval > 0 and yval > 0 :
                if game.current_state[xval][yval] == currentSymbol:
                        numCurrentSymbols += 1
                if game.current_state[xval][yval] == otherSymbol:
                        numOtherSymbols += 1
                xval -= 1
                yval -= 1
        #get the score
        score = score + pow(2, numCurrentSymbols) - pow(2, numOtherSymbols)
        print("score with added diagonal 2 is (total score for this cell): ", score)

        return score
