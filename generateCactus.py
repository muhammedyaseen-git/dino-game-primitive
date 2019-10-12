def generateCactus(self):
	'''
		This function will decide whether to generate Cactus or not
	'''
	
	# If there is no Cactus present on the screen it will generate the Cactus	
	if len(self.obs) == 0:
		return True
	
	#If    
	if self.width - max(self.obs) >= self.threshhold and  random.random() <= self.prob :
		return True

	return False
