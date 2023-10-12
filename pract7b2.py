class person:
    def __init__(self,first,last):
        self.firstname=first
        self.lastname=last
    def Name(self):
        return self.firstname+""+self.lastname
class Employee(person):
    def __init__(self,first,last,staffnum):
        person.__init__(self,first,last)
        self.staffnumber=staffnum

    def GetEmployee(self):
         return self.Name()+","+self.staffnumber
x=person("Nitesh","Shukla")
y=Employee("Brijesh","Shukla","1001")
print(x.firstname)
print(y.GetEmployee())
