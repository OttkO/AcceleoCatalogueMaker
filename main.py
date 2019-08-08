import sys
import os
from AcceleoFileParser import AcceleoFileParser

def main():
    if sys.argv[1] is not None:
        # Sets input directory for parsing MTL files
        inputDirectory = sys.argv[1]
        #Initiates parser
        mtlParser = AcceleoFileParser()
        #Parses all the files
        mtlParser.parseAll(inputDirectory)
        # Dump the data to a 3 different files.
        mtlParser.saveTemplatesToAFile()
        mtlParser.saveQueriesToAFile()
        mtlParser.saveQueriesAndTemplatesToOneFile()

main()