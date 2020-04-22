import time,os

from .mkdir_p import mkdir_p

# Return a unique output base directory
def getUniqueBasedir(outputDir):
    outDate   = time.strftime("%Y_%m_%d")
    revision  = 0
    outputRev = ""
    while True:
        revision += 1
        revFolder = outDate+"_REV_"+str(revision)
        #revFolder = outDate+"/Revision_"+str(revision) # To be discussed
        outputRev = os.path.join(outputDir,revFolder)
        if not os.path.exists(outputRev):
            return outputRev
        pass
    pass

def mkdir_rev(outputDir):
    outDirRev = getUniqueBasedir(outputDir)
    mkdir_p(outDirRev)
