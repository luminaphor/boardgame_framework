def printLoc(L1):
    for L in L1:
        print("Location Type: {}\nLocation ID: {}\nBoat Paths: {}\nTrain Paths: {}\nGeneral Paths: {}\n".format(L.locType,L.locID,L.boatPaths,L.trainPaths,L.generalPaths))

class boardLoc: #generic class for a location node
    locID=0 #unique ID for location. Assigned on object creation.
    totalID=0 #total location ID's. Increments each time a location object is created.

    def __init__(self): #initializes object creation.
        self.locID=self.totalID
        boardLoc.totalID+=1

        self.boatPaths= [] #contains possible destinations that can be travelled to from the location object, along with the type of path it is (i.e boat, train, generic)
        self.trainPaths= []
        self.generalPaths= []

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
        gpCount=len(self.generalPaths)
        tpCount=len(self.trainPaths)
        bpCount=len(self.boatPaths)

        return gpCount,tpCount,bpCount

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

class minorLoc(boardLoc): #Minor (numbered) location node. Inherits all properties from parent boardLoc class.
    def __init__(self,locNum,locType):
        super().__init__() #inherit all parent class properties and methods
        self.locNum=locNum
        self.locType=locType

class gameBoard: #game board class, will be used to actually arrange everything and manage events/character travel.
    def __init__(self,vertex):
        self.vertex=vertex
        #self.graph = self.vertex*[None]

    def createPath(self,loc1,loc2,isTrainPath=False,isBoatPath=False): #creates a path between two locations by assigning their location ID's to their respective path lists.
        #isBoatPath and isTrainPath are optional parameters, by default, the method assumes you are trying to create a generic path and so isTrainPath/isBoatPath are False.
        #however, on creation of path, you can enter True as a parameter for either.
        if isTrainPath:
            loc1.trainPaths.append(loc2.locID)
            loc2.trainPaths.append(loc1.locID)
        elif isBoatPath:
            loc1.boatPaths.append(loc2.locID)
            loc2.boatPaths.append(loc1.locID)
        else:
            loc1.generalPaths.append(loc2.locID)
            loc2.generalPaths.append(loc1.locID)

L2=majorLoc("Test Loc 1","Major Type")
L3=majorLoc("Test Loc 2", "Major Type")
L4=minorLoc(1,"Minor Type")
L5=minorLoc(2,"Minor Type")

board=gameBoard("v")

board.createPath(L2,L4,False,True)
board.createPath(L3,L4)
board.createPath(L4,L5,True)

print(L2.canTravel(L4))
print(L2.canTravel(L5))
#LDebug=[L2,L3,L4,L5]
#printLoc(LDebug)

