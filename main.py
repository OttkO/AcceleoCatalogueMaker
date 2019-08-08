import sys
import os
from AcceleoFileParser import AcceleoFileParser

def main():
    if sys.argv[1] is not None:
        # Sets input directory for parsing MTL files
        inputDirectory = sys.argv[1]
        mtlParser = AcceleoFileParser()
        # Loops through the files calling the parser
        for root, _, files in os.walk(inputDirectory):
            for file in files:
                if file.endswith('.mtl'):
                    relativePath = (os.path.join(root, file))            
                    mtlParser.parseFile(relativePath)
        
        print(mtlParser.get_templates())
main()