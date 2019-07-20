import requests

from bs4 import BeautifulSoup

class Course:
    def __init__(self, code=None, *args, **kwargs):
        if code is not None:    
            self.doc = code
            self.assignments = self.genAssignments()
            self.title = self.genTitle()
            self.categories = self.genCategories()
            self.earned = self.genEarned()
            self.possible = self.genPossible()
            self.weight = self.genWeight()
            self.average = self.genAverage()
            
        if kwargs is not None:
            try: 
                self.assignments = kwargs['assignments']
            except KeyError:
                pass
                
            try: 
                self.title = kwargs['title']
            except KeyError:
                pass
            
            try:
                self.categories = kwargs['categories']
            except KeyError:
                pass
                
            try:
                self.earned = kwargs['earned']
            except KeyError:
                pass
                
            try:
                self.possible = kwargs['possible']
            except KeyError:
                pass
                
            try:
                self.weight = kwargs['weight']
            except KeyError:
                pass
            
            try:
                self.average = kwargs['average']
            except KeyError:
                pass
                
    def genTitle(self):
        parseTitle = self.doc.findAll('a', attrs={'class': 'sg-header-heading'})
        rawTitle = BeautifulSoup(str(parseTitle[0]), 'html.parser')
        rawTitleParse = rawTitle.text.lstrip("\n\r\n| ").rstrip("\n| ")
        return rawTitleParse

    def genAssignments(self):
        rawAssgnList = self.doc.findAll('tr', attrs={"class": "sg-asp-table-data-row"})
        rawList = []
        for i in rawAssgnList:

            trList = BeautifulSoup(str(i), "html.parser")
            assgnList = trList.findAll("td")

            if len(assgnList) == 11:
                newList = []
                for a in assgnList:
                    rawTd = BeautifulSoup(str(a), "html.parser")
                    newList.append(rawTd.td.text)

                try:
                    rawList.append(assignment.Assignment(newList))
                except:
                    pass

        return rawList

    def genCategories(self):
        rawAssgnList = self.doc.findAll('tr', attrs={"class": "sg-asp-table-data-row"})
        rawList = []
        for i in rawAssgnList:

            trList = BeautifulSoup(str(i), "html.parser")
            assgnList = trList.findAll("td")

            if len(assgnList) == 6:
                    newList = []
                    for a in assgnList:
                        rawTd = BeautifulSoup(str(a), "html.parser")
                        newList.append(rawTd.td.text.encode("utf-8"))

                    rawList.append(newList)

        return rawList
        
    def genWeight(self):
        rawWeight = []
        for i in self.categories:
            rawWeight.append(float(i[4]))
            
        return rawWeight
        
    def genEarned(self):
        rawEarned = []
        for i in self.categories:
            rawEarned.append(i[1])
        
        return rawEarned
        
    def genPossible(self):
        rawPossible = []
        for i in self.categories:
            rawPossible.append(i[2])
        
        return rawPossible   
    
    
    def genAverage(self):
        total = 0.0
        earned = 0.0
        for i in self.categories:
            total += float(i[4])
            earned += float(i[5])

        if earned != 0:
            return (earned/total) * 100

    def getAssignments(self):
        return self.assignments
    
    def getAverage(self):
        return self.average
        
    def getPossible(self):
        return self.possible
        
    def getEarned(self):
        return self.earned
        
    def getWeight(self):
        return self.weight
        
    def getCategories(self):
        return self.categories
        
    def getTitle(self):
        return self.title
        
    def changeTitle(self):
        self.title = newValue
        
    def changeAverage(self):
        self.average = newValue
        
    def changeCategories(self):
        self.categories = newValue
        
    def changeAssignment(self):
        self.assignment = newValue
        
    def changeWeight(self):
        self.weight = newValue
        
    def changePossible(self):
        self.possible = newValue
        
    def changeEarned(self):
        self.earned = newValue
        
