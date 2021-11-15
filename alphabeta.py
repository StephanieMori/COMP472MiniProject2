import math

def alphabeta(self, alpha=-math.inf, beta=math.inf, max=False):
    # Minimizing for 'X' and maximizing for 'O'
    # Possible values are:
    # -1 - win for 'X'
    # 0  - a tie
    # 1  - loss for 'X'
    # We're initially setting it to 2 or -2 as worse than the worst case:
    value = math.inf
    if max:
        value = -math.inf
    x = None
    y = None
    result = self.is_end(self)
    if result == 'X':
        return (-1, x, y)
    elif result == 'O':
        return (1, x, y)
    elif result == '.':
        return (0, x, y)
    for i in range(0, self.n):
        for j in range(0, self.n):
            if self.current_state[i][j] == '.':
                if max:
                    self.current_state[i][j] = 'O'
                    (v, _, _) = self.alphabeta(alpha, beta, max=False)
                    if v > value:
                        value = v
                        x = i
                        y = j
                else:
                    self.current_state[i][j] = 'X'
                    (v, _, _) = self.alphabeta(alpha, beta, max=True)
                    if v < value:
                        value = v
                        x = i
                        y = j
                self.current_state[i][j] = '.'
                if max:
                    if value >= beta:
                        return (value, x, y)
                    if value > alpha:
                        alpha = value
                else:
                    if value <= alpha:
                        return (value, x, y)
                    if value < beta:
                        beta = value
    return (value, x, y)
