import os


def display():
    '''
        This function displays the current game background,
        the obstacles and the dinosaur
    
    '''
    
    
    # Fill the entire 2D array with 
    # space characters
    for i in range(self.height):
        for j in range(self.width):
            self.background[i][j] = ' '
    
    # Place all the obstacles as '|'
    # character into the background
    for col in self.obs:
        self.background[0][col] = '|'
    
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
    print(s)
