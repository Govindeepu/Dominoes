import random

class DominoesGame:
	snakes = [[6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]
	domino_snake = []
	domino_pieces = []
	status = ''

	def __init__(self):
		for i in range (0, 7):
			for j in range (0,7):
				if [j, i] not in self.domino_pieces:
					self.domino_pieces.append([i, j])

		random.shuffle(self.domino_pieces)
		self.stock_pieces = self.domino_pieces[0:14]
		self.player_pieces = self.domino_pieces[14:21]
		self.computer_pieces = self.domino_pieces[21:28]

		for snake in self.snakes:
			if snake in self.computer_pieces:
				self.domino_snake.append(snake)
				self.computer_pieces.remove(snake)
				self.status = 'player'
				break

			if snake in self.player_pieces:
				self.domino_snake.append(snake)
				self.player_pieces.remove(snake)
				self.status = 'computer'
				break



	def print_status(self):
		print('=' * 70)
		print(f'Stock size: {len(self.stock_pieces)}')
		print(f'Computer pieces: {len(self.computer_pieces)}\n')
		self.print_snake()

		print('Your pieces:')
		for i in range(len(self.player_pieces)):
			print(f'{i+1}: {self.player_pieces[i]}')

	def print_snake(self):
		if len(self.domino_snake) >= 6:
			print(" ".join(map(str, self.domino_snake[0:3])), '...', " ".join(map(str, self.domino_snake[-3:len(self.domino_snake)])))
		else:
			for i in range(len(self.domino_snake)):
				print(self.domino_snake[i], end='')
			print('\n')

	def user_turn(self):
		print("Status: It's your turn to make a move. Enter your command.")
		action = input()
		if action[0] == '-' and action[1:].isdigit() and len(self.player_pieces) >= int(action[1:]) > 0:
			self.put_domino('-', int(action[1:]) - 1, 'player')
		elif action.isdigit() and len(self.player_pieces) >= int(action) > 0:
				self.put_domino('+', int(action) - 1, 'player')
		elif action.isdigit() and int(action[0]) == 0:
			self.take_stock('player')
		else:
			print("Invalid input. Please try again.")
			self.user_turn()

	def computer_turn(self):
		print('Status: Computer is about to make a move. Press Enter to continue...')
		input()
		computer_chose = random.randint(1, len(self.computer_pieces))
		self.put_domino('+', computer_chose, 'computer')

	def computer_turn1(self):
		computer_chose = random.randint(1, len(self.computer_pieces))
		self.put_domino('+', computer_chose, 'computer')

	def put_domino(self, side_of_the_snake, domino_number, who):
		if who == 'player':
			sample = " ".join(map(str, self.domino_snake))
			a = sample[1]
			b = sample[-2]
			c = self.player_pieces[domino_number]
			d = c[0]
			e = c[1]
			if int(a) == int(e):
				domino = c
				self.player_pieces.pop(domino_number)
				self.domino_snake.insert(0, domino)
			elif int(a) == int(d):
				domino = [e, d]
				self.player_pieces.pop(domino_number)
				self.domino_snake.insert(0, domino)
			elif int(b) == int(d):
				domino = c
				self.player_pieces.pop(domino_number)
				self.domino_snake.append(domino)
			elif int(b) == int(e):
				domino = [e, d]
				self.player_pieces.pop(domino_number)
				self.domino_snake.append(domino)
			else:
				print("Illegal move. Please try again.")
				self.user_turn()
		elif who == 'computer':
			sample = " ".join(map(str, self.domino_snake))
			a = sample[1]
			b = sample[-2]
			c = self.computer_pieces[domino_number - 1]
			d = c[0]
			e = c[1]

			if int(a) == int(e):
				side_of_the_snake = '-'
				domino = c
				self.computer_pieces.pop(domino_number - 1)
				self.domino_snake.insert(0, domino)
			elif int(a) == int(d):
				domino = [e, d]

				self.computer_pieces.pop(domino_number - 1)
				self.domino_snake.insert(0, domino)
			elif int(b) == int(d):
				domino = c
				self.computer_pieces.pop(domino_number - 1)
				self.domino_snake.append(domino)
			elif int(b) == int(e):
				domino = [e, d]
				self.computer_pieces.pop(domino_number - 1)
				self.domino_snake.append(domino)
			else:
				try:
					if len(self.computer_pieces) > 0:
						self.computer_turn1()
				except RecursionError:
					if len(self.stock_pieces) > 0:
						self.take_stock('computer')
					else:
						print("Status: The game is over. It's a draw!")
						exit()
	def take_stock(self, who):
		domino = self.stock_pieces.pop()
		if who == 'player':
			self.player_pieces.append(domino)
		else:
			self.computer_pieces.append(domino)


	def check_winner(self):
		if len(self.player_pieces) == 0:
			print('Status: The game is over. You won!')
			exit()

		if len(self.computer_pieces) == 0:
			print('Status: The game is over. The computer won!')
			exit()
		if len(self.stock_pieces) == 0:
			print("Status: The game is over. It's a draw!")
			exit()

	def run(self):
		while len(self.stock_pieces)  and len(self.player_pieces) and len(self.computer_pieces):
			game.print_status()
			if self.status == 'player':
				self.status = 'computer'
				self.user_turn()

			else:
				self.status = 'player'
				self.computer_turn()

		game.print_status()
		self.check_winner()



game = DominoesGame()
game.run()