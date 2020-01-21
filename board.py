def printLoc(L1): #a little debug function i wrote that works for a list of boardLoc objects.
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
            
#-------------------------------------------------------------------------------------------------------------------------
#how this code works:
    #you have the boardLoc parent class, which is like the base class for creating a location object. 
    #When you create a location object, it is immediately assigned a unique ID, and 3 empty lists (boatPaths,trainPaths,generalPaths)
    #these 3 lists represent the type of path associated with your location object (boat,train,generic)
    #the values that eventually get added to these lists are the location ID's of the potential paths that can be traveled to. 

    #   for example, San Franciso might have a locID of 2, and Arkham might have a locID of 5. 
    #   If you create a train path between them, then San Francisco's trainPaths list should contain [5]
    #   and Arkhams should then contain [2] 

    #the minorLoc and majorLoc classes are just subclasses that inherit all properties from boardLoc. We don't need to worry too much about them right now
    #because they currently arent much different from the base boardLoc class.

    #the gameBoard class is eventually going to contain all the location objects, and allow us to network them together.
    #right now it has the createPath method, which allows us to actually create the paths between two locations.
    #it may be important to note that when you create a path from loc1 to loc2, the path from loc2 to loc1 is also automatically added.

    #you can access any of an objects properties by using dot notation:
    #objectVariableName.objectPropertyYouWantToAccess
    #for example if I wanted to see the boatPaths list for a boardLoc object called loc5, id say:
    #print(loc5.boatPaths)

    #you also invoke a classes methods in a similar fashion, for example:
    #loc5.hasBoatPaths()
    #or 
    #loc5.canTravel(loc2), which asks "is there a path going from loc5 to loc2?"

#methods I need to test, along with what they are supposed to do:
    #numGeneralPaths() - return the number of generic paths associated with the location
    #numTrainPaths()   - return number of train paths associated with the location
    #numBoatPaths()    - return number of boat paths associated with the location
    #numTotalPaths()   - returns total number of all paths associated with the location
    #hasTrainPaths()   - checks if the location has train paths, returns true if it does and false if it doesnt.
    #hasBoatPaths()    - checks if the location has boat paths, returns true if it does and false if it doesnt.
    #canTravel(loc2)   - determines if its possible to travel from the current location to loc2.

#feel free to define any functions or write loops or whatever you need to do to make debugging more efficient.

#DEBUG CODE HERE
L2 = boardLoc()
L3 = boardLoc() #here we create 2 boardLoc objects, named L2 and L3. They have been automatically assigned a unique locID and path lists.

board = gameBoard("v") #here we create a gameBoard class. 

board.createPath(L2,L3) 
#we then establish a generic path between L2 and L3. It has optional parameters to create a boat path or train path instead.
#if you wanted to create a train path between them you would say
#board.createPath(loc1,loc2,isTrainPath=True)
#or for a boat path you would say
#board.createPath(loc1,loc2,isBoatPath=True)

print(L2.trainPaths)

exit=input("Press Enter to Exit.")
#dont enter any code after this line.
