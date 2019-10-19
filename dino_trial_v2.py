import keyboard
import random
import os

terminal = (24, 80)
RED = '\033[35m'
GREEN = '\033[32m'
RESET = '\033[0m'

def viewScores():
	os.system("clear")
	myFile = open("high_scores.txt", "r")
	data = myFile.readlines()
	for line in data:
		print (line)
	os.system("sleep 2")
	myFile.close()
	return
	
class Game:
	# Initializes the game configuration
	def __init__(self, name, dim = terminal, thres = 15, prob = 0.1, col_dino = 3) :
		self.height = dim[0]
		self.width = dim[1]
		self.up = self.height - 4
		self.down = self.height - 1
		self.jump_dir = 0
		self.r_dino = self.down
		self.c_dino = col_dino
		self.threshold = thres
		self.obs = set ()
		self.prob = prob
		self.name = name
		self.score = 0
		# empty background (intitially)
		self.background = [ [' '] * self.width for i in range(0, self.height) ]

	def play(self):

		# game continues till its not over
		while (self.isGameOver()==False) :
			# displays the game in the background
			self.display()
			# checks for valid input
			if keyboard.is_pressed(' ') and self.jump_dir == 0:
				self.jump_dir = 1

			# updates the game configuration
			self.score=self.score+1
			self.update()
		   
		# update the score
		os.system('clear')
		print("Your Score\t" + str(self.score) + "\n")
		myFile = open("high_scores.txt")
		data = myFile.readlines()
		data.append(str(self.name) + "\t" + str(self.score))
		myFile.close()
		myFile = open("high_scores.txt", "w")
		sorteddata = []
		for line in data:
			sorteddata.append([line.split()[0],line.split()[1]])
		sorteddata.sort(key = lambda x : x[1])
		for (x,y) in sorteddata:
			myFile.write(x+ "\t" + str(y) + "\n")
		myFile.close()

	def display(self):
		# Fill the entire 2D array with 
		# space characters
		for i in range(self.height):
			for j in range(self.width):
				self.background[i][j] = ' '
       
		# Place all the obstacles as '|'
		# character into the background
		for col in self.obs:
			self.background[self.down][col] = '|'
       
		# Place the dinosaur into the background
		self.background[self.r_dino][self.c_dino] = '*'
		# Initialize string to be printed with
		# empty string
		s = ""
        
		# Place the background array contents
		# into the string to be printed
		for i in range(self.height):
			for j in range(self.width):
				s += self.background[i][j]
			s += "\n"
       
		# Clear the screen
		os.system('clear')
		# Print the string
		print (s)
		os.system("sleep 0.06")
   
	def generateCactus(self):
		'''
		This function will decide whether to generate Cactus or not
		'''
	    
		# If there is no Cactus present on the screen it will generate the Cactus	
		if len(self.obs) == 0:
			return True
	    
 
		if self.width - max(self.obs) >= self.threshold and  random.random() <= self.prob :
			return True
		return False

	def isGameOver(self):
		for col in self.obs:
			# Checking whether it Dino touched Cactus or not
			# if it touches return true indicating game is over
			if(col == self.c_dino and self.r_dino == self.height - 1):
				return True
		# Else return false indicating game is not over
		return False
	

	def update(self):
		if self.jump_dir == -1:
			self.r_dino += 1
		elif self.jump_dir == 1:
			self.r_dino -= 1
		if self.r_dino == self.up:
			self.jump_dir = -1
		elif self.r_dino == self.down:
			self.jump_dir = 0
        
		dummySet = set()
		for x in self.obs:
			x -= 1
			if(x != 0):
				dummySet.add(x)
        
		self.obs = dummySet
		dummySet = None
		if(self.generateCactus() == True):
			self.obs.add(self.width - 1)
		return

def console(background):
	s = ""
	for i in range(terminal[0]):
		for j in range(terminal[1]):
			s += background[i][j]
		s += '\n'
	os.system('clear')
	print(s)

def main():
	
	background = [ [' '] * terminal[1] for i in range(terminal[0]) ]
	simple = [GREEN + 'New Game' + RESET, GREEN + 'High Scores' + RESET, GREEN + 'Exit Game' + RESET]
	highlight = [RED + 'New Game' + RESET, RED + 'High Scores' + RESET, RED + 'Exit Game' + RESET]
	row_centre = terminal[0] // 2
	col_centre = terminal[1] // 2

	new_game = (col_centre - 6, col_centre + 11)
	high_score = (col_centre - 7, col_centre + 13)
	exit_game = (col_centre - 6, col_centre + 12)

	background[row_centre - 2][new_game[0] : new_game[1]] = highlight[0]
	background[row_centre][high_score[0] : high_score[1]] = simple[1]
	background[row_centre + 2][exit_game[0] : exit_game[1]] = simple[2]

	cur = 0
	while(True):
		console(background)
		if keyboard.is_pressed('s') :
			cur = (cur + 1) % 3
		elif keyboard.is_pressed('w') :
			cur = (cur - 1) % 3
		if cur == 0 :
			background[row_centre - 2][new_game[0] : new_game[1]] = highlight[0]
			background[row_centre][high_score[0] : high_score[1]] = simple[1]
			background[row_centre + 2][exit_game[0] : exit_game[1]] = simple[2]
			if keyboard.is_pressed(' '):
				os.system('clear')
				player = input("Username : ")
				game = Game(player)
				game.play()
		elif cur == 1:
			background[row_centre - 2][new_game[0] : new_game[1]] = simple[0]
			background[row_centre][high_score[0] : high_score[1]] = highlight[1]
			background[row_centre + 2][exit_game[0] : exit_game[1]] = simple[2]
			if keyboard.is_pressed(' '):
				viewScores()
		else :
			background[row_centre - 2][new_game[0] : new_game[1]] = simple[0]
			background[row_centre][high_score[0] : high_score[1]] = simple[1]
			background[row_centre + 2][exit_game[0] : exit_game[1]] = highlight[2]
			if keyboard.is_pressed(' '):
				print ("See you later")
				return

		os.system('sleep 0.15')
	
if __name__ == '__main__':
	main()
