def printLoc(L1): #a little debug function i wrote that works for a list of boardLoc objects.
    for L in L1:
        print("Location Type: {}\nLocation ID: {}\nBoat Paths: {}\nTrain Paths: {}\nGeneral Paths: {}\n".format(L.locType,L.locID,L.boatPaths,L.trainPaths,L.generalPaths))

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
