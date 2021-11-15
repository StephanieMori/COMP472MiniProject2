import complexHeuristic
import simpleHeuristic

def minimax(self,d1,d2,max=False):
		# Minimizing for 'X' and maximizing for 'O'
		# Possible values are:
		# -1 - win for 'X'
		# 0  - a tie
		# 1  - loss for 'X'
		# We're initially setting it to 2 or -2 as worse than the worst case:
		value = 2
		if max:value = -2
		x = None
		y = None
		#checking if the current move resulted in a draw or win or loss
		result = self.is_end()
		if result == 'X':
			return (-1, x, y)
		elif result == 'O':
			return (1, x, y)
		elif result == '.':
			return (0, x, y)
	  	#implementing Heuristics(?)
		if self.p1heuristic == 'e1':
			return (simpleHeuristic.scoreThisCell(self,x,y,self.n,self.s))
	  	else:
			return (complexHeuristic.scoreThisCell(self, x, y, self.n, self.s))
	  	if self.d2 == e1:
			return (simpleHeuristic.scoreThisCell(self,x,y,self.n,self.s))
	 	 else:
			(complexHeuristic.scoreThisCell(self, x, y, self.n, self.s))
	 
	 #
		 for i in range(0,self.n):
			for j in range(0,self.n):
				if (current_state[i][j] == '.'):
					if max:
						self.current_state[i][j]= 'O'
						(v,_,_)=self.minimax(d1,d2-1, max= False) #Min when max=false
			      if v> value:
							value=v
							x=i
							y=i
					else:
						self.current_state[i][j]= 'X'
						(v,_,_)=self.minimax(d1=1,d2, max= True)
			      if v> value:
							value=v
							x=i
							y=i
			    self.current_state[i][j]='.'
		return (value, x, y)