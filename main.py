from calcGrade import CalcGrade

class App():
    def __init__(self, username, password):
        self.page = CalcGrade(username, password)

    def getClassInfo(self):
        classes = self.page.getClasses()
        print("\n\n")
        gpa = 0;
        counter = 0;
        for i in range(0, len(self.page.getClasses())):
            print(classes[i].getTitle() + "   grade: " + str(classes[i].getAverage()))
            if str(classes[i].getAverage()) != "None":
                add = (100.0 - float(str(classes[i].getAverage())))/10
                gpa += (6.0 - add)
                counter += 1;
        print("\n")
        print("GPA:" + str(gpa / counter))
        print ("\n\n")

username = input("Please enter your username: ")
password = input("Please enter your password: ")

hac = App(username, password)

while True:
    command = input("What would you like to see? ")
    commandParsed = command.lower().split(" ")
    if commandParsed[0] == "grades" or commandParsed[0] == "grade" or commandParsed[0] == "class" or commandParsed[0] == "classes":
        hac.getClassInfo()
    elif commandParsed[0] == "quit" or commandParsed[0] == "exit":
        break
    else:
        print ("command not recognized")
