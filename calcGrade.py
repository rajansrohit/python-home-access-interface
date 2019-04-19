import requests
import course
from bs4 import BeautifulSoup

class CalcGrade:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        formData = {'Database': 10, 'LogOnDetails.UserName': self.username, 'LogOnDetails.Password': self.password}
        
        with requests.Session() as s:
            r = s.post("https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f", data = formData)
            print("Logging In...")
            
            r = s.get('https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx')
            print("Processing Grades...")

            self.doc = r
            self.soupDoc = BeautifulSoup(r.text, "html.parser")
            
        self.classes = self.getClasses()

    def getClasses(self):
        rawClassList = self.soupDoc.findAll('div', attrs={"class": "AssignmentClass"})
        classList = []
        for i in rawClassList:
            classList.append(course.Course(BeautifulSoup(str(i), "html.parser")))     
        
        return classList
