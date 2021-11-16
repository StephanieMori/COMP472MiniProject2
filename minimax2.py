import isEnd
import minimax2
import simpleHeuristic
import complexHeuristic
import math

currentDepth = 0
i = 0
j = 0

def minimax(self, max=False):
    # Minimizing for 'X' and maximizing for 'O'
    # Possible values are:
    # -1 - win for 'X'
    # 0  - a tie
    # 1  - loss for 'X'
    # We're initially setting it to 2 or -2 as worse than the worst case:
    value = 100000
    if max:
        value = -100000
    x = minimax2.i
    y = minimax2.j
    maxDepth = 0
    heuristic = None
    if self.player_turn == 'X':
        maxDepth = self.d1
        heuristic = self.p1heuristic
    else:
        maxDepth = self.d2
        heuristic = self.p2heuristic
#    currentDepth = 0
    result = isEnd.is_end(self)
    print("is end result : ", result)
    if result == 'X':
        minimax2.currentDepth -= 1
        return (-1, x, y)
    elif result == 'O':
        minimax2.currentDepth -= 1
        return (1, x, y)
    elif result == '.':
        minimax2.currentDepth -= 1
        return (0, x, y)
    elif minimax2.currentDepth >= maxDepth:
        #call heuristics - this is our last level of nodes
        minimax2.currentDepth -= 1
        if heuristic == 'e1':
            # call simple heuristic
            score = simpleHeuristic.scoreThisCell(self, x, y, self.n, self.s)
        else:
            # call complex heuristic
            score = complexHeuristic.scoreThisCell(self, x, y, self.n, self.s)
        print("score : ", score)
        return (score, x, y)

    for i in range(0, self.n):
        for j in range(0, self.n):
            if self.current_state[i][j] == '.':
                if max:
                    self.current_state[i][j] = 'O'
                    minimax2.currentDepth += 1
                    print("currentDepth:" , minimax2.currentDepth)
                    (v, _, _) = minimax(self, max=False)
                    print("v : ", v)
                    if v > value:
                        value = v
                        x = i
                        y = j
                else:
                    self.current_state[i][j] = 'X'
                    minimax2.currentDepth += 1
                    print("currentDepth:", minimax2.currentDepth)
                    (v, _, _) = minimax(self, max=True)
                    print("v : ", v)
                    if v < value:
                        value = v
                        x = i
                        y = j
                self.current_state[i][j] = '.'
    return (value, x, y)
