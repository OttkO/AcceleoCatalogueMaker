import re
import os
class AcceleoFileParser:
    templates = {}
    queries = {}
    currentFile = "N/A"
    
    def parseFile(self, fileName):
        #print("Analyzing " + fileName)
        with open(fileName) as fp:
            for _, line in enumerate(fp):
                self.currentFile = fileName
                self.readQueries(line)
                self.readTemplates(line)
              
    def readQueries(self, inp):
        res = re.match("\[query*", inp)
        if res:
            self.queries[self.currentFile] = inp

    def readTemplates(self, inp):
        res = re.match("\[template*", inp)
        if res:
            self.templates[self.currentFile] = inp
            
    def get_templates(self):
        return self.templates

    def get_queries(self):
        return self.queries
    
    def saveTemplatesToAFile(self):
        f = open("templates.txt","w")
        
        for i in self.templates:
            f.write( str(self.templates[i]) )
            
        f.close()
    
    def saveQueriesToAFile(self):
        f = open("queries.txt","w")
        
        for i in self.queries:
            f.write( str(self.queries[i]) )
            
        f.close()
    
    def saveQueriesAndTemplatesToOneFile(self):
        f = open("QueriesANdTemplates.txt","w")
        
        for i in self.templates:
            f.write(str(self.templates[i]))
        for i in self.queries:
            f.write( str(self.queries[i]) )
        f.close()
    def parseAll(self, inputDirectory):
        for root, _, files in os.walk(inputDirectory):
                for file in files:
                    if file.endswith('.mtl'):
                        relativePath = (os.path.join(root, file))            
                        self.parseFile(relativePath)
            
         
