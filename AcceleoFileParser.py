import re
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
