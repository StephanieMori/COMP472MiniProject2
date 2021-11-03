
	def is_end(self): 

		win = None
        n = len(self.current_state)
    
    # Vertical win
		for i in range(n):
			win = True
			for j in range(n):
				if self.current_state[j][i] != player:
					win = False
					break	
		if win:
			 return win

		# Horizontal win
		for i in range(n):
			win = True
			for j in range(n):
				if self.current_state[i][j] != player:
					win = False
					break
		if win:
			return win

    # checking diagonals
        win = True
        for i in range(n):
           if self.current_state[i][i] != player:
                    win = False
                    break
        if win:
            return win
	
    win = True
	  for i in range(n):
     if self.current_state[i][n - 1 - i] != player:
       win = False
       break
    if win:
      return win
	  return False

    for row in self.current_state:
      for item in row:
        if item == '.':
          return False
      return True
        
# Is whole board full?
    for row in self.current_state:
      for item in row:
        if item == '.':
          return False
      return True
    

