import gameboard
class Investigator:
    currentHP=0
    currentSanity=0
    currentLoc=None

    skills = {
        "lore":0,
        "inf":0,
        "obs":0,
        "str":0,
        "will":0
        }

    inventory=[]
    tickets={"boat":0,"train":0}

    def __init__ (self, name, occupation, maxHP,maxSanity, startLoc, startEquip = [],skillsList = []):
        self.name = name
        self.occupation = occupation

        self.maxHP = maxHP
        self.maxSanity = maxSanity

        self.currentHP = self.maxHP
        self.currentSanity= self.maxSanity

        self.startLoc=startLoc
        self.startEquip=startEquip

        for item in self.startEquip:
            self.inventory.append(item)

        self.skillsList=skillsList

        self.skills["lore"]=self.skillsList[0]
        self.skills["inf"]=self.skillsList[1]
        self.skills["obs"]=self.skillsList[2]
        self.skills["str"]=self.skillsList[3]
        self.skills["will"]=self.skillsList[4]

        self.currentLoc = self.startLoc
        self.startLoc.placeAtLoc(self)

    #methods
    def incSanity(self,inc=1):
        if (self.currentSanity+inc)<self.maxSanity: 
            self.currentSanity+=inc
        else:
            self.currentSanity=self.maxSanity

    def decSanity(self,dec=1):
        if (self.currentSanity-dec)<=0:
           self.currentSanity=0 
        else:
            self.currentSanity-=dec

    def incHP(self,inc=1):
        if (self.currentHP+inc)<self.maxHP:
            self.currentHP+=inc
        else:
            self.currentHP=self.maxHP

    def decHP(self,dec=1):
        if (self.currentHP-dec)<=0:
            self.currentHP=0
        else:
            self.currentHP-=dec
    
    def restAction(self):
        #cannot be performed if monster on space
        #cannot be performed twice in one turn
        self.incSanity()
        self.incHP()

    def prepForTravelAction(self,ticket):
        #cannot be performed if already performed this turn
        #can only purchase tickets in cities
        #can only purchase tickets with respective methods of travel
        #cannot have more than two tickets at a time
        pass
    
    def travelAction(self,destLoc):
        pass
    
    def showCurrentLoc(self):
        return self.currentLoc.showLocName()
      
gboard=gameboard.gameBoard()
p2=Investigator("Debugger Man", "Debugger",10,20,gboard.ML1,["deb1","deb2","deb1"],[5,6,7,8,9])
p3=Investigator("Debugger Stan", "Debugger",10,20,gboard.ML2,["deb1","deb2","deb1"],[5,6,7,8,9])

debugList=[p2,p3]

def checkMethods(dlist):
    print("CURRENT")
    for entity in dlist:
        print(entity.showCurrentLoc())

def accessLocs(bd):
    for loc in bd.locsList:
        allAtLoc=loc.checkLoc()
        for entity in allAtLoc:
            print("{} is in {}.".format(entity.name,loc.locName))

accessLocs(gboard) 
print("")
gboard.traversePath(p2,gboard.ML1,gboard.ML5)
gboard.traversePath(p3,gboard.ML2,gboard.ML1)

accessLocs(gboard)

#checkMethods(debugList)
print(p2.showCurrentLoc())
print(p3.showCurrentLoc())

#when an entity traverses path, their currentLoc attribute should be updated automatically.
