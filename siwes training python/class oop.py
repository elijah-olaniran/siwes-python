class Students:
    def __init__(self, name, age, gender, mat_no):
        self.name = name
        self.age = age
        self.gender = gender
        self.mat_no = mat_no
        self.level = "ND1"
        print(f' My name is {self.name} I am a Student of FCAHPTIB')
    def payFees(self):
        print(f'{self.name} has paid the amount of 53,000 for FCAHPTIB during {self.level}')
    def attendClass(self):
        print(f'{self.name} attended class regularly during first semester in {self.level}')
    def writeExam(self):
        print(f'{self.name} write {self.level} examination last year')


        
Student1 = Students("Elijah", 87, 'M', "NDCOM/19/375")


Student1.payFees()
        
Student1.attendClass()

Student1.writeExam()


#inheritance

class PartTimeStudents(Students):
    def __init__(self, name, age, gender, mat_no):
        Students.__init__(self, name, age, gender, mat_no)
    def payFees(self):
        print(f'{self.name} has paid the amount of 253,000 for FCAHPTIB during {self.level}')

pt_students = PartTimeStudents("abidemi", 87, 'M', "375")
    
pt_students.payFees()

pt_students.attendClass()

pt_students.writeExam()


#polymorphism


