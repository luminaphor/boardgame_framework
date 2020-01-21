def chooseAncientOne():
    #allow players to choose Ancient One. Set up game based on that.
    pass
def setupTokensAndDecks():
    #create gate stack - randomize tokens 
    #create Clue pool 
    #create general token pool - may not be necessary
    #create monster cup

    #shuffle expedition encounter cards into single deck.
    #shuffle spells/conditions into 2 separate decks
    pass
def chooseInvestigator():
    pass
def createMythosDeck():
    #use research encounter, special encounter, and msyery cards corresponding to AO only.
    #based on AO sheet.
    #3 piles based on color. 
    #take random cards of denoted color/quantity. shuffle together.
    #do for all stages.
    pass
def takeAction():
    pass
def travelAction():
    #move to adjacent space
    #may spend any num travel tokens to move an additional space.
    pass
def tradeAction():
    #may trade asset, artifact, clue, spell, ticket with another player on same space
    pass
def prepForTravelAction():
    #if on city space, gain 1 ticket of choice. Can only gain tickets of there
    #is an associated path.
    #cannot have more than 2.
    pass
def acquireAssetsAction():
    #if on city space. Test influence, gain assets from reserve with total value <= num successes.
    pass
def componentAction():
    #can perform actions of different components
    #may perform components held by other investigators in his space if its local.
    pass
def resolveTest():
    #roll dice specific to character.
    #return successes.
    pass

def debugInvestigatorClass(p1):
    print("NAME: {}\nOCCUPATION: {}\nSTARTING LOCATION: {}\n".format(p1.name, p1.occupation,p1.startLoc))
    print("MAX HP: {}, CURRENT HP: {}\nMAX SANITY: {}, CURRENT SANITY: {}\n".format(p1.maxHP,p1.currentHP,p1.maxSanity,p1.currentSanity))
    print("LORE: {}\nINFLUENCE: {}\nOBSERVATION: {}\nSTRENGTH: {}\nWILL: {}\n".format(p1.skills["lore"],p1.skills["inf"],p1.skills["obs"],p1.skills["str"],p1.skills["will"]))
    print("ITEMS HELD: {}".format(p1.inventory))
def showStats(p1):
    print("Current HP: {}, Current Sanity: {}".format(p1.currentHP,p1.currentSanity))
def debugInvestigatorStats(p1):
    showStats(p1)

    p1.decHP()
    p1.decSanity()
    showStats(p1)

    p1.decHP(3)
    p1.decSanity(5)
    showStats(p1)

    p1.incHP()
    p1.incSanity()
    showStats(p1)

    p1.incHP(5)
    p1.incSanity(7)
    showStats(p1)

    p1.decHP(10)
    p1.decSanity(20)
    showStats(p1)

#classes to define:
    #Ancient ones
    #Investigators

class Investigator:
    currentHP=0
    currentSanity=0

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

class location:
    def __init__(self,locType):
        self.locType=locType
    
class majorLoc(location):
    def __init__(self,name,locType):
        location.__init__(self,locType)
        self.name=name
    
class minorLoc(location):
    def __init__(self,locNumber,locType):
        location.__init__(self,locType)
        self.locNumber=locNumber

        #know which cities/areas are connected
        #know what methods of travel are available
        #major loc or numbered loc?
        #know location on game board
class gameBoard:
    def __init__(self):
        pass

#create ticket class maybe?
#board state class- organizes all locations
#location parent class -> major/minor child classes

p2=Investigator("Debug Investigator", "Debugger",10,20,"Debugger Land",["deb1","deb2","deb1"],[5,6,7,8,9])

#debugInvestigatorStats(p2)
#debugInvestigatorClass(p2)


