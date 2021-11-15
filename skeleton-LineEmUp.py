# based on code from https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python

import time
import isEnd
import random
import complexHeuristic
import simpleHeuristic
import alphabeta

class Game:
	#game parameters
	MINIMAX = 0
	ALPHABETA = 1
	HUMAN = 2
	AI = 3
	n = 0	#size of board
	b = 0	#number of blocks
	s = 0	#winning line-up streak
	d1 = 0	#max depth for adversarial search player 1
	d2 = 0	#max depth for adversarial search player 2
	t = 0	#max time in secs to return move
	alphabeta = None # if 1 then using alpha beta, if 0 then using minimax
	simpleH = 1 #1 is using simple heuristic, 0 is using complex heuristic
	mode = 0 #modes are 0:human-human 1:human-AI 2:AI-human 3:AI-AI
	player1Mode = None
	player2Mode = None
	p1heuristic = None # e1 = simple heuristic e2 = complex heuristic
	p2heuristic = None # e1 = simple heuristic e2 = complex heuristic
	
	def __init__(self, n, s, b, d1, d2, t, alphabeta, mode, recommend = True):
		self.initialize_game(self, n, s, b, d1, d2, t, alphabeta, mode)
		self.recommend = recommend

	# parameters are same as listed above
	def initialize_game(self, n, s, b, d1, d2, t, alphabeta, mode): # winning line-up size, number of blocks
		self.current_state = []
		if n>=3 and n<=10 : #validating the parameters and setting them to the game if valid
			self.n = n
		else :
			print(n, " is not a valid board size.")
			exit(0)
		if s>=3 and s<=n :
			self.s = s
		else :
			print(s, " is not a valid winning line-up size.")
			exit(0)
		if b>=0 and b<=2*n :
			self.b = b
		else :
			print(b, " is not a valid number for blocks.")
			exit(0)
		self.d1 = d1 # CHECK HOW TO VALIDATE THIS - n-b factorial
		self.d2 = d2 # CHECK HOW TO VALIDATE THIS
		self.t = t # CHECK HOW TO VALIDATE THIS
		self.alphabeta = alphabeta #determines if alphabeta is used or minimax
		if mode >= 0 and mode < 4:
			self.mode = mode
			if mode == 0:
				self.player1Mode = 'human'
				self.player2Mode = 'human'
			elif mode == 1:
				self.player1Mode = 'human'
				self.player2Mode = 'AI'
			elif mode == 2:
				self.player1Mode = 'AI'
				self.player2Mode = 'human'
			elif mode == 3:
				self.player1Mode = 'AI'
				self.player2Mode = 'AI'
		else:
			print("The input value for game mode is not valid, should be from 0 to 3")
			exit(0)
		for i in range(0, n):
			new = []
			for j in range(0, n):
				new.append(".")
			self.current_state.append(new)
		print("n=", self.n, " b=", self.b, " s=", self.s, " t=", t)
		#before setting first player, ask where want blocks, and set them
		self.setBlocks(self)
		# Ask users which heuristic they want
		self.setHeuristics(self)
		# Player X always plays first
		self.player_turn = 'X'

	def setBlocks(self): # method to ask user where want blocks, and validate and set them
		blocks = []
		for i in range(0, self.b):
			tryAgain = True
			while tryAgain is True:
				print('Enter a location for a block:')
				px = int(input('enter the x coordinate: '))
				py = int(input('enter the y coordinate: '))
				if self.is_valid(px, py):
					tryAgain = False
					self.current_state[px][py] = '*'
					thisBlock = "(",px,",",py,")"
					blocks.append(thisBlock)
				else:
					print('The location is not valid! Try again.')
		print(blocks)

	# function to ask human user what heuristic they want - human sets AI heuristic - if 2 AI then set at random
	def setHeuristics(self):
		tryAgain = True
		if self.mode == 0:	#human-human
			# first for player 1
			while tryAgain is True:
				print('Player 1 what heuristic would you like to use?')
				print('--> enter e1 for regular or e2 for complex')
				p1e = input()
				if p1e == 'e1' or p1e == 'e2':
					tryAgain = False
					self.p1heuristic = p1e
				else:
					print('This is not a valid input! Try again.')
			tryAgain = True
			# then for player 2
			while tryAgain is True:
				print('Player 2 what heuristic would you like to use?')
				print('--> enter e1 for regular or e2 for complex')
				p2e = input()
				if p2e == 'e1' or p2e == 'e2':
					tryAgain = False
					self.p2heuristic = p2e
				else:
					print('This is not a valid input! Try again.')
		elif self.mode == 1:	#human-AI
			# first for player 1
			while tryAgain is True:
				print('Player 1 what heuristic would you like to use?')
				print('--> enter e1 for regular or e2 for complex')
				p1e = input()
				if p1e == 'e1' or p1e == 'e2':
					tryAgain = False
					self.p1heuristic = p1e
				else:
					print('This is not a valid input! Try again.')
			tryAgain = True
			# then for player 2
			while tryAgain is True:
				print('Player 1 what heuristic would you like player 2 (AI) to use?')
				print('--> enter e1 for regular or e2 for complex')
				p2e = input()
				if p2e == 'e1' or p2e == 'e2':
					tryAgain = False
					self.p2heuristic = p2e
				else:
					print('This is not a valid input! Try again.')
		elif self.mode == 2:	#AI-human
			# first for player 1
			while tryAgain is True:
				print('Player 2 what heuristic would you like player 1 (AI) to use?')
				print('--> enter e1 for regular or e2 for complex')
				p1e = input()
				if p1e == 'e1' or p1e == 'e2':
					tryAgain = False
					self.p1heuristic = p1e
				else:
					print('This is not a valid input! Try again.')
			tryAgain = True
			# then for player 2
			while tryAgain is True:
				print('Player 2 what heuristic would you like to use?')
				print('--> enter e1 for regular or e2 for complex')
				p2e = input()
				if p2e == 'e1' or p2e == 'e2':
					tryAgain = False
					self.p2heuristic = p2e
				else:
					print('This is not a valid input! Try again.')
		else:	#AI-AI
			randomVal1 = random.randint(1, 3)
			randomVal2 = random.randint(1, 3)
			# for player 1
			if randomVal1 == 1:
				self.p1heuristic = 'e1'
			else:
				self.p1heuristic = 'e2'
			# for player 2
			if randomVal2 == 1:
				self.p2heuristic = 'e1'
			else:
				self.p2heuristic = 'e2'


	def draw_board(self): #edited to work with line em up
		print()
		for y in range(0, self.n):
			for x in range(0, self.n):
				print(F'{self.current_state[x][y]}', end="")
			print()
		print()
		
	def is_valid(self, px, py): #edited to work with line em up
		if px < 0 or px >= self.n or py < 0 or py >= self.n:
			return False
		elif self.current_state[px][py] != '.':
			return False
		else:
			return True

	def check_end(self): # works with line em up needs
		self.result = isEnd.is_end(self)
		# Printing the appropriate message if the game has ended
		if self.result != None:
			if self.result == 'X':
				print('The winner is X!')
			elif self.result == 'O':
				print('The winner is O!')
			elif self.result == '.':
				print("It's a tie!")
			self.initialize_game()
		return self.result

	def input_move(self):
		while True:
			print(F'Player {self.player_turn}, enter your move:')
			px = int(input('enter the x coordinate: '))
			py = int(input('enter the y coordinate: '))
			if self.is_valid(px, py):
				return (px,py)
			else:
				print('The move is not valid! Try again.')

	def switch_player(self):
		if self.player_turn == 'X':
			self.player_turn = 'O'
		elif self.player_turn == 'O':
			self.player_turn = 'X'
		return self.player_turn

	def minimax(self, max=False):
		# Minimizing for 'X' and maximizing for 'O'
		# Possible values are:
		# -1 - win for 'X'
		# 0  - a tie
		# 1  - loss for 'X'
		# We're initially setting it to 2 or -2 as worse than the worst case:
		value = 2
		if max:
			value = -2
		x = None
		y = None
		result = isEnd.is_end(self)
		if result == 'X':
			return (-1, x, y)
		elif result == 'O':
			return (1, x, y)
		elif result == '.':
			return (0, x, y)
		for i in range(0, 3):
			for j in range(0, 3):
				if self.current_state[i][j] == '.':
					if max:
						self.current_state[i][j] = 'O'
						(v, _, _) = self.minimax(max=False)
						if v > value:
							value = v
							x = i
							y = j
					else:
						self.current_state[i][j] = 'X'
						(v, _, _) = self.minimax(max=True)
						if v < value:
							value = v
							x = i
							y = j
					self.current_state[i][j] = '.'
		return (value, x, y)

	def play(self,algo=None,player_x=None,player_o=None):
		if algo == None:
			algo = self.ALPHABETA
		if player_x == None:
			player_x = self.HUMAN
		if player_o == None:
			player_o = self.HUMAN
		print("Player 1: ", self.player1Mode, " d=", self.d1, " a=", self.a, e1(regular)) # NEED TO CHECK THIS
		while True:
			self.draw_board()
			if self.check_end():
				return
			start = time.time()
			if algo == self.MINIMAX:
				if self.player_turn == 'X':
					(_, x, y) = self.minimax(max=False)
				else:
					(_, x, y) = self.minimax(max=True)
			else: # algo == self.
				# BETA
				if self.player_turn == 'X':
					(m, x, y) = alphabeta.alphabeta(max=False)
				else:
					(m, x, y) = alphabeta.alphabeta(max=True)
			end = time.time()
			if (self.player_turn == 'X' and player_x == self.HUMAN) or (self.player_turn == 'O' and player_o == self.HUMAN):
					if self.recommend:
						print(F'Evaluation time: {round(end - start, self.t)}s')
						print(F'Recommended move: x = {x}, y = {y}')
					(x,y) = self.input_move()
			if (self.player_turn == 'X' and player_x == self.AI) or (self.player_turn == 'O' and player_o == self.AI):
						print(F'Evaluation time: {round(end - start, self.t)}s')
						print(F'Player {self.player_turn} under AI control plays: x = {x}, y = {y}')
			self.current_state[x][y] = self.player_turn
			self.switch_player()

def main():
	# reminder - Game parameters are (self, n, s, b, d1, d2, t, alphabeta, mode, recommend = True)
	# note : recommend parameter is just to allow calculated recommendations - just gonna leave it that way
	g = Game( ... )
	g.play(algo=Game.ALPHABETA, player_x=Game.AI, player_o=Game.AI)
	g.play(algo=Game.MINIMAX, player_x=Game.AI, player_o=Game.HUMAN)

if __name__ == "__main__":
	main()

