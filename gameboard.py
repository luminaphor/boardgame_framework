class boardLoc: #generic class for a location node
    locID=0 #unique ID for location. Assigned on object creation.
    totalID=0 #total location ID's. Increments each time a location object is created.

    def __init__(self): #initializes object creation.
        self.locID=self.totalID
        boardLoc.totalID+=1

        self.boatPaths= [] #contains possible destinations that can be travelled to from the location object, along with the type of path it is (i.e boat, train, generic)
        self.trainPaths= []
        self.generalPaths= []
        
        self.atLoc=[]

    def placeAtLoc(self,entity):
        self.atLoc.append(entity)

    def removeFromLoc(self,entity):
        self.atLoc.remove(entity)

    def checkLoc(self):
        return self.atLoc

    def numGeneralPaths(self): #counts number of generic paths for object
        return len(self.generalPaths)

    def numTrainPaths(self): #counts number of train paths for object
        return len(self.trainPaths)

    def numBoatPaths(self): #counts number of boat paths for object
        return len(self.boatPaths)

    def numTotalPaths(self): #counts total number of paths available for object
        gpCount,tpCount,bpCount=self.checkPaths()
        return gpCount+tpCount+bpCount

    def checkPaths(self): #gathers individual number of all paths and stores in separate variables
        return (self.boatPaths,self.trainPaths,self.generalPaths)

    def hasTrainPaths(self): #checks if the object has train paths available, returns True if it does, and False otherwise.
        if len(self.trainPaths)>0:
            return True
        else:
            return False
    
    def hasBoatPaths(self): #checks if object has boat paths available, returns True if it does and False otherwise.
        if len(self.boatPaths)>0:
            return True
        else:
            return False

    def canTravel(self,loc2): #determines if its possible to travel to a location (entered as parameter loc2) from current object. 
        destID=loc2.locID

        if self.hasTrainPaths():
            if destID in self.trainPaths:
                return True

        elif self.hasBoatPaths():
            if destID in self.boatPaths:
                return True
        
        elif destID in self.generalPaths:
            return True
        
        else:
            return False
   
class majorLoc(boardLoc): #more specialized class for Major (named) location node. Inherits all properties from parent boardLoc class.
    def __init__(self,locName,locType):
        super().__init__() #inherit all parent class properties and methods
        self.locName=locName
        self.locType=locType

    def showLocName(self):
        return self.locName

class minorLoc(boardLoc): #Minor (numbered) location node. Inherits all properties from parent boardLoc class.
    def __init__(self,locNum,locType):
        super().__init__() #inherit all parent class properties and methods
        self.locNum=locNum
        self.locType=locType

class gameBoard: #game board class, will be used to actually arrange everything and manage events/character travel.
    ML1=majorLoc("San Franciso","City")
    ML2=majorLoc("Arkham","City")
    ML3=majorLoc("London","City")
    ML4=majorLoc("Tunguska","Wilderness")
    ML5=majorLoc("The Himalayas","Wilderness")

    mL1=minorLoc("1","City")
    mL2=minorLoc("2","Sea")
    mL3=minorLoc("3","Wilderness")
    mL4=minorLoc("4","City")
    mL5=minorLoc("5","City")

    locsList=[ML1,ML2,ML3,ML4,ML5,mL1,mL2,mL3,mL4,mL5]
    
    def __init__(self):
        self.createPath(self.ML1,self.ML2,isTrainPath=True)
        self.createPath(self.ML1,self.mL1)
        self.createPath(self.ML1,self.mL2)
        
        self.createPath(self.ML2,self.ML3)
        self.createPath(self.ML2,self.mL3)
        self.createPath(self.ML2,self.mL4)

    def createPath(self,loc1,loc2,isTrainPath=False,isBoatPath=False): #creates a path between two locations by assigning their location ID's to their respective path lists.
        if isTrainPath:
            loc1.trainPaths.append(loc2.locID)
            loc2.trainPaths.append(loc1.locID)
        elif isBoatPath:
            loc1.boatPaths.append(loc2.locID)
            loc2.boatPaths.append(loc1.locID)
        else:
            loc1.generalPaths.append(loc2.locID)
            loc2.generalPaths.append(loc1.locID)        

    def traversePath(self,entity,loc1,loc2):
        loc1.removeFromLoc(entity)
        loc2.placeAtLoc(entity)

def outputBoardPaths(listOfPaths):
    for path in listOfPaths:
        print("Location ID: {}\nPaths: {}\n".format(path.locID,path.checkPaths()))


