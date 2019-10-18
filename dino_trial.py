#import keyboard
import random
import os

def viewScores():
	os.system('clear')
	myFile = open("high_scores.txt")
	data=myFile.readlines()
	for line in data:
		print (line)
	os.system("sleep 2")
	myFile.close()
	return
	
class Game:
    # Initializes the game configuration
    def __init__(self,name, score = 0,dim = (60,240), thres = 15, prob = 0.3, col_dino = 3) :
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
      self.score=score
      # empty background (intitially)
      self.background = [ [' '] * self.width for i in range(0, self.height) ]
	
    def play(self):

      # game continues till its not over
      while (self.isGameOver()==False) :
        # displays the game in the background
        self.display()

        # checks for valid input
        #if keyboard.is_pressed(' ') and self.jump_dir == 0:
        #  self.jump_dir = 1

        # updates the game configuration
        self.score=self.score+1
        self.update()
        
      #to update the score
      os.system('clear')
      print("Your Score\t"+str(self.score)+"\n")
      myFile = open("high_scores.txt")
      data=myFile.readlines()
      data.append(str(self.name)+"\t"+str(self.score))
      myFile.close()
      myFile = open("high_scores.txt","w")
      sorteddata = []
      for line in data:
      	sorteddata.append([line.split()[0],line.split()[1]])
      sorteddata.sort(key = lambda x:x[1])
      for (x,y) in sorteddata:
      	myFile.write(x+"\t"+str(y)+"\n")
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
        print (s)
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


	
def main():
	while(True):
		os.system('clear')
		print("\t\tDINO GAME\n\n\n\n\n")
		print("\t1.	New Game\n")
		print("\t2.	High Scores\n")
		print("\t3.	Exit\n")
		choice = int(input("\n\n\n ENTER CHOICE (1-3): "))
		if choice == 1:
			os.system('clear')
			player_name = str(input("NAME 	: "))
			dino = Game(str(player_name))
			dino.play()
		elif choice == 2:
			viewScores()
		elif choice == 3:
			print("See you again!")
			os.system("sleep 2")
			return
	
if __name__ == '__main__':
	main()

