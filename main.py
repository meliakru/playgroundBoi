#This is a playground! It contains fun stuff!
def aProgram(afile):
    theFile = open(afile, "r+")
    count = 0
    lineTwo = "this is line 2"
    for line in theFile:
        #Don't forget to strip the file input in order to make comparisons
        aString = line.strip()
        if aString == lineTwo:
            line = "UPDATE".join(line)
            theFile.write(line)
        count = count + 1`
    theFile.close()

aProgram("Example.txt")