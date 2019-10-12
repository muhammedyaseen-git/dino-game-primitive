import keyboard
import random
import os

class Game:
    # Initializes the game configuration
    def __init__(self, dim = (60,240), thres = 15, prob = 0.3, col_dino = 3) :
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
        self.update()

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
            #print self.c_dino
            #print self.r_dino
            #self.background[self.r_dino][self.c_dino] = '*'
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
        print s
        os.system("sleep 0.06")
    
    def generateCactus(self):
	    '''
		    This function will decide whether to generate Cactus or not
	    '''
	    
	    # If there is no Cactus present on the screen it will generate the Cactus	
	    if len(self.obs) == 0:
		    return True
	    
	    #If    
	    if self.width - max(self.obs) >= self.threshold and  random.random() <= self.prob :
		    return True

	    return False

    def isGameOver(self):
	    for col in self.obs:
		    if(col == self.c_dino and self.r_dino == self.height - 1): # Checking whether it Dino touched Cactus or not
			    return True					   # if it touches return true indicating game is over
	    return False	# Else return false indicating game is not over
	

    def update(self):
        if self.jump_dir == -1:
            self.r_dino += 1
        elif self.jump_dir == 1:
            self.r_dino -= 1
        if self.r_dino == self.up:
            self.jump_dir = -1
        elif self.r_dino == self.down:
            self.jump_dir = 0
        
        dummySet=set()
        for x in self.obs:
            x -= 1
            if(x!=0):
                dummySet.add(x)
        
        self.obs = dummySet
        dummySet=None
        if(self.generateCactus()==True):
            self.obs.add(self.width - 1)
        return

dino = Game()
dino.play()

