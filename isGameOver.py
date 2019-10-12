def isGameOver(self):
	'''
		This function will check whether game is over or not if game 
		is over it returns True and else it returns False 
	'''
	for col in self.obs:
		if(col == self.c_dino and self.r_dino == self.height - 1): # Checking whether it Dino touched Cactus or not
			return True					   # if it touches return true indicating game is over
	return False	# Else return false indicating game is not over
	
