def update():
    if self.jumpDir == -1:
        self.r_dino += 1
    elif self.jumpDir == 1:
        self.r_dino -= 1
    if self.r_dino == self.up:
        self.jumpDir = -1
    elif self.r_dino == self.down:
        self.jumpDir = 0
    
    dummySet={}
    for x in self.obs:
        x -= 1
        if(x!=0):
            dummySet.add(x)
    
    self.obs = dummySet
    dummySet=None
    if(self.generateCactus()==True):
        self.obs.insert(self.width - 1)
    return


    
