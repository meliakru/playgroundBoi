#This is a playground! It contains fun stuff!
def aProgram(afile):
    theFile = open(afile, "r+")
    count = 0
    lineTwo = "this is line 2"
    for line in theFile:
        #Don't forget to strip the file input in order to make comparisons
        print(line)
    theFile.close()

if __name__ == "__main__":
    aProgram("Example.txt")